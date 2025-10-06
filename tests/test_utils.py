"""
Unit tests for utility functions module.

Tests cover string manipulation, list processing, data validation,
and dictionary operations with various input scenarios.
"""

import unittest
from utils import (
    reverse_string, is_palindrome, count_words,
    flatten_list, remove_duplicates, find_max_min,
    is_email_valid, validate_phone_number,
    merge_dicts, filter_dict_by_keys
)


class TestStringManipulation(unittest.TestCase):
    """Test suite for string manipulation functions."""

    def test_reverse_string_basic(self):
        """Test reversing basic strings."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string("12345"), "54321")

    def test_reverse_string_empty(self):
        """Test reversing empty string."""
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_single_char(self):
        """Test reversing single character."""
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_string_unicode(self):
        """Test reversing Unicode strings."""
        self.assertEqual(reverse_string("Hello 世界"), "界世 olleH")
        self.assertEqual(reverse_string("café"), "éfac")
        self.assertEqual(reverse_string("🚀🌟"), "🌟🚀")

    def test_reverse_string_special_chars(self):
        """Test reversing strings with special characters."""
        self.assertEqual(reverse_string("Hello, World!"), "!dlroW ,olleH")
        self.assertEqual(reverse_string("a@b#c$d"), "d$c#b@a")

    def test_is_palindrome_basic(self):
        """Test basic palindrome detection."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Madam"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("Python"))

    def test_is_palindrome_empty(self):
        """Test palindrome with empty string."""
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_single_char(self):
        """Test palindrome with single character."""
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))

    def test_is_palindrome_special_chars(self):
        """Test palindrome with special characters."""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("race car!"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))

    def test_is_palindrome_numbers(self):
        """Test palindrome with numbers."""
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("1a2b2a1"))
        self.assertFalse(is_palindrome("12345"))

    def test_count_words_basic(self):
        """Test word counting in basic strings."""
        self.assertEqual(count_words("Hello world"), 2)
        self.assertEqual(count_words("Python is awesome"), 3)
        self.assertEqual(count_words("one"), 1)

    def test_count_words_empty(self):
        """Test word counting with empty string."""
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("   "), 0)
        self.assertEqual(count_words("\t\n"), 0)

    def test_count_words_multiple_spaces(self):
        """Test word counting with multiple spaces."""
        self.assertEqual(count_words("Hello    world"), 2)
        self.assertEqual(count_words("  leading and trailing  "), 3)

    def test_count_words_special_chars(self):
        """Test word counting with special characters."""
        self.assertEqual(count_words("Hello, world!"), 2)
        self.assertEqual(count_words("it's don't can't"), 3)

    def test_count_words_unicode(self):
        """Test word counting with Unicode."""
        self.assertEqual(count_words("Hello 世界"), 2)
        self.assertEqual(count_words("café restaurant"), 2)


