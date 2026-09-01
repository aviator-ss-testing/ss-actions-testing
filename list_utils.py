from functools import wraps


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


def find_max(numbers):
    if not numbers:
        raise ValueError("Cannot find maximum of empty list")
    return max(numbers)


def find_min(numbers):
    if not numbers:
        raise ValueError("Cannot find minimum of empty list")
    return min(numbers)


def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


@memoize
def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
