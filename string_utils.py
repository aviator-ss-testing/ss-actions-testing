"""
String utility functions for text processing and validation.

This module provides various string manipulation functions including
text reversal, vowel counting, palindrome detection, word capitalization,
and duplicate character removal.
"""

from typing import Union


def reverse_string(text: str) -> str:
    """
    Reverse the order of characters in a string.

    Args:
        text (str): The input string to reverse

    Returns:
        str: The reversed string

    Raises:
        TypeError: If input is not a string

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'
        >>> reverse_string("")
        ''
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}")

    return text[::-1]


def count_vowels(text: str, case_sensitive: bool = False) -> int:
    """
    Count the number of vowels in a string.

    Args:
        text (str): The input string to analyze
        case_sensitive (bool): Whether to consider case when counting vowels

    Returns:
        int: The number of vowels found

    Raises:
        TypeError: If input is not a string

    Examples:
        >>> count_vowels("hello world")
        3
        >>> count_vowels("HELLO WORLD")
        3
        >>> count_vowels("HELLO WORLD", case_sensitive=True)
        3
        >>> count_vowels("xyz")
        0
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}")

    vowels = "aeiou" if case_sensitive else "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def is_palindrome(text: str, ignore_case: bool = True, ignore_spaces: bool = True) -> bool:
    """
    Check if a string is a palindrome (reads the same forwards and backwards).

    Args:
        text (str): The input string to check
        ignore_case (bool): Whether to ignore case differences
        ignore_spaces (bool): Whether to ignore spaces and punctuation

    Returns:
        bool: True if the string is a palindrome, False otherwise

    Raises:
        TypeError: If input is not a string

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("Aa", ignore_case=False)
        False
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}")

    processed_text = text

    if ignore_case:
        processed_text = processed_text.lower()

    if ignore_spaces:
        processed_text = ''.join(char for char in processed_text if char.isalnum())

    return processed_text == processed_text[::-1]


def capitalize_words(text: str, separator: str = " ") -> str:
    """
    Capitalize the first letter of each word in a string.

    Args:
        text (str): The input string to capitalize
        separator (str): The separator to split words on (default: space)

    Returns:
        str: The string with each word capitalized

    Raises:
        TypeError: If input is not a string

    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("python programming")
        'Python Programming'
        >>> capitalize_words("hello-world", separator="-")
        'Hello-World'
        >>> capitalize_words("")
        ''
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}")

    if not isinstance(separator, str):
        raise TypeError(f"Separator must be a string, got {type(separator).__name__}")

    if not text:
        return text

    words = text.split(separator)
    capitalized_words = [word.capitalize() if word else word for word in words]
    return separator.join(capitalized_words)


def remove_duplicates(text: str, preserve_order: bool = True) -> str:
    """
    Remove duplicate characters from a string.

    Args:
        text (str): The input string to process
        preserve_order (bool): Whether to preserve the original order of characters

    Returns:
        str: The string with duplicate characters removed

    Raises:
        TypeError: If input is not a string

    Examples:
        >>> remove_duplicates("hello")
        'helo'
        >>> remove_duplicates("programming")
        'progamin'
        >>> remove_duplicates("aabbcc")
        'abc'
        >>> remove_duplicates("")
        ''
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}")

    if not text:
        return text

    if preserve_order:
        seen = set()
        result = []
        for char in text:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)
    else:
        return ''.join(sorted(set(text)))


if __name__ == "__main__":
    print("String Utilities Demo:")
    print("-" * 30)

    test_string = "Hello World"
    print(f"Original string: '{test_string}'")
    print(f"Reversed: '{reverse_string(test_string)}'")
    print(f"Vowel count: {count_vowels(test_string)}")
    print(f"Is palindrome: {is_palindrome(test_string)}")
    print(f"Capitalized: '{capitalize_words(test_string.lower())}'")
    print(f"Duplicates removed: '{remove_duplicates(test_string.lower())}'")

    print("\nPalindrome tests:")
    palindromes = ["racecar", "A man a plan a canal Panama", "hello"]
    for text in palindromes:
        print(f"'{text}' -> {is_palindrome(text)}")