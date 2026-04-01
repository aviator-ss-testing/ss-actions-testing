"""List manipulation utilities.

This module provides common list manipulation functions including
flattening nested lists, chunking, rotation, finding duplicates,
and merging sorted lists.
"""


def flatten(nested_list):
    """Flatten an arbitrarily nested list.

    Time complexity: O(n) where n is total number of elements

    Args:
        nested_list (list): The nested list to flatten

    Returns:
        list: Flattened list containing all elements

    Examples:
        >>> flatten([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten([[1, 2], [3, 4]])
        [1, 2, 3, 4]
        >>> flatten([1, 2, 3])
        [1, 2, 3]
    """
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")

    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def chunk(lst, size):
    """Split a list into fixed-size chunks.

    Time complexity: O(n) where n is the length of the list

    Args:
        lst (list): The list to chunk
        size (int): The size of each chunk

    Returns:
        list: List of chunks (each chunk is a list)

    Raises:
        ValueError: If size is less than 1

    Examples:
        >>> chunk([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
        >>> chunk([1, 2, 3, 4], 2)
        [[1, 2], [3, 4]]
        >>> chunk([1, 2, 3], 5)
        [[1, 2, 3]]
    """
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list")
    if not isinstance(size, int):
        raise TypeError("Chunk size must be an integer")
    if size < 1:
        raise ValueError("Chunk size must be at least 1")

    result = []
    for i in range(0, len(lst), size):
        result.append(lst[i:i + size])
    return result


def rotate(lst, n):
    """Rotate list elements n positions to the right.

    Time complexity: O(len(lst))

    Args:
        lst (list): The list to rotate
        n (int): Number of positions to rotate (positive = right, negative = left)

    Returns:
        list: New list with elements rotated

    Examples:
        >>> rotate([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
        >>> rotate([1, 2, 3, 4, 5], -1)
        [2, 3, 4, 5, 1]
        >>> rotate([1, 2, 3], 0)
        [1, 2, 3]
    """
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list")
    if not isinstance(n, int):
        raise TypeError("Rotation amount must be an integer")

    if len(lst) == 0:
        return []

    n = n % len(lst)
    return lst[-n:] + lst[:-n] if n != 0 else lst[:]


def find_duplicates(lst):
    """Find and return duplicate elements in a list.

    Time complexity: O(n) where n is the length of the list

    Args:
        lst (list): The list to search for duplicates

    Returns:
        list: List of duplicate elements (each duplicate appears once)

    Examples:
        >>> find_duplicates([1, 2, 3, 2, 4, 3])
        [2, 3]
        >>> find_duplicates([1, 1, 1, 2, 2])
        [1, 2]
        >>> find_duplicates([1, 2, 3])
        []
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)


def merge_sorted(list1, list2):
    """Merge two sorted lists into a single sorted list efficiently.

    Time complexity: O(n + m) where n and m are lengths of input lists

    Args:
        list1 (list): First sorted list
        list2 (list): Second sorted list

    Returns:
        list: Merged sorted list

    Examples:
        >>> merge_sorted([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge_sorted([1, 2, 3], [4, 5, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge_sorted([], [1, 2, 3])
        [1, 2, 3]
    """
    if not isinstance(list1, list):
        raise TypeError("First argument must be a list")
    if not isinstance(list2, list):
        raise TypeError("Second argument must be a list")

    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result
