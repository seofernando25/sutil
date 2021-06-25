from sutil.utils.expr_parser import *
from collections import namedtuple


OpBehaviour = namedtuple('OpBehaviour', 'priority lmbd')

operations = {
    "+": OpBehaviour(0, lambda x, y: y+x),
    "-": OpBehaviour(0, lambda x, y: y-x),
    "/": OpBehaviour(1, lambda x, y: y/x),
    "*": OpBehaviour(1, lambda x, y: y*x),
    "!": OpBehaviour(2, lambda x: gamma(1+x)),
    "%": OpBehaviour(2, lambda x: x/100),
    "^": OpBehaviour(2, lambda x, y: y**x),
    "sin": OpBehaviour(99, lambda x: sin(x)),
    "cos": OpBehaviour(99, lambda x: cos(x)),
    "tan": OpBehaviour(99, lambda x: tan(x)),
    "asin": OpBehaviour(99, lambda x: asin(x)),
    "acos": OpBehaviour(99, lambda x: acos(x)),
    "atan": OpBehaviour(99, lambda x: atan2(x)),
    "ln": OpBehaviour(99, lambda x: log(x)),
    "log": OpBehaviour(99, lambda x: log10(x)),
    "sqrt": OpBehaviour(99, lambda x: sqrt(x)),
    "fact": OpBehaviour(99, lambda x: factorial(x)),
    "gamma": OpBehaviour(99, lambda x: gamma(x)),
}


def isClose(a, b):
    maxDelta = 0.01
    delta = abs(a - b)
    if delta > maxDelta:
        print(f"A: {a}")
        print(f"B: {b}")
        print(f"Delta: {delta}")
        return False
    return True


assert isClose(cos(25), calculate_string("cos(25)", operations))
assert isClose(1+25/5*3 ** 10, calculate_string("1+25/5*3^10", operations))

a = gamma(1+sin(1)) + gamma(4+1) - sqrt(4)
b = calculate_string("sin(1)! + 4! - sqrt(4)", operations)
assert isClose(a, b)

print("Ok!")
