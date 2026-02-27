"""List and dict helper functions using only the Python standard library."""

from collections import OrderedDict
from typing import Callable


def flatten(nested: list) -> list:
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def chunk(lst: list, size: int) -> list[list]:
    if size < 1:
        raise ValueError("size must be at least 1")
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def group_by(lst: list, key: Callable) -> dict:
    groups: dict = OrderedDict()
    for item in lst:
        k = key(item)
        if k not in groups:
            groups[k] = []
        groups[k].append(item)
    return groups


def dedupe_stable(lst: list) -> list:
    seen: set = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
