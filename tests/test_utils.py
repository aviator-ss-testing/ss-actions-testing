"""Test cases for utility functions module."""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import utils


class TestStringManipulation(unittest.TestCase):
    """Test cases for string manipulation functions."""

    def test_reverse_string_basic(self):
        """Test basic string reversal."""
        self.assertEqual(utils.reverse_string("hello"), "olleh")
        self.assertEqual(utils.reverse_string("Python"), "nohtyP")

    def test_reverse_string_empty(self):
        """Test reversing empty string."""
        self.assertEqual(utils.reverse_string(""), "")

    def test_reverse_string_single_char(self):
        """Test reversing single character."""
        self.assertEqual(utils.reverse_string("a"), "a")

    def test_reverse_string_unicode(self):
        """Test reversing Unicode strings."""
        self.assertEqual(utils.reverse_string("café"), "éfac")
        self.assertEqual(utils.reverse_string("你好世界"), "界世好你")
        self.assertEqual(utils.reverse_string("😀🎉🚀"), "🚀🎉😀")

    def test_reverse_string_special_chars(self):
        """Test reversing strings with special characters."""
        self.assertEqual(utils.reverse_string("hello!@#$%"), "%$#@!olleh")
        self.assertEqual(utils.reverse_string("a\nb\tc"), "c\tb\na")

    def test_is_palindrome_basic(self):
        """Test basic palindrome detection."""
        self.assertTrue(utils.is_palindrome("racecar"))
        self.assertTrue(utils.is_palindrome("noon"))
        self.assertFalse(utils.is_palindrome("hello"))

    def test_is_palindrome_case_insensitive(self):
        """Test palindrome with mixed case."""
        self.assertTrue(utils.is_palindrome("RaceCar"))
        self.assertTrue(utils.is_palindrome("NooN"))

    def test_is_palindrome_with_spaces(self):
        """Test palindrome with spaces and punctuation."""
        self.assertTrue(utils.is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(utils.is_palindrome("race car"))
        self.assertTrue(utils.is_palindrome("Was it a car or a cat I saw?"))

    def test_is_palindrome_empty(self):
        """Test empty string is palindrome."""
        self.assertTrue(utils.is_palindrome(""))

    def test_is_palindrome_single_char(self):
        """Test single character is palindrome."""
        self.assertTrue(utils.is_palindrome("a"))

    def test_is_palindrome_numbers(self):
        """Test palindrome with numbers."""
        self.assertTrue(utils.is_palindrome("12321"))
        self.assertFalse(utils.is_palindrome("12345"))

    def test_count_words_basic(self):
        """Test basic word counting."""
        self.assertEqual(utils.count_words("hello world"), 2)
        self.assertEqual(utils.count_words("one two three four"), 4)

    def test_count_words_empty(self):
        """Test word count of empty string."""
        self.assertEqual(utils.count_words(""), 0)
        self.assertEqual(utils.count_words("   "), 0)

    def test_count_words_single(self):
        """Test counting single word."""
        self.assertEqual(utils.count_words("hello"), 1)

    def test_count_words_extra_spaces(self):
        """Test word counting with multiple spaces."""
        self.assertEqual(utils.count_words("hello  world"), 2)
        self.assertEqual(utils.count_words("  hello   world  "), 2)

    def test_count_words_unicode(self):
        """Test word counting with Unicode characters."""
        self.assertEqual(utils.count_words("café résumé"), 2)
        self.assertEqual(utils.count_words("你好 世界"), 2)

    def test_count_words_special_chars(self):
        """Test word counting with special characters."""
        self.assertEqual(utils.count_words("hello-world"), 1)
        self.assertEqual(utils.count_words("test@example.com"), 1)


class TestListProcessing(unittest.TestCase):
    """Test cases for list processing functions."""

    def test_flatten_list_basic(self):
        """Test basic list flattening."""
        self.assertEqual(utils.flatten_list([1, 2, 3]), [1, 2, 3])
        self.assertEqual(utils.flatten_list([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_flatten_list_deeply_nested(self):
        """Test deeply nested list flattening."""
        self.assertEqual(utils.flatten_list([1, [2, [3, [4, 5]]]]), [1, 2, 3, 4, 5])
        self.assertEqual(utils.flatten_list([[[[1]]]]), [1])

    def test_flatten_list_empty(self):
        """Test flattening empty list."""
        self.assertEqual(utils.flatten_list([]), [])
        self.assertEqual(utils.flatten_list([[], [], []]), [])

    def test_flatten_list_mixed_types(self):
        """Test flattening list with mixed types."""
        self.assertEqual(utils.flatten_list([1, "hello", [2, "world"], 3.14]), [1, "hello", 2, "world", 3.14])
        self.assertEqual(utils.flatten_list([True, [False, [None]]]), [True, False, None])

    def test_flatten_list_with_strings(self):
        """Test flattening preserves strings (doesn't iterate over chars)."""
        result = utils.flatten_list(["hello", ["world"]])
        self.assertEqual(result, ["hello", "world"])

    def test_remove_duplicates_basic(self):
        """Test basic duplicate removal."""
        self.assertEqual(utils.remove_duplicates([1, 2, 2, 3, 3, 3]), [1, 2, 3])
        self.assertEqual(utils.remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_remove_duplicates_order_preserved(self):
        """Test that order is preserved when removing duplicates."""
        self.assertEqual(utils.remove_duplicates([3, 1, 2, 1, 3]), [3, 1, 2])

    def test_remove_duplicates_empty(self):
        """Test removing duplicates from empty list."""
        self.assertEqual(utils.remove_duplicates([]), [])

    def test_remove_duplicates_mixed_types(self):
        """Test removing duplicates with mixed types."""
        self.assertEqual(utils.remove_duplicates([1, "1", 1, "1", 2]), [1, "1", 2])
        self.assertEqual(utils.remove_duplicates([True, 1, False, 0]), [True, False])

    def test_remove_duplicates_strings(self):
        """Test removing duplicate strings."""
        self.assertEqual(utils.remove_duplicates(["a", "b", "a", "c", "b"]), ["a", "b", "c"])

    def test_remove_duplicates_unhashable(self):
        """Test removing duplicates with unhashable types (dicts, lists)."""
        result = utils.remove_duplicates([[1, 2], [3, 4], [1, 2]])
        self.assertEqual(len(result), 2)

    def test_find_max_min_basic(self):
        """Test finding max and min in basic lists."""
        self.assertEqual(utils.find_max_min([1, 2, 3, 4, 5]), (5, 1))
        self.assertEqual(utils.find_max_min([5, 4, 3, 2, 1]), (5, 1))

    def test_find_max_min_single_element(self):
        """Test finding max and min in single-element list."""
        self.assertEqual(utils.find_max_min([42]), (42, 42))

    def test_find_max_min_negative(self):
        """Test finding max and min with negative numbers."""
        self.assertEqual(utils.find_max_min([-5, -2, -10, -1]), (-1, -10))

    def test_find_max_min_mixed(self):
        """Test finding max and min with mixed positive and negative."""
        self.assertEqual(utils.find_max_min([-5, 0, 5, -10, 10]), (10, -10))

    def test_find_max_min_floats(self):
        """Test finding max and min with floating point numbers."""
        self.assertEqual(utils.find_max_min([1.5, 2.7, 0.3, 5.9]), (5.9, 0.3))

    def test_find_max_min_empty_raises(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError):
            utils.find_max_min([])

    def test_find_max_min_large_list(self):
        """Test performance with large list."""
        large_list = list(range(10000, 0, -1))
        self.assertEqual(utils.find_max_min(large_list), (10000, 1))


class TestDataValidation(unittest.TestCase):
    """Test cases for data validation functions."""

    def test_is_email_valid_basic(self):
        """Test basic valid email addresses."""
        self.assertTrue(utils.is_email_valid("user@example.com"))
        self.assertTrue(utils.is_email_valid("test.user@domain.com"))
        self.assertTrue(utils.is_email_valid("user+tag@example.org"))

    def test_is_email_valid_invalid(self):
        """Test invalid email addresses."""
        self.assertFalse(utils.is_email_valid("invalid"))
        self.assertFalse(utils.is_email_valid("@example.com"))
        self.assertFalse(utils.is_email_valid("user@"))
        self.assertFalse(utils.is_email_valid("user@.com"))
        self.assertFalse(utils.is_email_valid("user space@example.com"))

    def test_is_email_valid_edge_cases(self):
        """Test edge cases for email validation."""
        self.assertTrue(utils.is_email_valid("a@b.co"))
        self.assertTrue(utils.is_email_valid("user123@test-domain.com"))
        self.assertFalse(utils.is_email_valid(""))
        self.assertFalse(utils.is_email_valid("user@domain"))

    def test_is_email_valid_special_chars(self):
        """Test email validation with special characters."""
        self.assertTrue(utils.is_email_valid("user.name+tag@example.co.uk"))
        self.assertTrue(utils.is_email_valid("user_123@domain-test.com"))
        self.assertFalse(utils.is_email_valid("user#name@example.com"))

    def test_validate_phone_number_basic(self):
        """Test basic valid phone numbers."""
        self.assertTrue(utils.validate_phone_number("1234567890"))
        self.assertTrue(utils.validate_phone_number("11234567890"))

    def test_validate_phone_number_formatted(self):
        """Test valid phone numbers with formatting."""
        self.assertTrue(utils.validate_phone_number("(123) 456-7890"))
        self.assertTrue(utils.validate_phone_number("123-456-7890"))
        self.assertTrue(utils.validate_phone_number("1 (123) 456-7890"))
        self.assertTrue(utils.validate_phone_number("123.456.7890"))

    def test_validate_phone_number_invalid(self):
        """Test invalid phone numbers."""
        self.assertFalse(utils.validate_phone_number("123"))
        self.assertFalse(utils.validate_phone_number("12345"))
        self.assertFalse(utils.validate_phone_number("123456789012"))
        self.assertFalse(utils.validate_phone_number(""))

    def test_validate_phone_number_edge_cases(self):
        """Test edge cases for phone validation."""
        self.assertFalse(utils.validate_phone_number("abcdefghij"))
        self.assertTrue(utils.validate_phone_number("+1 (123) 456-7890"))
        self.assertFalse(utils.validate_phone_number("21234567890"))


class TestDictionaryManipulation(unittest.TestCase):
    """Test cases for dictionary manipulation functions."""

    def test_merge_dicts_basic(self):
        """Test basic dictionary merging."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        result = utils.merge_dicts(dict1, dict2)
        self.assertEqual(result, {"a": 1, "b": 2, "c": 3, "d": 4})

    def test_merge_dicts_override(self):
        """Test that dict2 values override dict1."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        result = utils.merge_dicts(dict1, dict2)
        self.assertEqual(result, {"a": 1, "b": 3, "c": 4})

    def test_merge_dicts_empty(self):
        """Test merging with empty dictionaries."""
        self.assertEqual(utils.merge_dicts({}, {"a": 1}), {"a": 1})
        self.assertEqual(utils.merge_dicts({"a": 1}, {}), {"a": 1})
        self.assertEqual(utils.merge_dicts({}, {}), {})

    def test_merge_dicts_original_unchanged(self):
        """Test that original dictionaries are not modified."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3}
        result = utils.merge_dicts(dict1, dict2)
        self.assertEqual(dict1, {"a": 1, "b": 2})
        self.assertEqual(dict2, {"c": 3})

    def test_merge_dicts_complex_values(self):
        """Test merging dictionaries with complex values."""
        dict1 = {"a": [1, 2], "b": {"nested": True}}
        dict2 = {"c": (3, 4), "d": None}
        result = utils.merge_dicts(dict1, dict2)
        self.assertEqual(result["a"], [1, 2])
        self.assertEqual(result["b"], {"nested": True})
        self.assertEqual(result["c"], (3, 4))
        self.assertIsNone(result["d"])

    def test_filter_dict_by_keys_basic(self):
        """Test basic dictionary filtering."""
        dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
        result = utils.filter_dict_by_keys(dictionary, ["a", "c"])
        self.assertEqual(result, {"a": 1, "c": 3})

    def test_filter_dict_by_keys_empty(self):
        """Test filtering with empty keys list."""
        dictionary = {"a": 1, "b": 2}
        result = utils.filter_dict_by_keys(dictionary, [])
        self.assertEqual(result, {})

    def test_filter_dict_by_keys_nonexistent(self):
        """Test filtering with nonexistent keys."""
        dictionary = {"a": 1, "b": 2}
        result = utils.filter_dict_by_keys(dictionary, ["c", "d"])
        self.assertEqual(result, {})

    def test_filter_dict_by_keys_mixed(self):
        """Test filtering with mix of existent and nonexistent keys."""
        dictionary = {"a": 1, "b": 2, "c": 3}
        result = utils.filter_dict_by_keys(dictionary, ["a", "x", "c", "y"])
        self.assertEqual(result, {"a": 1, "c": 3})

    def test_filter_dict_by_keys_original_unchanged(self):
        """Test that original dictionary is not modified."""
        dictionary = {"a": 1, "b": 2, "c": 3}
        result = utils.filter_dict_by_keys(dictionary, ["a"])
        self.assertEqual(dictionary, {"a": 1, "b": 2, "c": 3})

    def test_filter_dict_by_keys_all_keys(self):
        """Test filtering with all keys."""
        dictionary = {"a": 1, "b": 2}
        result = utils.filter_dict_by_keys(dictionary, ["a", "b"])
        self.assertEqual(result, {"a": 1, "b": 2})


class TestPerformance(unittest.TestCase):
    """Performance test cases for functions handling large datasets."""

    def test_flatten_list_large_dataset(self):
        """Test flattening performance with large nested list."""
        large_nested = [[i] for i in range(1000)]
        result = utils.flatten_list(large_nested)
        self.assertEqual(len(result), 1000)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[-1], 999)

    def test_remove_duplicates_large_dataset(self):
        """Test removing duplicates from large list."""
        large_list = list(range(500)) * 10
        result = utils.remove_duplicates(large_list)
        self.assertEqual(len(result), 500)
        self.assertEqual(sorted(result), list(range(500)))

    def test_reverse_string_large(self):
        """Test reversing very long string."""
        large_string = "a" * 10000
        result = utils.reverse_string(large_string)
        self.assertEqual(len(result), 10000)
        self.assertEqual(result, large_string)

    def test_count_words_large_text(self):
        """Test word counting on large text."""
        large_text = " ".join(["word"] * 5000)
        result = utils.count_words(large_text)
        self.assertEqual(result, 5000)

    def test_merge_dicts_large(self):
        """Test merging large dictionaries."""
        dict1 = {f"key{i}": i for i in range(1000)}
        dict2 = {f"key{i}": i * 2 for i in range(500, 1500)}
        result = utils.merge_dicts(dict1, dict2)
        self.assertEqual(len(result), 1500)
        self.assertEqual(result["key0"], 0)
        self.assertEqual(result["key500"], 1000)


if __name__ == '__main__':
    unittest.main()