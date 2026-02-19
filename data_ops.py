"""Data structure operations for lists and dictionaries."""


def find_duplicates(lst: list) -> list:
    """Find duplicate elements in a list.

    Args:
        lst: The list to search for duplicates

    Returns:
        A list of elements that appear more than once (without duplicates in result)
    """
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


def flatten_list(nested: list) -> list:
    """Flatten a nested list structure into a single-level list.

    Args:
        nested: The nested list to flatten

    Returns:
        A flattened list containing all elements from nested sublists
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """Merge two dictionaries, with dict2 values taking precedence.

    Args:
        dict1: The first dictionary
        dict2: The second dictionary (values override dict1 on conflicts)

    Returns:
        A new dictionary containing all key-value pairs from both dictionaries
    """
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def group_by_key(items: list[dict], key: str) -> dict:
    """Group a list of dictionaries by a specified key.

    Args:
        items: List of dictionaries to group
        key: The key to group by

    Returns:
        A dictionary where keys are unique values from the specified key,
        and values are lists of dictionaries with that key value
    """
    grouped = {}
    for item in items:
        if key in item:
            key_value = item[key]
            if key_value not in grouped:
                grouped[key_value] = []
            grouped[key_value].append(item)
    return grouped


def sort_by_multiple_keys(items: list[dict], keys: list[str]) -> list[dict]:
    """Sort a list of dictionaries by multiple keys in order.

    Args:
        items: List of dictionaries to sort
        keys: List of keys to sort by (in priority order)

    Returns:
        A new sorted list of dictionaries
    """
    sorted_items = items.copy()
    for key in reversed(keys):
        sorted_items.sort(key=lambda x: x.get(key, ""))
    return sorted_items
