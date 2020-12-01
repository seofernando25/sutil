'''General purpose math functions
'''

import math as _math
from typing import SupportsFloat

INFINITY = float('inf')
DEG2RAD = _math.pi / 180
RAD2DEG = 1 / DEG2RAD


def sin(num, iterations=8):
    '''Calculates sin using taylor series expansion'''
    num += _math.pi
    num %= 2 * _math.pi
    num -= _math.pi
    ret = 0
    for n in range(iterations):
        neg = (-1)**n
        v = num**(1+2*n) / factorial(1+n*2)
        v *= neg
        ret += v
    return ret


def cos(num, iterations=8):
    '''Calculates cosine using taylor series expansion'''
    return sin(num+_math.pi/2, iterations)


def factorial(n: SupportsFloat):
    '''Naive non-recursive factorial implementation'''
    # TODO Implement gamma function for better results with floating numbers
    if n == 1 or n == 0:
        return 1
    s = n
    while 1:
        s *= n-1
        n -= 1
        if n == 1:
            return s


def tan(f: SupportsFloat) -> float:
    return sin(f)/cos(f)


def gamma(n: SupportsFloat):
    pass


def asin(f: SupportsFloat) -> float:
    return _math.asin(f)


def acos(f: SupportsFloat) -> float:
    return _math.acos(f)


def atan(f: SupportsFloat) -> float:
    return _math.atan(f)


def atan2(y: SupportsFloat, x: SupportsFloat) -> float:
    return _math.atan2(y, x)


def sqrt(f: SupportsFloat) -> float:
    return _math.sqrt(f)


def abs(f: SupportsFloat) -> float:
    return -1 * f if f < 0 else f


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


def clamp(f: SupportsFloat, minimum: SupportsFloat, maximum: SupportsFloat) -> float:
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
