"""
Comprehensive test suite for data processing utilities module.

This module provides thorough testing for all data structure manipulation functions,
including edge cases, error conditions, and integration scenarios.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.data_processing import (
    flatten_list,
    merge_dictionaries,
    remove_duplicates_preserve_order,
    find_common_elements,
    csv_string_to_dict,
    dict_to_csv_string,
    normalize_data,
    chunk_list
)


class TestFlattenList(unittest.TestCase):
    """Test cases for flatten_list function."""
    
    def test_simple_nested_list(self):
        """Test flattening a simple nested list."""
        self.assertEqual(flatten_list([1, [2, 3], 4]), [1, 2, 3, 4])
    
    def test_deeply_nested_list(self):
        """Test flattening a deeply nested list structure."""
        nested = [1, [2, [3, [4, 5]], 6], 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(flatten_list(nested), expected)
    
    def test_empty_nested_lists(self):
        """Test flattening with empty nested lists."""
        self.assertEqual(flatten_list([1, [], [2, []], 3]), [1, 2, 3])
    
    def test_all_empty_lists(self):
        """Test flattening lists containing only empty lists."""
        self.assertEqual(flatten_list([[], [[]], []]), [])
    
    def test_single_level_list(self):
        """Test that single-level lists are returned unchanged."""
        self.assertEqual(flatten_list([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def test_empty_input_list(self):
        """Test flattening an empty list."""
        self.assertEqual(flatten_list([]), [])
    
    def test_mixed_data_types(self):
        """Test flattening with mixed data types."""
        nested = [1, ['hello', [2.5, True]], None]
        expected = [1, 'hello', 2.5, True, None]
        self.assertEqual(flatten_list(nested), expected)
    
    def test_non_list_input_raises_typeerror(self):
        """Test that non-list input raises TypeError."""
        with self.assertRaises(TypeError):
            flatten_list("not a list")
        with self.assertRaises(TypeError):
            flatten_list(123)
        with self.assertRaises(TypeError):
            flatten_list(None)


class TestMergeDictionaries(unittest.TestCase):
    """Test cases for merge_dictionaries function."""
    
    def test_merge_two_dictionaries(self):
        """Test merging two simple dictionaries."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)
    
    def test_merge_overlapping_keys(self):
        """Test that later dictionaries override earlier ones."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)
    
    def test_merge_multiple_dictionaries(self):
        """Test merging multiple dictionaries."""
        dict1 = {'a': 1}
        dict2 = {'b': 2}
        dict3 = {'c': 3}
        dict4 = {'a': 10, 'd': 4}
        expected = {'a': 10, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2, dict3, dict4), expected)
    
    def test_merge_empty_dictionaries(self):
        """Test merging empty dictionaries."""
        self.assertEqual(merge_dictionaries({}, {}), {})
        self.assertEqual(merge_dictionaries({'a': 1}, {}), {'a': 1})
        self.assertEqual(merge_dictionaries({}, {'b': 2}), {'b': 2})
    
    def test_merge_no_arguments(self):
        """Test merging with no arguments returns empty dict."""
        self.assertEqual(merge_dictionaries(), {})
    
    def test_merge_single_dictionary(self):
        """Test merging a single dictionary."""
        dict1 = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries(dict1), dict1)
    
    def test_merge_nested_dictionaries(self):
        """Test merging dictionaries with nested values."""
        dict1 = {'a': {'x': 1}, 'b': [1, 2]}
        dict2 = {'a': {'y': 2}, 'c': 'hello'}
        expected = {'a': {'y': 2}, 'b': [1, 2], 'c': 'hello'}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)
    
    def test_non_dict_argument_raises_typeerror(self):
        """Test that non-dictionary arguments raise TypeError."""
        with self.assertRaises(TypeError):
            merge_dictionaries({'a': 1}, "not a dict")
        with self.assertRaises(TypeError):
            merge_dictionaries(['a', 'list'])
        with self.assertRaises(TypeError):
            merge_dictionaries({'a': 1}, None)


class TestRemoveDuplicatesPreserveOrder(unittest.TestCase):
    """Test cases for remove_duplicates_preserve_order function."""
    
    def test_remove_simple_duplicates(self):
        """Test removing simple duplicates."""
        self.assertEqual(remove_duplicates_preserve_order([1, 2, 2, 3, 1]), [1, 2, 3])
    
    def test_no_duplicates(self):
        """Test list with no duplicates."""
        self.assertEqual(remove_duplicates_preserve_order([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def test_all_duplicates(self):
        """Test list where all elements are the same."""
        self.assertEqual(remove_duplicates_preserve_order([5, 5, 5, 5]), [5])
    
    def test_empty_list(self):
        """Test empty list."""
        self.assertEqual(remove_duplicates_preserve_order([]), [])
    
    def test_mixed_data_types(self):
        """Test removing duplicates with mixed data types."""
        input_list = [1, 'hello', 1, 2.5, 'hello', None, None]
        expected = [1, 'hello', 2.5, None]
        self.assertEqual(remove_duplicates_preserve_order(input_list), expected)
    
    def test_order_preservation(self):
        """Test that original order is preserved."""
        input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        expected = [3, 1, 4, 5, 9, 2, 6]
        self.assertEqual(remove_duplicates_preserve_order(input_list), expected)
    
    def test_non_list_input_raises_typeerror(self):
        """Test that non-list input raises TypeError."""
        with self.assertRaises(TypeError):
            remove_duplicates_preserve_order("string")
        with self.assertRaises(TypeError):
            remove_duplicates_preserve_order(123)
        with self.assertRaises(TypeError):
            remove_duplicates_preserve_order(None)


class TestFindCommonElements(unittest.TestCase):
    """Test cases for find_common_elements function."""
    
    def test_find_common_in_two_lists(self):
        """Test finding common elements in two lists."""
        result = find_common_elements([1, 2, 3], [2, 3, 4])
        self.assertEqual(set(result), {2, 3})
    
    def test_find_common_in_multiple_lists(self):
        """Test finding common elements in multiple lists."""
        result = find_common_elements([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])
        self.assertEqual(set(result), {3, 4})
    
    def test_no_common_elements(self):
        """Test when there are no common elements."""
        result = find_common_elements([1, 2], [3, 4], [5, 6])
        self.assertEqual(result, [])
    
    def test_single_list(self):
        """Test with a single list returns unique elements."""
        result = find_common_elements([1, 2, 2, 3])
        self.assertEqual(set(result), {1, 2, 3})
    
    def test_empty_lists(self):
        """Test with empty lists."""
        result = find_common_elements([], [1, 2], [2, 3])
        self.assertEqual(result, [])
    
    def test_all_empty_lists(self):
        """Test with all empty lists."""
        result = find_common_elements([], [], [])
        self.assertEqual(result, [])
    
    def test_identical_lists(self):
        """Test with identical lists."""
        result = find_common_elements([1, 2, 3], [1, 2, 3], [1, 2, 3])
        self.assertEqual(set(result), {1, 2, 3})
    
    def test_mixed_data_types(self):
        """Test with mixed data types."""
        result = find_common_elements([1, 'hello', 2.5], ['hello', 2.5, True], [2.5, 'hello', None])
        self.assertEqual(set(result), {'hello', 2.5})
    
    def test_no_arguments_raises_valueerror(self):
        """Test that no arguments raises ValueError."""
        with self.assertRaises(ValueError):
            find_common_elements()
    
    def test_non_list_argument_raises_typeerror(self):
        """Test that non-list arguments raise TypeError."""
        with self.assertRaises(TypeError):
            find_common_elements([1, 2], "not a list")
        with self.assertRaises(TypeError):
            find_common_elements(123, [1, 2])


class TestCSVStringToDict(unittest.TestCase):
    """Test cases for csv_string_to_dict function."""
    
    def test_simple_csv_conversion(self):
        """Test converting simple CSV string to dictionaries."""
        csv_data = "John,25,Engineer\nJane,30,Doctor"
        headers = ['name', 'age', 'profession']
        expected = [
            {'name': 'John', 'age': '25', 'profession': 'Engineer'},
            {'name': 'Jane', 'age': '30', 'profession': 'Doctor'}
        ]
        self.assertEqual(csv_string_to_dict(csv_data, headers), expected)
    
    def test_csv_with_spaces(self):
        """Test CSV with spaces around values."""
        csv_data = "John , 25 , Engineer\n Jane, 30,Doctor "
        headers = ['name', 'age', 'profession']
        expected = [
            {'name': 'John', 'age': '25', 'profession': 'Engineer'},
            {'name': 'Jane', 'age': '30', 'profession': 'Doctor'}
        ]
        self.assertEqual(csv_string_to_dict(csv_data, headers), expected)
    
    def test_single_row_csv(self):
        """Test CSV with single row."""
        csv_data = "Alice,28,Designer"
        headers = ['name', 'age', 'profession']
        expected = [{'name': 'Alice', 'age': '28', 'profession': 'Designer'}]
        self.assertEqual(csv_string_to_dict(csv_data, headers), expected)
    
    def test_empty_csv_string(self):
        """Test empty CSV string."""
        self.assertEqual(csv_string_to_dict("", ['a', 'b']), [])
        self.assertEqual(csv_string_to_dict("   ", ['a', 'b']), [])
    
    def test_csv_with_empty_values(self):
        """Test CSV with some empty values."""
        csv_data = "John,,Engineer\n,30,Doctor"
        headers = ['name', 'age', 'profession']
        expected = [
            {'name': 'John', 'age': '', 'profession': 'Engineer'},
            {'name': '', 'age': '30', 'profession': 'Doctor'}
        ]
        self.assertEqual(csv_string_to_dict(csv_data, headers), expected)
    
    def test_mismatched_columns_raises_valueerror(self):
        """Test that mismatched columns raise ValueError."""
        csv_data = "John,25\nJane,30,Doctor,Extra"
        headers = ['name', 'age', 'profession']
        with self.assertRaises(ValueError):
            csv_string_to_dict(csv_data, headers)
    
    def test_non_string_csv_raises_typeerror(self):
        """Test that non-string CSV input raises TypeError."""
        with self.assertRaises(TypeError):
            csv_string_to_dict(123, ['a', 'b'])
        with self.assertRaises(TypeError):
            csv_string_to_dict(None, ['a', 'b'])
    
    def test_non_list_headers_raises_typeerror(self):
        """Test that non-list headers raise TypeError."""
        with self.assertRaises(TypeError):
            csv_string_to_dict("a,b", "headers")
        with self.assertRaises(TypeError):
            csv_string_to_dict("a,b", None)


class TestDictToCSVString(unittest.TestCase):
    """Test cases for dict_to_csv_string function."""
    
    def test_simple_dict_to_csv(self):
        """Test converting simple dictionaries to CSV."""
        data = [
            {'name': 'John', 'age': 25, 'profession': 'Engineer'},
            {'name': 'Jane', 'age': 30, 'profession': 'Doctor'}
        ]
        headers = ['name', 'age', 'profession']
        expected = "John,25,Engineer\nJane,30,Doctor"
        self.assertEqual(dict_to_csv_string(data, headers), expected)
    
    def test_single_dict_to_csv(self):
        """Test converting single dictionary to CSV."""
        data = [{'name': 'Alice', 'age': 28}]
        headers = ['name', 'age']
        expected = "Alice,28"
        self.assertEqual(dict_to_csv_string(data, headers), expected)
    
    def test_empty_data_list(self):
        """Test empty data list."""
        self.assertEqual(dict_to_csv_string([], ['a', 'b']), "")
    
    def test_missing_keys_in_dict(self):
        """Test dictionaries with missing keys."""
        data = [
            {'name': 'John', 'age': 25},
            {'name': 'Jane', 'profession': 'Doctor'}
        ]
        headers = ['name', 'age', 'profession']
        expected = "John,25,\nJane,,Doctor"
        self.assertEqual(dict_to_csv_string(data, headers), expected)
    
    def test_extra_keys_in_dict(self):
        """Test dictionaries with extra keys not in headers."""
        data = [
            {'name': 'John', 'age': 25, 'city': 'NYC', 'country': 'USA'},
            {'name': 'Jane', 'age': 30, 'hobby': 'Reading'}
        ]
        headers = ['name', 'age']
        expected = "John,25\nJane,30"
        self.assertEqual(dict_to_csv_string(data, headers), expected)
    
    def test_non_string_values(self):
        """Test dictionaries with non-string values."""
        data = [
            {'name': 'John', 'age': 25, 'active': True},
            {'name': 'Jane', 'age': None, 'active': False}
        ]
        headers = ['name', 'age', 'active']
        expected = "John,25,True\nJane,None,False"
        self.assertEqual(dict_to_csv_string(data, headers), expected)
    
    def test_non_list_data_raises_typeerror(self):
        """Test that non-list data raises TypeError."""
        with self.assertRaises(TypeError):
            dict_to_csv_string("not a list", ['a', 'b'])
        with self.assertRaises(TypeError):
            dict_to_csv_string(None, ['a', 'b'])
    
    def test_non_dict_items_raises_valueerror(self):
        """Test that non-dictionary items raise ValueError."""
        with self.assertRaises(ValueError):
            dict_to_csv_string([{'a': 1}, "not a dict"], ['a'])
        with self.assertRaises(ValueError):
            dict_to_csv_string([123], ['a'])


class TestNormalizeData(unittest.TestCase):
    """Test cases for normalize_data function."""
    
    def test_normalize_to_default_range(self):
        """Test normalizing to default [0, 1] range."""
        data = [1, 2, 3, 4, 5]
        expected = [0.0, 0.25, 0.5, 0.75, 1.0]
        result = normalize_data(data)
        self.assertEqual(result, expected)
    
    def test_normalize_to_custom_range(self):
        """Test normalizing to custom range."""
        data = [10, 20, 30]
        expected = [-1.0, 0.0, 1.0]
        result = normalize_data(data, -1, 1)
        self.assertEqual(result, expected)
    
    def test_normalize_single_value(self):
        """Test normalizing list with single value."""
        data = [5]
        expected = [0]
        result = normalize_data(data)
        self.assertEqual(result, expected)
    
    def test_normalize_identical_values(self):
        """Test normalizing list with all identical values."""
        data = [3, 3, 3, 3]
        expected = [0, 0, 0, 0]
        result = normalize_data(data)
        self.assertEqual(result, expected)
    
    def test_normalize_negative_values(self):
        """Test normalizing with negative values."""
        data = [-2, -1, 0, 1, 2]
        expected = [0.0, 0.25, 0.5, 0.75, 1.0]
        result = normalize_data(data)
        self.assertEqual(result, expected)
    
    def test_normalize_floats(self):
        """Test normalizing floating point values."""
        data = [1.5, 2.5, 3.5]
        expected = [0.0, 0.5, 1.0]
        result = normalize_data(data)
        self.assertEqual(result, expected)
    
    def test_empty_data_raises_valueerror(self):
        """Test that empty data raises ValueError."""
        with self.assertRaises(ValueError):
            normalize_data([])
    
    def test_invalid_range_raises_valueerror(self):
        """Test that invalid range raises ValueError."""
        with self.assertRaises(ValueError):
            normalize_data([1, 2, 3], 1, 1)
        with self.assertRaises(ValueError):
            normalize_data([1, 2, 3], 2, 1)
    
    def test_non_numeric_data_raises_typeerror(self):
        """Test that non-numeric data raises TypeError."""
        with self.assertRaises(TypeError):
            normalize_data([1, 2, "three"])
        with self.assertRaises(TypeError):
            normalize_data([1, 2, None])
    
    def test_non_list_input_raises_typeerror(self):
        """Test that non-list input raises TypeError."""
        with self.assertRaises(TypeError):
            normalize_data("not a list")
        with self.assertRaises(TypeError):
            normalize_data(None)


class TestChunkList(unittest.TestCase):
    """Test cases for chunk_list function."""
    
    def test_chunk_evenly_divisible(self):
        """Test chunking list that divides evenly."""
        data = [1, 2, 3, 4, 5, 6]
        expected = [[1, 2], [3, 4], [5, 6]]
        result = chunk_list(data, 2)
        self.assertEqual(result, expected)
    
    def test_chunk_not_evenly_divisible(self):
        """Test chunking list that doesn't divide evenly."""
        data = [1, 2, 3, 4, 5]
        expected = [[1, 2], [3, 4], [5]]
        result = chunk_list(data, 2)
        self.assertEqual(result, expected)
    
    def test_chunk_size_larger_than_list(self):
        """Test chunk size larger than list."""
        data = [1, 2, 3]
        expected = [[1, 2, 3]]
        result = chunk_list(data, 5)
        self.assertEqual(result, expected)
    
    def test_chunk_size_one(self):
        """Test chunk size of 1."""
        data = [1, 2, 3, 4]
        expected = [[1], [2], [3], [4]]
        result = chunk_list(data, 1)
        self.assertEqual(result, expected)
    
    def test_empty_list(self):
        """Test chunking empty list."""
        result = chunk_list([], 3)
        self.assertEqual(result, [])
    
    def test_mixed_data_types(self):
        """Test chunking with mixed data types."""
        data = [1, 'hello', 2.5, None, True]
        expected = [[1, 'hello'], [2.5, None], [True]]
        result = chunk_list(data, 2)
        self.assertEqual(result, expected)
    
    def test_zero_chunk_size_raises_valueerror(self):
        """Test that zero chunk size raises ValueError."""
        with self.assertRaises(ValueError):
            chunk_list([1, 2, 3], 0)
    
    def test_negative_chunk_size_raises_valueerror(self):
        """Test that negative chunk size raises ValueError."""
        with self.assertRaises(ValueError):
            chunk_list([1, 2, 3], -1)
    
    def test_non_integer_chunk_size_raises_typeerror(self):
        """Test that non-integer chunk size raises TypeError."""
        with self.assertRaises(TypeError):
            chunk_list([1, 2, 3], 2.5)
        with self.assertRaises(TypeError):
            chunk_list([1, 2, 3], "2")
    
    def test_non_list_input_raises_typeerror(self):
        """Test that non-list input raises TypeError."""
        with self.assertRaises(TypeError):
            chunk_list("string", 2)
        with self.assertRaises(TypeError):
            chunk_list(None, 2)


