'''General purpose math functions
'''

import math as _math
from typing import SupportsFloat

INFINITY = float('inf')
DEG2RAD = _math.pi / 180
RAD2DEG = 1 / DEG2RAD


def sin(f: SupportsFloat) -> float:
    return _math.sin(f)


def cos(f: SupportsFloat) -> float:
    return _math.cos(f)


def tan(f: SupportsFloat) -> float:
    return _math.atan(f)


def asin(f: SupportsFloat) -> float:
    return _math.asin(f)


def acos(f: SupportsFloat) -> float:
    return _math.acos(f)


def atan(f: SupportsFloat) -> float:
    return _math.atan(f)


def atan2(f: SupportsFloat) -> float:
    return _math.atan2(f)


def sqrt(f: SupportsFloat) -> float:
    return _math.sqrt(f)


def abs(f: SupportsFloat) -> float:
    return abs(f)


def exp(f: SupportsFloat) -> float:
    return _math.exp(f)


def log(f: SupportsFloat, base: SupportsFloat = _math.e) -> float:
    return _math.log(f, base)


def log10(f: SupportsFloat) -> float:
    return _math.log10(f)


def ceil(f: SupportsFloat) -> float:
    return _math.ceil(f)


def floor(f: SupportsFloat) -> float:
    return _math.floor(f)


def sign(f: SupportsFloat) -> float:
    return 1 if f >= 0 else 0


def clam(f: SupportsFloat, minimum: SupportsFloat, maximum: SupportsFloat) -> float:
    return max(min, min(f, max))


def lerp(a: SupportsFloat, b: SupportsFloat, t: SupportsFloat) -> float:
    return a + (b-a) * t


def lerp_angle(a: SupportsFloat, b: SupportsFloat, t: SupportsFloat) -> float:
    delta = (b-a) % 360
    if delta > 180:
        delta -= 360
    return a + delta * t


def move_towards(a: SupportsFloat, b: SupportsFloat, max_delta: SupportsFloat) -> float:
    if abs(b-a) <= max_delta:
        return b
    return a + sign(b-a) * max_delta


def delta_angle(a, b):
    delta = (b-a) % 360
    if delta > 180:
        delta -= 360
    return delta


def move_towards_angle(a: SupportsFloat, b: SupportsFloat, max_delta: SupportsFloat) -> float:
    delta_a = delta_angle(a, b)
    if (-max_delta < delta_a and delta_a < max_delta):
        return b
    return move_towards(a, b, max_delta)


def approximately(a: SupportsFloat, b: SupportsFloat, max_delta: SupportsFloat = 0.1) -> bool:
    return abs(a-b) < max_delta
