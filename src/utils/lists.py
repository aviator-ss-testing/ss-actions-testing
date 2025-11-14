def find_max(numbers: list) -> int | float:
    """Find and return the maximum value in a list of numbers."""
    if not numbers:
        raise ValueError("Cannot find max of empty list")
    return max(numbers)


def filter_evens(numbers: list) -> list:
    """Filter and return only even numbers from the input list."""
    return [n for n in numbers if n % 2 == 0]


def deduplicate(items: list) -> list:
    """Remove duplicates from list while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
