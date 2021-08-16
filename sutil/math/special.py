import sutil.math.core as core
import sutil.math.integrate as integrate


# Heaviside function
def heaviside(x):
    if x < 0:
        return 0
    elif x == 0:
        return 0.5
    else:
        return 1


# Indicator function
def indicator(x, subset):
    if x in subset:
        return 1
    else:
        return 0


# Sawtooth function
def sawtooth(x):
    return x % 1


# Triangle function
def triangle(x):
    return 2 * abs((x / 2) - int((x / 2) + 0.5))


# Gamma function
def gamma(n):
    def f(x):
        return core.power(x, n - 1) * (1 / core.exp(x))

    v = integrate.trapezoidal(0, 10000, f, parts=10000)

    return v
