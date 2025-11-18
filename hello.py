"""
Demo script showcasing the utility functions.

This script demonstrates the various utility functions available in the utils package,
including string manipulation, data processing, and mathematical operations.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from utils import (
    reverse_string,
    is_palindrome,
    title_case,
    count_words,
    flatten_list,
    remove_duplicates,
    fibonacci,
    is_prime,
)


def main():
    print("=" * 60)
    print("Welcome to Python Utilities Demo!")
    print("=" * 60)
    print()

    print("--- String Utilities ---")
    message = "Hello, Aviator!"
    print(f"Original: {message}")
    print(f"Reversed: {reverse_string(message)}")
    print(f"Title case: {title_case('hello aviator from python utilities')}")
    print(f"Is palindrome: {is_palindrome('racecar')}")
    print(f"Word count: {count_words(message)}")
    print()

    print("--- Data Processing Utilities ---")
    nested_data = [[1, 2], [3, [4, 5]], 6]
    print(f"Nested list: {nested_data}")
    print(f"Flattened: {flatten_list(nested_data)}")

    duplicates = [1, 2, 2, 3, 3, 3, 4]
    print(f"With duplicates: {duplicates}")
    print(f"Deduplicated: {remove_duplicates(duplicates)}")
    print()

    print("--- Mathematical Utilities ---")
    print("Fibonacci sequence (first 10):", [fibonacci(n) for n in range(10)])
    print("Prime numbers up to 20:", [n for n in range(20) if is_prime(n)])
    print()

    print("=" * 60)
    print("All utilities working correctly!")
    print("=" * 60)


if __name__ == "__main__":
    main()
