"""Tests for string utilities module."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from utils.string_utils import reverse_string, is_palindrome, title_case, count_words


class TestReverseString:
    """Tests for reverse_string function."""

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("hello", "olleh"),
            ("world", "dlrow"),
            ("Python", "nohtyP"),
            ("", ""),
            ("a", "a"),
            ("ab", "ba"),
            ("racecar", "racecar"),
            ("hello world", "dlrow olleh"),
            ("123456", "654321"),
            ("!@#$%", "%$#@!"),
            ("Hello World!", "!dlroW olleH"),
            ("🎉🎊🎈", "🎈🎊🎉"),
            ("unicode café", "éfac edocinu"),
            ("a\nb\nc", "c\nb\na"),
        ],
    )
    def test_reverse_string(self, input_str, expected):
        """Test reverse_string with various inputs."""
        assert reverse_string(input_str) == expected

    def test_reverse_string_special_characters(self):
        """Test reverse_string with special characters."""
        assert reverse_string("hello\nworld") == "dlrow\nolleh"
        assert reverse_string("tab\tseparated") == "detarapes\tbat"
        assert reverse_string("  spaces  ") == "  secaps  "


class TestIsPalindrome:
    """Tests for is_palindrome function."""

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("racecar", True),
            ("RaceCar", True),
            ("RACECAR", True),
            ("radar", True),
            ("level", True),
            ("", True),
            ("a", True),
            ("aa", True),
            ("ab", False),
            ("hello", False),
            ("Python", False),
            ("A man a plan a canal Panama", False),
            ("Amanaplanacanalpanama", True),
            ("noon", True),
            ("Noon", True),
            ("NooN", True),
            ("hello world", False),
            ("12321", True),
            ("123456", False),
        ],
    )
    def test_is_palindrome(self, input_str, expected):
        """Test is_palindrome with various inputs."""
        assert is_palindrome(input_str) == expected

    def test_is_palindrome_case_insensitive(self):
        """Test that palindrome checking is case-insensitive."""
        assert is_palindrome("Aa") is True
        assert is_palindrome("AbBa") is True
        assert is_palindrome("RacEcaR") is True

    def test_is_palindrome_empty_string(self):
        """Test that empty string is considered a palindrome."""
        assert is_palindrome("") is True


class TestTitleCase:
    """Tests for title_case function."""

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("hello world", "Hello World"),
            ("the quick brown fox", "The Quick Brown Fox"),
            ("HELLO WORLD", "Hello World"),
            ("hello", "Hello"),
            ("", ""),
            ("a", "A"),
            ("the quick brown fox jumps over the lazy dog", "The Quick Brown Fox Jumps Over The Lazy Dog"),
            ("hello-world", "Hello-World"),
            ("hello_world", "Hello_World"),
            ("it's a beautiful day", "It'S A Beautiful Day"),
            ("don't stop", "Don'T Stop"),
            ("123 abc", "123 Abc"),
            ("  multiple   spaces  ", "  Multiple   Spaces  "),
            ("MiXeD CaSe", "Mixed Case"),
        ],
    )
    def test_title_case(self, input_str, expected):
        """Test title_case with various inputs."""
        assert title_case(input_str) == expected

    def test_title_case_preserves_spaces(self):
        """Test that title_case preserves multiple spaces."""
        assert title_case("hello  world") == "Hello  World"
        assert title_case("   hello") == "   Hello"

    def test_title_case_edge_cases(self):
        """Test title_case with edge cases."""
        assert title_case("a b c") == "A B C"
        assert title_case("123") == "123"
        assert title_case("!@#$%") == "!@#$%"


class TestCountWords:
    """Tests for count_words function."""

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("hello world", 2),
            ("hello", 1),
            ("", 0),
            ("   ", 0),
            ("\t", 0),
            ("\n", 0),
            ("  hello   world  ", 2),
            ("one two three four five", 5),
            ("the quick brown fox", 4),
            ("hello\nworld", 2),
            ("hello\tworld", 2),
            ("  multiple   spaces   between   words  ", 4),
            ("a", 1),
            ("a b c d e f", 6),
            ("123 456 789", 3),
            ("hello-world", 1),
            ("hello_world", 1),
            ("hello world!", 2),
            ("  \n  \t  ", 0),
        ],
    )
    def test_count_words(self, input_str, expected):
        """Test count_words with various inputs."""
        assert count_words(input_str) == expected

    def test_count_words_single_word(self):
        """Test count_words with single words."""
        assert count_words("hello") == 1
        assert count_words("Python") == 1
        assert count_words("word") == 1

    def test_count_words_multiple_words(self):
        """Test count_words with multiple words."""
        assert count_words("hello world") == 2
        assert count_words("one two three") == 3
        assert count_words("the quick brown fox jumps") == 5

    def test_count_words_extra_spaces(self):
        """Test count_words handles extra spaces correctly."""
        assert count_words("  hello   world  ") == 2
        assert count_words("   one    two    three   ") == 3
        assert count_words("hello     world") == 2

    def test_count_words_empty_and_whitespace(self):
        """Test count_words with empty strings and whitespace."""
        assert count_words("") == 0
        assert count_words("   ") == 0
        assert count_words("\t\t\t") == 0
        assert count_words("\n\n\n") == 0
        assert count_words("  \n\t  ") == 0
