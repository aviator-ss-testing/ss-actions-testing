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

    def test_with_spaces(self):
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_with_punctuation(self):
        assert is_palindrome("Was it a car or a cat I saw?") is True

    def test_empty_string(self):
        assert is_palindrome("") is True

    def test_single_character(self):
        assert is_palindrome("a") is True

    def test_numeric_palindrome(self):
        assert is_palindrome("12321") is True

    def test_numeric_non_palindrome(self):
        assert is_palindrome("12345") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_palindrome(None)

    def test_type_error_int(self):
        with pytest.raises(TypeError):
            is_palindrome(123)


class TestReverseWords:
    def test_basic(self):
        assert reverse_words("hello world") == "world hello"

    def test_single_word(self):
        assert reverse_words("hello") == "hello"

    def test_empty_string(self):
        assert reverse_words("") == ""

    def test_multiple_words(self):
        assert reverse_words("one two three four") == "four three two one"

    def test_extra_whitespace(self):
        assert reverse_words("  hello   world  ") == "world hello"

    def test_type_error(self):
        with pytest.raises(TypeError):
            reverse_words(None)


class TestCamelToSnake:
    def test_camel_case(self):
        assert camel_to_snake("camelCase") == "camel_case"

    def test_pascal_case(self):
        assert camel_to_snake("PascalCase") == "pascal_case"

    def test_already_snake(self):
        assert camel_to_snake("snake_case") == "snake_case"

    def test_empty_string(self):
        assert camel_to_snake("") == ""

    def test_single_word(self):
        assert camel_to_snake("hello") == "hello"

    def test_consecutive_uppercase(self):
        assert camel_to_snake("parseHTMLContent") == "parse_html_content"

    def test_acronym(self):
        assert camel_to_snake("HTMLParser") == "html_parser"

    def test_type_error(self):
        with pytest.raises(TypeError):
            camel_to_snake(None)


class TestSnakeToCamel:
    def test_basic(self):
        assert snake_to_camel("snake_case") == "snakeCase"

    def test_pascal_case(self):
        assert snake_to_camel("snake_case", upper_first=True) == "SnakeCase"

    def test_empty_string(self):
        assert snake_to_camel("") == ""

    def test_single_word(self):
        assert snake_to_camel("hello") == "hello"

    def test_multiple_underscores(self):
        assert snake_to_camel("one_two_three") == "oneTwoThree"

    def test_leading_trailing_underscores(self):
        assert snake_to_camel("_hello_world_") == "helloWorld"

    def test_type_error(self):
        with pytest.raises(TypeError):
            snake_to_camel(None)


class TestCountVowels:
    def test_basic(self):
        assert count_vowels("hello") == 2

    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_no_vowels(self):
        assert count_vowels("rhythm") == 0

    def test_empty_string(self):
        assert count_vowels("") == 0

    def test_case_insensitive(self):
        assert count_vowels("HELLO") == 2

    def test_mixed_case(self):
        assert count_vowels("HeLLo WoRLd") == 3

    def test_with_numbers_and_symbols(self):
        assert count_vowels("h3ll0 w0rld!") == 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            count_vowels(None)


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

    def test_max_length_equals_suffix_length(self):
        assert truncate_string("hello world", 3) == "..."

    def test_max_length_less_than_suffix(self):
        assert truncate_string("hello", 1) == "."

    def test_type_error_not_string(self):
        with pytest.raises(TypeError):
            truncate_string(None, 5)

    def test_type_error_max_length(self):
        with pytest.raises(TypeError):
            truncate_string("hello", "5")

    def test_value_error_negative_max_length(self):
        with pytest.raises(ValueError):
            truncate_string("hello", -1)
