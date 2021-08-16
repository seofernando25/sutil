def interp(a, b, t, d=1) -> float:
    return a + (b - a) * t**d


def inv_interp(a, b, t, d=1) -> float:
    return a + (b - a) * (1 - (1 - t)**d)


def lerp_angle(a, b, t) -> float:
    delta = (b - a) % 360
    if delta > 180:
        delta -= 360
    return a + delta * t


def delta_angle(a, b):
    delta = (b - a) % 360
    if delta > 180:
        delta -= 360
    return delta