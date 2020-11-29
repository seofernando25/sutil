'''Common mathematical vector abstractions
'''

from __future__ import annotations
from math import sqrt, pow
import sys
from functools import singledispatchmethod
from typing import SupportsFloat


class Vector2:

    def __init__(self, x: SupportsFloat = 0, y: SupportsFloat = 0) -> None:
        self.x = x
        self.y = y

    def sqr_magnitude(self) -> SupportsFloat:
        return pow(self.x, 2) + pow(self.y, 2)

    def magnitude(self) -> SupportsFloat:
        return sqrt(self.sqr_magnitude)

    def normalized(self) -> None:
        if(self.magnitude > sys.float_info.epsilon):
            return self/self.magnitude
        else:
            return Vector2()

    def clamp_magnitude(self, max_lenght: SupportsFloat) -> Vector2:
        if self.sqr_magnitude > pow(max_lenght, 2):
            mag = self.sqr_magnitude
            norm_x = self.x / mag
            norm_y = self.y / mag
            return Vector2(
                norm_x * max_lenght,
                norm_y * max_lenght
            )
        else:
            return self.clone()

    def clone(self) -> Vector2:
        return Vector2(self.x, self.y)

    def lerp(self, other: Vector2, t: SupportsFloat):
        return Vector2(
            x=self.x + (other.x - self.x) * t,
            y=self.y + (other.y - self.y) * t
        )

    def move_towards(self, target: Vector2, max_distance_delta: SupportsFloat) -> Vector2:
        dx = target.x - self.x
        dy = target.y - self.y

        sqr_distance = pow(dx, 2) + pow(dy, 2)
        if (sqr_distance == 0 or (max_distance_delta >= 0 and sqr_distance <= max_distance_delta**2)):
            return target

        distance_to_move = sqrt(sqr_distance)
        return Vector2(
            x=self.x + dx / distance_to_move * max_distance_delta,
            y=self.y + dy / distance_to_move * max_distance_delta
        )

    def dot(self, other: Vector2) -> SupportsFloat:
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return "Vector2({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Vector2({}, {})".format(self.x, self.y)

    def __hash__(self) -> int:
        return (hash(self.x) ^ hash(self.y) << 2)

    def __eq__(self, other: Vector2) -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other: Vector2) -> Vector2:
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2) -> Vector2:
        return Vector2(self.x - other.x, self.y - other.y)

    @singledispatchmethod
    def __mul__(self, other):
        return NotImplemented

    @singledispatchmethod
    def __div__(self, other: Vector2) -> Vector2:
        return NotImplemented

    def __neg__(self) -> Vector2:
        return Vector2(-self.x, -self.y)

    def __getitem__(self, key: int) -> SupportsFloat:
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        raise IndexError()

    def __setitem__(self, key: int, value: int) -> None:
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        raise IndexError()


@Vector2.__div__.register
def _(self, other: Vector2):
    return Vector2(self.x / other.x, self.y / other.y)


@Vector2.__div__.register
def _(self, other: SupportsFloat):
    return Vector2(self.x / other, self.y / other)


@Vector2.__mul__.register
def _(self, other: Vector2):
    return Vector2(self.x * other.x, self.y * other.y)


@Vector2.__mul__.register
def _(self, other: SupportsFloat):
    return Vector2(self.x * other, self.y * other)


class Vector3:

    def __init__(self, x: SupportsFloat = 0, y: SupportsFloat = 0, z: SupportsFloat = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def sqr_magnitude(self) -> SupportsFloat:
        return pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2)

    def magnitude(self) -> SupportsFloat:
        return sqrt(self.sqr_magnitude)

    def normalized(self) -> None:
        if(self.magnitude > sys.float_info.epsilon):
            return self/self.magnitude
        else:
            return Vector3()

    def clamp_magnitude(self, max_lenght: SupportsFloat) -> Vector3:
        if self.sqr_magnitude > pow(max_lenght, 2):
            mag = self.sqr_magnitude
            norm_x = self.x / mag
            norm_y = self.y / mag
            norm_z = self.z / mag
            return Vector3(
                norm_x * max_lenght,
                norm_y * max_lenght,
                norm_z * max_lenght
            )
        else:
            return self.clone()

    def clone(self) -> Vector3:
        return Vector3(self.x, self.y, self.z)

    def lerp(self, other: Vector3, t: SupportsFloat):
        return Vector3(
            x=self.x + (other.x - self.x) * t,
            y=self.y + (other.y - self.y) * t,
            z=self.z + (other.z - self.z) * t
        )

    def move_towards(self, target: Vector3, max_distance_delta: SupportsFloat) -> Vector3:
        dx = target.x - self.x
        dy = target.y - self.y
        dz = target.z - self.z

        sqr_distance = pow(dx, 2) + pow(dy, 2) + pow(dz, 2)
        if (sqr_distance == 0 or (max_distance_delta >= 0 and sqr_distance <= max_distance_delta**2)):
            return target

        distance_to_move = sqrt(sqr_distance)
        return Vector3(
            x=self.x + dx / distance_to_move * max_distance_delta,
            y=self.y + dy / distance_to_move * max_distance_delta,
            z=self.z + dz / distance_to_move * max_distance_delta
        )

    def dot(self, other: Vector3) -> SupportsFloat:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3(
            x=self.y * other.z - self.z * other.y,
            y=self.z * other.x - self.x * other.z,
            z=self.x * other.y - self.y * other.x
        )

    def __str__(self):
        return "Vector3({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self):
        return "Vector3({}, {}, {})".format(self.x, self.y, self.z)

    def __hash__(self) -> int:
        return (self.x) ^ (hash(self.y) << 2) ^ (hash(self.z) >> 2)

    def __eq__(self, other: Vector3) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other: Vector3) -> Vector3:
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector3) -> Vector3:
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    @ singledispatchmethod
    def __mul__(self, other):
        return NotImplemented

    @ singledispatchmethod
    def __div__(self, other: Vector3) -> Vector3:
        return NotImplemented

    def __neg__(self) -> Vector3:
        return Vector3(-self.x, -self.y, -self.z)

    def __getitem__(self, key: int) -> SupportsFloat:
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z
        raise IndexError()

    def __setitem__(self, key: int, value: int) -> None:
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value
        raise IndexError()


@ Vector3.__div__.register
def _(self, other: Vector3):
    return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)


@ Vector3.__div__.register
def _(self, other: SupportsFloat):
    return Vector3(self.x / other, self.y / other, self.z / other)


@ Vector3.__mul__.register
def _(self, other: Vector3):
    return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)


@ Vector3.__mul__.register
def _(self, other: SupportsFloat):
    return Vector3(self.x * other, self.y * other, self.z * other)
