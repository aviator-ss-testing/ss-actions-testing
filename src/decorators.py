import functools
import time
from typing import Any, Callable


def timer(func: Callable) -> Callable:
    """
    Decorator to measure and print function execution time.

    Example:
        @timer
        def slow_function():
            time.sleep(1)
            return "done"

    Args:
        func: The function to be timed

    Returns:
        Wrapped function that prints execution time
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"{func.__name__} took {elapsed:.4f} seconds to execute")
        return result
    return wrapper


def memoize(func: Callable) -> Callable:
    """
    Decorator to cache function results based on arguments.

    Example:
        @memoize
        def fibonacci(n):
            if n < 2:
                return n
            return fibonacci(n-1) + fibonacci(n-2)

    Args:
        func: The function whose results should be cached

    Returns:
        Wrapped function with caching capability
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    wrapper.cache = cache
    return wrapper


def validate_types(*expected_types):
    """
    Decorator to validate function argument types.

    Example:
        @validate_types(int, int)
        def add(a, b):
            return a + b

    Args:
        *expected_types: Expected types for each positional argument

    Returns:
        Decorator function that validates argument types

    Raises:
        TypeError: If any argument doesn't match expected type
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) != len(expected_types):
                raise TypeError(
                    f"{func.__name__} expects {len(expected_types)} arguments, "
                    f"got {len(args)}"
                )

            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"{func.__name__} argument {i} must be {expected_type.__name__}, "
                        f"got {type(arg).__name__}"
                    )

            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry(max_attempts: int = 3):
    """
    Decorator to retry function on exception.

    Example:
        @retry(max_attempts=3)
        def flaky_api_call():
            # May fail and will retry up to 3 times
            return requests.get("https://api.example.com")

    Args:
        max_attempts: Maximum number of attempts (default: 3)

    Returns:
        Decorator function that retries on exception

    Raises:
        Exception: The last exception if all attempts fail
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        continue

            raise last_exception
        return wrapper
    return decorator


def log_calls(func: Callable) -> Callable:
    """
    Decorator to log function calls with arguments.

    Example:
        @log_calls
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

    Args:
        func: The function to log calls for

    Returns:
        Wrapped function that logs calls
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper
