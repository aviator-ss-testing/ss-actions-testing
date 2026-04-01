"""Tests for the string_utils module."""
import pytest
from string_utils import (
    reverse_string,
    is_palindrome,
    count_vowels,
    to_title_case,
    remove_whitespace
)


class TestReverseString:
    """Tests for reverse_string function."""

    def test_reverse_empty_string(self):
        """Test reversing an empty string."""
        assert reverse_string("") == ""

    def test_reverse_single_character(self):
        """Test reversing a single character."""
        assert reverse_string("a") == "a"
        assert reverse_string("Z") == "Z"

    def test_reverse_simple_word(self):
        """Test reversing a simple word."""
        assert reverse_string("hello") == "olleh"
        assert reverse_string("Python") == "nohtyP"

    def test_reverse_multi_word_string(self):
        """Test reversing multi-word strings."""
        assert reverse_string("hello world") == "dlrow olleh"
        assert reverse_string("The quick brown fox") == "xof nworb kciuq ehT"

    def test_reverse_with_special_characters(self):
        """Test reversing strings with special characters."""
        assert reverse_string("hello!") == "!olleh"
        assert reverse_string("a-b-c") == "c-b-a"


class TestIsPalindrome:
    """Tests for is_palindrome function."""

    def test_palindrome_simple(self):
        """Test simple palindromes."""
        assert is_palindrome("racecar") is True
        assert is_palindrome("level") is True
        assert is_palindrome("noon") is True

    def test_palindrome_single_character(self):
        """Test single character is a palindrome."""
        assert is_palindrome("a") is True
        assert is_palindrome("Z") is True

    def test_palindrome_empty_string(self):
        """Test empty string is a palindrome."""
        assert is_palindrome("") is True

    def test_palindrome_mixed_case(self):
        """Test palindromes with mixed case."""
        assert is_palindrome("RaceCar") is True
        assert is_palindrome("Level") is True
        assert is_palindrome("NoOn") is True

    def test_palindrome_with_spaces(self):
        """Test palindromes with spaces."""
        assert is_palindrome("race car") is True
        assert is_palindrome("A man a plan a canal Panama") is True
        assert is_palindrome("Was it a car or a cat I saw") is True

    def test_not_palindrome(self):
        """Test non-palindrome strings."""
        assert is_palindrome("hello") is False
        assert is_palindrome("world") is False
        assert is_palindrome("python") is False

    def test_not_palindrome_with_spaces(self):
        """Test non-palindrome strings with spaces."""
        assert is_palindrome("hello world") is False
        assert is_palindrome("not a palindrome") is False


class TestCountVowels:
    """Tests for count_vowels function."""

    def test_count_vowels_no_vowels(self):
        """Test strings with no vowels."""
        assert count_vowels("bcdfg") == 0
        assert count_vowels("xyz") == 0
        assert count_vowels("123") == 0

    def test_count_vowels_all_vowels(self):
        """Test strings with all vowels."""
        assert count_vowels("aeiou") == 5
        assert count_vowels("AEIOU") == 5
        assert count_vowels("aeiouAEIOU") == 10

    def test_count_vowels_mixed(self):
        """Test strings with mixed vowels and consonants."""
        assert count_vowels("hello") == 2
        assert count_vowels("world") == 1
        assert count_vowels("python") == 1
        assert count_vowels("beautiful") == 5

    def test_count_vowels_empty_string(self):
        """Test empty string has zero vowels."""
        assert count_vowels("") == 0

    def test_count_vowels_case_insensitive(self):
        """Test vowel counting is case-insensitive."""
        assert count_vowels("AEIOUaeiou") == 10
        assert count_vowels("HeLLo") == 2

    def test_count_vowels_with_spaces_and_punctuation(self):
        """Test vowel counting with spaces and punctuation."""
        assert count_vowels("Hello, World!") == 3
        assert count_vowels("The quick brown fox") == 5


class TestToTitleCase:
    """Tests for to_title_case function."""

    def test_title_case_simple_word(self):
        """Test converting simple words to title case."""
        assert to_title_case("hello") == "Hello"
        assert to_title_case("world") == "World"

    def test_title_case_multiple_words(self):
        """Test converting multiple words to title case."""
        assert to_title_case("hello world") == "Hello World"
        assert to_title_case("the quick brown fox") == "The Quick Brown Fox"

    def test_title_case_already_capitalized(self):
        """Test strings already in title case."""
        assert to_title_case("Hello World") == "Hello World"
        assert to_title_case("Python Programming") == "Python Programming"

    def test_title_case_all_caps(self):
        """Test converting all caps to title case."""
        assert to_title_case("HELLO WORLD") == "Hello World"
        assert to_title_case("PYTHON") == "Python"

    def test_title_case_all_lowercase(self):
        """Test converting all lowercase to title case."""
        assert to_title_case("hello world") == "Hello World"
        assert to_title_case("python programming language") == "Python Programming Language"

    def test_title_case_empty_string(self):
        """Test empty string remains empty."""
        assert to_title_case("") == ""

    def test_title_case_with_apostrophes(self):
        """Test title case with apostrophes."""
        assert to_title_case("don't") == "Don'T"
        assert to_title_case("it's a wonderful day") == "It'S A Wonderful Day"


class TestRemoveWhitespace:
    """Tests for remove_whitespace function."""

    def test_remove_whitespace_simple_spaces(self):
        """Test removing simple spaces."""
        assert remove_whitespace("hello world") == "helloworld"
        assert remove_whitespace("a b c") == "abc"

    def test_remove_whitespace_multiple_spaces(self):
        """Test removing multiple consecutive spaces."""
        assert remove_whitespace("hello    world") == "helloworld"
        assert remove_whitespace("a  b  c") == "abc"

    def test_remove_whitespace_tabs(self):
        """Test removing tabs."""
        assert remove_whitespace("hello\tworld") == "helloworld"
        assert remove_whitespace("a\tb\tc") == "abc"

    def test_remove_whitespace_newlines(self):
        """Test removing newlines."""
        assert remove_whitespace("hello\nworld") == "helloworld"
        assert remove_whitespace("line1\nline2\nline3") == "line1line2line3"

    def test_remove_whitespace_mixed(self):
        """Test removing mixed whitespace types."""
        assert remove_whitespace("hello \t\n world") == "helloworld"
        assert remove_whitespace("a \n b \t c") == "abc"

    def test_remove_whitespace_no_whitespace(self):
        """Test string with no whitespace."""
        assert remove_whitespace("helloworld") == "helloworld"
        assert remove_whitespace("python") == "python"

    def test_remove_whitespace_empty_string(self):
        """Test empty string remains empty."""
        assert remove_whitespace("") == ""

    def test_remove_whitespace_only_whitespace(self):
        """Test string with only whitespace."""
        assert remove_whitespace("   ") == ""
        assert remove_whitespace("\t\n\r") == ""

    def test_remove_whitespace_leading_trailing(self):
        """Test removing leading and trailing whitespace."""
        assert remove_whitespace("  hello  ") == "hello"
        assert remove_whitespace("\thello\n") == "hello"
