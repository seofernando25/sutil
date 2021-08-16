'''General purpose math functions
'''

import math as _math
from math import pi, e, frexp
from typing import Callable, SupportsFloat


def fib_binet(n):
    '''Calculates nth fib number'''
    SQRT_5 = 2.2360679774997896964091736687312762354406183596115257242708972454
    A = (1 + SQRT_5) / 2
    B = (1 - SQRT_5) / 2
    res = (A**n - B**n) / (SQRT_5)
    return int(round(res))


# def move_towards(a: SupportsFloat, b: SupportsFloat,
#                  max_delta: SupportsFloat) -> float:
#     if abs(b - a) <= max_delta:
#         return b
#     return a + sign(b - a) * max_delta

# def move_towards_angle(a: SupportsFloat, b: SupportsFloat,
#                        max_delta: SupportsFloat) -> float:
#     delta_a = delta_angle(a, b)
#     if (-max_delta < delta_a and delta_a < max_delta):
#         return b
#     return move_towards(a, b, max_delta)
