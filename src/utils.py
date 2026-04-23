from functools import wraps


def validate_numbers(func):
    """Decorator that validates inputs are numeric types (int or float). Raises TypeError if any argument is not numeric."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or isinstance(arg, bool):
                raise TypeError(f"All arguments must be numeric. Got {type(arg).__name__}")
        for value in kwargs.values():
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(f"All arguments must be numeric. Got {type(value).__name__}")
        return func(*args, **kwargs)
    return wrapper
