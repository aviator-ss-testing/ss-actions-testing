"""Tests for the strings module."""

import pytest
from strings import is_palindrome, word_count, truncate, slugify


# --- is_palindrome ---

def test_is_palindrome_simple():
    assert is_palindrome("racecar") is True


def test_is_palindrome_case_insensitive():
    assert is_palindrome("Racecar") is True


def test_is_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_is_palindrome_not_palindrome():
    assert is_palindrome("hello") is False


def test_is_palindrome_empty():
    assert is_palindrome("") is True


def test_is_palindrome_single_char():
    assert is_palindrome("a") is True


def test_is_palindrome_numbers():
    assert is_palindrome("12321") is True


# --- word_count ---

def test_word_count_basic():
    assert word_count("hello world") == {"hello": 1, "world": 1}


def test_word_count_repeated_words():
    assert word_count("the cat sat on the mat") == {
        "the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1
    }


def test_word_count_case_insensitive():
    assert word_count("Hello hello HELLO") == {"hello": 3}


def test_word_count_empty():
    assert word_count("") == {}


def test_word_count_punctuation_stripped():
    result = word_count("hello, world!")
    assert result == {"hello": 1, "world": 1}


def test_word_count_unicode():
    result = word_count("café café")
    assert result.get("caf") == 2 or "café" in result or "caf" in result


# --- truncate ---

def test_truncate_no_truncation_needed():
    assert truncate("hello", 10) == "hello"


def test_truncate_exact_length():
    assert truncate("hello", 5) == "hello"


def test_truncate_truncates_with_default_suffix():
    assert truncate("hello world", 5) == "hello..."


def test_truncate_custom_suffix():
    assert truncate("hello world", 5, suffix="--") == "hello--"


def test_truncate_empty_string():
    assert truncate("", 5) == ""


def test_truncate_empty_suffix():
    assert truncate("hello world", 5, suffix="") == "hello"


# --- slugify ---

def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_multiple_spaces():
    assert slugify("Hello   World") == "hello-world"


def test_slugify_special_characters():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_leading_trailing_dashes():
    assert slugify("  Hello World  ") == "hello-world"


def test_slugify_empty():
    assert slugify("") == ""


def test_slugify_already_slug():
    assert slugify("hello-world") == "hello-world"


def test_slugify_numbers():
    assert slugify("Section 42") == "section-42"
