"""Tests for the strings module."""
import pytest
from strings import (
    capitalize_words,
    count_vowels,
    is_anagram,
    is_palindrome,
    reverse,
    truncate,
)


def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert is_palindrome("")
    assert is_palindrome("a")
    assert not is_palindrome("hello")


def test_reverse():
    assert reverse("hello") == "olleh"
    assert reverse("") == ""
    assert reverse("a") == "a"
    assert reverse("ab") == "ba"


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("") == ""
    assert capitalize_words("python") == "Python"
    assert capitalize_words("a b c") == "A B C"


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("") == 0
    assert count_vowels("xyz") == 0


def test_is_anagram():
    assert is_anagram("listen", "silent")
    assert is_anagram("Astronomer", "Moon starer")
    assert not is_anagram("hello", "world")
    assert is_anagram("", "")


def test_truncate():
    assert truncate("hello world", 5) == "he..."
    assert truncate("hello", 10) == "hello"
    assert truncate("hello", 5) == "hello"
    assert truncate("hello world", 8, suffix="…") == "hello w…"
    assert truncate("hello", 2) == ".."


def test_truncate_negative_max_len():
    with pytest.raises(ValueError, match="max_len must be non-negative"):
        truncate("hello", -1)
