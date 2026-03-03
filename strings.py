"""String utility functions using only the Python standard library."""

import re


def is_palindrome(s: str) -> bool:
    cleaned = re.sub(r"[^a-z0-9]", "", s.lower())
    return cleaned == cleaned[::-1]


def word_count(s: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in s.lower().split():
        stripped = re.sub(r"[^a-z0-9']", "", word)
        if stripped:
            counts[stripped] = counts.get(stripped, 0) + 1
    return counts


def truncate(s: str, max_len: int, suffix: str = "...") -> str:
    if len(s) <= max_len:
        return s
    return s[:max_len] + suffix


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")
