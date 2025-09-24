"""
Comprehensive test suite for data_utils module.

Tests all data manipulation functions including edge cases, error conditions,
nested data structures, empty collections, and mixed data types. Includes
memory efficiency tests and parametrized test scenarios.
"""

import unittest
import sys
import os
import time
from unittest.mock import patch

# Add parent directory to path for importing modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_utils import (
    flatten_list, merge_dictionaries, find_max_in_nested,
    group_by_key, sort_dict_by_value
)


class TestFlattenList(unittest.TestCase):
    """Test cases for flatten_list function."""

    def test_simple_nested_list(self):
        """Test flattening simple nested lists."""
        self.assertEqual(flatten_list([1, [2, 3], [4, [5, 6]]]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])
        self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])

    def test_empty_list(self):
        """Test flattening empty lists."""
        self.assertEqual(flatten_list([]), [])
        self.assertEqual(flatten_list([[]]), [])
        self.assertEqual(flatten_list([[], []]), [])

    def test_deeply_nested_list(self):
        """Test flattening deeply nested lists."""
        deeply_nested = [1, [2, [3, [4, [5]]]]]
        self.assertEqual(flatten_list(deeply_nested), [1, 2, 3, 4, 5])

        complex_nested = [1, [2, 3], [4, [5, [6, 7]], 8], 9]
        self.assertEqual(flatten_list(complex_nested), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_mixed_data_types(self):
        """Test flattening lists with mixed data types."""
        mixed_list = [1, ["hello", [2.5, True]], [None, [False, "world"]]]
        expected = [1, "hello", 2.5, True, None, False, "world"]
        self.assertEqual(flatten_list(mixed_list), expected)

    def test_single_element_lists(self):
        """Test flattening lists with single elements."""
        self.assertEqual(flatten_list([1]), [1])
        self.assertEqual(flatten_list([[1]]), [1])
        self.assertEqual(flatten_list([[[[[1]]]]]), [1])

    def test_string_and_number_mix(self):
        """Test flattening with strings and numbers."""
        mixed = ["a", [1, ["b", [2, "c"]], 3], "d"]
        expected = ["a", 1, "b", 2, "c", 3, "d"]
        self.assertEqual(flatten_list(mixed), expected)

    def test_unicode_content(self):
        """Test flattening with unicode content."""
        unicode_list = ["café", ["你好", ["🎉", "naïve"]]]
        expected = ["café", "你好", "🎉", "naïve"]
        self.assertEqual(flatten_list(unicode_list), expected)

    def test_type_error(self):
        """Test type error for non-list input."""
        with self.assertRaises(TypeError):
            flatten_list("not a list")
        with self.assertRaises(TypeError):
            flatten_list(123)
        with self.assertRaises(TypeError):
            flatten_list(None)
        with self.assertRaises(TypeError):
            flatten_list({'a': 1})

    def test_memory_efficiency_large_list(self):
        """Test memory efficiency with large nested lists."""
        # Create a large nested structure
        large_nested = []
        for i in range(100):
            large_nested.append([i * 10 + j for j in range(10)])

        start_time = time.time()
        result = flatten_list(large_nested)
        end_time = time.time()

        # Should complete within reasonable time
        self.assertLess(end_time - start_time, 1.0)  # Less than 1 second
        self.assertEqual(len(result), 1000)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[-1], 999)


