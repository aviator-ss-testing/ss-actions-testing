"""
Statistical utility functions module.

This module provides simple statistical functions for lists of numbers including
mean, median, mode, variance, and standard deviation calculations.
"""


def mean(numbers):
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        Arithmetic mean of the numbers

    Raises:
        ValueError: If list is empty or contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")

    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be numeric")

    return sum(numbers) / len(numbers)


def median(numbers):
    """
    Find the median value of a list of numbers.

    Handles both odd and even length lists. For even length lists,
    returns the average of the two middle values.

    Args:
        numbers: List of numeric values

    Returns:
        Median value

    Raises:
        ValueError: If list is empty or contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")

    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be numeric")

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
    Find the most frequent value in a list of numbers.

    If multiple values have the same highest frequency, returns one of them.
    If all values are unique, returns the first value.

    Args:
        numbers: List of numeric values

    Returns:
        Most frequent value

    Raises:
        ValueError: If list is empty or contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")

    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be numeric")

    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_frequency = max(frequency.values())
    for num, freq in frequency.items():
        if freq == max_frequency:
            return num


def variance(numbers):
    """
    Calculate the population variance of a list of numbers.

    Variance is the average of the squared differences from the mean.

    Args:
        numbers: List of numeric values

    Returns:
        Population variance

    Raises:
        ValueError: If list is empty or contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate variance of empty list")

    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be numeric")

    avg = mean(numbers)
    squared_diffs = [(x - avg) ** 2 for x in numbers]
    return sum(squared_diffs) / len(numbers)


def std_dev(numbers):
    """
    Calculate the standard deviation of a list of numbers.

    Standard deviation is the square root of the variance.

    Args:
        numbers: List of numeric values

    Returns:
        Standard deviation

    Raises:
        ValueError: If list is empty or contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of empty list")

    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be numeric")

    return variance(numbers) ** 0.5
