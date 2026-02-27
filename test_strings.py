"""Tests for the strings module."""
import pytest
from strings import is_palindrome, word_count, truncate, slugify


# is_palindrome tests

def test_palindrome_simple():
    assert is_palindrome("racecar") is True


def test_palindrome_case_insensitive():
    assert is_palindrome("Racecar") is True


def test_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_palindrome_non_palindrome():
    assert is_palindrome("hello") is False


def test_palindrome_empty():
    assert is_palindrome("") is True


def test_palindrome_single_char():
    assert is_palindrome("a") is True


def test_palindrome_spaces_only():
    assert is_palindrome("   ") is True


# word_count tests

def test_word_count_basic():
    assert word_count("hello world") == {"hello": 1, "world": 1}


def test_word_count_repeated():
    assert word_count("the cat sat on the mat") == {
        "the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1
    }


def test_word_count_case_insensitive():
    assert word_count("Hello hello HELLO") == {"hello": 3}


def test_word_count_empty():
    assert word_count("") == {}


def test_word_count_single_word():
    assert word_count("python") == {"python": 1}


# truncate tests

def test_truncate_exceeds_limit():
    assert truncate("Hello, world!", 5) == "Hello..."


def test_truncate_at_limit():
    assert truncate("Hello", 5) == "Hello"


def test_truncate_below_limit():
    assert truncate("Hi", 10) == "Hi"


def test_truncate_custom_suffix():
    assert truncate("Hello, world!", 5, suffix="--") == "Hello--"


def test_truncate_empty_string():
    assert truncate("", 5) == ""


def test_truncate_empty_suffix():
    assert truncate("Hello, world!", 5, suffix="") == "Hello"


# slugify tests

def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_special_characters():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_multiple_spaces():
    assert slugify("hello   world") == "hello-world"


def test_slugify_leading_trailing_dashes():
    assert slugify("  hello world  ") == "hello-world"


def test_slugify_empty():
    assert slugify("") == ""


def test_slugify_already_slug():
    assert slugify("hello-world") == "hello-world"


def test_slugify_numbers():
    assert slugify("Python 3.11 release") == "python-3-11-release"


def test_slugify_unicode_like_punctuation():
    assert slugify("café au lait") == "caf-au-lait"