class TestDataProcessingIntegration(unittest.TestCase):
    """Integration tests that combine multiple data processing functions."""
    
    def test_flatten_and_remove_duplicates(self):
        """Test combining flatten_list and remove_duplicates_preserve_order."""
        nested_data = [[1, 2], [2, 3, [3, 4]], [4, 5]]
        flattened = flatten_list(nested_data)
        result = remove_duplicates_preserve_order(flattened)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)
    
    def test_csv_roundtrip(self):
        """Test converting dict to CSV and back to dict."""
        original_data = [
            {'name': 'John', 'age': '25', 'city': 'NYC'},
            {'name': 'Jane', 'age': '30', 'city': 'LA'}
        ]
        headers = ['name', 'age', 'city']
        
        # Convert to CSV and back
        csv_string = dict_to_csv_string(original_data, headers)
        converted_back = csv_string_to_dict(csv_string, headers)
        
        self.assertEqual(converted_back, original_data)
    
    def test_normalize_and_chunk(self):
        """Test normalizing data and then chunking it."""
        data = [1, 5, 10, 15, 20]
        normalized = normalize_data(data)
        chunked = chunk_list(normalized, 2)
        expected = [[0.0, (4/19)], [(9/19), (14/19)], [1.0]]
        
        # Check structure is correct
        self.assertEqual(len(chunked), 3)
        self.assertEqual(len(chunked[0]), 2)
        self.assertEqual(len(chunked[1]), 2)
        self.assertEqual(len(chunked[2]), 1)
        
        # Check first and last values
        self.assertEqual(chunked[0][0], 0.0)
        self.assertEqual(chunked[2][0], 1.0)
    
    def test_merge_dicts_and_convert_to_csv(self):
        """Test merging dictionaries and converting result to CSV format."""
        dict1 = {'users': [{'name': 'John', 'age': 25}]}
        dict2 = {'users': [{'name': 'Jane', 'age': 30}]}
        dict3 = {'metadata': {'version': '1.0'}}
        
        merged = merge_dictionaries(dict1, dict2, dict3)
        
        # Should have dict2's users (later override) and metadata
        expected_keys = {'users', 'metadata'}
        self.assertEqual(set(merged.keys()), expected_keys)
        self.assertEqual(merged['users'], [{'name': 'Jane', 'age': 30}])
        self.assertEqual(merged['metadata'], {'version': '1.0'})
    
    def test_find_common_after_processing(self):
        """Test finding common elements after processing multiple lists."""
        list1 = [1, 2, 2, 3, 4, 4]
        list2 = [2, 3, 3, 4, 5, 5]
        list3 = [3, 4, 4, 5, 6, 6]
        
        # Remove duplicates from each list first
        processed_lists = [
            remove_duplicates_preserve_order(list1),
            remove_duplicates_preserve_order(list2),
            remove_duplicates_preserve_order(list3)
        ]
        
        common = find_common_elements(*processed_lists)
        self.assertEqual(set(common), {3, 4})
    
    def test_complex_nested_data_processing(self):
        """Test complex scenario with nested data structures."""
        # Start with complex nested structure
        complex_data = [
            [1, [2, 3]], 
            [[4, 5], 6], 
            [1, [7, [8, 2]]]
        ]
        
        # Flatten the structure
        flattened = flatten_list(complex_data)
        
        # Remove duplicates while preserving order
        unique_data = remove_duplicates_preserve_order(flattened)
        
        # Normalize the data
        normalized = normalize_data(unique_data)
        
        # Chunk into pairs
        chunked = chunk_list(normalized, 2)
        
        # Verify the processing chain worked correctly
        self.assertEqual(unique_data, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(len(normalized), 8)
        self.assertEqual(len(chunked), 4)
        self.assertTrue(all(len(chunk) == 2 for chunk in chunked))
    
    def test_error_propagation_in_integration(self):
        """Test that errors propagate correctly in integrated operations."""
        # Test with invalid data that should cause normalize_data to fail
        nested_invalid = [[1, 2], ['invalid', 3]]
        flattened = flatten_list(nested_invalid)
        
        # This should raise TypeError when trying to normalize
        with self.assertRaises(TypeError):
            normalize_data(flattened)
    
    def test_empty_data_integration(self):
        """Test integration with empty or minimal data."""
        # Empty nested structure
        empty_nested = [[], [[]], []]
        flattened = flatten_list(empty_nested)
        unique_data = remove_duplicates_preserve_order(flattened)
        
        self.assertEqual(flattened, [])
        self.assertEqual(unique_data, [])
        
        # Should handle empty list in chunking
        chunked = chunk_list(unique_data, 3)
        self.assertEqual(chunked, [])
    
    def test_data_consistency_through_pipeline(self):
        """Test that data maintains consistency through processing pipeline."""
        # Start with known data
        original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        
        # Process through pipeline
        unique_data = remove_duplicates_preserve_order(original)
        normalized = normalize_data(unique_data)
        chunked = chunk_list(normalized, 3)
        
        # Verify data consistency
        self.assertEqual(unique_data, [3, 1, 4, 5, 9, 2, 6])
        self.assertEqual(len(normalized), 7)
        self.assertEqual(sum(len(chunk) for chunk in chunked), 7)
        
        # Verify normalization bounds
        self.assertEqual(min(normalized), 0.0)
        self.assertEqual(max(normalized), 1.0)


if __name__ == '__main__':
    unittest.main()