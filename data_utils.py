"""Utility functions for common data manipulation tasks."""

from typing import Any, Callable, Dict, Hashable, List, Optional, TypeVar

T = TypeVar("T")
K = TypeVar("K", bound=Hashable)
V = TypeVar("V")


def flatten_list(lst: List[Any], depth: int = -1) -> List[Any]:
    """Flatten a nested list into a single flat list.

    Args:
        lst: The nested list to flatten.
        depth: Maximum depth to flatten. -1 means fully flatten. 0 returns a copy.

    Returns:
        A new flat list.

    Raises:
        TypeError: If lst is not a list.
        ValueError: If depth is less than -1.
    """
    if not isinstance(lst, list):
        raise TypeError(f"Expected list, got {type(lst).__name__}")
    if depth < -1:
        raise ValueError("depth must be -1 (unlimited) or a non-negative integer")

    def _flatten(items: List[Any], current_depth: int) -> List[Any]:
        result = []
        for item in items:
            if isinstance(item, list) and current_depth != 0:
                next_depth = current_depth - 1 if current_depth > 0 else current_depth
                result.extend(_flatten(item, next_depth))
            else:
                result.append(item)
        return result

    return _flatten(lst, depth)


def chunk_list(lst: List[T], size: int) -> List[List[T]]:
    """Split a list into chunks of a given size.

    Args:
        lst: The list to split.
        size: The size of each chunk.

    Returns:
        A list of chunks. The last chunk may be smaller than size.

    Raises:
        TypeError: If lst is not a list.
        ValueError: If size is not a positive integer.
    """
    if not isinstance(lst, list):
        raise TypeError(f"Expected list, got {type(lst).__name__}")
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError(f"size must be an int, got {type(size).__name__}")
    if size <= 0:
        raise ValueError("size must be a positive integer")
    return [lst[i : i + size] for i in range(0, len(lst), size)]


def merge_dicts(*dicts: Dict[K, V], strategy: str = "last") -> Dict[K, V]:
    """Merge multiple dictionaries into one.

    Args:
        *dicts: Dictionaries to merge.
        strategy: How to handle conflicting keys:
            - "last": The last dict's value wins (default).
            - "first": The first dict's value wins.
            - "error": Raise ValueError on conflicting keys.

    Returns:
        A new merged dictionary.

    Raises:
        TypeError: If any argument is not a dict.
        ValueError: If strategy is invalid, or if strategy="error" and keys conflict.
    """
    valid_strategies = {"last", "first", "error"}
    if strategy not in valid_strategies:
        raise ValueError(f"strategy must be one of {valid_strategies}, got {strategy!r}")
    for d in dicts:
        if not isinstance(d, dict):
            raise TypeError(f"Expected dict, got {type(d).__name__}")

    result: Dict[K, V] = {}
    for d in dicts:
        for key, value in d.items():
            if key in result:
                if strategy == "error":
                    raise ValueError(f"Conflicting key: {key!r}")
                elif strategy == "first":
                    continue
            result[key] = value
    return result


def find_duplicates(lst: List[T]) -> List[T]:
    """Find all duplicate values in a list.

    Args:
        lst: The list to search for duplicates.

    Returns:
        A list of values that appear more than once, ordered by their first
        occurrence in the input list.

    Raises:
        TypeError: If lst is not a list.
    """
    if not isinstance(lst, list):
        raise TypeError(f"Expected list, got {type(lst).__name__}")
    seen_order: List[T] = []
    seen_set: set = set()
    duplicate_set: set = set()
    for item in lst:
        if item in seen_set:
            duplicate_set.add(item)
        else:
            seen_set.add(item)
            seen_order.append(item)
    return [item for item in seen_order if item in duplicate_set]


def group_by(lst: List[T], key: Callable[[T], K]) -> Dict[K, List[T]]:
    """Group list items by a key function.

    Args:
        lst: The list to group.
        key: A callable that returns the grouping key for each item.

    Returns:
        A dictionary mapping each key to a list of items with that key,
        preserving insertion order.

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
        if k not in result:
            result[k] = []
        result[k].append(item)
    return result


def filter_none_values(d: Dict[K, Optional[V]]) -> Dict[K, V]:
    """Remove all keys whose value is None from a dictionary.

    Args:
        d: The dictionary to filter.

    Returns:
        A new dictionary with None values removed.

    Raises:
        TypeError: If d is not a dict.
    """
    if not isinstance(d, dict):
        raise TypeError(f"Expected dict, got {type(d).__name__}")
    return {k: v for k, v in d.items() if v is not None}
