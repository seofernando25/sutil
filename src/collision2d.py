from __future__ import annotations
from typing import List, Tuple
import mathf
import vector
from vector import Vector2


class AABB2D():
    """A 2D Axis-Aligned Bounding Box
    """

    def __init__(self) -> None:
        self.position = vector.Vector2
        self.dimension = vector.Vector2

    def collide(self, other: AABB2D) -> bool:
        s_dx_s = self.position.x + self.dimension.x
        s_dx_e = self.position.x

        o_dx_s = other.position.x
        o_dx_e = other.position.x + other.dimension.x

        overlap_x = min(s_dx_e, o_dx_e) > max(s_dx_s, o_dx_s)

        s_dy_s = other.position.y - other.dimension.y
        s_dy_e = other.position.y

        o_dy_s = other.position.y - other.dimension.y
        o_dy_e = other.position.y

        overlap_y = min(s_dy_e, o_dy_e) > max(s_dy_s, o_dy_s)

        return overlap_x and overlap_y


def point_point_col(a: vector.Vector2, b: vector.Vector2) -> bool:
    return a == b


def point_circle_col(a: vector.Vector2, circle_pos: vector.Vector2, circle_radius: float) -> bool:
    delta = (a - circle_pos)
    return delta.sqr_magnitude <= circle_radius


def point_aabb_col(a: vector.Vector2, aabb: AABB2D) -> bool:
    in_dx = aabb.position.x <= a.x <= aabb.position.x + aabb.dimension.x
    in_dy = aabb.position.y <= a.y <= aabb.position.y + aabb.dimension.y
    return in_dx and in_dy


def point_poly_col(p: vector.Vector2, points: List[Vector2]) -> bool:
    # Use even-odd rule
    i = 0
    j = len(points) - 1
    collide = False
    for index, value in enumerate(points):
        pass
    return collide


def point_poly_col(p: vector.Vector2, points: List[Vector2]) -> bool:
    last = points[-1]
    collision = False
    for current in points:
        poly_dy = (last.y - current.y)
        poly_dx = (last.x - current.x)
        edge_slope = poly_dy/poly_dx

        # Checks if the point is inside a 1D bounding box
        # with the line on the x axis
        inside_edge_x = min(current.x, last.x) <= p.x <= max(current.x, last.x)
        if not inside_edge_x:
            continue

        # Checks if the point is bellow the line
        intersects = p.y <= current.y + edge_slope * (p.x - current.x)
        if intersects:
            collision = not collision

        last = current

    return collision


def poly_to_aabb(points: List[Vector2]) -> AABB2D:
    left = min(p.x for p in points)
    bottom = min(p.y for p in points)
    top = max(p.y for p in points)
    right = max(p.x for p in points)
    return AABB2D(Vector2(left, top), Vector2(right-left, top-bottom))
