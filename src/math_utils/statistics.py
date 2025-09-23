"""
Statistical utilities module.

This module provides statistical calculation functions including mean, median,
mode, and standard deviation with proper input validation and error handling.
"""

from typing import List, Union
from collections import Counter
import math

Number = Union[int, float]


def _validate_numbers(numbers: List[Number]) -> None:
    """Validate input list for statistical calculations.

    Args:
        numbers: List of numbers to validate

    Raises:
        ValueError: If list is empty or contains non-numeric values
        TypeError: If input is not a list
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if len(numbers) == 0:
        raise ValueError("Cannot calculate statistics for empty list")

    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError(f"All elements must be numeric, found: {type(num).__name__}")


def mean(numbers: List[Number]) -> float:
    """Calculate the arithmetic mean (average) of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        The arithmetic mean as a float

    Raises:
        ValueError: If list is empty or contains non-numeric values
        TypeError: If input is not a list
    """
    _validate_numbers(numbers)
    return sum(numbers) / len(numbers)


def median(numbers: List[Number]) -> Union[int, float]:
    """Find the median (middle value) of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        The median value. Returns int if all inputs are int and result is whole number,
        otherwise returns float

    Raises:
        ValueError: If list is empty or contains non-numeric values
        TypeError: If input is not a list
    """
    _validate_numbers(numbers)
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        # Even number of elements - average of two middle values
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        result = (mid1 + mid2) / 2

        # Return int if result is a whole number and all inputs were int
        if result.is_integer() and all(isinstance(x, int) for x in numbers):
            return int(result)
        return result
    else:
        # Odd number of elements - return middle value
        return sorted_numbers[n // 2]


def mode(numbers: List[Number]) -> List[Number]:
    """Find the mode (most frequently occurring value(s)) in a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        List of the most frequent value(s). Returns list even for single mode.

    Raises:
        ValueError: If list is empty or contains non-numeric values
        TypeError: If input is not a list
    """
    _validate_numbers(numbers)

    # Count frequency of each number
    counter = Counter(numbers)
    max_count = max(counter.values())

    # Find all numbers with the maximum frequency
    modes = [num for num, count in counter.items() if count == max_count]

    # Sort the modes for consistent output
    return sorted(modes)


def standard_deviation(numbers: List[Number]) -> float:
    """Calculate the population standard deviation of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        The population standard deviation as a float

    Raises:
        ValueError: If list is empty or contains non-numeric values
        TypeError: If input is not a list
    """
    _validate_numbers(numbers)

    if len(numbers) == 1:
        return 0.0

    # Calculate mean
    avg = mean(numbers)

    # Calculate variance (average of squared differences from mean)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)

    # Standard deviation is square root of variance
    return math.sqrt(variance)