class TestMergeDictionaries(unittest.TestCase):
    """Test cases for merge_dictionaries function."""

    def test_simple_merge(self):
        """Test merging simple dictionaries."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_overlapping_keys(self):
        """Test merging dictionaries with overlapping keys."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}  # Later dict overwrites
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_multiple_dictionaries(self):
        """Test merging multiple dictionaries."""
        dict1 = {'a': 1}
        dict2 = {'a': 2, 'b': 3}
        dict3 = {'a': 4, 'c': 5}
        expected = {'a': 4, 'b': 3, 'c': 5}  # Last dict wins
        self.assertEqual(merge_dictionaries(dict1, dict2, dict3), expected)

    def test_empty_dictionaries(self):
        """Test merging empty dictionaries."""
        self.assertEqual(merge_dictionaries({}, {}), {})
        self.assertEqual(merge_dictionaries({'a': 1}, {}), {'a': 1})
        self.assertEqual(merge_dictionaries({}, {'b': 2}), {'b': 2})

    def test_no_arguments(self):
        """Test merging with no arguments."""
        self.assertEqual(merge_dictionaries(), {})

    def test_single_dictionary(self):
        """Test merging single dictionary."""
        single_dict = {'x': 10, 'y': 20}
        self.assertEqual(merge_dictionaries(single_dict), single_dict)

    def test_mixed_data_types_values(self):
        """Test merging dictionaries with mixed value types."""
        dict1 = {'a': 1, 'b': "hello", 'c': [1, 2, 3]}
        dict2 = {'d': {'nested': True}, 'e': None, 'f': 3.14}
        expected = {'a': 1, 'b': "hello", 'c': [1, 2, 3], 'd': {'nested': True}, 'e': None, 'f': 3.14}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_mixed_key_types(self):
        """Test merging dictionaries with mixed key types."""
        dict1 = {1: 'one', 'two': 2}
        dict2 = {3.0: 'three', (4, 5): 'tuple_key'}
        expected = {1: 'one', 'two': 2, 3.0: 'three', (4, 5): 'tuple_key'}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_unicode_keys_and_values(self):
        """Test merging dictionaries with unicode keys and values."""
        dict1 = {'café': 'coffee', '你好': 'hello'}
        dict2 = {'🎉': 'party', 'naïve': 'simple'}
        expected = {'café': 'coffee', '你好': 'hello', '🎉': 'party', 'naïve': 'simple'}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_type_error(self):
        """Test type error for non-dictionary inputs."""
        with self.assertRaises(TypeError):
            merge_dictionaries({'a': 1}, "not a dict")
        with self.assertRaises(TypeError):
            merge_dictionaries({'a': 1}, 123)
        with self.assertRaises(TypeError):
            merge_dictionaries([1, 2, 3])
        with self.assertRaises(TypeError):
            merge_dictionaries({'a': 1}, None)

    def test_memory_efficiency_large_dicts(self):
        """Test memory efficiency with large dictionaries."""
        # Create large dictionaries
        dict1 = {f'key_{i}': i for i in range(1000)}
        dict2 = {f'key_{i+1000}': i+1000 for i in range(1000)}

        start_time = time.time()
        result = merge_dictionaries(dict1, dict2)
        end_time = time.time()

        # Should complete within reasonable time
        self.assertLess(end_time - start_time, 1.0)  # Less than 1 second
        self.assertEqual(len(result), 2000)


