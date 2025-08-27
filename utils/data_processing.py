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


def csv_string_to_dict(csv_string, headers):
    """
    Parse a CSV string into a list of dictionaries using provided headers.
    
    Args:
        csv_string (str): CSV formatted string with rows separated by newlines
        headers (list): List of column headers to use as dictionary keys
        
    Returns:
        list: List of dictionaries, each representing a row from the CSV
        
    Raises:
        TypeError: If csv_string is not a string or headers is not a list
        ValueError: If CSV data doesn't match number of headers
    """
    if not isinstance(csv_string, str):
        raise TypeError("csv_string must be a string")
    if not isinstance(headers, list):
        raise TypeError("headers must be a list")
    
    if not csv_string.strip():
        return []
    
    lines = csv_string.strip().split('\n')
    result = []
    
    for line_num, line in enumerate(lines, 1):
        # Split by comma and strip whitespace
        values = [val.strip() for val in line.split(',')]
        
        if len(values) != len(headers):
            raise ValueError(f"Line {line_num} has {len(values)} values but {len(headers)} headers provided")
        
        row_dict = dict(zip(headers, values))
        result.append(row_dict)
    
    return result


def dict_to_csv_string(data, headers):
    """
    Convert a list of dictionaries to CSV string format.
    
    Args:
        data (list): List of dictionaries to convert to CSV
        headers (list): List of headers/keys to include in CSV output
        
    Returns:
        str: CSV formatted string with data rows
        
    Raises:
        TypeError: If data is not a list or headers is not a list
        ValueError: If data contains non-dictionary items
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")
    if not isinstance(headers, list):
        raise TypeError("headers must be a list")
    
    if not data:
        return ""
    
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("All items in data must be dictionaries")
    
    result = []
    for row_dict in data:
        row_values = []
        for header in headers:
            value = row_dict.get(header, "")
            row_values.append(str(value))
        result.append(",".join(row_values))
    
    return "\n".join(result)


def normalize_data(data, min_val=0, max_val=1):
    """
    Normalize numerical data to a specified range.
    
    Args:
        data (list): List of numerical values to normalize
        min_val (float): Minimum value of the normalized range (default: 0)
        max_val (float): Maximum value of the normalized range (default: 1)
        
    Returns:
        list: List of normalized values within the specified range
        
    Raises:
        TypeError: If data is not a list or contains non-numeric values
        ValueError: If min_val >= max_val or data is empty
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")
    
    if not data:
        raise ValueError("data cannot be empty")
    
    if min_val >= max_val:
        raise ValueError("min_val must be less than max_val")
    
    # Check if all values are numeric
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("All items in data must be numeric")
    
    data_min = min(data)
    data_max = max(data)
    
    # Handle case where all values are the same
    if data_min == data_max:
        return [min_val] * len(data)
    
    # Normalize to [min_val, max_val] range
    normalized = []
    for value in data:
        normalized_value = min_val + (value - data_min) * (max_val - min_val) / (data_max - data_min)
        normalized.append(normalized_value)
    
    return normalized


def chunk_list(lst, chunk_size):
    """
    Split a list into smaller chunks of specified size.
    
    Args:
        lst (list): The list to be chunked
        chunk_size (int): Size of each chunk (must be positive)
        
    Returns:
        list: List of lists, each containing chunk_size elements (last chunk may be smaller)
        
    Raises:
        TypeError: If lst is not a list or chunk_size is not an integer
        ValueError: If chunk_size is not positive
    """
    if not isinstance(lst, list):
        raise TypeError("lst must be a list")
    if not isinstance(chunk_size, int):
        raise TypeError("chunk_size must be an integer")
    
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    
    if not lst:
        return []
    
    chunks = []
    for i in range(0, len(lst), chunk_size):
        chunks.append(lst[i:i + chunk_size])
    
    return chunks