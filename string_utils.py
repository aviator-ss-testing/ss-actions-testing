"""String utility functions for common string operations."""

from typing import Optional
import re


def is_palindrome(text: Optional[str]) -> bool:
    """
    Check if a string is a palindrome (reads the same forwards and backwards).

    Ignores case, spaces, and punctuation. Returns False for None or empty strings.

    Args:
        text: The string to check

    Returns:
        True if the string is a palindrome, False otherwise

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False
    """
    if text is None or text == "":
        return False

    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()

    if not cleaned:
        return False

    return cleaned == cleaned[::-1]


def reverse_words(text: Optional[str]) -> str:
    """
    Reverse the order of words in a string.

    Words are separated by whitespace. Returns empty string for None input.

    Args:
        text: The string containing words to reverse

    Returns:
        String with words in reversed order

    Examples:
        >>> reverse_words("hello world")
        "world hello"
        >>> reverse_words("one two three")
        "three two one"
    """
    if text is None:
        return ""

    if text == "":
        return ""

    words = text.split()
    return " ".join(reversed(words))


def camel_to_snake(text: Optional[str]) -> str:
    """
    Convert camelCase or PascalCase string to snake_case.

    Args:
        text: The camelCase or PascalCase string to convert

    Returns:
        String in snake_case format, empty string for None input

    Examples:
        >>> camel_to_snake("camelCase")
        "camel_case"
        >>> camel_to_snake("PascalCase")
        "pascal_case"
        >>> camel_to_snake("alreadySnake_case")
        "already_snake_case"
    """
    if text is None:
        return ""

    if text == "":
        return ""

    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def snake_to_camel(text: Optional[str], capitalize_first: bool = False) -> str:
    """
    Convert snake_case string to camelCase or PascalCase.

    Args:
        text: The snake_case string to convert
        capitalize_first: If True, return PascalCase; if False, return camelCase

    Returns:
        String in camelCase or PascalCase format, empty string for None input

    Examples:
        >>> snake_to_camel("snake_case")
        "snakeCase"
        >>> snake_to_camel("snake_case", capitalize_first=True)
        "SnakeCase"
        >>> snake_to_camel("already_camel")
        "alreadyCamel"
    """
    if text is None:
        return ""

    if text == "":
        return ""

    components = text.split('_')

    if capitalize_first:
        return ''.join(word.capitalize() for word in components)
    else:
        return components[0] + ''.join(word.capitalize() for word in components[1:])


def count_vowels(text: Optional[str], include_y: bool = False) -> int:
    """
    Count the number of vowels in a string.

    Args:
        text: The string to count vowels in
        include_y: If True, treat 'y' as a vowel

    Returns:
        Number of vowels found (case-insensitive), 0 for None input

    Examples:
        >>> count_vowels("hello")
        2
        >>> count_vowels("rhythm")
        0
        >>> count_vowels("rhythm", include_y=True)
        1
    """
    if text is None:
        return 0

    vowels = "aeiouAEIOU"
    if include_y:
        vowels += "yY"

    return sum(1 for char in text if char in vowels)


def truncate_string(text: Optional[str], max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length, adding a suffix if truncated.

    Args:
        text: The string to truncate
        max_length: Maximum length of the result (including suffix)
        suffix: String to append when truncating (default: "...")

    Returns:
        Truncated string with suffix, or original string if shorter than max_length.
        Returns empty string for None input.

    Raises:
        ValueError: If max_length is less than the length of suffix

    Examples:
        >>> truncate_string("hello world", 8)
        "hello..."
        >>> truncate_string("short", 10)
        "short"
        >>> truncate_string("hello world", 8, suffix=">>")
        "hello>>"
    """
    if text is None:
        return ""

    if max_length < len(suffix):
        raise ValueError(f"max_length ({max_length}) must be at least {len(suffix)} (length of suffix)")

    if len(text) <= max_length:
        return text

    truncate_at = max_length - len(suffix)
    return text[:truncate_at] + suffix
