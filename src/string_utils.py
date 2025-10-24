"""String utility functions for common text operations."""


def reverse_string(s):
    """
    Reverse a string.

    Args:
        s (str): The string to reverse

    Returns:
        str: The reversed string

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError("reverse_string() argument must be a string")
    return s[::-1]


def is_palindrome(s):
    """
    Check if a string is a palindrome (case-insensitive).

    A palindrome is a string that reads the same forwards and backwards.

    Args:
        s (str): The string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError("is_palindrome() argument must be a string")
    normalized = s.lower()
    return normalized == normalized[::-1]


def word_count(text):
    """
    Count the number of words in text.

    Words are defined as sequences of non-whitespace characters separated by
    whitespace. Multiple whitespace characters are treated as a single separator.

    Args:
        text (str): The text to count words in

    Returns:
        int: The number of words in the text

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("word_count() argument must be a string")
    if not text or text.isspace():
        return 0
    return len(text.split())


def title_case(s):
    """
    Convert a string to title case.

    Title case capitalizes the first letter of each word and makes all other
    letters lowercase.

    Args:
        s (str): The string to convert

    Returns:
        str: The string in title case

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError("title_case() argument must be a string")
    return s.title()


def remove_duplicates(s):
    """
    Remove consecutive duplicate characters from a string.

    Only consecutive duplicates are removed. Non-consecutive duplicates are kept.

    Args:
        s (str): The string to process

    Returns:
        str: The string with consecutive duplicates removed

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError("remove_duplicates() argument must be a string")
    if not s:
        return s
    result = [s[0]]
    for char in s[1:]:
        if char != result[-1]:
            result.append(char)
    return ''.join(result)


def truncate(s, length, suffix='...'):
    """
    Truncate a string to a specified length and add a suffix if truncated.

    If the string is shorter than or equal to the specified length, it is
    returned unchanged. Otherwise, it is truncated and the suffix is appended.

    Args:
        s (str): The string to truncate
        length (int): The maximum length before truncation (not including suffix)
        suffix (str): The suffix to append if truncated (default: '...')

    Returns:
        str: The truncated string with suffix, or the original string if no
             truncation was needed

    Raises:
        TypeError: If s is not a string, length is not an integer, or suffix
                   is not a string
        ValueError: If length is negative
    """
    if not isinstance(s, str):
        raise TypeError("truncate() argument 's' must be a string")
    if not isinstance(length, int):
        raise TypeError("truncate() argument 'length' must be an integer")
    if not isinstance(suffix, str):
        raise TypeError("truncate() argument 'suffix' must be a string")
    if length < 0:
        raise ValueError("truncate() argument 'length' must be non-negative")
    if len(s) <= length:
        return s
    return s[:length] + suffix
