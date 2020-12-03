'''General purpose math functions
'''

import math as _math
from typing import Callable, SupportsFloat

INFINITY = float('inf')
DEG2RAD = _math.pi / 180
RAD2DEG = 1 / DEG2RAD
PI = _math.pi
EULER_NUMBER = _math.e

# NOTE The epsilon is also used as the minimum precision of some functions
EPSILON = 0.0001
ITERATIONS = 50


def sin(num):
    '''Calculates sin using taylor series expansion'''
    num += _math.pi
    num %= 2 * _math.pi
    num -= _math.pi
    ret = 0
    last = 0
    times = 0
    while True:
        neg = times % 2
        v = num**(1+2*times) / int_factorial(1+times*2)
        v *= neg
        ret += v
        diff = last - ret
        last = ret
        if abs(diff) < EPSILON:
            return ret
        times += 1
    return ret


def cos(num):
    '''Calculates cosine using taylor series expansion'''
    return sin(num+_math.pi/2)


def int_factorial(n: SupportsFloat):
    '''Naive non-recursive factorial implementation'''
    if n == 1 or n == 0:
        return 1
    s = n
    while 1:
        s *= n-1
        n -= 1
        if n == 1:
            return s


def factorial(n: SupportsFloat) -> int:
    # Currently unstable! not recommended
    return round(gamma(n+1))


def tan(f: SupportsFloat) -> float:
    return sin(f)/cos(f)


def gamma(n: SupportsFloat) -> float:
    def f(x): return power(x, n-1) * power(EULER_NUMBER, -x)
    splits = 8
    value = f(ITERATIONS)
    value += sum(2*f(k/splits) for k in range(ITERATIONS*splits))

    value /= (2 * splits)

    return value


def int_pow(base: SupportsFloat, exponent: int) -> float:
    '''O(log(n)) power function of positive integers numbers'''
    if exponent < 0:
        return 1 / int_pow(base, -exponent)
    elif exponent == 0:
        return 1
    elif base == 0:
        return 0

    value = 1
    while exponent > 0:
        if exponent & 1:
            value *= base

        base *= base
        exponent >>= 1
    return value


def power(base: SupportsFloat, exponent: SupportsFloat):
    if exponent < 0:
        return 1 / power(base, -exponent)
    if base == 0:
        if exponent == 0:
            return 1
        return 0

    int_part = int(exponent)
    float_part = exponent - int_part
    x = float_part * log_e(base)
    return int_pow(base, int_part) * exp(x)


def trapezium_integration(a: SupportsFloat, b: SupportsFloat, f: Callable[[SupportsFloat], SupportsFloat], parts: int = ITERATIONS):
    d = (b-a)/parts
    value = 0
    value += sum(2*f(a+d*k) for k in range(1, int(parts)))
    value += f(b)
    value += f(a)
    value *= d/2
    return value


def asin(f: SupportsFloat) -> float:
    return _math.asin(f)


def acos(f: SupportsFloat) -> float:
    return _math.acos(f)


def atan(f: SupportsFloat) -> float:
    return _math.atan(f)


def atan2(y: SupportsFloat, x: SupportsFloat) -> float:
    return _math.atan2(y, x)


def abs(f: SupportsFloat) -> float:
    return -1 * f if f < 0 else f


def exp(f: SupportsFloat) -> float:
    if f == 0:
        return 1
    if f < 0:
        return 1 / exp(-f)

    total = 1
    denominator = 1
    last = 0
    k_times = 1
    # Uses e^x taylor series
    # to compute the value
    # e^x = sum n^x / n!
    while True:
        denominator *= k_times
        total += int_pow(f, k_times) / denominator
        diff = last - total
        last = total
        if abs(diff) < EPSILON:
            return total
        k_times += 1


def log_e(val: SupportsFloat):
    # Using a "binary search" to find log e
    if val == 1:
        return 0
    if val == 0:
        return 1

    if val > 1:
        upper = _math.frexp(val)[1]
    else:
        upper = val

    lower = 0

    while True:
        mid_val = (upper + lower) / 2
        exp_val = exp(mid_val)

        if abs(exp_val-val) < EPSILON:
            return mid_val
        elif exp_val > val:
            upper = mid_val
        else:
            lower = mid_val


def log(f: SupportsFloat, base: SupportsFloat = EULER_NUMBER) -> float:
    return log2(f)/log2(base)


def log2(f) -> float:
    # Gets the mantissa and exponent of the floating-point
    mantissa, exponent = _math.frexp(f)
    return exponent + log_e(mantissa, 2)


def ceil(f: SupportsFloat) -> int:
    return floor(f) + 1


def floor(f: SupportsFloat) -> int:
    return int(f)


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
