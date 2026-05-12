"""List utility functions."""

from collections import Counter
from typing import Any, Callable


def flatten(nested: list) -> list:
    """Flatten a nested list one level deep.

    Args:
        nested: A list that may contain sublists

    Returns:
        A flattened list with one level of nesting removed
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def chunk(lst: list, size: int) -> list[list]:
    """Split a list into chunks of specified size.

    Args:
        lst: The list to chunk
        size: The size of each chunk

    Returns:
        A list of lists, where each sublist has at most 'size' elements
    """
    if size <= 0:
        raise ValueError("Chunk size must be positive")

    chunks = []
    for i in range(0, len(lst), size):
        chunks.append(lst[i:i + size])
    return chunks


def group_by(lst: list, key: Callable) -> dict:
    """Group list elements by a key function.

    Args:
        lst: The list to group
        key: A callable that returns the grouping key for each element

    Returns:
        A dictionary mapping keys to lists of elements
    """
    groups: dict = {}
    for item in lst:
        k = key(item)
        if k not in groups:
            groups[k] = []
        groups[k].append(item)
    return groups


def most_common(lst: list) -> Any:
    """Return the most common element in a list.

    Args:
        lst: The list to analyze

    Returns:
        The element that appears most often, or None for empty input
    """
    if not lst:
        return None

    counter = Counter(lst)
    return counter.most_common(1)[0][0]
