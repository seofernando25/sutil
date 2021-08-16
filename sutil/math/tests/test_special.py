import sutil.math.special as special
from sutil.math.core import approx


def test_gamma():
    assert approx(special.gamma(1), 1, 0.1)
    # print(special.gamma(5)),
    assert approx(special.gamma(5), 24.0, 0.1)
    assert approx(special.gamma(5.5), 52.3428, 0.1)
