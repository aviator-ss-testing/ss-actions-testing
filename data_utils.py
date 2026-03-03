"""Data utility functions for common data manipulation tasks."""

from typing import TypeVar, List, Dict, Any, Optional, Callable, Hashable
from collections import defaultdict
from itertools import islice


T = TypeVar('T')
K = TypeVar('K', bound=Hashable)
V = TypeVar('V')


def flatten_list(nested_list: Optional[List[Any]]) -> List[Any]:
    """
    Flatten a nested list into a single-level list.

    Recursively flattens lists at any depth. Non-list items are preserved.
    Returns empty list for None input.

    Args:
        nested_list: A list that may contain nested lists

    Returns:
        A flattened list containing all non-list elements

    Examples:
        >>> flatten_list([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_list([1, 2, 3])
        [1, 2, 3]
        >>> flatten_list([])
        []
    """
    if nested_list is None:
        return []

    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


def chunk_list(lst: Optional[List[T]], chunk_size: int) -> List[List[T]]:
    """
    Split a list into chunks of specified size.

    The last chunk may be smaller than chunk_size if the list length
    is not evenly divisible. Returns empty list for None input.

    Args:
        lst: The list to split into chunks
        chunk_size: The maximum size of each chunk

    Returns:
        A list of lists, where each inner list has at most chunk_size elements

    Raises:
        ValueError: If chunk_size is less than 1

    Examples:
        >>> chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
        >>> chunk_list([1, 2, 3], 3)
        [[1, 2, 3]]
        >>> chunk_list([], 2)
        []
    """
    if lst is None:
        return []

    if chunk_size < 1:
        raise ValueError(f"chunk_size must be at least 1, got {chunk_size}")

    result = []
    for i in range(0, len(lst), chunk_size):
        result.append(lst[i:i + chunk_size])

    return result


def merge_dicts(*dicts: Dict[K, V], deep: bool = False) -> Dict[K, V]:
    """
    Merge multiple dictionaries into a single dictionary.

    Later dictionaries override earlier ones for conflicting keys.
    If deep=True, recursively merges nested dictionaries.

    Args:
        *dicts: Variable number of dictionaries to merge
        deep: If True, recursively merge nested dictionaries

    Returns:
        A new dictionary containing all key-value pairs from input dicts

    Examples:
        >>> merge_dicts({"a": 1}, {"b": 2}, {"c": 3})
        {'a': 1, 'b': 2, 'c': 3}
        >>> merge_dicts({"a": 1}, {"a": 2})
        {'a': 2}
        >>> merge_dicts({"a": {"x": 1}}, {"a": {"y": 2}}, deep=True)
        {'a': {'x': 1, 'y': 2}}
    """
    if not dicts:
        return {}

    result: Dict[K, V] = {}

    for d in dicts:
        if d is None:
            continue

        for key, value in d.items():
            if deep and key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_dicts(result[key], value, deep=True)  # type: ignore
            else:
                result[key] = value

    return result


def find_duplicates(lst: Optional[List[T]]) -> List[T]:
    """
    Find all duplicate values in a list.

    Returns a list of items that appear more than once, in the order
    they first appear as duplicates. Returns empty list for None input.

    Args:
        lst: The list to search for duplicates

    Returns:
        A list of duplicate values (each duplicate appears once in result)

    Examples:
        >>> find_duplicates([1, 2, 3, 2, 4, 3, 5])
        [2, 3]
        >>> find_duplicates([1, 2, 3])
        []
        >>> find_duplicates([1, 1, 1])
        [1]
    """
    if lst is None:
        return []

    seen = set()
    duplicates = []
    duplicate_set = set()

    for item in lst:
        if item in seen and item not in duplicate_set:
            duplicates.append(item)
            duplicate_set.add(item)
        else:
            seen.add(item)

    return duplicates


def group_by(lst: Optional[List[T]], key_func: Callable[[T], K]) -> Dict[K, List[T]]:
    """
    Group items in a list by a key function.

    Creates a dictionary where keys are the result of applying key_func
    to each item, and values are lists of items that produced that key.
    Returns empty dict for None input.

    Args:
        lst: The list to group
        key_func: A function that takes an item and returns a hashable key

    Returns:
        A dictionary mapping keys to lists of items

    Examples:
        >>> group_by([1, 2, 3, 4, 5, 6], lambda x: x % 2)
        {1: [1, 3, 5], 0: [2, 4, 6]}
        >>> group_by(["apple", "banana", "apricot", "berry"], lambda x: x[0])
        {'a': ['apple', 'apricot'], 'b': ['banana', 'berry']}
        >>> group_by([], lambda x: x)
        {}
    """
    if lst is None:
        return {}

    result: Dict[K, List[T]] = defaultdict(list)

    for item in lst:
        key = key_func(item)
        result[key].append(item)

    return dict(result)


def filter_none_values(data: Optional[Dict[K, Optional[V]]]) -> Dict[K, V]:
    """
    Remove all key-value pairs where the value is None.

    Creates a new dictionary excluding entries with None values.
    Returns empty dict for None input.

    Args:
        data: A dictionary that may contain None values

    Returns:
        A new dictionary with all None values filtered out

    Examples:
        >>> filter_none_values({"a": 1, "b": None, "c": 3})
        {'a': 1, 'c': 3}
        >>> filter_none_values({"a": None, "b": None})
        {}
        >>> filter_none_values({})
        {}
    """
    if data is None:
        return {}

    return {k: v for k, v in data.items() if v is not None}
