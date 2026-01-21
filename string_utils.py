def reverse_string(s: str) -> str:
    """
    Reverse the input string.

    Args:
        s: The string to reverse

    Returns:
        The reversed string

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("")
        ''
    """
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """
    Check if a string reads the same forwards and backwards.
    Comparison is case-insensitive and ignores whitespace.

    Args:
        s: The string to check

    Returns:
        True if the string is a palindrome, False otherwise

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("RaceCar")
        True
        >>> is_palindrome("hello")
        False
    """
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def word_count(s: str) -> int:
    """
    Count the number of words in a string.
    Words are separated by whitespace.

    Args:
        s: The string to count words in

    Returns:
        The number of words in the string

    Examples:
        >>> word_count("hello world")
        2
        >>> word_count("")
        0
        >>> word_count("   multiple   spaces   ")
        2
    """
    if not s or not s.strip():
        return 0
    return len(s.split())


def title_case(s: str) -> str:
    """
    Capitalize the first letter of each word in a string.

    Args:
        s: The string to convert to title case

    Returns:
        The string with the first letter of each word capitalized

    Examples:
        >>> title_case("hello world")
        'Hello World'
        >>> title_case("HELLO WORLD")
        'Hello World'
        >>> title_case("")
        ''
    """
    return s.title()
