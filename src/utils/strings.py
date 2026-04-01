"""String manipulation utilities.

This module provides common string manipulation functions including
reversing words, palindrome checking, vowel counting, title casing,
and duplicate character removal.
"""


def reverse_words(text):
    """Reverse the order of words in a string.

    Args:
        text (str): The input string to reverse words in

    Returns:
        str: String with words in reversed order

    Examples:
        >>> reverse_words("hello world")
        'world hello'
        >>> reverse_words("one two three")
        'three two one'
        >>> reverse_words("single")
        'single'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    words = text.split()
    return ' '.join(reversed(words))


def is_palindrome(text):
    """Check if a string is a palindrome (case-insensitive).

    Args:
        text (str): The input string to check

    Returns:
        bool: True if text is palindrome, False otherwise

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("RaceCar")
        True
        >>> is_palindrome("hello")
        False
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    cleaned = text.lower().replace(' ', '')
    return cleaned == cleaned[::-1]


def count_vowels(text):
    """Count the number of vowels in a string.

    Args:
        text (str): The input string to count vowels in

    Returns:
        int: Number of vowel occurrences (a, e, i, o, u)

    Examples:
        >>> count_vowels("hello")
        2
        >>> count_vowels("AEIOU")
        5
        >>> count_vowels("rhythm")
        0
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def title_case(text):
    """Convert a string to title case.

    Args:
        text (str): The input string to convert

    Returns:
        str: String with each word capitalized

    Examples:
        >>> title_case("hello world")
        'Hello World'
        >>> title_case("the quick brown fox")
        'The Quick Brown Fox'
        >>> title_case("ALREADY UPPERCASE")
        'Already Uppercase'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return ' '.join(word.capitalize() for word in text.split())


def remove_duplicates(text):
    """Remove duplicate characters while preserving order.

    Args:
        text (str): The input string

    Returns:
        str: String with duplicates removed, first occurrence preserved

    Examples:
        >>> remove_duplicates("hello")
        'helo'
        >>> remove_duplicates("aabbcc")
        'abc'
        >>> remove_duplicates("abcdef")
        'abcdef'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
