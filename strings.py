"""String utility functions."""

import re


def is_palindrome(s: str) -> bool:
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    return cleaned == cleaned[::-1]


def word_count(s: str) -> dict[str, int]:
    words = s.lower().split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def truncate(s: str, max_len: int, suffix: str = "...") -> str:
    if len(s) <= max_len:
        return s
    return s[:max_len] + suffix


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")
