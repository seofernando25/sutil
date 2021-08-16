import sutil.math.integrate as integrate
from sutil.math.core import approx


def test_trapezoidal():
    assert approx(integrate.trapezoidal(0, 1, lambda x: x**x), 0.7834)
    assert approx(integrate.trapezoidal(10, 100, lambda x: 2 * x + 24 - x),
                  7110)
    print(integrate.trapezoidal(2, 5.1, lambda x: x**3 - 4 * (x**2) - 100))
    assert approx(
        integrate.trapezoidal(2, 5.1, lambda x: x**3 - 4 * (x**2) - 100, 500),
        -311.071)
