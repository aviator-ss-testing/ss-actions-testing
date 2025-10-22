"""Tests for list manipulation utilities."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.utils.lists import flatten, chunk, rotate, find_duplicates, merge_sorted


class TestFlatten(unittest.TestCase):

    def test_deeply_nested_lists(self):
        result = flatten([1, [2, [3, [4, [5]]]]])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_mixed_nesting_depths(self):
        result = flatten([1, [2, 3], 4, [5, [6, 7]], 8])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_empty_list(self):
        result = flatten([])
        self.assertEqual(result, [])

    def test_empty_nested_lists(self):
        result = flatten([[], [[]], [[], []]])
        self.assertEqual(result, [])

    def test_single_level_list(self):
        result = flatten([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_all_nested(self):
        result = flatten([[1], [2], [3]])
        self.assertEqual(result, [1, 2, 3])

    def test_type_error_non_list(self):
        with self.assertRaises(TypeError):
            flatten("not a list")

    def test_type_error_none(self):
        with self.assertRaises(TypeError):
            flatten(None)


class TestChunk(unittest.TestCase):

    def test_exact_division(self):
        result = chunk([1, 2, 3, 4, 5, 6], 2)
        self.assertEqual(result, [[1, 2], [3, 4], [5, 6]])

    def test_exact_division_size_three(self):
        result = chunk([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
        self.assertEqual(result, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_with_remainder(self):
        result = chunk([1, 2, 3, 4, 5], 2)
        self.assertEqual(result, [[1, 2], [3, 4], [5]])

    def test_with_remainder_larger_chunks(self):
        result = chunk([1, 2, 3, 4, 5, 6, 7], 3)
        self.assertEqual(result, [[1, 2, 3], [4, 5, 6], [7]])

    def test_empty_list(self):
        result = chunk([], 2)
        self.assertEqual(result, [])

    def test_chunk_size_larger_than_list(self):
        result = chunk([1, 2, 3], 5)
        self.assertEqual(result, [[1, 2, 3]])

    def test_chunk_size_one(self):
        result = chunk([1, 2, 3], 1)
        self.assertEqual(result, [[1], [2], [3]])

    def test_value_error_zero_size(self):
        with self.assertRaises(ValueError):
            chunk([1, 2, 3], 0)

    def test_value_error_negative_size(self):
        with self.assertRaises(ValueError):
            chunk([1, 2, 3], -1)

    def test_type_error_non_list(self):
        with self.assertRaises(TypeError):
            chunk("not a list", 2)

    def test_type_error_non_int_size(self):
        with self.assertRaises(TypeError):
            chunk([1, 2, 3], "2")


class TestRotate(unittest.TestCase):

    def test_positive_rotation(self):
        result = rotate([1, 2, 3, 4, 5], 2)
        self.assertEqual(result, [4, 5, 1, 2, 3])

    def test_positive_rotation_by_one(self):
        result = rotate([1, 2, 3, 4, 5], 1)
        self.assertEqual(result, [5, 1, 2, 3, 4])

    def test_negative_rotation(self):
        result = rotate([1, 2, 3, 4, 5], -1)
        self.assertEqual(result, [2, 3, 4, 5, 1])

    def test_negative_rotation_multiple(self):
        result = rotate([1, 2, 3, 4, 5], -2)
        self.assertEqual(result, [3, 4, 5, 1, 2])

    def test_rotation_larger_than_length(self):
        result = rotate([1, 2, 3, 4, 5], 7)
        self.assertEqual(result, [4, 5, 1, 2, 3])

    def test_rotation_multiple_of_length(self):
        result = rotate([1, 2, 3, 4, 5], 10)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_zero_rotation(self):
        result = rotate([1, 2, 3, 4, 5], 0)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_empty_list(self):
        result = rotate([], 3)
        self.assertEqual(result, [])

    def test_single_element(self):
        result = rotate([1], 5)
        self.assertEqual(result, [1])

    def test_type_error_non_list(self):
        with self.assertRaises(TypeError):
            rotate("not a list", 2)

    def test_type_error_non_int_rotation(self):
        with self.assertRaises(TypeError):
            rotate([1, 2, 3], "2")


class TestFindDuplicates(unittest.TestCase):

    def test_some_duplicates(self):
        result = find_duplicates([1, 2, 3, 2, 4, 3])
        self.assertEqual(sorted(result), [2, 3])

    def test_multiple_occurrences(self):
        result = find_duplicates([1, 1, 1, 2, 2, 3])
        self.assertEqual(sorted(result), [1, 2])

    def test_all_duplicates(self):
        result = find_duplicates([1, 1, 2, 2, 3, 3])
        self.assertEqual(sorted(result), [1, 2, 3])

    def test_no_duplicates(self):
        result = find_duplicates([1, 2, 3, 4, 5])
        self.assertEqual(result, [])

    def test_empty_list(self):
        result = find_duplicates([])
        self.assertEqual(result, [])

    def test_single_element(self):
        result = find_duplicates([1])
        self.assertEqual(result, [])

    def test_two_same_elements(self):
        result = find_duplicates([1, 1])
        self.assertEqual(result, [1])

    def test_string_duplicates(self):
        result = find_duplicates(['a', 'b', 'c', 'a', 'b'])
        self.assertEqual(sorted(result), ['a', 'b'])

    def test_type_error_non_list(self):
        with self.assertRaises(TypeError):
            find_duplicates("not a list")


class TestMergeSorted(unittest.TestCase):

    def test_equal_lengths(self):
        result = merge_sorted([1, 3, 5], [2, 4, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_different_lengths_first_longer(self):
        result = merge_sorted([1, 3, 5, 7, 9], [2, 4])
        self.assertEqual(result, [1, 2, 3, 4, 5, 7, 9])

    def test_different_lengths_second_longer(self):
        result = merge_sorted([1, 2], [3, 4, 5, 6, 7])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7])

    def test_empty_first_list(self):
        result = merge_sorted([], [1, 2, 3])
        self.assertEqual(result, [1, 2, 3])

    def test_empty_second_list(self):
        result = merge_sorted([1, 2, 3], [])
        self.assertEqual(result, [1, 2, 3])

    def test_both_empty(self):
        result = merge_sorted([], [])
        self.assertEqual(result, [])

    def test_duplicate_values_across_lists(self):
        result = merge_sorted([1, 3, 5], [1, 3, 5])
        self.assertEqual(result, [1, 1, 3, 3, 5, 5])

    def test_duplicate_values_mixed(self):
        result = merge_sorted([1, 2, 4, 4], [2, 3, 4])
        self.assertEqual(result, [1, 2, 2, 3, 4, 4, 4])

    def test_non_overlapping_ranges(self):
        result = merge_sorted([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_all_same_values(self):
        result = merge_sorted([1, 1, 1], [1, 1])
        self.assertEqual(result, [1, 1, 1, 1, 1])

    def test_type_error_first_non_list(self):
        with self.assertRaises(TypeError):
            merge_sorted("not a list", [1, 2, 3])

    def test_type_error_second_non_list(self):
        with self.assertRaises(TypeError):
            merge_sorted([1, 2, 3], "not a list")


if __name__ == '__main__':
    unittest.main()
