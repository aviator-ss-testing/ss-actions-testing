import functools


def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


def reverse_words(text):
    if not isinstance(text, str):
        raise TypeError(f"reverse_words requires a string, got {type(text).__name__}")

    if not text:
        return ""

    words = text.split()
    return " ".join(reversed(words))


@memoize
def count_vowels(text):
    if not isinstance(text, str):
        raise TypeError(f"count_vowels requires a string, got {type(text).__name__}")

    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def is_palindrome(text):
    if not isinstance(text, str):
        raise TypeError(f"is_palindrome requires a string, got {type(text).__name__}")

    normalized = "".join(text.lower().split())
    return normalized == normalized[::-1]


def truncate(text, length, suffix='...'):
    if not isinstance(text, str):
        raise TypeError(f"truncate requires a string, got {type(text).__name__}")
    if not isinstance(length, int):
        raise TypeError(f"length must be an integer, got {type(length).__name__}")
    if length < 0:
        raise ValueError(f"length must be non-negative, got {length}")

    if len(text) <= length:
        return text

    return text[:length] + suffix
