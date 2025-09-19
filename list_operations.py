"""
List Operations Module

A comprehensive module providing list processing functions with proper error handling
and input validation. Designed for integration testing scenarios with support for
empty lists, single-element lists, mixed data types, and various edge cases.
"""


def find_max(lst):
    """
    Find the maximum value in a list.

    Args:
        lst: A list containing comparable elements (numbers or strings)

    Returns:
        The maximum value from the list

    Raises:
        TypeError: If lst is not a list or contains incomparable types
        ValueError: If lst is empty
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    if len(lst) == 0:
        raise ValueError("Cannot find maximum of empty list")

    try:
        return max(lst)
    except TypeError as e:
        raise TypeError("List contains incomparable types") from e


def find_min(lst):
    """
    Find the minimum value in a list.

    Args:
        lst: A list containing comparable elements (numbers or strings)

    Returns:
        The minimum value from the list

    Raises:
        TypeError: If lst is not a list or contains incomparable types
        ValueError: If lst is empty
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    if len(lst) == 0:
        raise ValueError("Cannot find minimum of empty list")

    try:
        return min(lst)
    except TypeError as e:
        raise TypeError("List contains incomparable types") from e


def calculate_average(lst):
    """
    Calculate the average (arithmetic mean) of numeric values in a list.

    Args:
        lst: A list containing numeric values (int or float)

    Returns:
        float: The average of all values in the list

    Raises:
        TypeError: If lst is not a list or contains non-numeric values
        ValueError: If lst is empty
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    if len(lst) == 0:
        raise ValueError("Cannot calculate average of empty list")

    # Validate all elements are numeric
    for i, item in enumerate(lst):
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements must be numeric. Element at index {i} is {type(item).__name__}")

    return sum(lst) / len(lst)


def remove_duplicates(lst):
    """
    Remove duplicate values from a list while preserving original order.

    Args:
        lst: A list that may contain duplicate values

    Returns:
        list: A new list with duplicates removed, maintaining original order

    Raises:
        TypeError: If lst is not a list
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    seen = set()
    result = []

    for item in lst:
        # Handle unhashable types by using list lookup for those items
        try:
            if item not in seen:
                seen.add(item)
                result.append(item)
        except TypeError:
            # For unhashable types like lists or dicts, use linear search
            if item not in result:
                result.append(item)

    return result


def sort_list(lst, reverse=False):
    """
    Sort a list of comparable elements.

    Args:
        lst: A list containing comparable elements (numbers or strings)
        reverse: Boolean, if True sorts in descending order (default: False)

    Returns:
        list: A new sorted list

    Raises:
        TypeError: If lst is not a list or contains incomparable types
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    if not isinstance(reverse, bool):
        raise TypeError("reverse parameter must be a boolean")

    try:
        return sorted(lst, reverse=reverse)
    except TypeError as e:
        raise TypeError("List contains incomparable types") from e