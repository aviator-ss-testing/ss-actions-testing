"""String utility module for testing CI workflows."""


def is_palindrome(s: str) -> bool:
    """Check if a string reads the same forwards and backwards."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


def reverse(s: str) -> str:
    """Return the input with characters in reverse order."""
    return s[::-1]


def capitalize_words(s: str) -> str:
    """Uppercase the first character of each whitespace-separated word."""
    return ' '.join(word.capitalize() for word in s.split())


def count_vowels(s: str) -> int:
    """Count a/e/i/o/u characters case-insensitively."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


def is_anagram(s1: str, s2: str) -> bool:
    """Check if two strings contain the same letters disregarding case and whitespace."""
    cleaned1 = ''.join(char.lower() for char in s1 if not char.isspace())
    cleaned2 = ''.join(char.lower() for char in s2 if not char.isspace())
    return sorted(cleaned1) == sorted(cleaned2)


def truncate(s: str, max_len: int, suffix: str = "...") -> str:
    """Truncate strings longer than max_len with the supplied suffix."""
    if max_len < 0:
        raise ValueError("max_len cannot be negative")
    if len(s) <= max_len:
        return s
    return s[:max_len - len(suffix)] + suffix
