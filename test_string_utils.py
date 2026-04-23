"""Comprehensive tests for string_utils module."""

import pytest
from string_utils import (
    reverse_string,
    is_palindrome,
    word_count,
    title_case,
    strip_all_whitespace,
)


class TestReverseString:
    """Tests for reverse_string function."""

    def test_reverse_simple_string(self):
        assert reverse_string("hello") == "olleh"

    def test_reverse_empty_string(self):
        assert reverse_string("") == ""

    def test_reverse_single_character(self):
        assert reverse_string("a") == "a"

    def test_reverse_palindrome(self):
        assert reverse_string("racecar") == "racecar"

    def test_reverse_with_spaces(self):
        assert reverse_string("hello world") == "dlrow olleh"

    def test_reverse_with_special_characters(self):
        assert reverse_string("hello!@#") == "#@!olleh"

    def test_reverse_with_numbers(self):
        assert reverse_string("abc123") == "321cba"

    def test_reverse_unicode(self):
        assert reverse_string("café") == "éfac"


class TestIsPalindrome:
    """Tests for is_palindrome function."""

    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_palindrome_with_spaces(self):
        assert is_palindrome("race car") is True

    def test_palindrome_mixed_case(self):
        assert is_palindrome("RaceCar") is True

    def test_palindrome_sentence(self):
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_empty_string_is_palindrome(self):
        assert is_palindrome("") is True

    def test_single_character_is_palindrome(self):
        assert is_palindrome("a") is True

    def test_two_same_characters(self):
        assert is_palindrome("aa") is True

    def test_two_different_characters(self):
        assert is_palindrome("ab") is False

    def test_palindrome_with_multiple_spaces(self):
        assert is_palindrome("race  car") is True

    def test_palindrome_numbers_as_string(self):
        assert is_palindrome("12321") is True


class TestWordCount:
    """Tests for word_count function."""

    def test_simple_word_count(self):
        result = word_count("hello world hello")
        assert result == {"hello": 2, "world": 1}

    def test_empty_string(self):
        assert word_count("") == {}

    def test_single_word(self):
        assert word_count("hello") == {"hello": 1}

    def test_multiple_unique_words(self):
        result = word_count("the quick brown fox")
        assert result == {"the": 1, "quick": 1, "brown": 1, "fox": 1}

    def test_case_insensitive(self):
        result = word_count("Hello hello HELLO")
        assert result == {"hello": 3}

    def test_multiple_spaces(self):
        result = word_count("hello  world   hello")
        assert result == {"hello": 2, "world": 1}

    def test_with_punctuation_attached(self):
        result = word_count("hello, world! hello.")
        assert result == {"hello,": 1, "world!": 1, "hello.": 1}

    def test_sentence_with_duplicates(self):
        result = word_count("the cat and the dog and the bird")
        assert result == {"the": 3, "cat": 1, "and": 2, "dog": 1, "bird": 1}

    def test_whitespace_only(self):
        result = word_count("   ")
        assert result == {}


class TestTitleCase:
    """Tests for title_case function."""

    def test_simple_title_case(self):
        assert title_case("hello world") == "Hello World"

    def test_already_title_case(self):
        assert title_case("Hello World") == "Hello World"

    def test_all_uppercase(self):
        assert title_case("HELLO WORLD") == "Hello World"

    def test_all_lowercase(self):
        assert title_case("the quick brown fox") == "The Quick Brown Fox"

    def test_single_word(self):
        assert title_case("hello") == "Hello"

    def test_empty_string(self):
        assert title_case("") == ""

    def test_with_apostrophe(self):
        assert title_case("don't stop") == "Don'T Stop"

    def test_with_hyphen(self):
        assert title_case("well-known") == "Well-Known"

    def test_multiple_spaces(self):
        assert title_case("hello  world") == "Hello  World"

    def test_mixed_case_input(self):
        assert title_case("hElLo WoRlD") == "Hello World"


class TestStripAllWhitespace:
    """Tests for strip_all_whitespace function."""

    def test_simple_spaces(self):
        assert strip_all_whitespace("hello world") == "helloworld"

    def test_multiple_spaces(self):
        assert strip_all_whitespace("hello   world") == "helloworld"

    def test_leading_trailing_spaces(self):
        assert strip_all_whitespace("  hello world  ") == "helloworld"

    def test_no_spaces(self):
        assert strip_all_whitespace("helloworld") == "helloworld"

    def test_empty_string(self):
        assert strip_all_whitespace("") == ""

    def test_only_spaces(self):
        assert strip_all_whitespace("     ") == ""

    def test_tabs_and_newlines(self):
        assert strip_all_whitespace("hello\tworld\n") == "helloworld"

    def test_mixed_whitespace(self):
        assert strip_all_whitespace("hello \t\n world") == "helloworld"

    def test_single_word(self):
        assert strip_all_whitespace("hello") == "hello"

    def test_complex_whitespace(self):
        assert strip_all_whitespace("  the  quick \t brown \n fox  ") == "thequickbrownfox"


class TestIntegration:
    """Integration tests combining multiple functions."""

    def test_palindrome_after_strip_whitespace(self):
        text = "race car"
        stripped = strip_all_whitespace(text)
        assert is_palindrome(stripped) is True

    def test_reverse_title_case(self):
        text = "hello world"
        titled = title_case(text)
        reversed_titled = reverse_string(titled)
        assert reversed_titled == "dlroW olleH"

    def test_word_count_after_strip(self):
        text = "  hello   world  hello  "
        count = word_count(text)
        assert count == {"hello": 2, "world": 1}

    def test_empty_string_all_functions(self):
        assert reverse_string("") == ""
        assert is_palindrome("") is True
        assert word_count("") == {}
        assert title_case("") == ""
        assert strip_all_whitespace("") == ""
