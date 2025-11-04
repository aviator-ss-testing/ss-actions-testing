import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"{func.__name__} executed in {elapsed:.6f} seconds")
        return result
    return wrapper


def flatten(nested_list):
    if not isinstance(nested_list, list):
        raise TypeError(f"flatten requires a list, got {type(nested_list).__name__}")

    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def chunk(lst, size):
    if not isinstance(lst, list):
        raise TypeError(f"chunk requires a list, got {type(lst).__name__}")
    if not isinstance(size, int):
        raise TypeError(f"chunk size must be an integer, got {type(size).__name__}")
    if size <= 0:
        raise ValueError(f"chunk size must be positive, got {size}")

    result = []
    for i in range(0, len(lst), size):
        result.append(lst[i:i + size])
    return result


def unique_elements(lst):
    if not isinstance(lst, list):
        raise TypeError(f"unique_elements requires a list, got {type(lst).__name__}")

    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def running_average(numbers):
    if not isinstance(numbers, list):
        raise TypeError(f"running_average requires a list, got {type(numbers).__name__}")

    if not numbers:
        return []

    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError(f"All elements must be numbers, got {type(num).__name__}")

    result = []
    cumsum = 0
    for i, num in enumerate(numbers, 1):
        cumsum += num
        result.append(cumsum / i)
    return result
