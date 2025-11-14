def reverse_string(text: str) -> str:
    """Return the reversed version of the input string.

    Args:
        text: The string to reverse

    Returns:
        The reversed string
    """
    return text[::-1]


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in the string.

    Args:
        text: The string to capitalize

    Returns:
        The string with each word capitalized
    """
    return text.title()


def count_vowels(text: str) -> int:
    """Count the number of vowels in the string.

    Args:
        text: The string to count vowels in

    Returns:
        The number of vowels (a, e, i, o, u) in the string, case-insensitive
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def is_palindrome(text: str) -> bool:
    """Check if the string is a palindrome.

    Args:
        text: The string to check

    Returns:
        True if the string is a palindrome (reads the same forwards and backwards),
        False otherwise. Case-insensitive and ignores spaces.
    """
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
