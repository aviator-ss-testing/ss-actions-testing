"""List operation utility helpers."""


def chunk(items: list, size: int) -> list[list]:
    """Split items into consecutive chunks of length size (last chunk may be shorter)."""
    if size < 1:
        raise ValueError("size must be >= 1")
    return [items[i : i + size] for i in range(0, len(items), size)]


def dedupe(items: list) -> list:
    """Return items with duplicates removed, preserving first-seen order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def flatten_one_level(items: list) -> list:
    """Flatten one level of nesting from a list of lists."""
    return [x for sub in items for x in sub]
