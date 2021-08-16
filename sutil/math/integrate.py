def trapezoidal(start, stop, fun, parts=40):
    d = (stop - start) / parts
    value = 0
    value += sum(2 * fun(start + d * k) for k in range(1, int(parts)))
    value += fun(stop)
    value += fun(start)
    value *= d / 2
    return value