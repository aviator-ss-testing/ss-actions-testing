"""Tests for the string_utils module."""

import pytest
from string_utils import (
    camel_to_snake,
    count_vowels,
    is_palindrome,
    reverse_words,
    snake_to_camel,
    truncate_string,
)


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_simple_non_palindrome(self):
        assert is_palindrome("hello") is False

    def test_case_insensitive(self):
        assert is_palindrome("Racecar") is True

    def test_with_spaces_and_punctuation(self):
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_single_character(self):
        assert is_palindrome("a") is True

    def test_empty_string(self):
        assert is_palindrome("") is True

    def test_numeric_palindrome(self):
        assert is_palindrome("12321") is True

    def test_numeric_non_palindrome(self):
        assert is_palindrome("12345") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_palindrome(None)  # type: ignore[arg-type]

    def test_type_error_int(self):
        with pytest.raises(TypeError):
            is_palindrome(42)  # type: ignore[arg-type]


class TestReverseWords:
    def test_basic(self):
        assert reverse_words("hello world") == "world hello"

    def test_single_word(self):
        assert reverse_words("hello") == "hello"

    def test_multiple_spaces_collapsed(self):
        assert reverse_words("hello   world") == "world hello"

    def test_empty_string(self):
        assert reverse_words("") == ""

    def test_leading_trailing_spaces(self):
        assert reverse_words("  hello world  ") == "world hello"

    def test_three_words(self):
        assert reverse_words("one two three") == "three two one"

    def test_type_error(self):
        with pytest.raises(TypeError):
            reverse_words(None)  # type: ignore[arg-type]


class TestCamelToSnake:
    def test_camel_case(self):
        assert camel_to_snake("camelCase") == "camel_case"

    def test_pascal_case(self):
        assert camel_to_snake("PascalCase") == "pascal_case"

    def test_multiple_words(self):
        assert camel_to_snake("myVariableName") == "my_variable_name"

    def test_already_lower(self):
        assert camel_to_snake("lowercase") == "lowercase"

    def test_empty_string(self):
        assert camel_to_snake("") == ""

    def test_consecutive_uppercase(self):
        assert camel_to_snake("HTTPSRequest") == "https_request"

    def test_type_error(self):
        with pytest.raises(TypeError):
            camel_to_snake(None)  # type: ignore[arg-type]


class TestSnakeToCamel:
    def test_snake_to_camel(self):
        assert snake_to_camel("my_variable_name") == "myVariableName"

    def test_snake_to_pascal(self):
        assert snake_to_camel("my_variable_name", upper_first=True) == "MyVariableName"

    def test_single_word(self):
        assert snake_to_camel("hello") == "hello"

    def test_empty_string(self):
        assert snake_to_camel("") == ""

    def test_leading_underscore(self):
        assert snake_to_camel("_private") == "private"

    def test_multiple_underscores(self):
        assert snake_to_camel("a__b") == "aB"

    def test_type_error(self):
        with pytest.raises(TypeError):
            snake_to_camel(None)  # type: ignore[arg-type]


class TestCountVowels:
    def test_basic(self):
        assert count_vowels("hello") == 2

    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_no_vowels(self):
        assert count_vowels("rhythm") == 0

    def test_case_insensitive(self):
        assert count_vowels("HELLO") == 2

    def test_empty_string(self):
        assert count_vowels("") == 0

    def test_with_spaces_and_punctuation(self):
        assert count_vowels("Hello, World!") == 3

    def test_type_error(self):
        with pytest.raises(TypeError):
            count_vowels(None)  # type: ignore[arg-type]


class TestTruncateString:
    def test_no_truncation_needed(self):
        assert truncate_string("hello", 10) == "hello"

    def test_exact_length(self):
        assert truncate_string("hello", 5) == "hello"

    def test_truncation(self):
        assert truncate_string("hello world", 8) == "hello..."

    def test_custom_suffix(self):
        assert truncate_string("hello world", 7, suffix="--") == "hello--"

    def test_empty_string(self):
        assert truncate_string("", 5) == ""

    def test_max_length_zero(self):
        assert truncate_string("hello", 0) == ""

    def test_max_length_smaller_than_suffix(self):
        assert truncate_string("hello", 2) == ".."

    def test_type_error_string(self):
        with pytest.raises(TypeError):
            truncate_string(None, 5)  # type: ignore[arg-type]

    def test_type_error_suffix(self):
        with pytest.raises(TypeError):
            truncate_string("hello", 5, suffix=123)  # type: ignore[arg-type]

    def test_negative_max_length(self):
        with pytest.raises(ValueError):
            truncate_string("hello", -1)