class TestFindMaxInNested(unittest.TestCase):
    """Test cases for find_max_in_nested function."""

    def test_nested_list(self):
        """Test finding max in nested lists."""
        nested_list = [1, [2, 3], [4, [5, 6]]]
        self.assertEqual(find_max_in_nested(nested_list), 6)

    def test_nested_dict(self):
        """Test finding max in nested dictionaries."""
        nested_dict = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}, 'e': 5}
        self.assertEqual(find_max_in_nested(nested_dict), 5)

    def test_nested_tuple(self):
        """Test finding max in nested tuples."""
        nested_tuple = (1, (2, 3), (4, (5, 6)))
        self.assertEqual(find_max_in_nested(nested_tuple), 6)

    def test_mixed_nested_structures(self):
        """Test finding max in mixed nested structures."""
        mixed = [1, {'a': 2, 'b': (3, [4, {'c': 5}])}, 6]
        self.assertEqual(find_max_in_nested(mixed), 6)

    def test_single_values(self):
        """Test finding max with single values."""
        self.assertEqual(find_max_in_nested([42]), 42)
        self.assertEqual(find_max_in_nested({'single': 7}), 7)
        self.assertEqual(find_max_in_nested((99,)), 99)

    def test_negative_numbers(self):
        """Test finding max with negative numbers."""
        negative_data = [-5, [-1, -3], {'a': -2, 'b': [-4, -6]}]
        self.assertEqual(find_max_in_nested(negative_data), -1)

    def test_floating_point_numbers(self):
        """Test finding max with floating point numbers."""
        float_data = [1.1, [2.5, 3.7], {'a': 4.2, 'b': (5.9, 1.3)}]
        self.assertEqual(find_max_in_nested(float_data), 5.9)

    def test_mixed_int_float(self):
        """Test finding max with mixed integers and floats."""
        mixed_nums = [1, [2.5, 3], {'a': 4.2, 'b': [5, 6.1]}]
        self.assertEqual(find_max_in_nested(mixed_nums), 6.1)

    def test_deeply_nested(self):
        """Test finding max in deeply nested structures."""
        deeply_nested = [1, [2, [3, [4, [5, {'deep': {'deeper': [100, 99]}}]]]]]
        self.assertEqual(find_max_in_nested(deeply_nested), 100)

    def test_empty_structures(self):
        """Test finding max in empty structures raises ValueError."""
        with self.assertRaises(ValueError):
            find_max_in_nested([])
        with self.assertRaises(ValueError):
            find_max_in_nested({})
        with self.assertRaises(ValueError):
            find_max_in_nested(())

    def test_no_numeric_values(self):
        """Test finding max with no numeric values raises ValueError."""
        with self.assertRaises(ValueError):
            find_max_in_nested(['hello', {'world': 'test'}, ('no', 'numbers')])
        with self.assertRaises(ValueError):
            find_max_in_nested([None, True, False])

    def test_boolean_values_ignored(self):
        """Test that boolean values are correctly ignored."""
        data_with_bools = [1, [True, False, 2], {'a': 3, 'b': [False, True]}]
        self.assertEqual(find_max_in_nested(data_with_bools), 3)

    def test_type_error(self):
        """Test type error for invalid input types."""
        with self.assertRaises(TypeError):
            find_max_in_nested("string")
        with self.assertRaises(TypeError):
            find_max_in_nested(123)
        with self.assertRaises(TypeError):
            find_max_in_nested(None)

    def test_memory_efficiency_large_nested(self):
        """Test memory efficiency with large nested structures."""
        # Create large nested structure
        large_nested = []
        for i in range(100):
            large_nested.append({'data': [j for j in range(i*10, (i+1)*10)]})

        start_time = time.time()
        result = find_max_in_nested(large_nested)
        end_time = time.time()

        # Should complete within reasonable time
        self.assertLess(end_time - start_time, 1.0)  # Less than 1 second
        self.assertEqual(result, 999)


