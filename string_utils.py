"""String utility functions for common string manipulation tasks."""


def reverse_string(s: str) -> str:
    """
    Reverse a string.

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
    Check if a string is a palindrome, ignoring case and spaces.

    Args:
        s: The string to check

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
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def word_count(text: str) -> dict[str, int]:
    """
    Count the frequency of each word in the text.

    Args:
        text: The text to analyze

    Returns:
        A dictionary mapping each word to its frequency

    Examples:
        >>> word_count("hello world hello")
        {'hello': 2, 'world': 1}
        >>> word_count("")
        {}
    """
    if not text:
        return {}

    words = text.lower().split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def title_case(s: str) -> str:
    """
    Convert a string to title case (capitalize first letter of each word).

    Args:
        s: The string to convert

    Returns:
        The string in title case

    Examples:
        >>> title_case("hello world")
        'Hello World'
        >>> title_case("the quick brown fox")
        'The Quick Brown Fox'
    """
    return s.title()


def strip_all_whitespace(s: str) -> str:
    """
    Remove all whitespace from a string.

    Args:
        s: The string to process

    Returns:
        The string with all whitespace removed

    Examples:
        >>> strip_all_whitespace("hello world")
        'helloworld'
        >>> strip_all_whitespace("  multiple   spaces  ")
        'multiplespaces'
    """
    return "".join(s.split())
