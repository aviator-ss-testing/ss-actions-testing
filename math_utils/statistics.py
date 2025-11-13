from typing import List
from collections import Counter
from .operations import memoize


def mean(values: List[float]) -> float:
    """Calculate the average of a list of numbers."""
    if not values:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(values) / len(values)


def median(values: List[float]) -> float:
    """Calculate the middle value of a sorted list."""
    if not values:
        raise ValueError("Cannot calculate median of an empty list")
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    return sorted_values[mid]


def mode(values: List[float]) -> float:
    """Calculate the most frequent value in a list."""
    if not values:
        raise ValueError("Cannot calculate mode of an empty list")
    counter = Counter(values)
    max_count = max(counter.values())
    modes = [val for val, count in counter.items() if count == max_count]
    return modes[0]


@memoize
def variance(values: tuple) -> float:
    """Calculate the variance of a list of numbers."""
    if not values:
        raise ValueError("Cannot calculate variance of an empty list")
    values_list = list(values)
    avg = mean(values_list)
    return sum((x - avg) ** 2 for x in values_list) / len(values_list)


@memoize
def standard_deviation(values: tuple) -> float:
    """Calculate the standard deviation with memoization."""
    if not values:
        raise ValueError("Cannot calculate standard deviation of an empty list")
    return variance(values) ** 0.5
