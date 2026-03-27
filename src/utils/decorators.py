import time
import functools


def timer(func):
    """
    Decorator to measure and print function execution time.

    Usage:
        @timer
        def my_function():
            # function code
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.6f} seconds")
        return result
    return wrapper


def memoize(func):
    """
    Decorator to cache function results based on arguments.

    Usage:
        @memoize
        def expensive_function(x):
            # function code
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    return wrapper


def validate_types(**type_specs):
    """
    Decorator to enforce type checking on function arguments.

    Usage:
        @validate_types(x=int, y=str)
        def my_function(x, y):
            # function code
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_args = func.__code__.co_varnames[:func.__code__.co_argcount]

            for i, arg in enumerate(args):
                if i < len(func_args):
                    arg_name = func_args[i]
                    if arg_name in type_specs:
                        expected_type = type_specs[arg_name]
                        if not isinstance(arg, expected_type):
                            raise TypeError(
                                f"Argument '{arg_name}' must be of type {expected_type.__name__}, "
                                f"got {type(arg).__name__}"
                            )

            for arg_name, arg_value in kwargs.items():
                if arg_name in type_specs:
                    expected_type = type_specs[arg_name]
                    if not isinstance(arg_value, expected_type):
                        raise TypeError(
                            f"Argument '{arg_name}' must be of type {expected_type.__name__}, "
                            f"got {type(arg_value).__name__}"
                        )

            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry(max_attempts=3, delay=0.1, exceptions=(Exception,)):
    """
    Decorator to retry function execution on failure.

    Args:
        max_attempts: Maximum number of retry attempts (default: 3)
        delay: Delay in seconds between retries (default: 0.1)
        exceptions: Tuple of exception types to catch (default: Exception)

    Usage:
        @retry(max_attempts=5, delay=0.5)
        def unreliable_function():
            # function code
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
                    else:
                        raise last_exception

            raise last_exception
        return wrapper
    return decorator
