"""String utility functions."""
import re


def is_palindrome(s: str) -> bool:
    """Check if a string reads the same forwards and backwards.

    Case-insensitive, ignores non-alphanumeric characters.
    """
    cleaned = re.sub(r"[^a-z0-9]", "", s.lower())
    return cleaned == cleaned[::-1]


def reverse(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def capitalize_words(s: str) -> str:
    """Capitalize the first letter of each whitespace-separated word."""
    return " ".join(word[:1].upper() + word[1:] for word in s.split(" "))


def count_vowels(s: str) -> int:
    """Count vowels (a, e, i, o, u) in a string, case-insensitive."""
    return sum(1 for c in s.lower() if c in "aeiou")


def is_anagram(a: str, b: str) -> bool:
    """Check if two strings are anagrams, ignoring case and whitespace."""
    return sorted(a.lower().replace(" ", "")) == sorted(b.lower().replace(" ", ""))


def truncate(s: str, max_len: int, suffix: str = "...") -> str:
    """Truncate s to max_len characters, appending suffix if truncation occurs."""
    if max_len < 0:
        raise ValueError("max_len must be non-negative")
    if len(s) <= max_len:
        return s
    if max_len <= len(suffix):
        return suffix[:max_len]
    return s[: max_len - len(suffix)] + suffix
