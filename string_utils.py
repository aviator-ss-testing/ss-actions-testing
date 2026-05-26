"""String utility functions for common string manipulation operations."""


def reverse_string(s):
    """
    Reverse a string.

    Args:
        s: String to reverse

    Returns:
        Reversed string

    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")
    return s[::-1]


def is_palindrome(s):
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    Case-insensitive and ignores whitespace.

    Args:
        s: String to check

    Returns:
        True if palindrome, False otherwise

    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")

    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_vowels(s):
    """
    Count the number of vowels in a string.

    Args:
        s: String to count vowels in

    Returns:
        Number of vowels (a, e, i, o, u) - case insensitive

    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")

    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def title_case(s):
    """
    Convert string to title case (first letter of each word capitalized).

    Args:
        s: String to convert

    Returns:
        String in title case

    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")

    return s.title()


def remove_whitespace(s, mode="all"):
    """
    Remove whitespace from a string.

    Args:
        s: String to process
        mode: 'all' (remove all whitespace), 'leading' (remove leading),
              'trailing' (remove trailing), or 'both' (remove leading and trailing)

    Returns:
        String with whitespace removed according to mode

    Raises:
        TypeError: If input is not a string
        ValueError: If mode is not valid
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")

    valid_modes = ["all", "leading", "trailing", "both"]
    if mode not in valid_modes:
        raise ValueError(f"Invalid mode '{mode}'. Must be one of {valid_modes}")

    if mode == "all":
        return "".join(s.split())
    elif mode == "leading":
        return s.lstrip()
    elif mode == "trailing":
        return s.rstrip()
    elif mode == "both":
        return s.strip()


def truncate(s, length, ellipsis=True):
    """
    Truncate a string to a specified length.

    Args:
        s: String to truncate
        length: Maximum length (must be non-negative)
        ellipsis: If True, add '...' to truncated strings (default: True)

    Returns:
        Truncated string

    Raises:
        TypeError: If input is not a string or length is not an integer
        ValueError: If length is negative
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")
    if not isinstance(length, int):
        raise TypeError(f"Length must be integer, got {type(length).__name__}")
    if length < 0:
        raise ValueError("Length must be non-negative")

    if len(s) <= length:
        return s

    if ellipsis:
        if length < 3:
            return s[:length]
        return s[:length - 3] + "..."
    else:
        return s[:length]
