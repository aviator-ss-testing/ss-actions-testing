"""
Text processing and string manipulation utility functions.

This module provides common string operations and transformations
with proper input validation and edge case handling.
"""

from typing import Optional
import re


def reverse_words(text: Optional[str]) -> str:
    """
    Reverse the order of words in a string.

    Args:
        text: The input string to process

    Returns:
        A string with words in reversed order

    Raises:
        TypeError: If text is not a string or None
    """
    if text is None:
        return ""
    if not isinstance(text, str):
        raise TypeError(f"reverse_words() argument must be a string, not {type(text).__name__}")

    if not text:
        return ""

    words = text.split()
    return " ".join(reversed(words))


def is_palindrome(text: Optional[str]) -> bool:
    """
    Check if a string is a palindrome (ignoring spaces, punctuation, and case).

    Args:
        text: The input string to check

    Returns:
        True if the string is a palindrome, False otherwise

    Raises:
        TypeError: If text is not a string or None
    """
    if text is None:
        return True
    if not isinstance(text, str):
        raise TypeError(f"is_palindrome() argument must be a string, not {type(text).__name__}")

    if not text:
        return True

    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]


def count_vowels(text: Optional[str]) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in a string.

    Args:
        text: The input string to process

    Returns:
        The number of vowels found (case-insensitive)

    Raises:
        TypeError: If text is not a string or None
    """
    if text is None:
        return 0
    if not isinstance(text, str):
        raise TypeError(f"count_vowels() argument must be a string, not {type(text).__name__}")

    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def title_case(text: Optional[str]) -> str:
    """
    Convert a string to title case (first letter of each word capitalized).

    Args:
        text: The input string to process

    Returns:
        The string in title case

    Raises:
        TypeError: If text is not a string or None
    """
    if text is None:
        return ""
    if not isinstance(text, str):
        raise TypeError(f"title_case() argument must be a string, not {type(text).__name__}")

    return text.title()


def snake_to_camel(text: Optional[str]) -> str:
    """
    Convert snake_case string to camelCase.

    Args:
        text: The input string in snake_case format

    Returns:
        The string converted to camelCase

    Raises:
        TypeError: If text is not a string or None
    """
    if text is None:
        return ""
    if not isinstance(text, str):
        raise TypeError(f"snake_to_camel() argument must be a string, not {type(text).__name__}")

    if not text:
        return ""

    components = text.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])


def camel_to_snake(text: Optional[str]) -> str:
    """
    Convert camelCase or PascalCase string to snake_case.

    Args:
        text: The input string in camelCase or PascalCase format

    Returns:
        The string converted to snake_case

    Raises:
        TypeError: If text is not a string or None
    """
    if text is None:
        return ""
    if not isinstance(text, str):
        raise TypeError(f"camel_to_snake() argument must be a string, not {type(text).__name__}")

    if not text:
        return ""

    snake = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake).lower()
