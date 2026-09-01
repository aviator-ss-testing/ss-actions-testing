from functools import wraps


def validate_string(func):
    """Decorator that validates input is a non-empty string."""
    @wraps(func)
    def wrapper(text, *args, **kwargs):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        if not text:
            raise ValueError("Input string cannot be empty")
        return func(text, *args, **kwargs)
    return wrapper


@validate_string
def reverse_string(text):
    """Return the reversed string."""
    return text[::-1]


@validate_string
def count_vowels(text):
    """Return count of vowels (a, e, i, o, u) in text, case-insensitive."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


@validate_string
def capitalize_words(text):
    """Capitalize first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())
