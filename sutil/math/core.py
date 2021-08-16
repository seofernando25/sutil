# Extract the exponent of floats
from math import frexp as _frexp
from math import pi, e

DEG2RAD = pi / 180
RAD2DEG = 1 / DEG2RAD


def exp(x) -> float:
    """Returns e ^x"""
    if x == 0:
        return 1
    if x < 0:
        return 1 / exp(-x)

    total = 1
    denominator = 1
    last = float('inf')
    k_times = 1
    x_top = x
    # Uses e^x taylor series
    # to compute the value
    # e^x = sum n^x / n!

    while True:
        try:
            denominator *= k_times
            total += x_top / denominator
            x_top *= x
            diff = last - total
            last = total
            if abs(diff) < 0.00000000001:
                return last
            k_times += 1
        except OverflowError:
            return total

    return last


def power(base, exponent):
    if exponent == 0:
        return 1
    if base == 0:
        return 0
    return exp(exponent * log(base))


def log_e(val):
    delta = 1
    ret = 1
    while delta > 0.00000000001:
        last = ret
        ret += 2 * ((val - exp(ret)) / (val + exp(ret)))
        delta = abs(ret - last)
    return ret


def log(x, base=e):
    return log_e(float(x)) / log_e(float(base))


def ceil(x) -> int:
    return floor(x) + 1


def floor(x) -> int:
    return int(x)


def sign(x) -> float:
    return 1 if x >= 0 else 0


def clamp(x, minimum, maximum):
    return max(minimum, min(maximum, x))


def approx(x, y, tolerance=0.001):
    return abs(x - y) < tolerance


def factorial(n):
    if n in [1, 0]:
        return 1
    s = n
    while 1:
        s *= n - 1
        n -= 1
        if n == 1:
            return s


def factorize(n):
    if n == 1:
        return [1]
    factors = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                factors.append(i)
                n //= i
                break
    return factors


# Gets the LCM of two numbers
def lcm(x, y):
    x_count = 1
    y_count = 1
    m_x = x
    m_y = y
    while m_x != m_y:
        if m_x < m_y:
            m_x = x * x_count
            x_count += 1
        else:
            m_y = y * y_count
            y_count += 1
    return m_x


# TOOD GCD