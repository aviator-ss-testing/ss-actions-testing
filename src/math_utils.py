import functools


def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument must be non-negative, got {arg}")
        return func(*args, **kwargs)
    return wrapper


@validate_positive
def factorial(n):
    if not isinstance(n, int):
        raise TypeError(f"Factorial requires an integer, got {type(n).__name__}")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("GCD requires integer arguments")

    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b
    return a


@validate_positive
def is_prime(n):
    if not isinstance(n, int):
        raise TypeError(f"Prime check requires an integer, got {type(n).__name__}")

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


@validate_positive
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError(f"Fibonacci requires an integer, got {type(n).__name__}")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
