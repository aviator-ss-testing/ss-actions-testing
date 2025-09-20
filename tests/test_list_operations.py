"""
Comprehensive test suite for list_operations module.

This module provides thorough test coverage for all list processing functions
including positive cases, negative cases, edge cases, and error conditions.
Tests validate proper error handling and boundary value scenarios.
"""

import unittest
import sys
import os

# Add the parent directory to the path so we can import the modules being tested
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from list_operations import find_max, find_min, calculate_average, remove_duplicates, sort_list


class TestListOperations(unittest.TestCase):
    """Test suite for list operations module with comprehensive coverage."""

    def setUp(self):
        """Set up test data for list operations tests."""
        # Numeric test data
        self.numeric_list = [3, 1, 4, 1, 5, 9, 2, 6]
        self.single_number = [42]
        self.negative_numbers = [-5, -2, -8, -1]
        self.mixed_numbers = [3.14, 2, 7.5, 1]
        self.zeros = [0, 0, 0]

        # String test data
        self.string_list = ["apple", "banana", "cherry", "date"]
        self.single_string = ["hello"]
        self.mixed_case_strings = ["Apple", "apple", "APPLE", "aPpLe"]

        # Edge case data
        self.empty_list = []
        self.duplicate_numbers = [5, 3, 5, 1, 3, 5]
        self.mixed_types_valid = [1, 2, 3]  # All comparable
        self.mixed_types_invalid = [1, "string", 3]  # Incomparable

        # Complex objects for remove_duplicates testing
        self.with_unhashable = [1, [1, 2], 3, [1, 2], 4]
        self.with_dicts = [{"a": 1}, {"b": 2}, {"a": 1}]

    def tearDown(self):
        """Clean up after each test."""
        pass

    # Tests for find_max function
    def test_find_max_numeric_list(self):
        """Test find_max with numeric values."""
        result = find_max(self.numeric_list)
        self.assertEqual(result, 9)

    def test_find_max_single_element(self):
        """Test find_max with single element."""
        result = find_max(self.single_number)
        self.assertEqual(result, 42)

    def test_find_max_negative_numbers(self):
        """Test find_max with negative numbers."""
        result = find_max(self.negative_numbers)
        self.assertEqual(result, -1)

    def test_find_max_string_list(self):
        """Test find_max with strings (lexicographic order)."""
        result = find_max(self.string_list)
        self.assertEqual(result, "date")

    def test_find_max_empty_list(self):
        """Test find_max raises ValueError for empty list."""
        with self.assertRaises(ValueError) as context:
            find_max(self.empty_list)
        self.assertIn("Cannot find maximum of empty list", str(context.exception))

    def test_find_max_non_list_input(self):
        """Test find_max raises TypeError for non-list input."""
        with self.assertRaises(TypeError) as context:
            find_max("not a list")
        self.assertIn("Input must be a list", str(context.exception))

    def test_find_max_incomparable_types(self):
        """Test find_max raises TypeError for incomparable types."""
        with self.assertRaises(TypeError) as context:
            find_max(self.mixed_types_invalid)
        self.assertIn("List contains incomparable types", str(context.exception))

    # Tests for find_min function
    def test_find_min_numeric_list(self):
        """Test find_min with numeric values."""
        result = find_min(self.numeric_list)
        self.assertEqual(result, 1)

    def test_find_min_single_element(self):
        """Test find_min with single element."""
        result = find_min(self.single_number)
        self.assertEqual(result, 42)

    def test_find_min_negative_numbers(self):
        """Test find_min with negative numbers."""
        result = find_min(self.negative_numbers)
        self.assertEqual(result, -8)

    def test_find_min_string_list(self):
        """Test find_min with strings (lexicographic order)."""
        result = find_min(self.string_list)
        self.assertEqual(result, "apple")

    def test_find_min_empty_list(self):
        """Test find_min raises ValueError for empty list."""
        with self.assertRaises(ValueError) as context:
            find_min(self.empty_list)
        self.assertIn("Cannot find minimum of empty list", str(context.exception))

    def test_find_min_non_list_input(self):
        """Test find_min raises TypeError for non-list input."""
        with self.assertRaises(TypeError) as context:
            find_min(None)
        self.assertIn("Input must be a list", str(context.exception))

    def test_find_min_incomparable_types(self):
        """Test find_min raises TypeError for incomparable types."""
        with self.assertRaises(TypeError) as context:
            find_min(self.mixed_types_invalid)
        self.assertIn("List contains incomparable types", str(context.exception))

    # Tests for calculate_average function
    def test_calculate_average_numeric_list(self):
        """Test calculate_average with numeric values."""
        result = calculate_average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3.0)

    def test_calculate_average_single_element(self):
        """Test calculate_average with single element."""
        result = calculate_average([10])
        self.assertEqual(result, 10.0)

    def test_calculate_average_floats(self):
        """Test calculate_average with floating point numbers."""
        result = calculate_average([1.5, 2.5, 3.0])
        self.assertAlmostEqual(result, 2.333333333333333)

    def test_calculate_average_negative_numbers(self):
        """Test calculate_average with negative numbers."""
        result = calculate_average([-1, -2, -3])
        self.assertEqual(result, -2.0)

    def test_calculate_average_zeros(self):
        """Test calculate_average with zeros."""
        result = calculate_average(self.zeros)
        self.assertEqual(result, 0.0)

    def test_calculate_average_empty_list(self):
        """Test calculate_average raises ValueError for empty list."""
        with self.assertRaises(ValueError) as context:
            calculate_average(self.empty_list)
        self.assertIn("Cannot calculate average of empty list", str(context.exception))

    def test_calculate_average_non_list_input(self):
        """Test calculate_average raises TypeError for non-list input."""
        with self.assertRaises(TypeError) as context:
            calculate_average(123)
        self.assertIn("Input must be a list", str(context.exception))

    def test_calculate_average_non_numeric_values(self):
        """Test calculate_average raises TypeError for non-numeric values."""
        with self.assertRaises(TypeError) as context:
            calculate_average([1, "string", 3])
        self.assertIn("All elements must be numeric", str(context.exception))

    def test_calculate_average_mixed_numeric_types(self):
        """Test calculate_average works with mixed int/float."""
        result = calculate_average([1, 2.0, 3])
        self.assertEqual(result, 2.0)

    # Tests for remove_duplicates function
    def test_remove_duplicates_numeric(self):
        """Test remove_duplicates with numeric values."""
        result = remove_duplicates(self.duplicate_numbers)
        expected = [5, 3, 1]
        self.assertEqual(result, expected)

    def test_remove_duplicates_strings(self):
        """Test remove_duplicates with strings."""
        result = remove_duplicates(["a", "b", "a", "c", "b"])
        expected = ["a", "b", "c"]
        self.assertEqual(result, expected)

    def test_remove_duplicates_no_duplicates(self):
        """Test remove_duplicates when no duplicates exist."""
        result = remove_duplicates([1, 2, 3, 4])
        expected = [1, 2, 3, 4]
        self.assertEqual(result, expected)

    def test_remove_duplicates_all_same(self):
        """Test remove_duplicates when all elements are the same."""
        result = remove_duplicates([7, 7, 7, 7])
        expected = [7]
        self.assertEqual(result, expected)

    def test_remove_duplicates_empty_list(self):
        """Test remove_duplicates with empty list."""
        result = remove_duplicates(self.empty_list)
        expected = []
        self.assertEqual(result, expected)

    def test_remove_duplicates_single_element(self):
        """Test remove_duplicates with single element."""
        result = remove_duplicates([42])
        expected = [42]
        self.assertEqual(result, expected)

    def test_remove_duplicates_unhashable_types(self):
        """Test remove_duplicates with unhashable types like lists."""
        result = remove_duplicates(self.with_unhashable)
        expected = [1, [1, 2], 3, 4]
        self.assertEqual(result, expected)

    def test_remove_duplicates_mixed_types(self):
        """Test remove_duplicates with mixed data types."""
        test_list = [1, "a", 1, 2.5, "a", 2.5]
        result = remove_duplicates(test_list)
        expected = [1, "a", 2.5]
        self.assertEqual(result, expected)

    def test_remove_duplicates_non_list_input(self):
        """Test remove_duplicates raises TypeError for non-list input."""
        with self.assertRaises(TypeError) as context:
            remove_duplicates("not a list")
        self.assertIn("Input must be a list", str(context.exception))

    # Tests for sort_list function
    def test_sort_list_numeric_ascending(self):
        """Test sort_list with numeric values in ascending order."""
        result = sort_list([3, 1, 4, 1, 5])
        expected = [1, 1, 3, 4, 5]
        self.assertEqual(result, expected)

    def test_sort_list_numeric_descending(self):
        """Test sort_list with numeric values in descending order."""
        result = sort_list([3, 1, 4, 1, 5], reverse=True)
        expected = [5, 4, 3, 1, 1]
        self.assertEqual(result, expected)

    def test_sort_list_strings_ascending(self):
        """Test sort_list with strings in ascending order."""
        result = sort_list(["charlie", "alice", "bob"])
        expected = ["alice", "bob", "charlie"]
        self.assertEqual(result, expected)

    def test_sort_list_strings_descending(self):
        """Test sort_list with strings in descending order."""
        result = sort_list(["charlie", "alice", "bob"], reverse=True)
        expected = ["charlie", "bob", "alice"]
        self.assertEqual(result, expected)

    def test_sort_list_empty(self):
        """Test sort_list with empty list."""
        result = sort_list(self.empty_list)
        expected = []
        self.assertEqual(result, expected)

    def test_sort_list_single_element(self):
        """Test sort_list with single element."""
        result = sort_list([42])
        expected = [42]
        self.assertEqual(result, expected)

    def test_sort_list_already_sorted(self):
        """Test sort_list with already sorted list."""
        result = sort_list([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)

    def test_sort_list_reverse_sorted(self):
        """Test sort_list with reverse sorted list."""
        result = sort_list([5, 4, 3, 2, 1])
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)

    def test_sort_list_non_list_input(self):
        """Test sort_list raises TypeError for non-list input."""
        with self.assertRaises(TypeError) as context:
            sort_list("not a list")
        self.assertIn("Input must be a list", str(context.exception))

    def test_sort_list_invalid_reverse_parameter(self):
        """Test sort_list raises TypeError for invalid reverse parameter."""
        with self.assertRaises(TypeError) as context:
            sort_list([1, 2, 3], reverse="invalid")
        self.assertIn("reverse parameter must be a boolean", str(context.exception))

    def test_sort_list_incomparable_types(self):
        """Test sort_list raises TypeError for incomparable types."""
        with self.assertRaises(TypeError) as context:
            sort_list([1, "string", 3])
        self.assertIn("List contains incomparable types", str(context.exception))

    def test_sort_list_preserves_original(self):
        """Test that sort_list doesn't modify the original list."""
        original = [3, 1, 4, 1, 5]
        original_copy = original.copy()
        result = sort_list(original)

        # Original list should be unchanged
        self.assertEqual(original, original_copy)
        # Result should be sorted
        self.assertEqual(result, [1, 1, 3, 4, 5])

    # Integration tests combining multiple functions
    def test_integration_max_min_average(self):
        """Integration test using multiple functions on the same data."""
        test_data = [10, 5, 8, 3, 7, 9, 1, 6, 4, 2]

        max_val = find_max(test_data)
        min_val = find_min(test_data)
        avg_val = calculate_average(test_data)

        self.assertEqual(max_val, 10)
        self.assertEqual(min_val, 1)
        self.assertEqual(avg_val, 5.5)

    def test_integration_remove_duplicates_then_sort(self):
        """Integration test: remove duplicates then sort."""
        test_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

        no_duplicates = remove_duplicates(test_data)
        sorted_result = sort_list(no_duplicates)

        expected = [1, 2, 3, 4, 5, 6, 9]
        self.assertEqual(sorted_result, expected)

    def test_boundary_very_large_numbers(self):
        """Test with very large numbers."""
        large_numbers = [10**10, 10**15, 10**5]

        self.assertEqual(find_max(large_numbers), 10**15)
        self.assertEqual(find_min(large_numbers), 10**5)
        self.assertAlmostEqual(calculate_average(large_numbers),
                             (10**10 + 10**15 + 10**5) / 3)

    def test_boundary_very_small_numbers(self):
        """Test with very small numbers."""
        small_numbers = [1e-10, 1e-15, 1e-5]

        self.assertEqual(find_max(small_numbers), 1e-5)
        self.assertEqual(find_min(small_numbers), 1e-15)
        self.assertAlmostEqual(calculate_average(small_numbers),
                             (1e-10 + 1e-15 + 1e-5) / 3)


if __name__ == '__main__':
    unittest.main()