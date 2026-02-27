"""Tests for the strings module."""

import pytest
from strings import is_palindrome, word_count, truncate, slugify


# is_palindrome

def test_is_palindrome_simple():
    assert is_palindrome("racecar") is True


def test_is_palindrome_mixed_case():
    assert is_palindrome("Racecar") is True


def test_is_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_is_palindrome_not_palindrome():
    assert is_palindrome("hello") is False


def test_is_palindrome_empty():
    assert is_palindrome("") is True


def test_is_palindrome_single_char():
    assert is_palindrome("a") is True


def test_is_palindrome_spaces_only():
    assert is_palindrome("   ") is True


# word_count

def test_word_count_basic():
    assert word_count("hello world hello") == {"hello": 2, "world": 1}


def test_word_count_case_insensitive():
    assert word_count("Hello hello HELLO") == {"hello": 3}


def test_word_count_empty():
    assert word_count("") == {}


def test_word_count_single_word():
    assert word_count("python") == {"python": 1}


def test_word_count_multiple_spaces():
    assert word_count("a  b  a") == {"a": 2, "b": 1}


# truncate

def test_truncate_no_truncation_needed():
    assert truncate("hello", 10) == "hello"


def test_truncate_exact_length():
    assert truncate("hello", 5) == "hello"


def test_truncate_truncates():
    assert truncate("hello world", 5) == "hello..."


def test_truncate_custom_suffix():
    assert truncate("hello world", 5, suffix="!") == "hello!"


def test_truncate_empty_string():
    assert truncate("", 5) == ""


def test_truncate_empty_suffix():
    assert truncate("hello world", 5, suffix="") == "hello"


# slugify

def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_multiple_spaces():
    assert slugify("hello   world") == "hello-world"


def test_slugify_special_chars():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_leading_trailing_dashes():
    assert slugify("  hello  ") == "hello"


def test_slugify_empty():
    assert slugify("") == ""


def test_slugify_already_slug():
    assert slugify("hello-world") == "hello-world"


def test_slugify_numbers():
    assert slugify("Python 3.11 release") == "python-3-11-release"
