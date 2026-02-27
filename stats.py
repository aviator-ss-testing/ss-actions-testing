"""Basic descriptive statistics using only the Python standard library."""

import math
from collections import Counter


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("mean requires at least one value")
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    if not values:
        raise ValueError("median requires at least one value")
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 1:
        return sorted_values[mid]
    return (sorted_values[mid - 1] + sorted_values[mid]) / 2


def mode(values: list[float]) -> float:
    if not values:
        raise ValueError("mode requires at least one value")
    counts = Counter(values)
    max_count = max(counts.values())
    candidates = [v for v, c in counts.items() if c == max_count]
    return min(candidates)


def stdev(values: list[float]) -> float:
    if len(values) < 2:
        raise ValueError("stdev requires at least two values")
    m = mean(values)
    variance = sum((x - m) ** 2 for x in values) / (len(values) - 1)
    return math.sqrt(variance)
