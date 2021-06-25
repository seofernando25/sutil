'''A simple calculator parser using RPN to parse a string
'''

import re
from math import *


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def tokenize(string, operations):
    """Splits a string into a list using the operations as the separators
    """

    # Just removing whitespace
    string = string.replace(" ", "")

    # What the fuck?
    # Regex shortcut to split the string using the operations as the separators
    float_regex = "\d*\.?\d+|[\(\)]"
    for key in operations.keys():
        value = operations[key]
        if len(key) == 1:
            float_regex += "|" + "[\\" + key + "]"
        else:
            float_regex += "|" + key
        # "|".join(operations)
        # pass
    rgx = re.compile(float_regex)

    results = rgx.finditer(string)
    exprList = []
    for reg in results:
        start, end = reg.span()
        exprList.append(string[start: end])
    return exprList


def to_rpn(tokens, operations):
    """Sort tokens from tokenize using their priority and type
    """

    out_queue = []
    op_stack = []

    for token in tokens:
        if(is_float(token)):
            out_queue.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            while op_stack[-1] != "(":
                out_queue.append(op_stack.pop())
            op_stack.pop()
        elif token in list(operations.keys()):
            if operations[token].priority >= 0:
                while len(op_stack) >= 1 and op_stack[-1] != "(" and (
                        operations[op_stack[-1]].priority >= operations[token].priority):
                    # If brackets are unbalanced, popping the stack will throw an error
                    out_queue.append(op_stack.pop())
            op_stack.append(token)

    while len(op_stack) != 0:
        out_queue.append(op_stack.pop())
    return out_queue


def calculate(rpn_tokens, operations):
    val_stack = []

    for token in rpn_tokens:
        if(is_float(token)):
            val_stack.append(token)
        elif token in list(operations.keys()):
            args = []
            for x in range(operations[token].lmbd.__code__.co_argcount):
                # If this throws an error user didn't give enough args for a function
                args.append(float(val_stack.pop()))
            result = operations[token].lmbd(*args)
            val_stack.append(result)

    # If the value stack is bigger than one we probably made an error
    assert len(val_stack) == 1
    return val_stack[0]


def calculate_string(string, operations):
    """Calculates the string given operations
    """

    tokenized = tokenize(string, operations)
    rpn = to_rpn(tokenized, operations)
    return calculate(rpn, operations)
