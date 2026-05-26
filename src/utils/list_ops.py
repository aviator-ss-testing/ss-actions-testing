def chunk_list(lst, size):
    """
    Split a list into chunks of specified size.

    Args:
        lst: List to be chunked
        size: Size of each chunk (must be positive integer)

    Returns:
        List of lists, where each sublist has at most 'size' elements

    Raises:
        TypeError: If lst is not a list or size is not an integer
        ValueError: If size is not positive
    """
    if not isinstance(lst, list):
        raise TypeError(f"chunk_list() first argument must be a list, not {type(lst).__name__}")

    if not isinstance(size, int):
        raise TypeError(f"chunk_list() size must be an integer, not {type(size).__name__}")

    if size <= 0:
        raise ValueError("chunk_list() size must be positive")

    if not lst:
        return []

    chunks = []
    for i in range(0, len(lst), size):
        chunks.append(lst[i:i + size])

    return chunks


def flatten(nested_list):
    """
    Flatten a nested list structure into a single-level list.

    Args:
        nested_list: A list that may contain nested lists at any depth

    Returns:
        A flattened list containing all elements

    Raises:
        TypeError: If nested_list is not a list
    """
    if not isinstance(nested_list, list):
        raise TypeError(f"flatten() argument must be a list, not {type(nested_list).__name__}")

    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


def find_duplicates(lst):
    """
    Find all duplicate elements in a list.

    Args:
        lst: List to search for duplicates

    Returns:
        List of elements that appear more than once (unique duplicates, order preserved)

    Raises:
        TypeError: If lst is not a list
    """
    if not isinstance(lst, list):
        raise TypeError(f"find_duplicates() argument must be a list, not {type(lst).__name__}")

    seen = set()
    duplicates = []

    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)

    return duplicates


def rotate_list(lst, positions):
    """
    Rotate list elements by specified number of positions.

    Positive positions rotate right, negative rotate left.

    Args:
        lst: List to be rotated
        positions: Number of positions to rotate (can be negative)

    Returns:
        New list with elements rotated

    Raises:
        TypeError: If lst is not a list or positions is not an integer
    """
    if not isinstance(lst, list):
        raise TypeError(f"rotate_list() first argument must be a list, not {type(lst).__name__}")

    if not isinstance(positions, int):
        raise TypeError(f"rotate_list() positions must be an integer, not {type(positions).__name__}")

    if not lst:
        return []

    positions = positions % len(lst)

    return lst[-positions:] + lst[:-positions] if positions else lst[:]


def list_stats(lst):
    """
    Calculate statistical measures for a numeric list.

    Args:
        lst: List of numeric values

    Returns:
        Dictionary with keys: 'min', 'max', 'mean', 'median'

    Raises:
        TypeError: If lst is not a list or contains non-numeric values
        ValueError: If lst is empty
    """
    if not isinstance(lst, list):
        raise TypeError(f"list_stats() argument must be a list, not {type(lst).__name__}")

    if not lst:
        raise ValueError("list_stats() cannot calculate statistics for empty list")

    for item in lst:
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise TypeError(f"list_stats() requires numeric values, found {type(item).__name__}")

    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    min_val = sorted_lst[0]
    max_val = sorted_lst[-1]
    mean_val = sum(lst) / n

    if n % 2 == 0:
        median_val = (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        median_val = sorted_lst[n // 2]

    return {
        'min': min_val,
        'max': max_val,
        'mean': mean_val,
        'median': median_val
    }
