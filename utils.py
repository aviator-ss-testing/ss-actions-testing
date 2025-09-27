"""
Utility Functions Module

This module provides various utility functions for string manipulation,
data processing, and common programming tasks.
"""

from typing import List, Dict, Any, Tuple, Union
import re


def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Args:
        s: The string to reverse

    Returns:
        The reversed string
    """
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    Ignores case and non-alphanumeric characters.

    Args:
        s: The string to check

    Returns:
        True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]


def count_words(s: str) -> int:
    """
    Count the number of words in a string.

    Args:
        s: The string to count words in

    Returns:
        The number of words in the string
    """
    if not s or not s.strip():
        return 0
    return len(s.split())


def flatten_list(nested_list: List[Any]) -> List[Any]:
    """
    Flatten a nested list structure into a single-level list.

    Args:
        nested_list: The nested list to flatten

    Returns:
        A flattened list containing all elements
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def remove_duplicates(lst: List[Any]) -> List[Any]:
    """
    Remove duplicates from a list while preserving order.

    Args:
        lst: The list to remove duplicates from

    Returns:
        A new list with duplicates removed
    """
    seen = set()
    result = []
    for item in lst:
        # Handle unhashable types by using their string representation
        try:
            if item not in seen:
                seen.add(item)
                result.append(item)
        except TypeError:
            # For unhashable types, check manually
            if item not in result:
                result.append(item)
    return result


def find_max_min(lst: List[Union[int, float]]) -> Tuple[Union[int, float], Union[int, float]]:
    """
    Find the maximum and minimum values in a list of numbers.

    Args:
        lst: The list of numbers to analyze

    Returns:
        A tuple containing (max_value, min_value)

    Raises:
        ValueError: If the list is empty
    """
    if not lst:
        raise ValueError("Cannot find max/min of empty list")

    return max(lst), min(lst)


def is_email_valid(email: str) -> bool:
    """
    Validate if an email address has a basic valid format.

    Args:
        email: The email address to validate

    Returns:
        True if the email format is valid, False otherwise
    """
    # Basic email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone_number(phone: str) -> bool:
    """
    Validate if a phone number has a basic valid format.
    Accepts various common phone number formats.

    Args:
        phone: The phone number to validate

    Returns:
        True if the phone number format is valid, False otherwise
    """
    # Remove all non-digit characters for validation
    digits_only = re.sub(r'[^\d]', '', phone)

    # Check if it has 10 or 11 digits (US format)
    if len(digits_only) == 10:
        return True
    elif len(digits_only) == 11 and digits_only[0] == '1':
        return True

    return False


def merge_dicts(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Merge two dictionaries. Values from dict2 override values from dict1.

    Args:
        dict1: The first dictionary
        dict2: The second dictionary (takes precedence)

    Returns:
        A new dictionary containing merged key-value pairs
    """
    result = dict1.copy()
    result.update(dict2)
    return result


def filter_dict_by_keys(dictionary: Dict[Any, Any], keys: List[Any]) -> Dict[Any, Any]:
    """
    Filter a dictionary to only include specified keys.

    Args:
        dictionary: The dictionary to filter
        keys: List of keys to include in the filtered dictionary

    Returns:
        A new dictionary containing only the specified keys
    """
    return {key: dictionary[key] for key in keys if key in dictionary}