import re
import datetime
import os
from pathlib import Path
from typing import List, Tuple, Any, Union
from collections import Counter


# String manipulation functions
def reverse_string(s: str) -> str:
    """Return the reverse of the input string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (ignoring case and spaces)."""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    """Count the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


# List/data manipulation functions
def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Flatten a nested list of any depth."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def remove_duplicates(lst: List[Any]) -> List[Any]:
    """Remove duplicates from a list while preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def find_max_min(lst: List[Union[int, float]]) -> Tuple[Union[int, float], Union[int, float]]:
    """Find the maximum and minimum values in a list of numbers."""
    if not lst:
        raise ValueError("Cannot find max/min of empty list")
    return max(lst), min(lst)


# Validation utilities
def is_email_valid(email: str) -> bool:
    """Validate email address using regex pattern."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_phone_valid(phone: str) -> bool:
    """Validate phone number using regex pattern (supports US format)."""
    pattern = r'^\+?1?[-.\s]?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})$'
    return re.match(pattern, phone) is not None


# Date/time utilities
def days_between(date1: datetime.date, date2: datetime.date) -> int:
    """Calculate the number of days between two dates."""
    return abs((date2 - date1).days)


def format_date(date: datetime.date, format_string: str = "%Y-%m-%d") -> str:
    """Format a date according to the specified format string."""
    return date.strftime(format_string)


def is_weekend(date: datetime.date) -> bool:
    """Check if a given date falls on a weekend (Saturday or Sunday)."""
    return date.weekday() >= 5


# File/path utilities
def get_file_extension(filename: str) -> str:
    """Extract the file extension from a filename."""
    path = Path(filename)
    return path.suffix.lower()


def create_directory_if_not_exists(directory_path: str) -> bool:
    """Create a directory if it doesn't exist. Returns True if created, False if already exists."""
    try:
        os.makedirs(directory_path, exist_ok=True)
        return not os.path.exists(directory_path)
    except OSError as e:
        raise OSError(f"Failed to create directory {directory_path}: {e}")