class TestGroupByKey(unittest.TestCase):
    """Test cases for group_by_key function."""

    def test_simple_grouping(self):
        """Test simple grouping by key."""
        data = [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 25},
            {'name': 'Charlie', 'age': 30}
        ]
        expected = {
            25: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 25}],
            30: [{'name': 'Charlie', 'age': 30}]
        }
        self.assertEqual(group_by_key(data, 'age'), expected)

    def test_empty_list(self):
        """Test grouping empty list."""
        self.assertEqual(group_by_key([], 'any_key'), {})

    def test_single_item(self):
        """Test grouping single item."""
        data = [{'category': 'fruit', 'name': 'apple'}]
        expected = {'fruit': [{'category': 'fruit', 'name': 'apple'}]}
        self.assertEqual(group_by_key(data, 'category'), expected)

    def test_all_same_group(self):
        """Test grouping where all items have same key value."""
        data = [
            {'type': 'vehicle', 'name': 'car'},
            {'type': 'vehicle', 'name': 'truck'},
            {'type': 'vehicle', 'name': 'bicycle'}
        ]
        expected = {
            'vehicle': [
                {'type': 'vehicle', 'name': 'car'},
                {'type': 'vehicle', 'name': 'truck'},
                {'type': 'vehicle', 'name': 'bicycle'}
            ]
        }
        self.assertEqual(group_by_key(data, 'type'), expected)

    def test_missing_key_in_some_items(self):
        """Test grouping when some items don't have the key."""
        data = [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob'},  # Missing age key
            {'name': 'Charlie', 'age': 30}
        ]
        expected = {
            25: [{'name': 'Alice', 'age': 25}],
            30: [{'name': 'Charlie', 'age': 30}]
        }
        self.assertEqual(group_by_key(data, 'age'), expected)

    def test_mixed_key_types(self):
        """Test grouping with mixed key value types."""
        data = [
            {'id': 1, 'name': 'first'},
            {'id': '1', 'name': 'second'},  # String '1'
            {'id': 1, 'name': 'third'},     # Integer 1
            {'id': 2.0, 'name': 'fourth'}   # Float 2.0
        ]
        expected = {
            1: [{'id': 1, 'name': 'first'}, {'id': 1, 'name': 'third'}],
            '1': [{'id': '1', 'name': 'second'}],
            2.0: [{'id': 2.0, 'name': 'fourth'}]
        }
        self.assertEqual(group_by_key(data, 'id'), expected)

    def test_complex_key_values(self):
        """Test grouping with complex key values."""
        data = [
            {'coords': (1, 2), 'name': 'point1'},
            {'coords': (1, 2), 'name': 'point2'},
            {'coords': (3, 4), 'name': 'point3'}
        ]
        expected = {
            (1, 2): [{'coords': (1, 2), 'name': 'point1'}, {'coords': (1, 2), 'name': 'point2'}],
            (3, 4): [{'coords': (3, 4), 'name': 'point3'}]
        }
        self.assertEqual(group_by_key(data, 'coords'), expected)

    def test_unicode_keys_and_values(self):
        """Test grouping with unicode keys and values."""
        data = [
            {'language': '中文', 'country': 'China'},
            {'language': '中文', 'country': 'Taiwan'},
            {'language': 'English', 'country': 'USA'},
            {'language': 'français', 'country': 'France'}
        ]
        expected = {
            '中文': [
                {'language': '中文', 'country': 'China'},
                {'language': '中文', 'country': 'Taiwan'}
            ],
            'English': [{'language': 'English', 'country': 'USA'}],
            'français': [{'language': 'français', 'country': 'France'}]
        }
        self.assertEqual(group_by_key(data, 'language'), expected)

    def test_type_errors(self):
        """Test type errors for invalid inputs."""
        valid_data = [{'key': 'value'}]

        # Non-list data
        with self.assertRaises(TypeError):
            group_by_key({'not': 'list'}, 'key')
        with self.assertRaises(TypeError):
            group_by_key("string", 'key')

        # Non-string key
        with self.assertRaises(ValueError):
            group_by_key(valid_data, 123)
        with self.assertRaises(ValueError):
            group_by_key(valid_data, None)
        with self.assertRaises(ValueError):
            group_by_key(valid_data, '')  # Empty string

        # Non-dict items in list
        with self.assertRaises(TypeError):
            group_by_key(['not', 'dicts'], 'key')
        with self.assertRaises(TypeError):
            group_by_key([{'valid': 1}, 'invalid'], 'key')

    def test_memory_efficiency_large_dataset(self):
        """Test memory efficiency with large datasets."""
        # Create large dataset
        large_data = []
        for i in range(1000):
            large_data.append({'category': f'cat_{i % 10}', 'id': i})

        start_time = time.time()
        result = group_by_key(large_data, 'category')
        end_time = time.time()

        # Should complete within reasonable time
        self.assertLess(end_time - start_time, 1.0)  # Less than 1 second
        self.assertEqual(len(result), 10)  # 10 different categories
        # Each category should have 100 items
        for category_items in result.values():
            self.assertEqual(len(category_items), 100)


