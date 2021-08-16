from sutil.math import core


def test_floor():
    assert core.floor(1.5) == 1
    assert core.floor(1.4) == 1
    assert core.floor(1.6) == 1
    assert core.floor(1.7) == 1
    assert core.floor(2.0) == 2


def test_power():
    assert core.approx(core.power(2, -4), 0.0625)
    assert core.approx(core.power(2, -3), 0.125)
    assert core.approx(core.power(2, -2), 0.25)
    assert core.approx(core.power(2, -1), 0.5)
    assert core.approx(core.power(2, 0), 1)
    assert core.approx(core.power(2, 1), 2)
    assert core.approx(core.power(5, 10), 5**10)


def test_log():
    assert core.approx(core.log(2), 0.69314)
    assert core.approx(core.log(2, 10), 0.3010)
    assert core.approx(core.log(35, 16), 1.2823)
    assert core.approx(core.log(2, 2), 1)


def test_exp():
    assert core.approx(core.exp(0), 1)
    assert core.approx(core.exp(1), 2.71828)
    assert core.approx(core.exp(2), 7.38905)
    assert core.approx(core.exp(3), 20.0855)