import time
import functools
from typing import get_type_hints


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.6f} seconds")
        return result
    return wrapper


def retry(attempts=3, delay=1):
    if not isinstance(attempts, int) or attempts < 1:
        raise ValueError("Attempts must be a positive integer")
    if not isinstance(delay, (int, float)) or delay < 0:
        raise ValueError("Delay must be a non-negative number")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < attempts - 1:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator


def validate_types(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        hints = get_type_hints(func)

        all_args = list(args)
        arg_names = list(func.__code__.co_varnames[:func.__code__.co_argcount])

        for i, (arg_name, arg_value) in enumerate(zip(arg_names, all_args)):
            if arg_name in hints:
                expected_type = hints[arg_name]
                if not isinstance(arg_value, expected_type):
                    raise TypeError(
                        f"Argument '{arg_name}' must be {expected_type.__name__}, "
                        f"got {type(arg_value).__name__}"
                    )

        for key, value in kwargs.items():
            if key in hints:
                expected_type = hints[key]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Argument '{key}' must be {expected_type.__name__}, "
                        f"got {type(value).__name__}"
                    )

        return func(*args, **kwargs)
    return wrapper


def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in cache:
            return cache[cache_key]

        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result

    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()

    return wrapper
