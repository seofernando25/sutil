from math import pi

INFINITY = float('inf')
DEG2RAD = pi / 180
RAD2DEG = 1 / DEG2RAD
PI = 3.1415926535897932
E = 2.7182818284590452


def int_factorial(n):
    '''Naive non-recursive factorial implementation'''
    if n in [1, 0]:
        return 1
    s = n
    while True:
        s *= n - 1
        n -= 1
        if n == 1:
            return s


def sin(num, eps=0.0001):
    '''Calculates sin using taylor series expansion'''
    num += pi
    num %= 2 * pi
    num -= pi
    ret = 0
    last = 0
    times = 0
    while True:
        neg = times % 2
        v = num**(1 + 2 * times) / int_factorial(1 + times * 2)
        v *= neg
        ret += v
        diff = last - ret
        last = ret
        if abs(diff) < eps:
            return last
        times += 1


def cos(num):
    '''Calculates cosine using taylor series expansion'''
    return sin(num + pi / 2)


def tan(num):
    return sin(num) / cos(num)


def arctan(num):
    # TODO This gets values wrong outside of the range [-1, 1]
    s = num
    last_s = s
    sign = 1
    c = 3
    while True:
        try:
            sign *= -1
            s += sign * (num**c) / c
            c += 2
            if abs(last_s - s) < 0.1:
                return s
            last_s = s
        except OverflowError:
            return s


def delta_angle(a, b):
    delta = (b - a) % 360
    if delta > 180:
        delta -= 360
    return delta


#TODO: Add arctan and arctan2

# def rect_to_polar(x, y):
#     """Convert rectangular coordinates to polar coordinates"""
#     r = power(x * x + y * y, 0.5)
#     theta = atan2(y, x)
#     return r, theta


def polar_to_rect(r, theta):
    """Convert polar coordinates to rectangular coordinates"""
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y