"""
Data Utilities Module

This module provides utility functions for data structure manipulation including
operations on lists, dictionaries, and nested data structures. All functions
include comprehensive error handling and work with various input sizes and edge cases.
"""

from typing import List, Dict, Any, Union, Tuple
from collections import defaultdict


def flatten_list(nested_list: List[Any]) -> List[Any]:
    """
    Flatten a nested list of arbitrary depth.

    Args:
        nested_list: A list that may contain nested lists of any depth

    Returns:
        A flat list containing all elements from the nested structure

    Raises:
        TypeError: If input is not a list

    Examples:
        >>> flatten_list([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_list([])
        []
        >>> flatten_list([1, 2, 3])
        [1, 2, 3]
    """
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")

    result = []

    def _flatten_recursive(lst):
        for item in lst:
            if isinstance(item, list):
                _flatten_recursive(item)
            else:
                result.append(item)

    _flatten_recursive(nested_list)
    return result


def merge_dictionaries(*dicts: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Merge multiple dictionaries into one, with later dictionaries overriding earlier ones.

    Args:
        *dicts: Variable number of dictionaries to merge

    Returns:
        A new dictionary containing all key-value pairs from input dictionaries

    Raises:
        TypeError: If any input is not a dictionary

    Examples:
        >>> merge_dictionaries({'a': 1}, {'b': 2}, {'a': 3})
        {'a': 3, 'b': 2}
        >>> merge_dictionaries({}, {'x': 10})
        {'x': 10}
        >>> merge_dictionaries()
        {}
    """
    if not dicts:
        return {}

    for d in dicts:
        if not isinstance(d, dict):
            raise TypeError("All inputs must be dictionaries")

    result = {}
    for dictionary in dicts:
        result.update(dictionary)

    return result


def find_max_in_nested(data: Union[List, Dict, Tuple]) -> Union[int, float]:
    """
    Find the maximum numeric value in a nested data structure.

    Args:
        data: A nested structure (list, dict, or tuple) containing numeric values

    Returns:
        The maximum numeric value found in the structure

    Raises:
        TypeError: If input is not a list, dict, or tuple
        ValueError: If no numeric values are found in the structure

    Examples:
        >>> find_max_in_nested([1, [2, 3], {'a': 4, 'b': [5, 6]}])
        6
        >>> find_max_in_nested({'x': {'y': 10, 'z': [8, 12]}, 'w': 7})
        12
        >>> find_max_in_nested((1, (2, 3), 4))
        4
    """
    if not isinstance(data, (list, dict, tuple)):
        raise TypeError("Input must be a list, dictionary, or tuple")

    numeric_values = []

    def _extract_numbers(obj):
        if isinstance(obj, (int, float)) and not isinstance(obj, bool):
            numeric_values.append(obj)
        elif isinstance(obj, (list, tuple)):
            for item in obj:
                _extract_numbers(item)
        elif isinstance(obj, dict):
            for value in obj.values():
                _extract_numbers(value)

    _extract_numbers(data)

    if not numeric_values:
        raise ValueError("No numeric values found in the data structure")

    return max(numeric_values)


def group_by_key(data: List[Dict[str, Any]], key: str) -> Dict[Any, List[Dict[str, Any]]]:
    """
    Group a list of dictionaries by a specified key.

    Args:
        data: List of dictionaries to group
        key: The key to group by

    Returns:
        Dictionary where keys are unique values from the specified key,
        and values are lists of dictionaries that have that key value

    Raises:
        TypeError: If data is not a list or contains non-dictionary items
        ValueError: If key is empty or not a string

    Examples:
        >>> data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 30}]
        >>> group_by_key(data, 'age')
        {25: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 25}], 30: [{'name': 'Charlie', 'age': 30}]}
        >>> group_by_key([], 'key')
        {}
    """
    if not isinstance(data, list):
        raise TypeError("Data must be a list")

    if not isinstance(key, str) or not key:
        raise ValueError("Key must be a non-empty string")

    for item in data:
        if not isinstance(item, dict):
            raise TypeError("All items in data must be dictionaries")

    result = defaultdict(list)

    for item in data:
        if key in item:
            result[item[key]].append(item)

    return dict(result)


def sort_dict_by_value(dictionary: Dict[Any, Union[int, float]], reverse: bool = False) -> Dict[Any, Union[int, float]]:
    """
    Sort a dictionary by its values.

    Args:
        dictionary: Dictionary with numeric values to sort
        reverse: If True, sort in descending order; if False, ascending order

    Returns:
        New dictionary sorted by values

    Raises:
        TypeError: If input is not a dictionary or values are not numeric

    Examples:
        >>> sort_dict_by_value({'a': 3, 'b': 1, 'c': 2})
        {'b': 1, 'c': 2, 'a': 3}
        >>> sort_dict_by_value({'x': 10, 'y': 5, 'z': 15}, reverse=True)
        {'z': 15, 'x': 10, 'y': 5}
        >>> sort_dict_by_value({})
        {}
    """
    if not isinstance(dictionary, dict):
        raise TypeError("Input must be a dictionary")

    if not dictionary:
        return {}

    for key, value in dictionary.items():
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError(f"All values must be numeric. Found non-numeric value: {value}")

    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=reverse)
    return dict(sorted_items)