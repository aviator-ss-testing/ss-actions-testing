"""
String utility functions for text processing and manipulation.
"""

from typing import Optional
import re


def reverse_words(text: Optional[str]) -> str:
    """
    Reverse the order of words in a string.

    Args:
        text: Input string to reverse words

    Returns:
        String with words in reversed order

    Raises:
        TypeError: If text is not a string or None
    """
    if text is None:
        return ""
    if not isinstance(text, str):
        raise TypeError("Argument must be a string or None")

    if not text.strip():
        return ""

    words = text.split()
    return " ".join(reversed(words))


def is_palindrome(text: Optional[str]) -> bool:
    """
    Check if a string is a palindrome (ignoring spaces, punctuation, and case).

    Args:
        text: Input string to check

    Returns:
        True if text is a palindrome, False otherwise

    Raises:
        TypeError: If text is not a string or None
    """
    if text is None:
        return True
    if not isinstance(text, str):
        raise TypeError("Argument must be a string or None")

    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]


def count_vowels(text: Optional[str]) -> int:
    """
    Count the number of vowels in a string (case-insensitive).

    Args:
        text: Input string to count vowels

    Returns:
        Number of vowels found in the string

    Raises:
        TypeError: If text is not a string or None
    """
    if text is None:
        return 0
    if not isinstance(text, str):
        raise TypeError("Argument must be a string or None")

    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def title_case(text: Optional[str]) -> str:
    """
    Convert a string to title case (capitalize first letter of each word).

    Args:
        text: Input string to convert

    Returns:
        String in title case format

    Raises:
        TypeError: If text is not a string or None
    """
    if text is None:
        return ""
    if not isinstance(text, str):
        raise TypeError("Argument must be a string or None")

    if not text:
        return ""

    return text.title()


def snake_to_camel(text: Optional[str]) -> str:
    """
    Convert snake_case string to camelCase.

    Args:
        text: Input string in snake_case format

    Returns:
        String in camelCase format

    Raises:
        TypeError: If text is not a string or None
    """
    if text is None:
        return ""
    if not isinstance(text, str):
        raise TypeError("Argument must be a string or None")

    if not text:
        return ""

    components = text.split('_')
    return components[0].lower() + ''.join(word.capitalize() for word in components[1:])


def camel_to_snake(text: Optional[str]) -> str:
    """
    Convert camelCase or PascalCase string to snake_case.

    Args:
        text: Input string in camelCase or PascalCase format

    Returns:
        String in snake_case format

    Raises:
        TypeError: If text is not a string or None
    """
    if text is None:
        return ""
    if not isinstance(text, str):
        raise TypeError("Argument must be a string or None")

    if not text:
        return ""

    result = re.sub(r'(?<!^)(?=[A-Z])', '_', text)
    return result.lower()
