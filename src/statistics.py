"""
Statistics utilities module providing common statistical functions.

This module contains functions for calculating various statistical measures
on lists of numbers with appropriate error handling and input validation.
"""

import math
from typing import List, Union, Tuple
from collections import Counter


def mean(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers: List of numbers to calculate mean for

    Returns:
        float: The arithmetic mean

    Raises:
        ValueError: If the list is empty
        TypeError: If the list contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All values must be numeric")

    return sum(numbers) / len(numbers)


def median(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the median of a list of numbers.

    Args:
        numbers: List of numbers to calculate median for

    Returns:
        float: The median value

    Raises:
        ValueError: If the list is empty
        TypeError: If the list contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All values must be numeric")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        # Even number of elements - return average of middle two
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        # Odd number of elements - return middle element
        return float(sorted_numbers[n // 2])


def mode(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Calculate the mode(s) of a list of numbers.

    Args:
        numbers: List of numbers to calculate mode for

    Returns:
        List: List of mode values (can be multiple if there's a tie)

    Raises:
        ValueError: If the list is empty
        TypeError: If the list contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All values must be numeric")

    counts = Counter(numbers)
    max_count = max(counts.values())

    return [value for value, count in counts.items() if count == max_count]


def standard_deviation(numbers: List[Union[int, float]], sample: bool = False) -> float:
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        numbers: List of numbers to calculate standard deviation for
        sample: If True, calculate sample standard deviation (n-1). If False, population (n)

    Returns:
        float: The standard deviation

    Raises:
        ValueError: If the list is empty or has only one element when sample=True
        TypeError: If the list contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of empty list")

    if sample and len(numbers) < 2:
        raise ValueError("Sample standard deviation requires at least 2 values")

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All values must be numeric")

    mean_val = mean(numbers)
    squared_diffs = [(x - mean_val) ** 2 for x in numbers]

    divisor = len(numbers) - 1 if sample else len(numbers)
    variance_val = sum(squared_diffs) / divisor

    return math.sqrt(variance_val)


def variance(numbers: List[Union[int, float]], sample: bool = False) -> float:
    """
    Calculate the variance of a list of numbers.

    Args:
        numbers: List of numbers to calculate variance for
        sample: If True, calculate sample variance (n-1). If False, population (n)

    Returns:
        float: The variance

    Raises:
        ValueError: If the list is empty or has only one element when sample=True
        TypeError: If the list contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate variance of empty list")

    if sample and len(numbers) < 2:
        raise ValueError("Sample variance requires at least 2 values")

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All values must be numeric")

    mean_val = mean(numbers)
    squared_diffs = [(x - mean_val) ** 2 for x in numbers]

    divisor = len(numbers) - 1 if sample else len(numbers)
    return sum(squared_diffs) / divisor


def min_max(numbers: List[Union[int, float]]) -> Tuple[Union[int, float], Union[int, float]]:
    """
    Find the minimum and maximum values in a list of numbers.

    Args:
        numbers: List of numbers to find min/max for

    Returns:
        Tuple: (minimum, maximum) values

    Raises:
        ValueError: If the list is empty
        TypeError: If the list contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot find min/max of empty list")

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All values must be numeric")

    return (min(numbers), max(numbers))


def range_calc(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculate the range (max - min) of a list of numbers.

    Args:
        numbers: List of numbers to calculate range for

    Returns:
        Union[int, float]: The range value

    Raises:
        ValueError: If the list is empty
        TypeError: If the list contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate range of empty list")

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All values must be numeric")

    min_val, max_val = min_max(numbers)
    return max_val - min_val


def percentile(numbers: List[Union[int, float]], p: Union[int, float]) -> float:
    """
    Calculate the p-th percentile of a list of numbers.

    Args:
        numbers: List of numbers to calculate percentile for
        p: Percentile to calculate (0-100)

    Returns:
        float: The percentile value

    Raises:
        ValueError: If the list is empty or percentile is not between 0-100
        TypeError: If the list contains non-numeric values or p is not numeric
    """
    if not numbers:
        raise ValueError("Cannot calculate percentile of empty list")

    if not isinstance(p, (int, float)):
        raise TypeError("Percentile must be numeric")

    if not 0 <= p <= 100:
        raise ValueError("Percentile must be between 0 and 100")

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All values must be numeric")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    # Handle edge cases
    if p == 0:
        return float(sorted_numbers[0])
    if p == 100:
        return float(sorted_numbers[-1])

    # Calculate index using the standard formula
    index = (p / 100) * (n - 1)

    # If index is a whole number, return that element
    if index.is_integer():
        return float(sorted_numbers[int(index)])

    # Otherwise, interpolate between the two nearest elements
    lower_index = int(index)
    upper_index = lower_index + 1
    fraction = index - lower_index

    lower_value = sorted_numbers[lower_index]
    upper_value = sorted_numbers[upper_index]

    return lower_value + fraction * (upper_value - lower_value)