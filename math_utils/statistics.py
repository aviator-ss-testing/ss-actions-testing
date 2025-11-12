"""
Statistics utility functions for common statistical calculations.

This module provides statistical functions operating on lists of numbers:
- Mean (average) calculation
- Median (middle value) calculation
- Mode (most common value) calculation
- Variance and standard deviation
"""


def mean(numbers):
    """
    Calculate the arithmetic mean (average) of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        The arithmetic mean of the numbers

    Raises:
        ValueError: If the list is empty

    Examples:
        >>> mean([1, 2, 3, 4, 5])
        3.0
        >>> mean([10, 20])
        15.0
        >>> mean([5])
        5.0
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")

    return sum(numbers) / len(numbers)


def median(numbers):
    """
    Calculate the median (middle value) of a list of numbers.

    Handles both odd and even length lists. For even length lists,
    returns the average of the two middle values.

    Args:
        numbers: List of numeric values

    Returns:
        The median value

    Raises:
        ValueError: If the list is empty

    Examples:
        >>> median([1, 2, 3, 4, 5])
        3
        >>> median([1, 2, 3, 4])
        2.5
        >>> median([5])
        5
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2


def mode(numbers):
    """
    Find the most common value (mode) in a list of numbers.

    If multiple values appear with the same highest frequency,
    returns a list of all modes. If all values appear once,
    returns all values as modes.

    Args:
        numbers: List of numeric values

    Returns:
        A list of the most common value(s)

    Raises:
        ValueError: If the list is empty

    Examples:
        >>> mode([1, 2, 2, 3, 3, 3])
        [3]
        >>> mode([1, 1, 2, 2, 3])
        [1, 2]
        >>> mode([1, 2, 3])
        [1, 2, 3]
    """
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")

    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_frequency = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_frequency]

    return sorted(modes)


def variance(numbers):
    """
    Calculate the variance of a list of numbers.

    Uses the population variance formula: sum((x - mean)²) / n

    Args:
        numbers: List of numeric values

    Returns:
        The variance of the numbers

    Raises:
        ValueError: If the list is empty

    Examples:
        >>> variance([1, 2, 3, 4, 5])
        2.0
        >>> variance([2, 4, 6, 8, 10])
        8.0
    """
    if not numbers:
        raise ValueError("Cannot calculate variance of empty list")

    avg = mean(numbers)
    squared_diffs = [(x - avg) ** 2 for x in numbers]
    return sum(squared_diffs) / len(numbers)


def standard_deviation(numbers):
    """
    Calculate the standard deviation of a list of numbers.

    Standard deviation is the square root of variance.

    Args:
        numbers: List of numeric values

    Returns:
        The standard deviation of the numbers

    Raises:
        ValueError: If the list is empty

    Examples:
        >>> standard_deviation([1, 2, 3, 4, 5])
        1.4142135623730951
        >>> standard_deviation([2, 4, 6, 8, 10])
        2.8284271247461903
    """
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of empty list")

    return variance(numbers) ** 0.5
