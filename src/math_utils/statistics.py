"""
Statistical operations module for mathematical calculations.

This module provides functions for common statistical operations including
measures of central tendency and variability.
"""
from typing import List, Union
import math
from collections import Counter



def mean(x: List[Union[int, float]]) -> float:
    """
    Calculate the arithmetic mean (average) of a list of numbers.

    Args:
        x: List of numeric values

    Returns:
        float: The arithmetic mean of the numbers
    """
    return sum(x) / len(x)


def median(x: List[Union[int, float]]) -> Union[int, float]:
    """
    Find the median (middle value) of a list of numbers.

    Args:
        x: List of numeric values

    Returns:
        Union[int, float]: The median value
    """
    sorted_x = sorted(x)
    n = len(sorted_x)

    if n % 2 == 1:
        # Odd number of elements, return middle element
        return sorted_x[n // 2]
    else:
        # Even number of elements, return average of two middle elements
        mid1 = sorted_x[n // 2 - 1]
        mid2 = sorted_x[n // 2]
        return (mid1 + mid2) / 2


def mode(x: List[Union[int, float]]) -> Union[int, float]:
    """
    Find the mode (most frequent value) of a list of numbers.

    Args:
        x: List of numeric values

    Returns:
        Union[int, float]: The most frequent value

    Raises:
        ValueError: If has no unique mode
    """
    # Count frequencies of each number
    counter = Counter(x)
    max_count = max(counter.values())

    # Find all numbers with maximum frequency
    modes = [num for num, count in counter.items() if count == max_count]

    if len(modes) > 1:
        raise ValueError("No unique mode found - multiple values have the same highest frequency")

    return modes[0]


def standard_deviation(x: List[Union[int, float]]) -> float:
    """
    Calculate the population standard deviation of a list of numbers.

    Args:
        x: List of numeric values

    Returns:
        float: The population standard deviation
    """
    # Calculate mean
    mean_value = mean(x)

    # Calculate squared differences from mean
    squared_diffs = [(num - mean_value) ** 2 for num in x]

    # Calculate variance (population variance, not sample)
    variance = sum(squared_diffs) / len(x)

    # Return standard deviation (square root of variance)
    return math.sqrt(variance)