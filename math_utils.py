def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    return base ** exponent


def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("Prime check is only defined for integers")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci(length):
    if not isinstance(length, int):
        raise TypeError("Fibonacci length must be an integer")
    if length < 0:
        raise ValueError("Fibonacci length must be non-negative")
    if length == 0:
        return []
    if length == 1:
        return [0]
    if length == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, length):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence
