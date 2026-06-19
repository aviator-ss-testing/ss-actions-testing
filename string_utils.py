"""String manipulation utilities for various text operations."""


def reverse_string(s: str) -> str:
    """Reverse a string.

    Args:
        s: The string to reverse

    Returns:
        The reversed string
    """
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive, ignoring spaces).

    Args:
        s: The string to check

    Returns:
        True if the string is a palindrome, False otherwise
    """
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    """Count the number of vowels in a string.

    Args:
        s: The string to count vowels in

    Returns:
        The number of vowels (a, e, i, o, u) in the string, case-insensitive
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def to_title_case(s: str) -> str:
    """Convert a string to title case.

    Args:
        s: The string to convert

    Returns:
        The string in title case (first letter of each word capitalized)
    """
    return s.title()


def remove_whitespace(s: str) -> str:
    """Remove all whitespace from a string.

    Args:
        s: The string to remove whitespace from

    Returns:
        The string with all whitespace removed
    """
    return "".join(s.split())
