"""Utility functions for common data manipulation tasks."""

from typing import Any, Callable, Dict, Hashable, List, Optional, TypeVar

T = TypeVar("T")
K = TypeVar("K", bound=Hashable)


def flatten_list(nested: List[Any]) -> List[Any]:
    """Flatten a nested list of arbitrary depth into a single flat list.

    Args:
        nested: A list that may contain nested lists at any depth.

    Returns:
        A flat list with all elements in order.

    Raises:
        TypeError: If nested is not a list.
    """
    if not isinstance(nested, list):
        raise TypeError(f"Expected list, got {type(nested).__name__}")
    result: List[Any] = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def chunk_list(lst: List[T], size: int) -> List[List[T]]:
    """Split a list into chunks of a given size.

    The last chunk may be smaller than size if the list length is not
    evenly divisible.

    Args:
        lst: The list to split.
        size: The maximum size of each chunk.

    Returns:
        A list of sublists, each of length at most size.

    Raises:
        TypeError: If lst is not a list.
        ValueError: If size is not a positive integer.
    """
    if not isinstance(lst, list):
        raise TypeError(f"Expected list, got {type(lst).__name__}")
    if not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")
    return [lst[i : i + size] for i in range(0, len(lst), size)]


def merge_dicts(*dicts: Dict[Any, Any], overwrite: bool = True) -> Dict[Any, Any]:
    """Merge multiple dictionaries into one.

    Args:
        *dicts: Dictionaries to merge.
        overwrite: If True (default), later dicts overwrite earlier ones on
            conflicting keys. If False, the first value encountered is kept.

    Returns:
        A new dictionary containing all key-value pairs.

    Raises:
        TypeError: If any argument is not a dictionary.
    """
    for d in dicts:
        if not isinstance(d, dict):
            raise TypeError(f"Expected dict, got {type(d).__name__}")
    result: Dict[Any, Any] = {}
    for d in dicts:
        for key, value in d.items():
            if overwrite or key not in result:
                result[key] = value
    return result


def find_duplicates(lst: List[T]) -> List[T]:
    """Return a list of elements that appear more than once, preserving order.

    Each duplicate value is included only once in the result regardless of
    how many times it appears in the input.

    Args:
        lst: The list to search for duplicates.

    Returns:
        A list of duplicate values in the order they first appeared.

    Raises:
        TypeError: If lst is not a list.
    """
    if not isinstance(lst, list):
        raise TypeError(f"Expected list, got {type(lst).__name__}")

    def _hashable(item: Any) -> Any:
        try:
            hash(item)
            return item
        except TypeError:
            return str(item)

    counts: Dict[Any, int] = {}
    for item in lst:
        k = _hashable(item)
        counts[k] = counts.get(k, 0) + 1

    seen: set = set()
    duplicates: List[T] = []
    for item in lst:
        k = _hashable(item)
        if counts[k] > 1 and k not in seen:
            duplicates.append(item)
            seen.add(k)
    return duplicates


def group_by(lst: List[T], key: Callable[[T], K]) -> Dict[K, List[T]]:
    """Group list elements by a key function.

    Args:
        lst: The list of items to group.
        key: A callable that returns the grouping key for each item.

    Returns:
        A dictionary mapping each key to the list of items that produced it.

    Raises:
        TypeError: If lst is not a list or key is not callable.
    """
    if not isinstance(lst, list):
        raise TypeError(f"Expected list, got {type(lst).__name__}")
    if not callable(key):
        raise TypeError("key must be callable")
    result: Dict[K, List[T]] = {}
    for item in lst:
        k = key(item)
        result.setdefault(k, []).append(item)
    return result


def filter_none_values(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """Return a copy of a dictionary with all None-valued keys removed.

    Args:
        d: The dictionary to filter.

    Returns:
        A new dictionary containing only entries whose values are not None.

    Raises:
        TypeError: If d is not a dictionary.
    """
    if not isinstance(d, dict):
        raise TypeError(f"Expected dict, got {type(d).__name__}")
    return {k: v for k, v in d.items() if v is not None}