class TestSortDictByValue(unittest.TestCase):
    """Test cases for sort_dict_by_value function."""

    def test_simple_sorting(self):
        """Test simple sorting by value."""
        input_dict = {'a': 3, 'b': 1, 'c': 2}
        expected = {'b': 1, 'c': 2, 'a': 3}
        self.assertEqual(sort_dict_by_value(input_dict), expected)

    def test_reverse_sorting(self):
        """Test reverse (descending) sorting."""
        input_dict = {'x': 10, 'y': 5, 'z': 15}
        expected = {'z': 15, 'x': 10, 'y': 5}
        self.assertEqual(sort_dict_by_value(input_dict, reverse=True), expected)

    def test_empty_dictionary(self):
        """Test sorting empty dictionary."""
        self.assertEqual(sort_dict_by_value({}), {})
        self.assertEqual(sort_dict_by_value({}, reverse=True), {})

    def test_single_item(self):
        """Test sorting single-item dictionary."""
        single_item = {'only': 42}
        self.assertEqual(sort_dict_by_value(single_item), single_item)
        self.assertEqual(sort_dict_by_value(single_item, reverse=True), single_item)

    def test_equal_values(self):
        """Test sorting with equal values."""
        equal_values = {'a': 5, 'b': 5, 'c': 5}
        result = sort_dict_by_value(equal_values)
        # Order should be consistent but may vary
        self.assertEqual(len(result), 3)
        self.assertTrue(all(v == 5 for v in result.values()))

    def test_negative_values(self):
        """Test sorting with negative values."""
        negative_dict = {'a': -1, 'b': -5, 'c': -2}
        expected = {'b': -5, 'c': -2, 'a': -1}
        self.assertEqual(sort_dict_by_value(negative_dict), expected)

    def test_floating_point_values(self):
        """Test sorting with floating point values."""
        float_dict = {'pi': 3.14, 'e': 2.71, 'phi': 1.618}
        expected = {'phi': 1.618, 'e': 2.71, 'pi': 3.14}
        self.assertEqual(sort_dict_by_value(float_dict), expected)

    def test_mixed_int_float_values(self):
        """Test sorting with mixed integer and float values."""
        mixed_dict = {'a': 3, 'b': 1.5, 'c': 2, 'd': 2.7}
        expected = {'b': 1.5, 'c': 2, 'd': 2.7, 'a': 3}
        self.assertEqual(sort_dict_by_value(mixed_dict), expected)

    def test_complex_keys(self):
        """Test sorting with complex key types."""
        complex_keys = {(1, 2): 10, 'string': 5, 42: 15}
        result = sort_dict_by_value(complex_keys)
        # Check that values are sorted correctly
        values = list(result.values())
        self.assertEqual(values, [5, 10, 15])

    def test_unicode_keys(self):
        """Test sorting with unicode keys."""
        unicode_dict = {'café': 3, 'naïve': 1, '你好': 2}
        result = sort_dict_by_value(unicode_dict)
        values = list(result.values())
        self.assertEqual(values, [1, 2, 3])

    def test_type_errors(self):
        """Test type errors for invalid inputs."""
        # Non-dictionary input
        with self.assertRaises(TypeError):
            sort_dict_by_value([1, 2, 3])
        with self.assertRaises(TypeError):
            sort_dict_by_value("string")
        with self.assertRaises(TypeError):
            sort_dict_by_value(None)

        # Non-numeric values
        with self.assertRaises(TypeError):
            sort_dict_by_value({'a': 'string', 'b': 2})
        with self.assertRaises(TypeError):
            sort_dict_by_value({'a': 1, 'b': None})
        with self.assertRaises(TypeError):
            sort_dict_by_value({'a': 1, 'b': [1, 2, 3]})
        with self.assertRaises(TypeError):
            sort_dict_by_value({'a': True, 'b': 2})  # Boolean should fail

    def test_memory_efficiency_large_dict(self):
        """Test memory efficiency with large dictionaries."""
        # Create large dictionary
        large_dict = {f'key_{i}': i for i in range(1000, 0, -1)}  # Reverse order

        start_time = time.time()
        result = sort_dict_by_value(large_dict)
        end_time = time.time()

        # Should complete within reasonable time
        self.assertLess(end_time - start_time, 1.0)  # Less than 1 second

        # Check that it's sorted correctly
        values = list(result.values())
        self.assertEqual(values, list(range(1, 1001)))

    def test_preserve_original_dict(self):
        """Test that original dictionary is not modified."""
        original = {'a': 3, 'b': 1, 'c': 2}
        original_copy = original.copy()

        sort_dict_by_value(original)
        self.assertEqual(original, original_copy)


