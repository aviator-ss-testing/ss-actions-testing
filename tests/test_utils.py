"""
Comprehensive unit tests for the utils module.
Tests all string manipulation, numeric operations, and list processing functions.
"""

import pytest
from utils import (
    reverse_string, capitalize_words, clean_whitespace,
    fibonacci, factorial, is_prime,
    flatten_list, unique_elements, filter_even
)


class TestStringManipulation:
    """Test string manipulation functions."""

    def test_reverse_string_basic(self):
        assert reverse_string("hello") == "olleh"
        assert reverse_string("python") == "nohtyp"

    def test_reverse_string_empty(self):
        assert reverse_string("") == ""

    def test_reverse_string_single_char(self):
        assert reverse_string("a") == "a"

    def test_reverse_string_palindrome(self):
        assert reverse_string("racecar") == "racecar"

    def test_reverse_string_with_spaces(self):
        assert reverse_string("hello world") == "dlrow olleh"

    def test_reverse_string_with_special_chars(self):
        assert reverse_string("hello!@#") == "#@!olleh"

    @pytest.mark.parametrize("input_str,expected", [
        ("abc", "cba"),
        ("123", "321"),
        ("a1b2c3", "3c2b1a"),
        ("!@#$%", "%$#@!"),
    ])
    def test_reverse_string_parametrized(self, input_str, expected):
        assert reverse_string(input_str) == expected

    def test_capitalize_words_basic(self):
        assert capitalize_words("hello world") == "Hello World"
        assert capitalize_words("python is great") == "Python Is Great"

    def test_capitalize_words_empty(self):
        assert capitalize_words("") == ""

    def test_capitalize_words_single_word(self):
        assert capitalize_words("hello") == "Hello"

    def test_capitalize_words_already_capitalized(self):
        assert capitalize_words("Hello World") == "Hello World"

    def test_capitalize_words_mixed_case(self):
        assert capitalize_words("hELLo WoRLd") == "Hello World"

    def test_capitalize_words_with_numbers(self):
        assert capitalize_words("hello 123 world") == "Hello 123 World"

    @pytest.mark.parametrize("input_str,expected", [
        ("one two three", "One Two Three"),
        ("a b c", "A B C"),
        ("testing 123", "Testing 123"),
        ("multiple   spaces", "Multiple Spaces"),
    ])
    def test_capitalize_words_parametrized(self, input_str, expected):
        assert capitalize_words(input_str) == expected

    def test_clean_whitespace_basic(self):
        assert clean_whitespace("  hello    world  ") == "hello world"
        assert clean_whitespace("python\t\tis\n\ngreat") == "python is great"

    def test_clean_whitespace_empty(self):
        assert clean_whitespace("") == ""

    def test_clean_whitespace_only_spaces(self):
        assert clean_whitespace("   ") == ""

    def test_clean_whitespace_no_extra_spaces(self):
        assert clean_whitespace("hello world") == "hello world"

    def test_clean_whitespace_mixed_whitespace(self):
        assert clean_whitespace("  hello\t\n  world  \r\n") == "hello world"

    @pytest.mark.parametrize("input_str,expected", [
        ("  a  b  c  ", "a b c"),
        ("\t\thello\n\nworld\r\r", "hello world"),
        ("multiple   spaces   between", "multiple spaces between"),
        ("   leading and trailing   ", "leading and trailing"),
    ])
    def test_clean_whitespace_parametrized(self, input_str, expected):
        assert clean_whitespace(input_str) == expected


