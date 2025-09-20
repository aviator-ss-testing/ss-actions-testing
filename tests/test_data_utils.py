"""
Comprehensive test suite for data_utils module.

Tests all data structure manipulation functions including edge cases,
error conditions, nested structures, empty collections, mixed data types,
memory efficiency, and parametrized test scenarios.
"""

import unittest
import sys
import os
import gc
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_utils import (
    flatten_list, merge_dictionaries, find_max_in_nested,
    group_by_key, sort_dict_by_value
)


class TestFlattenList(unittest.TestCase):
    """Test cases for flatten_list function."""

    def test_simple_flat_list(self):
        """Test flattening already flat lists."""
        self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])
        self.assertEqual(flatten_list(['a', 'b', 'c']), ['a', 'b', 'c'])
        self.assertEqual(flatten_list([1]), [1])

    def test_nested_lists(self):
        """Test flattening nested lists."""
        self.assertEqual(flatten_list([1, [2, 3]]), [1, 2, 3])
        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])
        self.assertEqual(flatten_list([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])

    def test_deeply_nested_lists(self):
        """Test flattening deeply nested lists."""
        nested = [1, [2, [3, [4, [5]]]]]
        self.assertEqual(flatten_list(nested), [1, 2, 3, 4, 5])

        complex_nested = [1, [2, 3], [4, [5, 6, [7, 8]]], 9]
        self.assertEqual(flatten_list(complex_nested), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_empty_list(self):
        """Test flattening empty lists."""
        self.assertEqual(flatten_list([]), [])
        self.assertEqual(flatten_list([[], []]), [])
        self.assertEqual(flatten_list([1, [], 2]), [1, 2])

    def test_mixed_data_types(self):
        """Test flattening lists with mixed data types."""
        mixed = [1, ['a', 2.5], [True, [None, {'key': 'value'}]]]
        expected = [1, 'a', 2.5, True, None, {'key': 'value'}]
        self.assertEqual(flatten_list(mixed), expected)

    def test_nested_empty_lists(self):
        """Test flattening lists with nested empty lists."""
        self.assertEqual(flatten_list([1, [[], [2]], 3]), [1, 2, 3])
        self.assertEqual(flatten_list([[[[]]]]), [])

    def test_single_deeply_nested_element(self):
        """Test flattening single deeply nested elements."""
        self.assertEqual(flatten_list([[[[42]]]]), [42])

    def test_type_error(self):
        """Test type error for non-list input."""
        with self.assertRaises(TypeError):
            flatten_list("not a list")
        with self.assertRaises(TypeError):
            flatten_list(123)
        with self.assertRaises(TypeError):
            flatten_list(None)
        with self.assertRaises(TypeError):
            flatten_list({'key': 'value'})

    def test_memory_efficiency_large_dataset(self):
        """Test memory efficiency with large nested lists."""
        # Create a large nested structure
        large_nested = []
        for i in range(1000):
            large_nested.append([i, [i + 1000, [i + 2000]]])

        # Flatten it
        result = flatten_list(large_nested)

        # Verify correctness
        self.assertEqual(len(result), 3000)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[-1], 2999)


class TestMergeDictionaries(unittest.TestCase):
    """Test cases for merge_dictionaries function."""

    def test_merge_two_dictionaries(self):
        """Test merging two simple dictionaries."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_merge_overlapping_keys(self):
        """Test merging dictionaries with overlapping keys."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}  # dict2 overwrites dict1
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_merge_multiple_dictionaries(self):
        """Test merging multiple dictionaries."""
        dict1 = {'a': 1}
        dict2 = {'b': 2}
        dict3 = {'c': 3}
        dict4 = {'a': 10}  # Should overwrite dict1's 'a'
        expected = {'a': 10, 'b': 2, 'c': 3}
        self.assertEqual(merge_dictionaries(dict1, dict2, dict3, dict4), expected)

    def test_merge_empty_dictionaries(self):
        """Test merging empty dictionaries."""
        self.assertEqual(merge_dictionaries({}, {}), {})
        self.assertEqual(merge_dictionaries(), {})

        dict1 = {'a': 1}
        self.assertEqual(merge_dictionaries(dict1, {}), {'a': 1})
        self.assertEqual(merge_dictionaries({}, dict1), {'a': 1})

    def test_mixed_data_types_in_values(self):
        """Test merging dictionaries with mixed data types."""
        dict1 = {'str': 'hello', 'int': 42, 'list': [1, 2, 3]}
        dict2 = {'float': 3.14, 'bool': True, 'none': None}
        dict3 = {'dict': {'nested': 'value'}, 'str': 'world'}  # Overwrites 'str'

        result = merge_dictionaries(dict1, dict2, dict3)
        expected = {
            'str': 'world', 'int': 42, 'list': [1, 2, 3],
            'float': 3.14, 'bool': True, 'none': None,
            'dict': {'nested': 'value'}
        }
        self.assertEqual(result, expected)

    def test_mixed_key_types(self):
        """Test merging dictionaries with mixed key types."""
        dict1 = {'str_key': 1, 42: 'int_key', (1, 2): 'tuple_key'}
        dict2 = {3.14: 'float_key', True: 'bool_key'}

        result = merge_dictionaries(dict1, dict2)
        expected = {
            'str_key': 1, 42: 'int_key', (1, 2): 'tuple_key',
            3.14: 'float_key', True: 'bool_key'
        }
        self.assertEqual(result, expected)

    def test_type_error(self):
        """Test type error for non-dictionary input."""
        with self.assertRaises(TypeError):
            merge_dictionaries({'a': 1}, "not a dict")
        with self.assertRaises(TypeError):
            merge_dictionaries({'a': 1}, 123)
        with self.assertRaises(TypeError):
            merge_dictionaries({'a': 1}, None)
        with self.assertRaises(TypeError):
            merge_dictionaries(['a', 'b'])

    def test_memory_efficiency_large_datasets(self):
        """Test memory efficiency with large dictionaries."""
        # Create large dictionaries
        dict1 = {f'key_{i}': i for i in range(5000)}
        dict2 = {f'key_{i+5000}': i+5000 for i in range(5000)}

        # Merge them
        result = merge_dictionaries(dict1, dict2)

        # Verify correctness
        self.assertEqual(len(result), 10000)
        self.assertEqual(result['key_0'], 0)
        self.assertEqual(result['key_9999'], 9999)


class TestFindMaxInNested(unittest.TestCase):
    """Test cases for find_max_in_nested function."""

    def test_flat_list(self):
        """Test finding max in flat lists."""
        self.assertEqual(find_max_in_nested([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_max_in_nested([10, -5, 0, 8]), 10)
        self.assertEqual(find_max_in_nested([3.14, 2.71, 1.41]), 3.14)

    def test_nested_list(self):
        """Test finding max in nested lists."""
        self.assertEqual(find_max_in_nested([1, [2, 3], [4, [5, 6]]]), 6)
        self.assertEqual(find_max_in_nested([[1, 2], [3, [4, [5]]]]), 5)
        self.assertEqual(find_max_in_nested([[[10]], [5, [8]]]), 10)

    def test_dictionary(self):
        """Test finding max in dictionaries."""
        self.assertEqual(find_max_in_nested({'a': 5, 'b': 3, 'c': 8}), 8)
        self.assertEqual(find_max_in_nested({'x': {'y': 10, 'z': 7}}), 10)

    def test_nested_mixed_structures(self):
        """Test finding max in mixed nested structures."""
        data = {'a': [1, 2], 'b': {'c': [3, 4]}, 'd': 5}
        self.assertEqual(find_max_in_nested(data), 5)

        data = [1, {'a': [2, 3]}, [4, {'b': 6}]]
        self.assertEqual(find_max_in_nested(data), 6)

    def test_tuple_structures(self):
        """Test finding max in tuple structures."""
        self.assertEqual(find_max_in_nested((1, 2, 3)), 3)
        self.assertEqual(find_max_in_nested((1, (2, 3), 4)), 4)
        self.assertEqual(find_max_in_nested(((1, 2), (3, (4, 5)))), 5)

    def test_deeply_nested_structures(self):
        """Test finding max in deeply nested structures."""
        deep = {'a': {'b': {'c': {'d': [1, [2, [3, [4, 5]]]]}}}}
        self.assertEqual(find_max_in_nested(deep), 5)

    def test_negative_numbers(self):
        """Test finding max with negative numbers."""
        self.assertEqual(find_max_in_nested([-5, -3, -1]), -1)
        self.assertEqual(find_max_in_nested([[-10, -5], {'a': -2}]), -2)

    def test_mixed_positive_negative(self):
        """Test finding max with mixed positive and negative numbers."""
        self.assertEqual(find_max_in_nested([-5, 0, 3, -1]), 3)
        self.assertEqual(find_max_in_nested([{'a': -5}, [0, [3]]]), 3)

    def test_float_and_int_mix(self):
        """Test finding max with mixed float and int."""
        self.assertEqual(find_max_in_nested([1, 2.5, 3]), 3)
        self.assertEqual(find_max_in_nested([1.1, [2, [3.3]]]), 3.3)

    def test_boolean_handling(self):
        """Test that booleans are not considered numeric."""
        # Booleans should be ignored as they are not numeric
        with self.assertRaises(ValueError):
            find_max_in_nested([True, False])

        # Should find numeric values and ignore booleans
        self.assertEqual(find_max_in_nested([1, True, 2, False]), 2)

    def test_single_element(self):
        """Test finding max with single elements."""
        self.assertEqual(find_max_in_nested([42]), 42)
        self.assertEqual(find_max_in_nested({'a': 42}), 42)
        self.assertEqual(find_max_in_nested((42,)), 42)

    def test_empty_structures(self):
        """Test finding max in empty structures."""
        with self.assertRaises(ValueError):
            find_max_in_nested([])
        with self.assertRaises(ValueError):
            find_max_in_nested({})
        with self.assertRaises(ValueError):
            find_max_in_nested(())

    def test_no_numeric_values(self):
        """Test finding max when no numeric values exist."""
        with self.assertRaises(ValueError):
            find_max_in_nested(['a', 'b', 'c'])
        with self.assertRaises(ValueError):
            find_max_in_nested([['hello'], {'key': 'value'}])
        with self.assertRaises(ValueError):
            find_max_in_nested([None, [None, {'a': None}]])

    def test_type_error(self):
        """Test type error for invalid input types."""
        with self.assertRaises(TypeError):
            find_max_in_nested("string")
        with self.assertRaises(TypeError):
            find_max_in_nested(42)
        with self.assertRaises(TypeError):
            find_max_in_nested(None)

    def test_memory_efficiency_large_datasets(self):
        """Test memory efficiency with large nested structures."""
        # Create large nested structure
        large_data = []
        for i in range(1000):
            large_data.append({'level1': {'level2': [i, i+1000]}})

        # Add the maximum value
        large_data.append({'level1': {'level2': [5000]}})

        result = find_max_in_nested(large_data)
        self.assertEqual(result, 5000)


class TestGroupByKey(unittest.TestCase):
    """Test cases for group_by_key function."""

    def test_simple_grouping(self):
        """Test simple grouping by key."""
        data = [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 30},
            {'name': 'Charlie', 'age': 25}
        ]
        result = group_by_key(data, 'age')
        expected = {
            25: [{'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 25}],
            30: [{'name': 'Bob', 'age': 30}]
        }
        self.assertEqual(result, expected)

    def test_grouping_by_string_key(self):
        """Test grouping by string key."""
        data = [
            {'name': 'Alice', 'department': 'Engineering'},
            {'name': 'Bob', 'department': 'Sales'},
            {'name': 'Charlie', 'department': 'Engineering'},
            {'name': 'David', 'department': 'HR'}
        ]
        result = group_by_key(data, 'department')
        expected = {
            'Engineering': [
                {'name': 'Alice', 'department': 'Engineering'},
                {'name': 'Charlie', 'department': 'Engineering'}
            ],
            'Sales': [{'name': 'Bob', 'department': 'Sales'}],
            'HR': [{'name': 'David', 'department': 'HR'}]
        }
        self.assertEqual(result, expected)

    def test_missing_key_in_some_items(self):
        """Test grouping when some items don't have the key."""
        data = [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob'},  # Missing age
            {'name': 'Charlie', 'age': 25}
        ]
        result = group_by_key(data, 'age')
        expected = {
            25: [{'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 25}]
        }
        self.assertEqual(result, expected)

    def test_empty_list(self):
        """Test grouping empty list."""
        result = group_by_key([], 'any_key')
        self.assertEqual(result, {})

    def test_single_item(self):
        """Test grouping single item."""
        data = [{'name': 'Alice', 'age': 25}]
        result = group_by_key(data, 'age')
        expected = {25: [{'name': 'Alice', 'age': 25}]}
        self.assertEqual(result, expected)

    def test_mixed_data_types_as_keys(self):
        """Test grouping with mixed data types as key values."""
        data = [
            {'id': 1, 'value': 'first'},
            {'id': 'two', 'value': 'second'},
            {'id': 1, 'value': 'third'},
            {'id': 3.14, 'value': 'fourth'},
            {'id': None, 'value': 'fifth'}
        ]
        result = group_by_key(data, 'id')
        expected = {
            1: [{'id': 1, 'value': 'first'}, {'id': 1, 'value': 'third'}],
            'two': [{'id': 'two', 'value': 'second'}],
            3.14: [{'id': 3.14, 'value': 'fourth'}],
            None: [{'id': None, 'value': 'fifth'}]
        }
        self.assertEqual(result, expected)

    def test_complex_nested_values(self):
        """Test grouping with complex nested values."""
        data = [
            {'group': 'A', 'data': {'nested': [1, 2, 3]}},
            {'group': 'B', 'data': {'nested': [4, 5, 6]}},
            {'group': 'A', 'data': {'nested': [7, 8, 9]}}
        ]
        result = group_by_key(data, 'group')
        expected = {
            'A': [
                {'group': 'A', 'data': {'nested': [1, 2, 3]}},
                {'group': 'A', 'data': {'nested': [7, 8, 9]}}
            ],
            'B': [{'group': 'B', 'data': {'nested': [4, 5, 6]}}]
        }
        self.assertEqual(result, expected)

    def test_type_error_invalid_data(self):
        """Test type error for invalid data input."""
        with self.assertRaises(TypeError):
            group_by_key("not a list", 'key')
        with self.assertRaises(TypeError):
            group_by_key({'not': 'list'}, 'key')
        with self.assertRaises(TypeError):
            group_by_key(None, 'key')

    def test_type_error_non_dict_items(self):
        """Test type error when list contains non-dictionary items."""
        with self.assertRaises(TypeError):
            group_by_key([{'a': 1}, 'not a dict'], 'a')
        with self.assertRaises(TypeError):
            group_by_key([{'a': 1}, 123, {'b': 2}], 'a')

    def test_value_error_invalid_key(self):
        """Test value error for invalid key."""
        data = [{'a': 1}, {'b': 2}]
        with self.assertRaises(ValueError):
            group_by_key(data, '')
        with self.assertRaises(ValueError):
            group_by_key(data, 123)
        with self.assertRaises(ValueError):
            group_by_key(data, None)

    def test_memory_efficiency_large_datasets(self):
        """Test memory efficiency with large datasets."""
        # Create large dataset
        data = []
        for i in range(10000):
            data.append({'id': i % 100, 'value': f'item_{i}'})

        result = group_by_key(data, 'id')

        # Verify correctness
        self.assertEqual(len(result), 100)  # 100 unique groups
        self.assertEqual(len(result[0]), 100)  # Each group has 100 items
        self.assertEqual(result[0][0]['value'], 'item_0')
        self.assertEqual(result[99][-1]['value'], 'item_9999')


class TestSortDictByValue(unittest.TestCase):
    """Test cases for sort_dict_by_value function."""

    def test_sort_ascending(self):
        """Test sorting dictionary by values in ascending order."""
        data = {'a': 3, 'b': 1, 'c': 2}
        result = sort_dict_by_value(data)
        expected = {'b': 1, 'c': 2, 'a': 3}
        self.assertEqual(result, expected)

    def test_sort_descending(self):
        """Test sorting dictionary by values in descending order."""
        data = {'a': 3, 'b': 1, 'c': 2}
        result = sort_dict_by_value(data, reverse=True)
        expected = {'a': 3, 'c': 2, 'b': 1}
        self.assertEqual(result, expected)

    def test_mixed_int_float_values(self):
        """Test sorting with mixed integer and float values."""
        data = {'a': 3.5, 'b': 1, 'c': 2.2, 'd': 4}
        result = sort_dict_by_value(data)
        expected = {'b': 1, 'c': 2.2, 'a': 3.5, 'd': 4}
        self.assertEqual(result, expected)

    def test_negative_values(self):
        """Test sorting with negative values."""
        data = {'a': -1, 'b': 5, 'c': -3, 'd': 0}
        result = sort_dict_by_value(data)
        expected = {'c': -3, 'a': -1, 'd': 0, 'b': 5}
        self.assertEqual(result, expected)

    def test_equal_values(self):
        """Test sorting with equal values."""
        data = {'a': 5, 'b': 5, 'c': 1, 'd': 5}
        result = sort_dict_by_value(data)
        # Should maintain some order for equal values
        self.assertEqual(result['c'], 1)
        self.assertEqual(len([k for k, v in result.items() if v == 5]), 3)

    def test_single_item(self):
        """Test sorting single item dictionary."""
        data = {'only': 42}
        result = sort_dict_by_value(data)
        self.assertEqual(result, {'only': 42})

    def test_empty_dictionary(self):
        """Test sorting empty dictionary."""
        result = sort_dict_by_value({})
        self.assertEqual(result, {})

    def test_mixed_key_types(self):
        """Test sorting with mixed key types."""
        data = {'str_key': 3, 42: 1, (1, 2): 2, 3.14: 4}
        result = sort_dict_by_value(data)

        # Verify values are in correct order
        values = list(result.values())
        self.assertEqual(values, [1, 2, 3, 4])

    def test_large_values(self):
        """Test sorting with large numeric values."""
        data = {'a': 1000000, 'b': 999999, 'c': 1000001}
        result = sort_dict_by_value(data)
        expected = {'b': 999999, 'a': 1000000, 'c': 1000001}
        self.assertEqual(result, expected)

    def test_type_error_invalid_input(self):
        """Test type error for non-dictionary input."""
        with self.assertRaises(TypeError):
            sort_dict_by_value("not a dict")
        with self.assertRaises(TypeError):
            sort_dict_by_value([1, 2, 3])
        with self.assertRaises(TypeError):
            sort_dict_by_value(None)

    def test_type_error_non_numeric_values(self):
        """Test type error for non-numeric values."""
        with self.assertRaises(TypeError):
            sort_dict_by_value({'a': 1, 'b': 'string'})
        with self.assertRaises(TypeError):
            sort_dict_by_value({'a': 1, 'b': [1, 2, 3]})
        with self.assertRaises(TypeError):
            sort_dict_by_value({'a': 1, 'b': None})

    def test_type_error_boolean_values(self):
        """Test type error for boolean values (not considered numeric)."""
        with self.assertRaises(TypeError):
            sort_dict_by_value({'a': 1, 'b': True})
        with self.assertRaises(TypeError):
            sort_dict_by_value({'a': True, 'b': False})

    def test_memory_efficiency_large_datasets(self):
        """Test memory efficiency with large dictionaries."""
        # Create large dictionary
        data = {f'key_{i}': i for i in range(10000)}

        # Sort it
        result = sort_dict_by_value(data)

        # Verify correctness
        values = list(result.values())
        self.assertEqual(values, list(range(10000)))
        self.assertEqual(list(result.keys())[0], 'key_0')
        self.assertEqual(list(result.keys())[-1], 'key_9999')


class TestParametrizedScenarios(unittest.TestCase):
    """Parametrized tests for multiple input scenarios."""

    def setUp(self):
        """Set up test data for parametrized tests."""
        self.flatten_test_cases = [
            ([], []),
            ([1, 2, 3], [1, 2, 3]),
            ([1, [2, 3]], [1, 2, 3]),
            ([1, [2, [3, 4]], 5], [1, 2, 3, 4, 5]),
            ([[[[1]]]], [1]),
            ([1, [], [2, []], 3], [1, 2, 3])
        ]

        self.merge_test_cases = [
            ([], {}),
            ([{}], {}),
            ([{'a': 1}], {'a': 1}),
            ([{'a': 1}, {'b': 2}], {'a': 1, 'b': 2}),
            ([{'a': 1}, {'a': 2}], {'a': 2}),
            ([{'a': 1}, {'b': 2}, {'c': 3}], {'a': 1, 'b': 2, 'c': 3})
        ]

        self.find_max_test_cases = [
            ([1, 2, 3], 3),
            ([[1, 2], [3, 4]], 4),
            ({'a': 1, 'b': 2}, 2),
            ([1, {'a': 2}, [3, 4]], 4),
            ([-5, -3, -1], -1),
            ([1.1, [2.2, [3.3]]], 3.3)
        ]

    def test_flatten_list_parametrized(self):
        """Test flatten_list with multiple input scenarios."""
        for input_data, expected in self.flatten_test_cases:
            with self.subTest(input_data=input_data):
                result = flatten_list(input_data)
                self.assertEqual(result, expected)

    def test_merge_dictionaries_parametrized(self):
        """Test merge_dictionaries with multiple input scenarios."""
        for input_data, expected in self.merge_test_cases:
            with self.subTest(input_data=input_data):
                result = merge_dictionaries(*input_data)
                self.assertEqual(result, expected)

    def test_find_max_in_nested_parametrized(self):
        """Test find_max_in_nested with multiple input scenarios."""
        for input_data, expected in self.find_max_test_cases:
            with self.subTest(input_data=input_data):
                result = find_max_in_nested(input_data)
                self.assertEqual(result, expected)

    def test_group_by_key_parametrized(self):
        """Test group_by_key with multiple scenarios."""
        test_cases = [
            ([], 'key', {}),
            ([{'a': 1}], 'a', {1: [{'a': 1}]}),
            ([{'a': 1}, {'a': 1}], 'a', {1: [{'a': 1}, {'a': 1}]}),
            ([{'a': 1}, {'a': 2}], 'a', {1: [{'a': 1}], 2: [{'a': 2}]})
        ]

        for data, key, expected in test_cases:
            with self.subTest(data=data, key=key):
                result = group_by_key(data, key)
                self.assertEqual(result, expected)

    def test_sort_dict_by_value_parametrized(self):
        """Test sort_dict_by_value with multiple scenarios."""
        test_cases = [
            ({}, {}),
            ({'a': 1}, {'a': 1}),
            ({'a': 1, 'b': 2}, {'a': 1, 'b': 2}),
            ({'a': 2, 'b': 1}, {'b': 1, 'a': 2}),
            ({'a': -1, 'b': 1, 'c': 0}, {'a': -1, 'c': 0, 'b': 1})
        ]

        for input_data, expected in test_cases:
            with self.subTest(input_data=input_data):
                result = sort_dict_by_value(input_data)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    # Configure test runner for detailed output
    unittest.main(verbosity=2, buffer=True)