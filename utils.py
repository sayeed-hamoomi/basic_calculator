from collections import defaultdict


def addition(inputs):
    result = 0
    for i in inputs:
        result += i

    return result


def subtraction(inputs: list):
    result = inputs.pop(0)
    for i in inputs:
        result -= i
    return result


def multiplication(inputs: list):
    result = 1
    for i in inputs:
        result *= i

    return result


def division(inputs: list):
    result = inputs.pop(0)
    for i in inputs:
        result /= i
    return result


def modulus(inputs):
    result = inputs.pop(0)
    for i in inputs:
        result %= i
    return result


def exponent(inputs):
    result = inputs.pop(0)
    for i in inputs:
        result **= i
    return result


def floor_division(inputs):
    result = inputs.pop(0)
    for i in inputs:
        result //= i
    return result


def mean(inputs, op):
    result = addition(inputs)

    return result / op


def median(inputs: list, op):
    inputs.sort()
    if op % 2 != 0:
        result = inputs[op // 2]
    else:
        op -= 1
        result = (inputs[op // 2] + inputs[(op // 2) + 1]) / 2
    return result


def mode(inputs):
    d = defaultdict(lambda: 0)
