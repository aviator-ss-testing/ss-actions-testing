from .decorators import timer, memoize


@timer
def reverse_words(text):
    """
    Reverse the order of words in a string.

    Args:
        text: String to reverse word order

    Returns:
        String with words in reverse order

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Argument 'text' must be of type str, got {type(text).__name__}")

    words = text.split()
    return ' '.join(reversed(words))


def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in a string (case-insensitive).

    Args:
        text: String to count vowels in

    Returns:
        Integer count of vowels

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Argument 'text' must be of type str, got {type(text).__name__}")

    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)


@memoize
def is_palindrome(text):
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    Comparison is case-insensitive and ignores spaces.

    Args:
        text: String to check

    Returns:
        Boolean indicating if text is a palindrome

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Argument 'text' must be of type str, got {type(text).__name__}")

    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]


def title_case(text):
    """
    Convert a string to title case (first letter of each word capitalized).

    Args:
        text: String to convert

    Returns:
        String in title case

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Argument 'text' must be of type str, got {type(text).__name__}")

    return text.title()


def remove_duplicates(text):
    """
    Remove duplicate characters from a string while preserving order.

    Args:
        text: String to process

    Returns:
        String with duplicate characters removed

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Argument 'text' must be of type str, got {type(text).__name__}")

    seen = set()
    result = []

    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return ''.join(result)
