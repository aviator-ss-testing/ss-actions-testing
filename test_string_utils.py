"""Tests for the string_utils module."""
import pytest
from string_utils import (
    is_palindrome,
    reverse_words,
    camel_to_snake,
    snake_to_camel,
    count_vowels,
    truncate_string,
)


class TestIsPalindrome:
    """Tests for is_palindrome function."""

    def test_simple_palindrome(self):
        """Test basic palindrome strings."""
        assert is_palindrome("racecar") is True
        assert is_palindrome("level") is True
        assert is_palindrome("noon") is True

    def test_case_insensitive(self):
        """Test palindrome detection is case-insensitive."""
        assert is_palindrome("Racecar") is True
        assert is_palindrome("RaceCar") is True
        assert is_palindrome("LEVEL") is True

    def test_with_spaces_and_punctuation(self):
        """Test palindrome with spaces and punctuation."""
        assert is_palindrome("A man a plan a canal Panama") is True
        assert is_palindrome("Was it a car or a cat I saw") is True
        assert is_palindrome("Madam, I'm Adam") is True
        assert is_palindrome("A Santa at NASA") is True

    def test_not_palindrome(self):
        """Test strings that are not palindromes."""
        assert is_palindrome("hello") is False
        assert is_palindrome("world") is False
        assert is_palindrome("python") is False

    def test_single_character(self):
        """Test single character strings."""
        assert is_palindrome("a") is True
        assert is_palindrome("Z") is True

    def test_empty_and_none(self):
        """Test empty string and None input."""
        assert is_palindrome("") is False
        assert is_palindrome(None) is False

    def test_special_characters_only(self):
        """Test strings with only special characters."""
        assert is_palindrome("!!!") is False
        assert is_palindrome("   ") is False
        assert is_palindrome("@#$") is False

    def test_numbers(self):
        """Test numeric palindromes."""
        assert is_palindrome("12321") is True
        assert is_palindrome("12345") is False


class TestReverseWords:
    """Tests for reverse_words function."""

    def test_simple_reverse(self):
        """Test basic word reversal."""
        assert reverse_words("hello world") == "world hello"
        assert reverse_words("one two three") == "three two one"

    def test_single_word(self):
        """Test single word string."""
        assert reverse_words("hello") == "hello"
        assert reverse_words("word") == "word"

    def test_multiple_spaces(self):
        """Test strings with multiple spaces."""
        assert reverse_words("hello  world") == "world hello"
        assert reverse_words("one   two   three") == "three two one"

    def test_leading_trailing_spaces(self):
        """Test strings with leading/trailing spaces."""
        assert reverse_words("  hello world  ") == "world hello"
        assert reverse_words(" test ") == "test"

    def test_empty_and_none(self):
        """Test empty string and None input."""
        assert reverse_words("") == ""
        assert reverse_words(None) == ""

    def test_special_characters(self):
        """Test strings with special characters."""
        assert reverse_words("hello! world?") == "world? hello!"
        assert reverse_words("one-two three_four") == "three_four one-two"


class TestCamelToSnake:
    """Tests for camel_to_snake function."""

    def test_camel_case(self):
        """Test camelCase conversion."""
        assert camel_to_snake("camelCase") == "camel_case"
        assert camel_to_snake("myVariableName") == "my_variable_name"
        assert camel_to_snake("thisIsATest") == "this_is_a_test"

    def test_pascal_case(self):
        """Test PascalCase conversion."""
        assert camel_to_snake("PascalCase") == "pascal_case"
        assert camel_to_snake("MyClassName") == "my_class_name"
        assert camel_to_snake("ThisIsATest") == "this_is_a_test"

    def test_already_snake_case(self):
        """Test already snake_case strings."""
        assert camel_to_snake("snake_case") == "snake_case"
        assert camel_to_snake("already_snake") == "already_snake"

    def test_single_word(self):
        """Test single word strings."""
        assert camel_to_snake("word") == "word"
        assert camel_to_snake("Word") == "word"

    def test_consecutive_capitals(self):
        """Test strings with consecutive capital letters."""
        assert camel_to_snake("HTTPResponse") == "http_response"
        assert camel_to_snake("XMLParser") == "xml_parser"

    def test_with_numbers(self):
        """Test strings with numbers."""
        assert camel_to_snake("camelCase123") == "camel_case123"
        assert camel_to_snake("test123Value") == "test123_value"

    def test_empty_and_none(self):
        """Test empty string and None input."""
        assert camel_to_snake("") == ""
        assert camel_to_snake(None) == ""


