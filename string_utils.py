"""String utility functions for common text operations."""

import re


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive, ignoring spaces)."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def word_count(s: str) -> dict[str, int]:
    """Count the occurrences of each word in a string."""
    words = s.lower().split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def to_snake_case(s: str) -> str:
    """Convert camelCase or PascalCase string to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def truncate(s: str, max_len: int, suffix: str = "...") -> str:
    """Truncate a string to max_len characters, appending suffix if truncated."""
    if len(s) <= max_len:
        return s
    return s[:max_len - len(suffix)] + suffix