class TestListProcessing(unittest.TestCase):
    """Test suite for list processing functions."""

    def test_flatten_list_basic(self):
        """Test flattening basic nested lists."""
        self.assertEqual(flatten_list([1, [2, 3], 4]), [1, 2, 3, 4])
        self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])

    def test_flatten_list_empty(self):
        """Test flattening empty list."""
        self.assertEqual(flatten_list([]), [])

    def test_flatten_list_deeply_nested(self):
        """Test flattening deeply nested lists."""
        self.assertEqual(flatten_list([1, [2, [3, [4, 5]]]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten_list([[[[[1]]]]]), [1])

    def test_flatten_list_mixed_types(self):
        """Test flattening lists with mixed types."""
        self.assertEqual(flatten_list([1, ['a', 'b'], 2.5, [True]]), [1, 'a', 'b', 2.5, True])
        self.assertEqual(flatten_list([1, [None], ['test']]), [1, None, 'test'])

    def test_flatten_list_nested_structures(self):
        """Test flattening with various nested structures."""
        self.assertEqual(flatten_list([[1, 2], [3, 4], [5, 6]]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(flatten_list([[], [1], [], [2, 3]]), [1, 2, 3])

    def test_remove_duplicates_basic(self):
        """Test removing duplicates from basic lists."""
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 3]), [1, 2, 3])
        self.assertEqual(remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_remove_duplicates_empty(self):
        """Test removing duplicates from empty list."""
        self.assertEqual(remove_duplicates([]), [])

    def test_remove_duplicates_order(self):
        """Test that order is preserved when removing duplicates."""
        self.assertEqual(remove_duplicates([3, 1, 2, 1, 3]), [3, 1, 2])
        self.assertEqual(remove_duplicates([5, 4, 3, 2, 1, 1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_remove_duplicates_mixed_types(self):
        """Test removing duplicates with mixed types."""
        self.assertEqual(remove_duplicates([1, '1', 1, '1']), [1, '1'])
        self.assertEqual(remove_duplicates([1, 1.0, 2, 2.0]), [1, 2])

    def test_remove_duplicates_strings(self):
        """Test removing duplicates from string list."""
        self.assertEqual(remove_duplicates(['a', 'b', 'a', 'c']), ['a', 'b', 'c'])
        self.assertEqual(remove_duplicates(['hello', 'world', 'hello']), ['hello', 'world'])

    def test_remove_duplicates_unhashable(self):
        """Test removing duplicates with unhashable types."""
        result = remove_duplicates([[1, 2], [3, 4], [1, 2]])
        self.assertEqual(len(result), 2)
        self.assertIn([1, 2], result)
        self.assertIn([3, 4], result)

    def test_find_max_min_basic(self):
        """Test finding max and min in basic lists."""
        self.assertEqual(find_max_min([1, 2, 3, 4, 5]), (5, 1))
        self.assertEqual(find_max_min([5, 4, 3, 2, 1]), (5, 1))

    def test_find_max_min_single_element(self):
        """Test finding max and min with single element."""
        self.assertEqual(find_max_min([42]), (42, 42))

    def test_find_max_min_floats(self):
        """Test finding max and min with floats."""
        self.assertEqual(find_max_min([1.5, 2.7, 0.3, 9.1]), (9.1, 0.3))

    def test_find_max_min_mixed_numbers(self):
        """Test finding max and min with mixed int and float."""
        self.assertEqual(find_max_min([1, 2.5, 3, 0.5]), (3, 0.5))

    def test_find_max_min_negative(self):
        """Test finding max and min with negative numbers."""
        self.assertEqual(find_max_min([-5, -1, -10, -3]), (-1, -10))
        self.assertEqual(find_max_min([-5, 0, 5]), (5, -5))

    def test_find_max_min_empty_raises_error(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError) as context:
            find_max_min([])
        self.assertIn("empty", str(context.exception).lower())


class TestDataValidation(unittest.TestCase):
    """Test suite for data validation functions."""

    def test_is_email_valid_basic(self):
        """Test basic valid email addresses."""
        self.assertTrue(is_email_valid("test@example.com"))
        self.assertTrue(is_email_valid("user@domain.org"))
        self.assertTrue(is_email_valid("name@company.co.uk"))

    def test_is_email_valid_with_plus(self):
        """Test email with plus sign."""
        self.assertTrue(is_email_valid("user+tag@example.com"))

    def test_is_email_valid_with_dots(self):
        """Test email with dots in username."""
        self.assertTrue(is_email_valid("first.last@example.com"))
        self.assertTrue(is_email_valid("user.name@sub.domain.com"))

    def test_is_email_valid_with_numbers(self):
        """Test email with numbers."""
        self.assertTrue(is_email_valid("user123@example.com"))
        self.assertTrue(is_email_valid("123@456.com"))

    def test_is_email_invalid_no_at(self):
        """Test invalid email without @ symbol."""
        self.assertFalse(is_email_valid("userexample.com"))
        self.assertFalse(is_email_valid("invalid"))

    def test_is_email_invalid_no_domain(self):
        """Test invalid email without domain."""
        self.assertFalse(is_email_valid("user@"))
        self.assertFalse(is_email_valid("@example.com"))

    def test_is_email_invalid_no_tld(self):
        """Test invalid email without TLD."""
        self.assertFalse(is_email_valid("user@domain"))
        self.assertFalse(is_email_valid("user@domain."))

    def test_is_email_invalid_spaces(self):
        """Test invalid email with spaces."""
        self.assertFalse(is_email_valid("user name@example.com"))
        self.assertFalse(is_email_valid("user@exam ple.com"))

    def test_is_email_invalid_special_chars(self):
        """Test invalid email with special characters."""
        self.assertFalse(is_email_valid("user#name@example.com"))
        self.assertFalse(is_email_valid("user@exam!ple.com"))

    def test_is_email_edge_cases(self):
        """Test email edge cases."""
        self.assertFalse(is_email_valid(""))
        self.assertFalse(is_email_valid("@"))
        self.assertFalse(is_email_valid("@@"))

    def test_validate_phone_number_basic(self):
        """Test basic valid phone numbers."""
        self.assertTrue(validate_phone_number("1234567890"))
        self.assertTrue(validate_phone_number("9876543210"))

    def test_validate_phone_number_with_country_code(self):
        """Test phone number with country code."""
        self.assertTrue(validate_phone_number("11234567890"))
        self.assertTrue(validate_phone_number("19876543210"))

    def test_validate_phone_number_formatted(self):
        """Test formatted phone numbers."""
        self.assertTrue(validate_phone_number("(123) 456-7890"))
        self.assertTrue(validate_phone_number("123-456-7890"))
        self.assertTrue(validate_phone_number("1-234-567-8900"))

    def test_validate_phone_number_with_spaces(self):
        """Test phone number with spaces."""
        self.assertTrue(validate_phone_number("123 456 7890"))
        self.assertTrue(validate_phone_number("1 234 567 8900"))

    def test_validate_phone_number_with_dots(self):
        """Test phone number with dots."""
        self.assertTrue(validate_phone_number("123.456.7890"))

    def test_validate_phone_number_invalid_too_short(self):
        """Test invalid phone number (too short)."""
        self.assertFalse(validate_phone_number("123456789"))
        self.assertFalse(validate_phone_number("12345"))

    def test_validate_phone_number_invalid_too_long(self):
        """Test invalid phone number (too long)."""
        self.assertFalse(validate_phone_number("123456789012"))
        self.assertFalse(validate_phone_number("21234567890"))

    def test_validate_phone_number_invalid_format(self):
        """Test invalid phone number format."""
        self.assertFalse(validate_phone_number(""))
        self.assertFalse(validate_phone_number("abcdefghij"))

    def test_validate_phone_number_edge_cases(self):
        """Test phone number edge cases."""
        self.assertFalse(validate_phone_number(""))
        self.assertFalse(validate_phone_number("()- "))


class TestDictionaryManipulation(unittest.TestCase):
    """Test suite for dictionary manipulation functions."""

    def test_merge_dicts_basic(self):
        """Test merging basic dictionaries."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        result = merge_dicts(dict1, dict2)
        self.assertEqual(result, {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_merge_dicts_override(self):
        """Test that dict2 values override dict1."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        result = merge_dicts(dict1, dict2)
        self.assertEqual(result, {'a': 1, 'b': 3, 'c': 4})

    def test_merge_dicts_empty(self):
        """Test merging with empty dictionaries."""
        self.assertEqual(merge_dicts({}, {}), {})
        self.assertEqual(merge_dicts({'a': 1}, {}), {'a': 1})
        self.assertEqual(merge_dicts({}, {'b': 2}), {'b': 2})

    def test_merge_dicts_nested(self):
        """Test merging dictionaries with nested values."""
        dict1 = {'a': 1, 'b': {'x': 10}}
        dict2 = {'c': 3}
        result = merge_dicts(dict1, dict2)
        self.assertEqual(result, {'a': 1, 'b': {'x': 10}, 'c': 3})

    def test_merge_dicts_various_types(self):
        """Test merging dictionaries with various value types."""
        dict1 = {'str': 'hello', 'int': 42, 'float': 3.14}
        dict2 = {'bool': True, 'list': [1, 2, 3], 'none': None}
        result = merge_dicts(dict1, dict2)
        self.assertEqual(len(result), 6)
        self.assertEqual(result['str'], 'hello')
        self.assertEqual(result['list'], [1, 2, 3])

    def test_merge_dicts_original_unchanged(self):
        """Test that original dictionaries are not modified."""
        dict1 = {'a': 1}
        dict2 = {'b': 2}
        result = merge_dicts(dict1, dict2)
        self.assertEqual(dict1, {'a': 1})
        self.assertEqual(dict2, {'b': 2})
        self.assertEqual(result, {'a': 1, 'b': 2})

    def test_filter_dict_by_keys_basic(self):
        """Test filtering dictionary by basic keys."""
        d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        result = filter_dict_by_keys(d, ['a', 'c'])
        self.assertEqual(result, {'a': 1, 'c': 3})

    def test_filter_dict_by_keys_empty(self):
        """Test filtering with empty keys list."""
        d = {'a': 1, 'b': 2}
        result = filter_dict_by_keys(d, [])
        self.assertEqual(result, {})

    def test_filter_dict_by_keys_empty_dict(self):
        """Test filtering empty dictionary."""
        result = filter_dict_by_keys({}, ['a', 'b'])
        self.assertEqual(result, {})

    def test_filter_dict_by_keys_nonexistent(self):
        """Test filtering with nonexistent keys."""
        d = {'a': 1, 'b': 2}
        result = filter_dict_by_keys(d, ['c', 'd'])
        self.assertEqual(result, {})

    def test_filter_dict_by_keys_mixed(self):
        """Test filtering with mix of existing and nonexistent keys."""
        d = {'a': 1, 'b': 2, 'c': 3}
        result = filter_dict_by_keys(d, ['a', 'x', 'c', 'y'])
        self.assertEqual(result, {'a': 1, 'c': 3})

    def test_filter_dict_by_keys_nested(self):
        """Test filtering dictionary with nested values."""
        d = {'a': 1, 'b': {'x': 10}, 'c': [1, 2, 3]}
        result = filter_dict_by_keys(d, ['b', 'c'])
        self.assertEqual(result, {'b': {'x': 10}, 'c': [1, 2, 3]})

    def test_filter_dict_by_keys_original_unchanged(self):
        """Test that original dictionary is not modified."""
        d = {'a': 1, 'b': 2, 'c': 3}
        result = filter_dict_by_keys(d, ['a'])
        self.assertEqual(d, {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(result, {'a': 1})


class TestUnicodeAndSpecialChars(unittest.TestCase):
    """Test suite for Unicode and special character handling."""

    def test_unicode_strings(self):
        """Test functions with Unicode characters."""
        self.assertEqual(reverse_string("こんにちは"), "はちにんこ")
        self.assertTrue(is_palindrome("こんにちにんこ"))
        self.assertEqual(count_words("Hello мир world"), 3)

    def test_emoji_handling(self):
        """Test functions with emoji."""
        self.assertEqual(reverse_string("Hello 😀 World"), "dlroW 😀 olleH")
        self.assertEqual(count_words("😀 😁 😂"), 3)

    def test_special_characters_in_lists(self):
        """Test list functions with special characters."""
        self.assertEqual(flatten_list(['😀', ['😁', '😂']]), ['😀', '😁', '😂'])
        self.assertEqual(remove_duplicates(['café', 'café', 'naïve']), ['café', 'naïve'])

    def test_unicode_in_dicts(self):
        """Test dictionary functions with Unicode keys and values."""
        dict1 = {'名前': 'John', 'город': 'Moscow'}
        dict2 = {'país': 'Spain'}
        result = merge_dicts(dict1, dict2)
        self.assertIn('名前', result)
        self.assertIn('país', result)


class TestErrorHandling(unittest.TestCase):
    """Test suite for error handling and invalid input types."""

    def test_string_functions_with_invalid_types(self):
        """Test string functions with invalid input types."""
        with self.assertRaises((TypeError, AttributeError)):
            reverse_string(123)

        with self.assertRaises((TypeError, AttributeError)):
            is_palindrome(None)

        with self.assertRaises((TypeError, AttributeError)):
            count_words(42)

    def test_list_functions_with_invalid_types(self):
        """Test list functions with invalid input types."""
        with self.assertRaises((TypeError, AttributeError)):
            flatten_list("not a list")

        with self.assertRaises((TypeError, AttributeError)):
            remove_duplicates(123)

    def test_find_max_min_with_non_numeric(self):
        """Test find_max_min with non-numeric values."""
        with self.assertRaises((TypeError, ValueError)):
            find_max_min(['a', 'b', 'c'])

    def test_validation_with_invalid_types(self):
        """Test validation functions with invalid input types."""
        with self.assertRaises((TypeError, AttributeError)):
            is_email_valid(123)

        with self.assertRaises((TypeError, AttributeError)):
            validate_phone_number(None)

    def test_dict_functions_with_invalid_types(self):
        """Test dictionary functions with invalid input types."""
        with self.assertRaises((TypeError, AttributeError)):
            merge_dicts("not a dict", {})

        with self.assertRaises((TypeError, AttributeError)):
            filter_dict_by_keys("not a dict", ['a'])


if __name__ == '__main__':
    unittest.main()
