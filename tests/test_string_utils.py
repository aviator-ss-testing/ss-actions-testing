"""Tests for string manipulation utilities.

This module contains comprehensive tests for all string utility functions
including reverse_string, is_palindrome, title_case, and count_words.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils.string_utils import reverse_string, is_palindrome, title_case, count_words


class TestReverseString:
    """Tests for the reverse_string function."""

    @pytest.mark.parametrize("input_str,expected", [
        ("hello", "olleh"),
        ("world", "dlrow"),
        ("Python", "nohtyP"),
        ("a", "a"),
        ("ab", "ba"),
        ("racecar", "racecar"),
    ])
    def test_reverse_string_normal_cases(self, input_str, expected):
        """Test reverse_string with normal string inputs."""
        assert reverse_string(input_str) == expected

    def test_reverse_string_empty(self):
        """Test reverse_string with empty string."""
        assert reverse_string("") == ""

    @pytest.mark.parametrize("input_str,expected", [
        ("hello world", "dlrow olleh"),
        ("  spaces  ", "  secaps  "),
        ("\ttabs\t", "\tsbat\t"),
        ("\nlines\n", "\nsenil\n"),
    ])
    def test_reverse_string_with_whitespace(self, input_str, expected):
        """Test reverse_string with various whitespace characters."""
        assert reverse_string(input_str) == expected

    @pytest.mark.parametrize("input_str,expected", [
        ("hello!", "!olleh"),
        ("what?", "?tahw"),
        ("test@123", "321@tset"),
        ("$100.00", "00.001$"),
        ("a-b_c+d", "d+c_b-a"),
    ])
    def test_reverse_string_with_special_characters(self, input_str, expected):
        """Test reverse_string with special characters."""
        assert reverse_string(input_str) == expected

    @pytest.mark.parametrize("input_str,expected", [
        ("hello🌍", "🌍olleh"),
        ("🎉🎊🎈", "🎈🎊🎉"),
        ("café", "éfac"),
        ("日本語", "語本日"),
    ])
    def test_reverse_string_with_unicode(self, input_str, expected):
        """Test reverse_string with unicode characters including emojis."""
        assert reverse_string(input_str) == expected

    def test_reverse_string_long_string(self):
        """Test reverse_string with a long string."""
        input_str = "a" * 1000
        expected = "a" * 1000
        assert reverse_string(input_str) == expected


class TestIsPalindrome:
    """Tests for the is_palindrome function."""

    @pytest.mark.parametrize("input_str,expected", [
        ("racecar", True),
        ("level", True),
        ("noon", True),
        ("radar", True),
        ("a", True),
        ("aa", True),
    ])
    def test_is_palindrome_true_cases(self, input_str, expected):
        """Test is_palindrome with strings that are palindromes."""
        assert is_palindrome(input_str) == expected

    @pytest.mark.parametrize("input_str,expected", [
        ("hello", False),
        ("world", False),
        ("Python", False),
        ("ab", False),
        ("abc", False),
    ])
    def test_is_palindrome_false_cases(self, input_str, expected):
        """Test is_palindrome with strings that are not palindromes."""
        assert is_palindrome(input_str) == expected

    @pytest.mark.parametrize("input_str,expected", [
        ("RaceCar", True),
        ("Level", True),
        ("NOON", True),
        ("RaDaR", True),
        ("A", True),
    ])
    def test_is_palindrome_mixed_case(self, input_str, expected):
        """Test is_palindrome with mixed case strings."""
        assert is_palindrome(input_str) == expected

    def test_is_palindrome_empty_string(self):
        """Test is_palindrome with empty string."""
        assert is_palindrome("") is True

    @pytest.mark.parametrize("input_str,expected", [
        ("race car", False),
        ("a man a plan a canal panama", False),
        ("  ", True),
        ("a a", True),
        ("ab ba", True),
        ("ab cd", False),
    ])
    def test_is_palindrome_with_spaces(self, input_str, expected):
        """Test is_palindrome with spaces."""
        assert is_palindrome(input_str) == expected

    @pytest.mark.parametrize("input_str,expected", [
        ("12321", True),
        ("12345", False),
        ("a1b1a", True),
        ("!@#@!", True),
    ])
    def test_is_palindrome_with_numbers_and_special_chars(self, input_str, expected):
        """Test is_palindrome with numbers and special characters."""
        assert is_palindrome(input_str) == expected


class TestTitleCase:
    """Tests for the title_case function."""

    @pytest.mark.parametrize("input_str,expected", [
        ("hello world", "Hello World"),
        ("python programming", "Python Programming"),
        ("the quick brown fox", "The Quick Brown Fox"),
        ("a b c", "A B C"),
    ])
    def test_title_case_normal_cases(self, input_str, expected):
        """Test title_case with normal string inputs."""
        assert title_case(input_str) == expected

    def test_title_case_empty_string(self):
        """Test title_case with empty string."""
        assert title_case("") == ""

    def test_title_case_single_word(self):
        """Test title_case with single word."""
        assert title_case("python") == "Python"

    @pytest.mark.parametrize("input_str,expected", [
        ("HELLO WORLD", "Hello World"),
        ("lowercase", "Lowercase"),
        ("MiXeD CaSe", "Mixed Case"),
    ])
    def test_title_case_various_cases(self, input_str, expected):
        """Test title_case with various input cases."""
        assert title_case(input_str) == expected

    @pytest.mark.parametrize("input_str,expected", [
        ("  hello world  ", "  Hello World  "),
        ("hello  world", "Hello  World"),
        ("\thello\tworld", "\tHello\tWorld"),
    ])
    def test_title_case_extra_spaces(self, input_str, expected):
        """Test title_case with extra spaces and tabs."""
        assert title_case(input_str) == expected

    @pytest.mark.parametrize("input_str,expected", [
        ("hello-world", "Hello-World"),
        ("don't stop", "Don'T Stop"),
        ("it's a test", "It'S A Test"),
        ("hello_world", "Hello_World"),
    ])
    def test_title_case_with_special_characters(self, input_str, expected):
        """Test title_case with special characters."""
        assert title_case(input_str) == expected

    @pytest.mark.parametrize("input_str,expected", [
        ("123 test", "123 Test"),
        ("test 123", "Test 123"),
        ("hello123world", "Hello123World"),
    ])
    def test_title_case_with_numbers(self, input_str, expected):
        """Test title_case with numbers."""
        assert title_case(input_str) == expected


class TestCountWords:
    """Tests for the count_words function."""

    @pytest.mark.parametrize("input_str,expected", [
        ("hello", 1),
        ("hello world", 2),
        ("the quick brown fox", 4),
        ("one two three four five", 5),
    ])
    def test_count_words_normal_cases(self, input_str, expected):
        """Test count_words with normal string inputs."""
        assert count_words(input_str) == expected

    def test_count_words_empty_string(self):
        """Test count_words with empty string."""
        assert count_words("") == 0

    def test_count_words_single_word(self):
        """Test count_words with single word."""
        assert count_words("hello") == 1

    @pytest.mark.parametrize("input_str,expected", [
        ("  hello  ", 1),
        ("  hello   world  ", 2),
        ("   multiple   spaces   between   ", 3),
        ("  ", 0),
        ("   ", 0),
    ])
    def test_count_words_extra_spaces(self, input_str, expected):
        """Test count_words with extra spaces."""
        assert count_words(input_str) == expected

    @pytest.mark.parametrize("input_str,expected", [
        ("\thello\tworld", 2),
        ("\n\nhello\n\nworld\n\n", 2),
        ("\t\t", 0),
        ("\n", 0),
        ("hello\tworld\ntest", 3),
    ])
    def test_count_words_with_tabs_and_newlines(self, input_str, expected):
        """Test count_words with tabs and newlines."""
        assert count_words(input_str) == expected

    @pytest.mark.parametrize("input_str,expected", [
        ("hello-world", 1),
        ("it's a test", 3),
        ("hello@world.com", 1),
        ("test!@#$%test", 1),
    ])
    def test_count_words_with_special_characters(self, input_str, expected):
        """Test count_words with special characters."""
        assert count_words(input_str) == expected

    @pytest.mark.parametrize("input_str,expected", [
        ("hello123", 1),
        ("123", 1),
        ("hello 123 world", 3),
    ])
    def test_count_words_with_numbers(self, input_str, expected):
        """Test count_words with numbers."""
        assert count_words(input_str) == expected

    def test_count_words_only_whitespace(self):
        """Test count_words with only whitespace characters."""
        assert count_words("   \t\n  ") == 0
