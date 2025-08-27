"""
Data structure manipulation and processing utility functions module.

This module provides utilities for working with common data structures
including lists, dictionaries, and data conversion operations.
"""


def flatten_list(nested_list):
    """
    Flatten a nested list structure into a single-level list.
    
    Args:
        nested_list: A list that may contain other lists at any nesting level
        
    Returns:
        list: A flattened list containing all elements from the nested structure
        
    Raises:
        TypeError: If input is not a list or contains non-list sequences that can't be flattened
    """
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")
    
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def merge_dictionaries(*dicts):
    """
    Merge multiple dictionaries into a single dictionary.
    Later dictionaries override values from earlier ones for duplicate keys.
    
    Args:
        *dicts: Variable number of dictionary arguments to merge
        
    Returns:
        dict: A new dictionary containing all key-value pairs from input dictionaries
        
    Raises:
        TypeError: If any argument is not a dictionary
    """
    if not dicts:
        return {}
    
    for d in dicts:
        if not isinstance(d, dict):
            raise TypeError("All arguments must be dictionaries")
    
    result = {}
    for d in dicts:
        result.update(d)
    return result


def remove_duplicates_preserve_order(lst):
    """
    Remove duplicates from a list while preserving the original order.
    
    Args:
        lst (list): The input list that may contain duplicate elements
        
    Returns:
        list: A new list with duplicates removed, maintaining original order
        
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def find_common_elements(*lists):
    """
    Find elements that are common to all input lists.
    
    Args:
        *lists: Variable number of lists to find common elements from
        
    Returns:
        list: A list of elements that appear in all input lists
        
    Raises:
        TypeError: If any argument is not a list
        ValueError: If no lists are provided
    """
    if not lists:
        raise ValueError("At least one list must be provided")
    
    for lst in lists:
        if not isinstance(lst, list):
            raise TypeError("All arguments must be lists")
    
    if len(lists) == 1:
        return list(set(lists[0]))
    
    common = set(lists[0])
    for lst in lists[1:]:
        common = common.intersection(set(lst))
    
    return list(common)