class TestParametrizedScenarios(unittest.TestCase):
    """Test parametrized scenarios for multiple input combinations."""

    def test_flatten_list_parametrized(self):
        """Test flatten_list with multiple parameter combinations."""
        test_cases = [
            ([], []),
            ([1], [1]),
            ([1, 2, 3], [1, 2, 3]),
            ([1, [2]], [1, 2]),
            ([1, [2, [3]]], [1, 2, 3]),
            ([[[[1]]]], [1]),
            ([1, [2, 3], [4, [5, 6]], 7], [1, 2, 3, 4, 5, 6, 7]),
            (["a", ["b", ["c"]]], ["a", "b", "c"]),
            ([None, [True, [False]]], [None, True, False])
        ]

        for input_val, expected in test_cases:
            with self.subTest(input_val=input_val):
                self.assertEqual(flatten_list(input_val), expected)

    def test_count_vowels_parametrized(self):
        """Test count_vowels from string_utils with multiple scenarios."""
        from string_utils import count_vowels

        test_cases = [
            ("", 0),
            ("bcdfg", 0),
            ("aeiou", 5),
            ("AEIOU", 5),
            ("hello", 2),
            ("HELLO", 2),
            ("Programming", 3),
            ("café", 2),
            ("你好world", 1)  # Only 'o' is a vowel
        ]

        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                self.assertEqual(count_vowels(input_str), expected)

    def test_merge_dictionaries_parametrized(self):
        """Test merge_dictionaries with multiple parameter combinations."""
        test_cases = [
            ([], {}),
            ([{}], {}),
            ([{'a': 1}], {'a': 1}),
            ([{'a': 1}, {'b': 2}], {'a': 1, 'b': 2}),
            ([{'a': 1}, {'a': 2}], {'a': 2}),
            ([{'a': 1}, {'b': 2}, {'c': 3}], {'a': 1, 'b': 2, 'c': 3}),
            ([{'a': 1}, {'a': 2}, {'a': 3}], {'a': 3}),
            ([{1: 'one'}, {'two': 2}, {3.0: 'three'}], {1: 'one', 'two': 2, 3.0: 'three'})
        ]

        for dicts_list, expected in test_cases:
            with self.subTest(dicts_list=dicts_list):
                self.assertEqual(merge_dictionaries(*dicts_list), expected)

    def test_find_max_parametrized(self):
        """Test find_max_in_nested with multiple parameter combinations."""
        test_cases = [
            ([1], 1),
            ([1, 2, 3], 3),
            ([1, [2, 3]], 3),
            ({'a': 1, 'b': 2}, 2),
            ((1, 2, 3), 3),
            ([1, {'a': 2}, (3, 4)], 4),
            ([-1, [-2, -3]], -1),
            ([1.5, [2.7, 3.1]], 3.1),
            ([1, [2, [3, [4]]]], 4)
        ]

        for input_data, expected in test_cases:
            with self.subTest(input_data=input_data):
                self.assertEqual(find_max_in_nested(input_data), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)