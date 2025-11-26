"""Data manipulation utilities.

This module provides common data manipulation functions including
flattening lists, removing duplicates, grouping, and filtering.
"""

from typing import Any, Dict, List


def flatten_list(nested_list: list) -> list:
    """Flatten a nested list to a single level.

    Args:
        nested_list: A list that may contain nested lists at any depth
    Returns:
        A flattened list with all nested elements at the same level
    Examples:
        >>> flatten_list([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def remove_duplicates(items: list) -> list:
    """Remove duplicate items from a list while preserving order.

    Args:
        items: A list that may contain duplicate elements
    Returns:
        A list with duplicates removed, maintaining original order
    Examples:
        >>> remove_duplicates([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def group_by_key(items: List[Dict[str, Any]], key: str) -> Dict[str, List[Dict[str, Any]]]:
    """Group a list of dictionaries by a specified key.

    Args:
        items: A list of dictionaries to group
        key: The dictionary key to group by
    Returns:
        A dict mapping key values to lists of dicts with that value
    Examples:
        >>> group_by_key([{"name": "Alice", "age": 30}, {"name": "Bob", "age": 30}], "age")
        {30: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 30}]}
    """
    result = {}
    for item in items:
        if key in item:
            key_value = item[key]
            if key_value not in result:
                result[key_value] = []
            result[key_value].append(item)
    return result


def filter_none(items: list) -> list:
    """Remove None values from a list.

    Args:
        items: A list that may contain None values
    Returns:
        A list with all None values removed
    Examples:
        >>> filter_none([1, None, 2, None, 3])
        [1, 2, 3]
    """
    return [item for item in items if item is not None]
