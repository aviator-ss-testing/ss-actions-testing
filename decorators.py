"""
Decorator functions module providing various decorator patterns for testing and functionality enhancement.

This module implements common decorator patterns including timing, retry, caching, validation,
and logging decorators that can be applied to functions to add cross-cutting concerns.
"""

import time
import functools
import random
import logging
from datetime import datetime
from typing import Any, Callable, Dict, Optional, Tuple, Union, Type


def timing(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that measures and prints the execution time of a function.

    Args:
        func: The function to be timed

    Returns:
        Wrapped function that prints execution time

    Example:
        @timing
        def slow_function():
            time.sleep(1)
            return "done"
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0, exceptions: Tuple[Type[Exception], ...] = (Exception,)) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator that retries function execution on failure.

    Args:
        max_attempts: Maximum number of execution attempts (default: 3)
        delay: Delay in seconds between attempts (default: 1.0)
        exceptions: Tuple of exception types to catch and retry on (default: (Exception,))

    Returns:
        Wrapped function that retries on specified exceptions

    Example:
        @retry(max_attempts=5, delay=0.5)
        def unreliable_function():
            if random.random() < 0.7:
                raise ValueError("Random failure")
            return "success"
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"Attempt {attempt + 1} failed for {func.__name__}: {e}. Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print(f"All {max_attempts} attempts failed for {func.__name__}")

            if last_exception:
                raise last_exception

        return wrapper
    return decorator


def cache(maxsize: Optional[int] = 128) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator that caches function results to improve performance on repeated calls.

    Args:
        maxsize: Maximum number of cached results (default: 128, None for unlimited)

    Returns:
        Wrapped function with caching capability

    Example:
        @cache(maxsize=50)
        def expensive_computation(n):
            time.sleep(0.1)  # Simulate expensive operation
            return n ** 2
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        cache_dict: Dict[Tuple[Any, ...], Any] = {}
        access_order: list = []

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Create a cache key from args and kwargs
            key = (args, tuple(sorted(kwargs.items())))

            if key in cache_dict:
                # Move to end for LRU tracking
                access_order.remove(key)
                access_order.append(key)
                return cache_dict[key]

            # Compute result
            result = func(*args, **kwargs)

            # Add to cache
            cache_dict[key] = result
            access_order.append(key)

            # Enforce maxsize limit
            if maxsize is not None and len(cache_dict) > maxsize:
                oldest_key = access_order.pop(0)
                del cache_dict[oldest_key]

            return result

        def cache_info() -> Dict[str, Any]:
            """Get cache statistics."""
            return {
                'hits': len([k for k in access_order if k in cache_dict]),
                'misses': 0,  # This is simplified
                'maxsize': maxsize,
                'currsize': len(cache_dict)
            }

        def cache_clear() -> None:
            """Clear the cache."""
            cache_dict.clear()
            access_order.clear()

        wrapper.cache_info = cache_info  # type: ignore
        wrapper.cache_clear = cache_clear  # type: ignore

        return wrapper
    return decorator


def validate(*validators: Callable[[Any], bool]) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator that validates function arguments before execution.

    Args:
        *validators: Variable number of validation functions that return True if valid

    Returns:
        Wrapped function that validates arguments before execution

    Raises:
        ValueError: If any validation fails

    Example:
        def is_positive(x):
            return x > 0

        def is_integer(x):
            return isinstance(x, int)

        @validate(is_integer, is_positive)
        def square_root(n):
            return n ** 0.5
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Validate positional arguments
            for i, arg in enumerate(args):
                for j, validator in enumerate(validators):
                    if not validator(arg):
                        raise ValueError(f"Argument {i} failed validation {j} in function {func.__name__}")

            # Validate keyword arguments
            for key, value in kwargs.items():
                for j, validator in enumerate(validators):
                    if not validator(value):
                        raise ValueError(f"Keyword argument '{key}' failed validation {j} in function {func.__name__}")

            return func(*args, **kwargs)
        return wrapper
    return decorator


def validate_types(**type_specs: Type[Any]) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator that validates function arguments match specified types.

    Args:
        **type_specs: Keyword arguments mapping parameter names to expected types

    Returns:
        Wrapped function that validates argument types before execution

    Raises:
        TypeError: If any argument doesn't match its expected type

    Example:
        @validate_types(name=str, age=int, height=float)
        def create_person(name, age, height):
            return {"name": name, "age": age, "height": height}
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            import inspect
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()

            for param_name, expected_type in type_specs.items():
                if param_name in bound.arguments:
                    value = bound.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"Parameter '{param_name}' expected {expected_type.__name__}, "
                            f"got {type(value).__name__} in function {func.__name__}"
                        )

            return func(*args, **kwargs)
        return wrapper
    return decorator


def log_calls(logger_name: Optional[str] = None, level: int = logging.INFO) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator that logs function calls with parameters and return values.

    Args:
        logger_name: Name of the logger to use (default: function's module name)
        level: Logging level to use (default: logging.INFO)

    Returns:
        Wrapped function that logs calls and results

    Example:
        @log_calls(level=logging.DEBUG)
        def add_numbers(a, b):
            return a + b
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        logger = logging.getLogger(logger_name or func.__module__)

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Log function call
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)

            logger.log(level, f"Calling {func.__name__}({signature})")

            start_time = datetime.now()
            try:
                result = func(*args, **kwargs)
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds()

                logger.log(level, f"{func.__name__} returned {result!r} in {duration:.4f}s")
                return result
            except Exception as e:
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds()

                logger.log(logging.ERROR, f"{func.__name__} raised {type(e).__name__}: {e} after {duration:.4f}s")
                raise

        return wrapper
    return decorator


def simple_log(message: str = "") -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Simple decorator that prints function calls with optional custom message.

    Args:
        message: Optional custom message to include in log output

    Returns:
        Wrapped function that prints call information

    Example:
        @simple_log("Processing data")
        def process_data(data):
            return len(data)
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            prefix = f"[{timestamp}] {message} " if message else f"[{timestamp}] "

            args_str = ", ".join(repr(arg) for arg in args)
            kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            all_args = ", ".join(filter(None, [args_str, kwargs_str]))

            print(f"{prefix}Calling {func.__name__}({all_args})")

            try:
                result = func(*args, **kwargs)
                print(f"{prefix}{func.__name__} completed successfully -> {result!r}")
                return result
            except Exception as e:
                print(f"{prefix}{func.__name__} failed with {type(e).__name__}: {e}")
                raise

        return wrapper
    return decorator