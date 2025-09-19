import unittest
import datetime
import tempfile
import shutil
import os
from pathlib import Path
from unittest.mock import patch, mock_open

import utils


class TestStringManipulation(unittest.TestCase):
    """Test suite for string manipulation functions."""

    def test_reverse_string_normal_cases(self):
        """Test reverse_string with normal input cases."""
        self.assertEqual(utils.reverse_string("hello"), "olleh")
        self.assertEqual(utils.reverse_string("world"), "dlrow")
        self.assertEqual(utils.reverse_string("Python"), "nohtyP")

    def test_reverse_string_edge_cases(self):
        """Test reverse_string with edge cases."""
        self.assertEqual(utils.reverse_string(""), "")
        self.assertEqual(utils.reverse_string("a"), "a")
        self.assertEqual(utils.reverse_string("12345"), "54321")
        self.assertEqual(utils.reverse_string("!@#$%"), "%$#@!")

    def test_reverse_string_special_characters(self):
        """Test reverse_string with special characters and spaces."""
        self.assertEqual(utils.reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(utils.reverse_string("a b c"), "c b a")
        self.assertEqual(utils.reverse_string("test!@#"), "#@!tset")

    def test_is_palindrome_true_cases(self):
        """Test is_palindrome with valid palindromes."""
        self.assertTrue(utils.is_palindrome("racecar"))
        self.assertTrue(utils.is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(utils.is_palindrome("race a car"))
        self.assertTrue(utils.is_palindrome("12321"))
        self.assertTrue(utils.is_palindrome("Madam"))

    def test_is_palindrome_false_cases(self):
        """Test is_palindrome with non-palindromes."""
        self.assertFalse(utils.is_palindrome("hello"))
        self.assertFalse(utils.is_palindrome("world"))
        self.assertFalse(utils.is_palindrome("Python"))
        self.assertFalse(utils.is_palindrome("12345"))

    def test_is_palindrome_edge_cases(self):
        """Test is_palindrome with edge cases."""
        self.assertTrue(utils.is_palindrome(""))
        self.assertTrue(utils.is_palindrome("a"))
        self.assertTrue(utils.is_palindrome("A"))
        self.assertTrue(utils.is_palindrome("!@#@!"))

    def test_count_vowels_normal_cases(self):
        """Test count_vowels with normal strings."""
        self.assertEqual(utils.count_vowels("hello"), 2)
        self.assertEqual(utils.count_vowels("world"), 1)
        self.assertEqual(utils.count_vowels("Python"), 1)
        self.assertEqual(utils.count_vowels("aeiou"), 5)
        self.assertEqual(utils.count_vowels("AEIOU"), 5)

    def test_count_vowels_edge_cases(self):
        """Test count_vowels with edge cases."""
        self.assertEqual(utils.count_vowels(""), 0)
        self.assertEqual(utils.count_vowels("bcdfg"), 0)
        self.assertEqual(utils.count_vowels("12345"), 0)
        self.assertEqual(utils.count_vowels("!@#$%"), 0)

    def test_count_vowels_mixed_case(self):
        """Test count_vowels with mixed case strings."""
        self.assertEqual(utils.count_vowels("Hello World"), 3)
        self.assertEqual(utils.count_vowels("AeIoU"), 5)
        self.assertEqual(utils.count_vowels("Programming Is Fun"), 5)


class TestListManipulation(unittest.TestCase):
    """Test suite for list manipulation functions."""

    def test_flatten_list_normal_cases(self):
        """Test flatten_list with normal nested lists."""
        self.assertEqual(utils.flatten_list([1, [2, 3], 4]), [1, 2, 3, 4])
        self.assertEqual(utils.flatten_list([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])
        self.assertEqual(utils.flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_flatten_list_edge_cases(self):
        """Test flatten_list with edge cases."""
        self.assertEqual(utils.flatten_list([]), [])
        self.assertEqual(utils.flatten_list([1, 2, 3]), [1, 2, 3])
        self.assertEqual(utils.flatten_list([[]]), [])
        self.assertEqual(utils.flatten_list([[[]]]), [])

    def test_flatten_list_mixed_types(self):
        """Test flatten_list with mixed data types."""
        self.assertEqual(utils.flatten_list([1, ["hello", 2], 3.5]), [1, "hello", 2, 3.5])
        self.assertEqual(utils.flatten_list([True, [False, [None]]]), [True, False, None])

    def test_remove_duplicates_normal_cases(self):
        """Test remove_duplicates with normal lists."""
        self.assertEqual(utils.remove_duplicates([1, 2, 2, 3, 3, 3]), [1, 2, 3])
        self.assertEqual(utils.remove_duplicates(['a', 'b', 'a', 'c']), ['a', 'b', 'c'])
        self.assertEqual(utils.remove_duplicates([1, 1, 1, 1]), [1])

    def test_remove_duplicates_edge_cases(self):
        """Test remove_duplicates with edge cases."""
        self.assertEqual(utils.remove_duplicates([]), [])
        self.assertEqual(utils.remove_duplicates([1]), [1])
        self.assertEqual(utils.remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_remove_duplicates_order_preservation(self):
        """Test that remove_duplicates preserves original order."""
        result = utils.remove_duplicates([3, 1, 2, 1, 3, 2])
        self.assertEqual(result, [3, 1, 2])

        result = utils.remove_duplicates(['z', 'a', 'b', 'a', 'z'])
        self.assertEqual(result, ['z', 'a', 'b'])

    def test_find_max_min_normal_cases(self):
        """Test find_max_min with normal lists."""
        self.assertEqual(utils.find_max_min([1, 2, 3, 4, 5]), (5, 1))
        self.assertEqual(utils.find_max_min([5, 4, 3, 2, 1]), (5, 1))
        self.assertEqual(utils.find_max_min([1.5, 2.7, 0.3, 4.8]), (4.8, 0.3))

    def test_find_max_min_single_element(self):
        """Test find_max_min with single element."""
        self.assertEqual(utils.find_max_min([42]), (42, 42))
        self.assertEqual(utils.find_max_min([3.14]), (3.14, 3.14))

    def test_find_max_min_negative_numbers(self):
        """Test find_max_min with negative numbers."""
        self.assertEqual(utils.find_max_min([-1, -5, -3]), (-1, -5))
        self.assertEqual(utils.find_max_min([-10, 5, -3, 8]), (8, -10))

    def test_find_max_min_empty_list(self):
        """Test find_max_min raises error for empty list."""
        with self.assertRaises(ValueError) as context:
            utils.find_max_min([])
        self.assertEqual(str(context.exception), "Cannot find max/min of empty list")


class TestValidationUtilities(unittest.TestCase):
    """Test suite for validation utility functions."""

    def test_is_email_valid_true_cases(self):
        """Test is_email_valid with valid email addresses."""
        valid_emails = [
            "test@example.com",
            "user.name@domain.co.uk",
            "first+last@subdomain.example.org",
            "123456@numbers.com",
            "test_user@test-domain.net"
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(utils.is_email_valid(email))

    def test_is_email_valid_false_cases(self):
        """Test is_email_valid with invalid email addresses."""
        invalid_emails = [
            "invalid-email",
            "@domain.com",
            "user@",
            "user@domain",
            "user.domain.com",
            "user@@domain.com",
            "user@domain..com",
            ""
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(utils.is_email_valid(email))

    def test_is_phone_valid_true_cases(self):
        """Test is_phone_valid with valid phone numbers."""
        valid_phones = [
            "1234567890",
            "(123) 456-7890",
            "123-456-7890",
            "123.456.7890",
            "+1 123 456 7890",
            "1-123-456-7890"
        ]
        for phone in valid_phones:
            with self.subTest(phone=phone):
                self.assertTrue(utils.is_phone_valid(phone))

    def test_is_phone_valid_false_cases(self):
        """Test is_phone_valid with invalid phone numbers."""
        invalid_phones = [
            "12345",
            "123456789012345",
            "abc-def-ghij",
            "(123) 45-7890",
            "123-45-67890",
            "+44 123 456 7890",  # UK format
            ""
        ]
        for phone in invalid_phones:
            with self.subTest(phone=phone):
                self.assertFalse(utils.is_phone_valid(phone))


class TestDateTimeUtilities(unittest.TestCase):
    """Test suite for date/time utility functions."""

    def test_days_between_normal_cases(self):
        """Test days_between with normal date ranges."""
        date1 = datetime.date(2023, 1, 1)
        date2 = datetime.date(2023, 1, 10)
        self.assertEqual(utils.days_between(date1, date2), 9)

        date1 = datetime.date(2023, 1, 15)
        date2 = datetime.date(2023, 1, 5)
        self.assertEqual(utils.days_between(date1, date2), 10)

    def test_days_between_same_date(self):
        """Test days_between with same dates."""
        date = datetime.date(2023, 1, 1)
        self.assertEqual(utils.days_between(date, date), 0)

    def test_days_between_different_years(self):
        """Test days_between across different years."""
        date1 = datetime.date(2022, 12, 31)
        date2 = datetime.date(2023, 1, 1)
        self.assertEqual(utils.days_between(date1, date2), 1)

        date1 = datetime.date(2023, 1, 1)
        date2 = datetime.date(2024, 1, 1)
        self.assertEqual(utils.days_between(date1, date2), 365)

    def test_format_date_default_format(self):
        """Test format_date with default format."""
        date = datetime.date(2023, 5, 15)
        self.assertEqual(utils.format_date(date), "2023-05-15")

    def test_format_date_custom_formats(self):
        """Test format_date with various custom formats."""
        date = datetime.date(2023, 5, 15)

        test_cases = [
            ("%d/%m/%Y", "15/05/2023"),
            ("%B %d, %Y", "May 15, 2023"),
            ("%m-%d-%y", "05-15-23"),
            ("%A, %B %d, %Y", "Monday, May 15, 2023")
        ]

        for format_str, expected in test_cases:
            with self.subTest(format=format_str):
                self.assertEqual(utils.format_date(date, format_str), expected)

    def test_is_weekend_weekend_dates(self):
        """Test is_weekend with weekend dates."""
        saturday = datetime.date(2023, 5, 13)  # Saturday
        sunday = datetime.date(2023, 5, 14)    # Sunday

        self.assertTrue(utils.is_weekend(saturday))
        self.assertTrue(utils.is_weekend(sunday))

    def test_is_weekend_weekday_dates(self):
        """Test is_weekend with weekday dates."""
        weekdays = [
            datetime.date(2023, 5, 15),  # Monday
            datetime.date(2023, 5, 16),  # Tuesday
            datetime.date(2023, 5, 17),  # Wednesday
            datetime.date(2023, 5, 18),  # Thursday
            datetime.date(2023, 5, 19),  # Friday
        ]

        for date in weekdays:
            with self.subTest(date=date):
                self.assertFalse(utils.is_weekend(date))


class TestFileSystemUtilities(unittest.TestCase):
    """Test suite for file system utility functions."""

    def setUp(self):
        """Set up temporary directory for file system tests."""
        self.test_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.test_dir)

    def test_get_file_extension_normal_cases(self):
        """Test get_file_extension with normal filenames."""
        test_cases = [
            ("document.pdf", ".pdf"),
            ("image.jpg", ".jpg"),
            ("script.py", ".py"),
            ("archive.tar.gz", ".gz"),
            ("README.md", ".md")
        ]

        for filename, expected in test_cases:
            with self.subTest(filename=filename):
                self.assertEqual(utils.get_file_extension(filename), expected)

    def test_get_file_extension_no_extension(self):
        """Test get_file_extension with files without extensions."""
        self.assertEqual(utils.get_file_extension("README"), "")
        self.assertEqual(utils.get_file_extension("Makefile"), "")
        self.assertEqual(utils.get_file_extension("file_without_ext"), "")

    def test_get_file_extension_case_handling(self):
        """Test get_file_extension converts to lowercase."""
        self.assertEqual(utils.get_file_extension("FILE.TXT"), ".txt")
        self.assertEqual(utils.get_file_extension("Image.JPG"), ".jpg")
        self.assertEqual(utils.get_file_extension("Document.PDF"), ".pdf")

    def test_get_file_extension_with_path(self):
        """Test get_file_extension with full file paths."""
        self.assertEqual(utils.get_file_extension("/path/to/file.txt"), ".txt")
        self.assertEqual(utils.get_file_extension("../relative/path/file.py"), ".py")
        self.assertEqual(utils.get_file_extension("./current/dir/file.json"), ".json")

    def test_create_directory_if_not_exists_new_directory(self):
        """Test creating a new directory."""
        new_dir = os.path.join(self.test_dir, "new_directory")

        # Directory should not exist initially
        self.assertFalse(os.path.exists(new_dir))

        # Create directory
        result = utils.create_directory_if_not_exists(new_dir)

        # Directory should now exist
        self.assertTrue(os.path.exists(new_dir))
        self.assertTrue(os.path.isdir(new_dir))

    def test_create_directory_if_not_exists_existing_directory(self):
        """Test with directory that already exists."""
        existing_dir = os.path.join(self.test_dir, "existing")
        os.makedirs(existing_dir)

        # Should not raise error and directory should still exist
        utils.create_directory_if_not_exists(existing_dir)
        self.assertTrue(os.path.exists(existing_dir))

    def test_create_directory_if_not_exists_nested_path(self):
        """Test creating nested directory structure."""
        nested_dir = os.path.join(self.test_dir, "level1", "level2", "level3")

        utils.create_directory_if_not_exists(nested_dir)

        self.assertTrue(os.path.exists(nested_dir))
        self.assertTrue(os.path.isdir(nested_dir))

    @patch('os.makedirs')
    def test_create_directory_if_not_exists_os_error(self, mock_makedirs):
        """Test handling of OS errors during directory creation."""
        mock_makedirs.side_effect = OSError("Permission denied")

        with self.assertRaises(OSError) as context:
            utils.create_directory_if_not_exists("/invalid/path")

        self.assertIn("Failed to create directory", str(context.exception))
        self.assertIn("Permission denied", str(context.exception))


class TestParametrizedCases(unittest.TestCase):
    """Test suite for parametrized test scenarios."""

    def test_string_functions_with_unicode(self):
        """Test string functions with Unicode characters."""
        unicode_strings = [
            ("café", "éfac"),  # reverse_string
            ("אמא", True),     # is_palindrome (Hebrew)
            ("naïve", 3),      # count_vowels
        ]

        for input_str, expected in unicode_strings:
            with self.subTest(input=input_str):
                if isinstance(expected, str):
                    self.assertEqual(utils.reverse_string(input_str), expected)
                elif isinstance(expected, bool):
                    self.assertEqual(utils.is_palindrome(input_str), expected)
                elif isinstance(expected, int):
                    self.assertEqual(utils.count_vowels(input_str), expected)

    def test_list_functions_with_various_types(self):
        """Test list functions with different data types."""
        mixed_lists = [
            [1, "hello", 3.14, True, None],
            [[], [1], [1, 2], [1, 2, 3]],
            ["a", "b", "c", 1, 2, 3]
        ]

        for test_list in mixed_lists:
            with self.subTest(list=test_list):
                # Test flatten_list doesn't crash with mixed types
                if any(isinstance(item, list) for item in test_list):
                    result = utils.flatten_list(test_list)
                    self.assertIsInstance(result, list)

                # Test remove_duplicates preserves order
                unique_result = utils.remove_duplicates(test_list)
                self.assertIsInstance(unique_result, list)

    def test_date_functions_edge_dates(self):
        """Test date functions with edge case dates."""
        edge_dates = [
            datetime.date(2000, 2, 29),  # Leap year
            datetime.date(1900, 2, 28),  # Non-leap year
            datetime.date(2023, 12, 31), # Year end
            datetime.date(2024, 1, 1),   # Year start
        ]

        for test_date in edge_dates:
            with self.subTest(date=test_date):
                # Test format_date works with edge dates
                formatted = utils.format_date(test_date)
                self.assertIsInstance(formatted, str)

                # Test is_weekend works with edge dates
                weekend_result = utils.is_weekend(test_date)
                self.assertIsInstance(weekend_result, bool)


if __name__ == '__main__':
    # Run all tests with verbose output
    unittest.main(verbosity=2)