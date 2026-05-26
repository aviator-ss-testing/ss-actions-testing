import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.list_ops import chunk_list, flatten, find_duplicates, rotate_list, list_stats


class TestListOps(unittest.TestCase):

    def test_chunk_list_normal_even_division(self):
        self.assertEqual(chunk_list([1, 2, 3, 4, 5, 6], 2), [[1, 2], [3, 4], [5, 6]])
        self.assertEqual(chunk_list([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

    def test_chunk_list_normal_uneven_division(self):
        self.assertEqual(chunk_list([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(chunk_list([1, 2, 3, 4, 5, 6, 7], 3), [[1, 2, 3], [4, 5, 6], [7]])

    def test_chunk_list_chunk_size_one(self):
        self.assertEqual(chunk_list([1, 2, 3], 1), [[1], [2], [3]])
        self.assertEqual(chunk_list(['a', 'b'], 1), [['a'], ['b']])

    def test_chunk_list_chunk_size_larger_than_list(self):
        self.assertEqual(chunk_list([1, 2, 3], 10), [[1, 2, 3]])
        self.assertEqual(chunk_list(['a'], 5), [['a']])

    def test_chunk_list_empty_list(self):
        self.assertEqual(chunk_list([], 3), [])
        self.assertEqual(chunk_list([], 1), [])

    def test_chunk_list_single_element(self):
        self.assertEqual(chunk_list([42], 1), [[42]])
        self.assertEqual(chunk_list([42], 5), [[42]])

    def test_chunk_list_large_list(self):
        large_list = list(range(100))
        result = chunk_list(large_list, 10)
        self.assertEqual(len(result), 10)
        self.assertEqual(result[0], list(range(10)))
        self.assertEqual(result[-1], list(range(90, 100)))

    def test_chunk_list_strings(self):
        self.assertEqual(chunk_list(['a', 'b', 'c', 'd', 'e'], 2), [['a', 'b'], ['c', 'd'], ['e']])

    def test_chunk_list_mixed_types(self):
        self.assertEqual(chunk_list([1, 'a', 2.5, True, None], 2), [[1, 'a'], [2.5, True], [None]])

    def test_chunk_list_invalid_size_zero(self):
        with self.assertRaises(ValueError):
            chunk_list([1, 2, 3], 0)

    def test_chunk_list_invalid_size_negative(self):
        with self.assertRaises(ValueError):
            chunk_list([1, 2, 3], -1)
        with self.assertRaises(ValueError):
            chunk_list([1, 2, 3], -5)

    def test_chunk_list_invalid_size_type(self):
        with self.assertRaises(TypeError):
            chunk_list([1, 2, 3], 2.5)
        with self.assertRaises(TypeError):
            chunk_list([1, 2, 3], "2")
        with self.assertRaises(TypeError):
            chunk_list([1, 2, 3], None)

    def test_chunk_list_invalid_list_type(self):
        with self.assertRaises(TypeError):
            chunk_list("not a list", 2)
        with self.assertRaises(TypeError):
            chunk_list(123, 2)
        with self.assertRaises(TypeError):
            chunk_list(None, 2)

    def test_flatten_single_level(self):
        self.assertEqual(flatten([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(flatten(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_flatten_two_levels(self):
        self.assertEqual(flatten([[1, 2], [3, 4]]), [1, 2, 3, 4])
        self.assertEqual(flatten([[1], [2], [3]]), [1, 2, 3])

    def test_flatten_three_levels(self):
        self.assertEqual(flatten([[[1, 2]], [[3, 4]]]), [1, 2, 3, 4])
        self.assertEqual(flatten([[[1]], [[2]], [[3]]]), [1, 2, 3])

    def test_flatten_deep_nesting(self):
        self.assertEqual(flatten([[[[1, 2]]], [[[3, 4]]]]), [1, 2, 3, 4])
        self.assertEqual(flatten([[[[[5]]]]]), [5])

    def test_flatten_mixed_nesting(self):
        self.assertEqual(flatten([1, [2, 3], 4, [5, [6, 7]]]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(flatten([[1, 2], 3, [4, [5, 6]], 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_flatten_empty_list(self):
        self.assertEqual(flatten([]), [])

    def test_flatten_nested_empty_lists(self):
        self.assertEqual(flatten([[], [], []]), [])
        self.assertEqual(flatten([[[]], [[]]]), [])

    def test_flatten_single_element(self):
        self.assertEqual(flatten([42]), [42])
        self.assertEqual(flatten([[42]]), [42])

    def test_flatten_strings_in_nested_lists(self):
        self.assertEqual(flatten([['a', 'b'], ['c', 'd']]), ['a', 'b', 'c', 'd'])

    def test_flatten_mixed_types_nested(self):
        self.assertEqual(flatten([[1, 'a'], [2.5, True], [None]]), [1, 'a', 2.5, True, None])

    def test_flatten_large_nested_list(self):
        large_nested = [[i, i+1] for i in range(0, 100, 2)]
        result = flatten(large_nested)
        self.assertEqual(len(result), 100)
        self.assertEqual(result, list(range(100)))

    def test_flatten_invalid_type(self):
        with self.assertRaises(TypeError):
            flatten("not a list")
        with self.assertRaises(TypeError):
            flatten(123)
        with self.assertRaises(TypeError):
            flatten(None)

    def test_find_duplicates_no_duplicates(self):
        self.assertEqual(find_duplicates([1, 2, 3, 4, 5]), [])
        self.assertEqual(find_duplicates(['a', 'b', 'c']), [])

    def test_find_duplicates_simple_duplicates(self):
        self.assertEqual(find_duplicates([1, 2, 3, 2, 4]), [2])
        self.assertEqual(find_duplicates([1, 1, 2, 3]), [1])

    def test_find_duplicates_multiple_duplicates(self):
        self.assertEqual(find_duplicates([1, 2, 3, 2, 3, 4]), [2, 3])
        self.assertEqual(find_duplicates([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_find_duplicates_many_occurrences(self):
        self.assertEqual(find_duplicates([1, 1, 1, 1, 2, 2, 2, 3]), [1, 2])
        self.assertEqual(find_duplicates([5, 5, 5, 5, 5]), [5])

    def test_find_duplicates_order_preserved(self):
        self.assertEqual(find_duplicates([3, 1, 2, 1, 3, 4]), [1, 3])
        self.assertEqual(find_duplicates([5, 3, 2, 3, 5, 1, 2]), [3, 5, 2])

    def test_find_duplicates_empty_list(self):
        self.assertEqual(find_duplicates([]), [])

    def test_find_duplicates_single_element(self):
        self.assertEqual(find_duplicates([42]), [])

    def test_find_duplicates_all_same(self):
        self.assertEqual(find_duplicates([7, 7, 7, 7, 7]), [7])

    def test_find_duplicates_strings(self):
        self.assertEqual(find_duplicates(['a', 'b', 'a', 'c', 'b']), ['a', 'b'])

    def test_find_duplicates_mixed_types(self):
        self.assertEqual(find_duplicates([1, 'a', 2, 'a', 1, None, None]), ['a', 1, None])

    def test_find_duplicates_large_list(self):
        large_list = [i % 10 for i in range(100)]
        result = find_duplicates(large_list)
        self.assertEqual(sorted(result), list(range(10)))

    def test_find_duplicates_invalid_type(self):
        with self.assertRaises(TypeError):
            find_duplicates("not a list")
        with self.assertRaises(TypeError):
            find_duplicates(123)
        with self.assertRaises(TypeError):
            find_duplicates(None)

    def test_rotate_list_positive_small(self):
        self.assertEqual(rotate_list([1, 2, 3, 4, 5], 1), [5, 1, 2, 3, 4])
        self.assertEqual(rotate_list([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])

    def test_rotate_list_positive_large(self):
        self.assertEqual(rotate_list([1, 2, 3, 4, 5], 3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate_list([1, 2, 3], 5), [2, 3, 1])

    def test_rotate_list_negative_small(self):
        self.assertEqual(rotate_list([1, 2, 3, 4, 5], -1), [2, 3, 4, 5, 1])
        self.assertEqual(rotate_list([1, 2, 3, 4, 5], -2), [3, 4, 5, 1, 2])

    def test_rotate_list_negative_large(self):
        self.assertEqual(rotate_list([1, 2, 3, 4, 5], -3), [4, 5, 1, 2, 3])
        self.assertEqual(rotate_list([1, 2, 3], -5), [3, 1, 2])

    def test_rotate_list_zero(self):
        self.assertEqual(rotate_list([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])

    def test_rotate_list_full_rotation(self):
        self.assertEqual(rotate_list([1, 2, 3, 4], 4), [1, 2, 3, 4])
        self.assertEqual(rotate_list([1, 2, 3, 4], -4), [1, 2, 3, 4])

    def test_rotate_list_empty_list(self):
        self.assertEqual(rotate_list([], 5), [])
        self.assertEqual(rotate_list([], -3), [])

    def test_rotate_list_single_element(self):
        self.assertEqual(rotate_list([42], 1), [42])
        self.assertEqual(rotate_list([42], -1), [42])
        self.assertEqual(rotate_list([42], 100), [42])

    def test_rotate_list_strings(self):
        self.assertEqual(rotate_list(['a', 'b', 'c', 'd'], 1), ['d', 'a', 'b', 'c'])
        self.assertEqual(rotate_list(['a', 'b', 'c', 'd'], -1), ['b', 'c', 'd', 'a'])

    def test_rotate_list_mixed_types(self):
        self.assertEqual(rotate_list([1, 'a', 2.5, True], 2), [2.5, True, 1, 'a'])

    def test_rotate_list_large_list(self):
        large_list = list(range(100))
        result = rotate_list(large_list, 10)
        self.assertEqual(result[:10], list(range(90, 100)))
        self.assertEqual(result[10:], list(range(90)))

    def test_rotate_list_invalid_positions_type(self):
        with self.assertRaises(TypeError):
            rotate_list([1, 2, 3], 2.5)
        with self.assertRaises(TypeError):
            rotate_list([1, 2, 3], "2")
        with self.assertRaises(TypeError):
            rotate_list([1, 2, 3], None)

    def test_rotate_list_invalid_list_type(self):
        with self.assertRaises(TypeError):
            rotate_list("not a list", 2)
        with self.assertRaises(TypeError):
            rotate_list(123, 2)
        with self.assertRaises(TypeError):
            rotate_list(None, 2)

    def test_list_stats_basic_integers(self):
        result = list_stats([1, 2, 3, 4, 5])
        self.assertEqual(result['min'], 1)
        self.assertEqual(result['max'], 5)
        self.assertEqual(result['mean'], 3.0)
        self.assertEqual(result['median'], 3)

    def test_list_stats_unsorted_integers(self):
        result = list_stats([5, 2, 8, 1, 9])
        self.assertEqual(result['min'], 1)
        self.assertEqual(result['max'], 9)
        self.assertEqual(result['mean'], 5.0)
        self.assertEqual(result['median'], 5)

    def test_list_stats_floats(self):
        result = list_stats([1.5, 2.5, 3.5, 4.5, 5.5])
        self.assertEqual(result['min'], 1.5)
        self.assertEqual(result['max'], 5.5)
        self.assertEqual(result['mean'], 3.5)
        self.assertEqual(result['median'], 3.5)

    def test_list_stats_mixed_int_float(self):
        result = list_stats([1, 2.5, 3, 4.5, 5])
        self.assertEqual(result['min'], 1)
        self.assertEqual(result['max'], 5)
        self.assertEqual(result['mean'], 3.2)
        self.assertEqual(result['median'], 3)

    def test_list_stats_single_element(self):
        result = list_stats([42])
        self.assertEqual(result['min'], 42)
        self.assertEqual(result['max'], 42)
        self.assertEqual(result['mean'], 42)
        self.assertEqual(result['median'], 42)

    def test_list_stats_two_elements(self):
        result = list_stats([10, 20])
        self.assertEqual(result['min'], 10)
        self.assertEqual(result['max'], 20)
        self.assertEqual(result['mean'], 15.0)
        self.assertEqual(result['median'], 15.0)

    def test_list_stats_even_length_median(self):
        result = list_stats([1, 2, 3, 4])
        self.assertEqual(result['median'], 2.5)
        result = list_stats([10, 20, 30, 40])
        self.assertEqual(result['median'], 25.0)

    def test_list_stats_odd_length_median(self):
        result = list_stats([1, 2, 3])
        self.assertEqual(result['median'], 2)
        result = list_stats([10, 20, 30, 40, 50])
        self.assertEqual(result['median'], 30)

    def test_list_stats_negative_numbers(self):
        result = list_stats([-5, -2, -8, -1, -9])
        self.assertEqual(result['min'], -9)
        self.assertEqual(result['max'], -1)
        self.assertEqual(result['mean'], -5.0)
        self.assertEqual(result['median'], -5)

    def test_list_stats_mixed_positive_negative(self):
        result = list_stats([-2, -1, 0, 1, 2])
        self.assertEqual(result['min'], -2)
        self.assertEqual(result['max'], 2)
        self.assertEqual(result['mean'], 0.0)
        self.assertEqual(result['median'], 0)

    def test_list_stats_all_same_values(self):
        result = list_stats([7, 7, 7, 7, 7])
        self.assertEqual(result['min'], 7)
        self.assertEqual(result['max'], 7)
        self.assertEqual(result['mean'], 7.0)
        self.assertEqual(result['median'], 7)

    def test_list_stats_large_list(self):
        large_list = list(range(1, 101))
        result = list_stats(large_list)
        self.assertEqual(result['min'], 1)
        self.assertEqual(result['max'], 100)
        self.assertEqual(result['mean'], 50.5)
        self.assertEqual(result['median'], 50.5)

    def test_list_stats_empty_list_raises_error(self):
        with self.assertRaises(ValueError):
            list_stats([])

    def test_list_stats_invalid_list_type(self):
        with self.assertRaises(TypeError):
            list_stats("not a list")
        with self.assertRaises(TypeError):
            list_stats(123)
        with self.assertRaises(TypeError):
            list_stats(None)

    def test_list_stats_non_numeric_values_raises_error(self):
        with self.assertRaises(TypeError):
            list_stats([1, 2, "3", 4])
        with self.assertRaises(TypeError):
            list_stats(["a", "b", "c"])
        with self.assertRaises(TypeError):
            list_stats([1, 2, None, 4])

    def test_list_stats_boolean_values_raises_error(self):
        with self.assertRaises(TypeError):
            list_stats([True, False, True])
        with self.assertRaises(TypeError):
            list_stats([1, 2, True, 4])


if __name__ == '__main__':
    unittest.main()