class TestNumericUtilities:
    """Test numeric utility functions."""

    def test_fibonacci_base_cases(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    def test_fibonacci_small_numbers(self):
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5

    def test_fibonacci_larger_numbers(self):
        assert fibonacci(10) == 55
        assert fibonacci(15) == 610

    def test_fibonacci_negative_input(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            fibonacci(-1)
        with pytest.raises(ValueError, match="cannot be negative"):
            fibonacci(-10)

    @pytest.mark.parametrize("n,expected", [
        (0, 0), (1, 1), (2, 1), (3, 2), (4, 3),
        (5, 5), (6, 8), (7, 13), (8, 21), (9, 34)
    ])
    def test_fibonacci_parametrized(self, n, expected):
        assert fibonacci(n) == expected

    def test_factorial_base_cases(self):
        assert factorial(0) == 1
        assert factorial(1) == 1

    def test_factorial_small_numbers(self):
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120

    def test_factorial_larger_numbers(self):
        assert factorial(6) == 720
        assert factorial(10) == 3628800

    def test_factorial_negative_input(self):
        with pytest.raises(ValueError, match="not defined for negative"):
            factorial(-1)
        with pytest.raises(ValueError, match="not defined for negative"):
            factorial(-5)

    @pytest.mark.parametrize("n,expected", [
        (0, 1), (1, 1), (2, 2), (3, 6), (4, 24),
        (5, 120), (6, 720), (7, 5040)
    ])
    def test_factorial_parametrized(self, n, expected):
        assert factorial(n) == expected

    def test_is_prime_small_numbers(self):
        assert not is_prime(0)
        assert not is_prime(1)
        assert is_prime(2)
        assert is_prime(3)
        assert not is_prime(4)
        assert is_prime(5)

    def test_is_prime_negative_numbers(self):
        assert not is_prime(-1)
        assert not is_prime(-5)
        assert not is_prime(-17)

    def test_is_prime_known_primes(self):
        known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for prime in known_primes:
            assert is_prime(prime)

    def test_is_prime_known_composites(self):
        known_composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25]
        for composite in known_composites:
            assert not is_prime(composite)

    def test_is_prime_larger_numbers(self):
        assert is_prime(97)
        assert is_prime(101)
        assert not is_prime(100)
        assert not is_prime(99)

    @pytest.mark.parametrize("n,expected", [
        (2, True), (3, True), (4, False), (5, True),
        (6, False), (7, True), (8, False), (9, False),
        (10, False), (11, True), (17, True), (25, False)
    ])
    def test_is_prime_parametrized(self, n, expected):
        assert is_prime(n) == expected


class TestListProcessing:
    """Test list processing functions."""

    def test_flatten_list_basic(self):
        assert flatten_list([1, [2, 3], 4]) == [1, 2, 3, 4]
        assert flatten_list([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

    def test_flatten_list_empty(self):
        assert flatten_list([]) == []

    def test_flatten_list_no_nesting(self):
        assert flatten_list([1, 2, 3, 4]) == [1, 2, 3, 4]

    def test_flatten_list_deeply_nested(self):
        nested = [1, [2, [3, [4, [5]]]]]
        expected = [1, 2, 3, 4, 5]
        assert flatten_list(nested) == expected

    def test_flatten_list_mixed_types(self):
        nested = [1, ['a', [2, 'b']], 3]
        expected = [1, 'a', 2, 'b', 3]
        assert flatten_list(nested) == expected

    def test_flatten_list_empty_sublists(self):
        assert flatten_list([1, [], 2, [3, []]]) == [1, 2, 3]

    @pytest.mark.parametrize("nested_list,expected", [
        ([1, [2, 3]], [1, 2, 3]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([1, [2, [3]]], [1, 2, 3]),
        ([[], [1], []], [1]),
    ])
    def test_flatten_list_parametrized(self, nested_list, expected):
        assert flatten_list(nested_list) == expected

    def test_unique_elements_basic(self):
        assert unique_elements([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
        assert unique_elements(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']

    def test_unique_elements_empty(self):
        assert unique_elements([]) == []

    def test_unique_elements_no_duplicates(self):
        assert unique_elements([1, 2, 3, 4]) == [1, 2, 3, 4]

    def test_unique_elements_all_same(self):
        assert unique_elements([1, 1, 1, 1]) == [1]

    def test_unique_elements_mixed_types(self):
        result = unique_elements([1, 'a', 1, 'b', 'a', 2])
        assert result == [1, 'a', 'b', 2]

    def test_unique_elements_preserves_order(self):
        assert unique_elements([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [3, 1, 4, 5, 9, 2, 6]

    @pytest.mark.parametrize("input_list,expected", [
        ([1, 1, 2, 2, 3], [1, 2, 3]),
        (['x', 'y', 'x'], ['x', 'y']),
        ([1, 2, 3], [1, 2, 3]),
        ([5, 5, 5], [5]),
    ])
    def test_unique_elements_parametrized(self, input_list, expected):
        assert unique_elements(input_list) == expected

    def test_filter_even_basic(self):
        assert filter_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
        assert filter_even([1, 3, 5, 7]) == []

    def test_filter_even_empty(self):
        assert filter_even([]) == []

    def test_filter_even_all_even(self):
        assert filter_even([2, 4, 6, 8]) == [2, 4, 6, 8]

    def test_filter_even_with_zero(self):
        assert filter_even([0, 1, 2, 3]) == [0, 2]

    def test_filter_even_negative_numbers(self):
        assert filter_even([-4, -3, -2, -1, 0, 1, 2]) == [-4, -2, 0, 2]

    def test_filter_even_floats(self):
        assert filter_even([1.0, 2.0, 3.0, 4.0]) == [2.0, 4.0]
        assert filter_even([1.5, 2.5, 3.5]) == []

    def test_filter_even_mixed_types(self):
        result = filter_even([1, 2, 'a', 4, None, 6])
        assert result == [2, 4, 6]

    @pytest.mark.parametrize("numbers,expected", [
        ([1, 2, 3, 4], [2, 4]),
        ([0, 1, 2], [0, 2]),
        ([-2, -1, 0, 1, 2], [-2, 0, 2]),
        ([1, 3, 5], []),
    ])
    def test_filter_even_parametrized(self, numbers, expected):
        assert filter_even(numbers) == expected


class TestErrorHandling:
    """Test error handling and edge cases."""

    def test_string_functions_with_none(self):
        with pytest.raises(AttributeError):
            reverse_string(None)
        with pytest.raises(AttributeError):
            capitalize_words(None)
        with pytest.raises(AttributeError):
            clean_whitespace(None)

    def test_numeric_functions_with_invalid_types(self):
        with pytest.raises(TypeError):
            fibonacci("string")
        with pytest.raises(TypeError):
            factorial(3.14)
        with pytest.raises(TypeError):
            is_prime("not a number")

    def test_list_functions_with_invalid_types(self):
        with pytest.raises(TypeError):
            flatten_list("not a list")
        with pytest.raises(TypeError):
            unique_elements("not a list")
        with pytest.raises(TypeError):
            filter_even("not a list")


class TestPerformance:
    """Test performance characteristics with larger inputs."""

    def test_fibonacci_performance(self):
        result = fibonacci(30)
        assert result == 832040

    def test_factorial_performance(self):
        result = factorial(15)
        assert result == 1307674368000

    def test_is_prime_performance(self):
        assert is_prime(982451653)
        assert not is_prime(982451654)

    def test_flatten_list_large(self):
        large_nested = [[i] for i in range(1000)]
        result = flatten_list(large_nested)
        assert len(result) == 1000
        assert result[0] == 0
        assert result[-1] == 999

    def test_unique_elements_large(self):
        large_list = list(range(500)) * 2
        result = unique_elements(large_list)
        assert len(result) == 500
        assert result == list(range(500))

    def test_filter_even_large(self):
        large_list = list(range(1000))
        result = filter_even(large_list)
        assert len(result) == 500
        assert all(n % 2 == 0 for n in result)