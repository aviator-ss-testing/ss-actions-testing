"""
Statistical operations module for mathematical calculations.

This module provides functions for common statistical operations including
measures of central tendency and variability.
"""
from typing import List, Union
import math
from collections import Counter


def _validate_numbers(numbers: List[Union[int, float]]) -> None:
    """
    Validate that the input is a non-empty list of numeric values.

    Args:
        numbers: List of numbers to validate

    Raises:
        ValueError: If list is empty or contains non-numeric values
        TypeError: If input is not a list
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if len(numbers) == 0:
        raise ValueError("Cannot perform statistical operations on empty list")

    for i, num in enumerate(numbers):
        if not isinstance(num, (int, float)):
            raise ValueError(f"All elements must be numeric. Found {type(num).__name__} at index {i}")


def mean(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the arithmetic mean (average) of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        float: The arithmetic mean of the numbers

    Raises:
        ValueError: If list is empty or contains non-numeric values
        TypeError: If input is not a list
    """
    _validate_numbers(numbers)
    return sum(numbers) / len(numbers)


def median(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Find the median (middle value) of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        Union[int, float]: The median value

    Raises:
        ValueError: If list is empty or contains non-numeric values
        TypeError: If input is not a list
    """
    _validate_numbers(numbers)
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        # Odd number of elements, return middle element
        return sorted_numbers[n // 2]
    else:
        # Even number of elements, return average of two middle elements
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2


def mode(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Find the mode (most frequent value) of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        Union[int, float]: The most frequent value

    Raises:
        ValueError: If list is empty, contains non-numeric values, or has no unique mode
        TypeError: If input is not a list
    """
    _validate_numbers(numbers)

    # Count frequencies of each number
    counter = Counter(numbers)
    max_count = max(counter.values())

    # Find all numbers with maximum frequency
    modes = [num for num, count in counter.items() if count == max_count]

    if len(modes) > 1:
        raise ValueError("No unique mode found - multiple values have the same highest frequency")

    return modes[0]


def standard_deviation(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the population standard deviation of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        float: The population standard deviation

    Raises:
        ValueError: If list is empty or contains non-numeric values
        TypeError: If input is not a list
    """
    _validate_numbers(numbers)

    # Calculate mean
    mean_value = mean(numbers)

    # Calculate squared differences from mean
    squared_diffs = [(x - mean_value) ** 2 for x in numbers]

    # Calculate variance (population variance, not sample)
    variance = sum(squared_diffs) / len(numbers)

    # Return standard deviation (square root of variance)
    return math.sqrt(variance)