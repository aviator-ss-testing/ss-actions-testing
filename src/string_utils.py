def reverse_string(s):
    """
    Reverse a string using Python slicing.

    Args:
        s: The string to reverse

    Returns:
        str: The reversed string

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")
    return s[::-1]


def is_palindrome(s):
    """
    Check if a string is a palindrome (case-insensitive).

    A palindrome reads the same forwards and backwards, ignoring case.

    Args:
        s: The string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")
    normalized = s.lower()
    return normalized == normalized[::-1]


def word_count(text):
    """
    Count the number of words in a text string.

    Words are separated by whitespace. Multiple consecutive whitespace
    characters are treated as a single separator.

    Args:
        text: The text string to count words in

    Returns:
        int: The number of words in the text

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}")
    if not text or text.isspace():
        return 0
    return len(text.split())


def title_case(s):
    """
    Convert a string to title case.

    Title case capitalizes the first letter of each word.

    Args:
        s: The string to convert

    Returns:
        str: The string in title case

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")
    return s.title()


def remove_duplicates(s):
    """
    Remove consecutive duplicate characters from a string.

    Only consecutive duplicates are removed. For example, "aabbcc" becomes "abc",
    but "abcabc" remains "abcabc".

    Args:
        s: The string to process

    Returns:
        str: String with consecutive duplicates removed

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")
    if not s:
        return s

    result = [s[0]]
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            result.append(s[i])

    return ''.join(result)


def truncate(s, length, suffix='...'):
    """
    Truncate a string to a specified length, adding a suffix if truncated.

    If the string is shorter than or equal to the specified length, it is
    returned unchanged. Otherwise, it is truncated and the suffix is appended.

    Args:
        s: The string to truncate
        length: Maximum length before truncation (must be non-negative)
        suffix: String to append after truncation (default: '...')

    Returns:
        str: The truncated string with suffix, or original string if no truncation needed

    Raises:
        TypeError: If s is not a string, length is not an integer, or suffix is not a string
        ValueError: If length is negative
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string for s, got {type(s).__name__}")
    if not isinstance(length, int):
        raise TypeError(f"Expected int for length, got {type(length).__name__}")
    if not isinstance(suffix, str):
        raise TypeError(f"Expected string for suffix, got {type(suffix).__name__}")
    if length < 0:
        raise ValueError("length must be non-negative")

    if len(s) <= length:
        return s

    return s[:length] + suffix
