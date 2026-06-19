"""Tests for the string_utils module."""

from string_utils import is_palindrome, word_count, to_snake_case, truncate


def test_is_palindrome_normal_cases():
    """Test palindrome detection with normal cases."""
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True


def test_is_palindrome_edge_cases():
    """Test palindrome detection with edge cases."""
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("ab") is False


def test_word_count_normal_cases():
    """Test word counting with normal cases."""
    assert word_count("hello world") == {"hello": 1, "world": 1}
    assert word_count("hello hello world") == {"hello": 2, "world": 1}
    assert word_count("The quick brown fox") == {"the": 1, "quick": 1, "brown": 1, "fox": 1}


def test_word_count_edge_cases():
    """Test word counting with edge cases."""
    assert word_count("") == {}
    assert word_count("single") == {"single": 1}
    assert word_count("test test test") == {"test": 3}


def test_to_snake_case_normal_cases():
    """Test camelCase/PascalCase to snake_case conversion."""
    assert to_snake_case("camelCase") == "camel_case"
    assert to_snake_case("PascalCase") == "pascal_case"
    assert to_snake_case("someVariableName") == "some_variable_name"


def test_to_snake_case_edge_cases():
    """Test snake_case conversion with edge cases."""
    assert to_snake_case("already_snake_case") == "already_snake_case"
    assert to_snake_case("single") == "single"
    assert to_snake_case("") == ""


def test_truncate_normal_cases():
    """Test string truncation with normal cases."""
    assert truncate("Hello, World!", 10) == "Hello, ..."
    assert truncate("Short", 10) == "Short"
    assert truncate("This is a long string", 15) == "This is a lo..."


def test_truncate_edge_cases():
    """Test string truncation with edge cases and custom suffix."""
    assert truncate("", 10) == ""
    assert truncate("Exact", 5) == "Exact"
    assert truncate("Hello, World!", 10, suffix=">>") == "Hello, Wo>>"
    assert truncate("Test", 10, suffix="...") == "Test"