class TestSnakeToCamel:
    """Tests for snake_to_camel function."""

    def test_to_camel_case(self):
        """Test conversion to camelCase."""
        assert snake_to_camel("snake_case") == "snakeCase"
        assert snake_to_camel("my_variable_name") == "myVariableName"
        assert snake_to_camel("this_is_a_test") == "thisIsATest"

    def test_to_pascal_case(self):
        """Test conversion to PascalCase."""
        assert snake_to_camel("snake_case", capitalize_first=True) == "SnakeCase"
        assert snake_to_camel("my_class_name", capitalize_first=True) == "MyClassName"
        assert snake_to_camel("this_is_a_test", capitalize_first=True) == "ThisIsATest"

    def test_single_word(self):
        """Test single word strings."""
        assert snake_to_camel("word") == "word"
        assert snake_to_camel("word", capitalize_first=True) == "Word"

    def test_with_numbers(self):
        """Test strings with numbers."""
        assert snake_to_camel("test_123_value") == "test123Value"
        assert snake_to_camel("version_2_api") == "version2Api"

    def test_multiple_underscores(self):
        """Test strings with consecutive underscores."""
        assert snake_to_camel("test__case") == "testCase"
        assert snake_to_camel("my___var") == "myVar"

    def test_empty_and_none(self):
        """Test empty string and None input."""
        assert snake_to_camel("") == ""
        assert snake_to_camel(None) == ""
        assert snake_to_camel("", capitalize_first=True) == ""
        assert snake_to_camel(None, capitalize_first=True) == ""


class TestCountVowels:
    """Tests for count_vowels function."""

    def test_simple_counting(self):
        """Test basic vowel counting."""
        assert count_vowels("hello") == 2
        assert count_vowels("world") == 1
        assert count_vowels("aeiou") == 5

    def test_case_insensitive(self):
        """Test vowel counting is case-insensitive."""
        assert count_vowels("HELLO") == 2
        assert count_vowels("AEiOu") == 5

    def test_no_vowels(self):
        """Test strings with no vowels."""
        assert count_vowels("rhythm") == 0
        assert count_vowels("fly") == 0
        assert count_vowels("xyz") == 0

    def test_with_y_parameter(self):
        """Test include_y parameter."""
        assert count_vowels("rhythm", include_y=False) == 0
        assert count_vowels("rhythm", include_y=True) == 1
        assert count_vowels("happy", include_y=False) == 1
        assert count_vowels("happy", include_y=True) == 2
        assert count_vowels("RHYTHM", include_y=True) == 1

    def test_mixed_content(self):
        """Test strings with mixed content."""
        assert count_vowels("hello world 123") == 3
        assert count_vowels("test@example.com") == 4

    def test_empty_and_none(self):
        """Test empty string and None input."""
        assert count_vowels("") == 0
        assert count_vowels(None) == 0
        assert count_vowels(None, include_y=True) == 0

    def test_only_vowels(self):
        """Test strings with only vowels."""
        assert count_vowels("aaa") == 3
        assert count_vowels("AEIOU") == 5

    def test_special_characters(self):
        """Test strings with special characters."""
        assert count_vowels("!@#$%") == 0
        assert count_vowels("hello!") == 2


class TestTruncateString:
    """Tests for truncate_string function."""

    def test_truncate_longer_string(self):
        """Test truncating strings longer than max_length."""
        assert truncate_string("hello world", 8) == "hello..."
        assert truncate_string("this is a long string", 10) == "this is..."
        assert truncate_string("truncate me", 9) == "trunca..."

    def test_no_truncation_needed(self):
        """Test strings shorter than max_length."""
        assert truncate_string("short", 10) == "short"
        assert truncate_string("exactly", 7) == "exactly"
        assert truncate_string("test", 100) == "test"

    def test_custom_suffix(self):
        """Test custom suffix parameter."""
        assert truncate_string("hello world", 8, suffix=">>") == "hello>>"
        assert truncate_string("hello world", 9, suffix="...") == "hello..."
        assert truncate_string("test string", 8, suffix=" [more]") == "t [more]"

    def test_empty_suffix(self):
        """Test with empty suffix."""
        assert truncate_string("hello world", 5, suffix="") == "hello"
        assert truncate_string("test", 2, suffix="") == "te"

    def test_exact_length(self):
        """Test string exactly at max_length."""
        assert truncate_string("exactly10!", 10) == "exactly10!"
        assert truncate_string("test", 4) == "test"

    def test_empty_and_none(self):
        """Test empty string and None input."""
        assert truncate_string("", 10) == ""
        assert truncate_string(None, 10) == ""

    def test_invalid_max_length(self):
        """Test max_length less than suffix length raises error."""
        with pytest.raises(ValueError, match="max_length .* must be at least"):
            truncate_string("hello", 2, suffix="...")
        with pytest.raises(ValueError, match="max_length .* must be at least"):
            truncate_string("test", 1, suffix=">>")

    def test_special_characters(self):
        """Test truncating strings with special characters."""
        assert truncate_string("hello@example.com", 10) == "hello@e..."
        assert truncate_string("test/path/file", 10) == "test/pa..."

    def test_unicode_characters(self):
        """Test truncating strings with unicode characters."""
        assert truncate_string("hello 世界", 8) == "hello ..."
        assert truncate_string("emoji 😀 test", 10) == "emoji 😀..."
