"""Utility functions for common string operations."""

import re


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive, ignoring non-alphanumeric).

    Args:
        s: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Raises:
        TypeError: If s is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s).__name__}")
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    return cleaned == cleaned[::-1]


def reverse_words(s: str) -> str:
    """Reverse the order of words in a string.

    Args:
        s: The input string.

    Returns:
        The string with word order reversed.

    Raises:
        TypeError: If s is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s).__name__}")
    return " ".join(s.split()[::-1])


def camel_to_snake(s: str) -> str:
    """Convert a camelCase or PascalCase string to snake_case.

    Args:
        s: The camelCase/PascalCase string to convert.

    Returns:
        The snake_case equivalent.

    Raises:
        TypeError: If s is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s).__name__}")
    if not s:
        return s
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    return s.lower()


def snake_to_camel(s: str, upper_first: bool = False) -> str:
    """Convert a snake_case string to camelCase or PascalCase.

    Args:
        s: The snake_case string to convert.
        upper_first: If True, return PascalCase (capitalize first word too).

    Returns:
        The camelCase or PascalCase equivalent.

    Raises:
        TypeError: If s is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s).__name__}")
    if not s:
        return s
    parts = [p for p in s.split("_") if p]
    if not parts:
        return s
    if upper_first:
        return "".join(word.capitalize() for word in parts)
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


def count_vowels(s: str) -> int:
    """Count the number of vowels (a, e, i, o, u) in a string.

    Args:
        s: The string to count vowels in.

    Returns:
        The number of vowels (case-insensitive).

    Raises:
        TypeError: If s is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s).__name__}")
    return sum(1 for ch in s.lower() if ch in "aeiou")


def truncate_string(s: str, max_length: int, suffix: str = "...") -> str:
    """Truncate a string to a maximum length, appending a suffix if truncated.

    Args:
        s: The string to truncate.
        max_length: The maximum allowed length of the result (including suffix).
        suffix: The suffix to append when truncating (default "...").

    Returns:
        The original string if it fits, otherwise a truncated version with suffix.

    Raises:
        TypeError: If s or suffix is not a string.
        ValueError: If max_length is negative or smaller than the suffix length.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s).__name__}")
    if not isinstance(suffix, str):
        raise TypeError(f"suffix must be a str, got {type(suffix).__name__}")
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if len(s) <= max_length:
        return s
    cut = max_length - len(suffix)
    if cut < 0:
        return suffix[:max_length]
    return s[:cut] + suffix
