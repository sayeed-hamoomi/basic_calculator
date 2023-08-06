def addition(*inputs):
    result = 0
    for i in inputs:
        result += i

    return result


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def modulus(a, b):
    return a % b


def exponent(a, b):
    return a**b


def floor_division(a, b):
    return a // b
