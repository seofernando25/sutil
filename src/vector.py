'''Common mathematical vector abstractions
'''

from __future__ import annotations
from math import sqrt, pow
import sys
from functools import singledispatchmethod
from typing import SupportsFloat
import mathf

# region Vector 2


class Vector2:

    def __init__(self, x: SupportsFloat = 0, y: SupportsFloat = 0) -> None:
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value) -> float:
        self._y = value

    @property
    def xy(self) -> Vector2:
        return self.clone()

    def sqr_magnitude(self) -> float:
        return pow(self.x, 2) + pow(self.y, 2)

    def magnitude(self) -> float:
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

    def dot(self, other: Vector2) -> float:
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

    def __getitem__(self, key: int) -> float:
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

# endregion

# region Vector 3


class Vector3:

    def __init__(self, x: SupportsFloat = 0, y: SupportsFloat = 0, z: SupportsFloat = 0) -> None:
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    @property
    def xy(self) -> Vector2:
        return Vector2(self.x, self.y)

    @property
    def xz(self) -> Vector2:
        return Vector2(self.x, self.z)

    @property
    def yz(self) -> Vector2:
        return Vector2(self.y, self.z)

    @property
    def xyz(self) -> Vector3:
        return self.clone()

    def sqr_magnitude(self) -> float:
        return pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2)

    def magnitude(self) -> float:
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

    def dot(self, other: Vector3) -> float:
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

    def __getitem__(self, key: int) -> float:
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

# endregion

# region Quaternion


class Quaternion():

    def __init__(self, x=0, y=0, z=0, w=1) -> None:
        self._x = x
        self._y = y
        self._z = z
        self._w = w

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    @property
    def w(self) -> float:
        return self._w

    @w.setter
    def w(self, value):
        self._w = value

    @classmethod
    def identity():
        return Quaternion()

    def __getitem__(self, key: int) -> float:
        if key == 0:
            return self._x
        elif key == 1:
            return self._y
        elif key == 2:
            return self._z
        elif key == 3:
            return self._w
        raise IndexError()

    def __setitem__(self, key: int, value: int) -> None:
        if key == 0:
            self._x = value
        elif key == 1:
            self._y = value
        elif key == 2:
            self._z = value
        elif key == 2:
            self._w = value
        raise IndexError()

    def dot(self, other: Vector2) -> float:
        return self.x * other.x + self.y * other.y + self.w * other.w

    def to_euler_angles(self) -> Vector3:
        '''Converts a quaternions to yaw, pitch and roll'''

        # Roll
        sinr_cosp = 2 * (self.w * self.x + self.y * self.z)
        cosr_cosp = 1 - 2 * (self.x * self.x + self.y * self.y)
        roll = mathf.atan2(sinr_cosp, cosr_cosp)

        # Pitch
        sinp = 2 * (self.w * self.y - self.z * self.x)
        pitch = mathf.asin(mathf.clamp(sinp, -1, 1))

        # Yaw
        siny_cosp = 2 * (self.w * self.z + self.x * self.y)
        cosy_cosp = 1 - 2 * (self.y * self.y + self.z * self.z)
        yaw = mathf.atan2(siny_cosp, cosy_cosp)

        euler = Vector3(yaw, pitch, roll)

        negative_flip = -sys.float_info.epsilon * mathf.RAD2DEG
        positive_flip = 360.0 + negative_flip

        if euler.x < negative_flip:
            euler.x += 360.0
        elif euler.x > positive_flip:
            euler.x -= 360

        if euler.y < negative_flip:
            euler.y += 360.0
        elif euler.y > positive_flip:
            euler.y -= 360

        if euler.z < negative_flip:
            euler.z += 360.0
        elif euler.z > positive_flip:
            euler.z -= 360

        return euler

    def normalized(self) -> Quaternion:
        mag = mathf.sqrt(self.dot(self))
        if mag < sys.float_info.epsilon:
            return Quaternion.identity
        return Quaternion(self.x / mag, self.y / mag, self.z / mag, self.w / mag)

    @singledispatchmethod
    def __mul__(self, other):
        return NotImplemented

    def __eq__(self, other: Quaternion) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w


@Quaternion.__mul__.register
def _(self, other: Quaternion) -> Quaternion:
    '''Combine rotations'''
    # No one knows how this witchcraft works
    # It works
    #       - Todd Howard
    x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
    y = self.w * other.y + self.y * other.w + self.z * other.x - self.x * other.z
    z = self.w * other.z + self.z * other.w + self.x * other.y - self.y * other.x
    w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
    return Quaternion(x, y, z, w)


@Quaternion.__mul__.register
def _(self, point: Vector3) -> Vector3:
    '''Rotates point with rotation'''
    x = self.x * 2.0
    y = self.y * 2.0
    z = self.z * 2.0
    xx = self.x * x
    yy = self.y * y
    zz = self.z * z
    xy = self.x * y
    xz = self.x * z
    yz = self.y * z
    wx = self.w * x
    wy = self.w * y
    wz = self.w * z

    px = (1.0 - (yy + zz)) * point.x + \
        (xy - wz) * point.y + (xz + wy) * point.z
    py = (xy + wz) * point.x + (1.0 - (xx + zz)) * \
        point.y + (yz - wx) * point.z
    pz = (xz - wy) * point.x + (yz + wx) * \
        point.y + (1.0 - (xx + yy)) * point.z
    return Vector3(px, py, pz)

# endregion
