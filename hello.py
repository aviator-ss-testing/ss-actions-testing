"""
Main demonstration module showcasing mathematical operations, utilities, and decorators.

This module serves as an integration point and usage example for all modules
in the Python utilities package.
"""

import math_ops
import utils
from decorators import timer, log_calls, retry, validate_types, memoize


def main():
    print("=" * 60)
    print("Python Utilities Demonstration")
    print("=" * 60)
    print()

    print("--- Mathematical Operations ---")
    print(f"Addition: 10 + 5 = {math_ops.add(10, 5)}")
    print(f"Subtraction: 10 - 5 = {math_ops.subtract(10, 5)}")
    print(f"Multiplication: 10 * 5 = {math_ops.multiply(10, 5)}")
    print(f"Division: 10 / 5 = {math_ops.divide(10, 5)}")
    print(f"Factorial of 5: {math_ops.factorial(5)}")
    print(f"Fibonacci(10): {math_ops.fibonacci(10)}")
    print(f"Is 17 prime? {math_ops.is_prime(17)}")
    print(f"GCD(48, 18) = {math_ops.gcd(48, 18)}")
    print()

    print("--- String Utilities ---")
    test_string = "Hello, World!"
    print(f"Original: '{test_string}'")
    print(f"Reversed: '{utils.reverse_string(test_string)}'")
    print(f"Is palindrome? {utils.is_palindrome(test_string)}")
    print(f"Word count: {utils.count_words(test_string)}")
    print(f"Is 'racecar' a palindrome? {utils.is_palindrome('racecar')}")
    print()

    print("--- List Processing ---")
    nested = [1, [2, 3], [4, [5, 6]]]
    print(f"Nested list: {nested}")
    print(f"Flattened: {utils.flatten_list(nested)}")
    duplicates = [1, 2, 2, 3, 3, 3, 4]
    print(f"With duplicates: {duplicates}")
    print(f"Removed duplicates: {utils.remove_duplicates(duplicates)}")
    numbers = [5, 2, 9, 1, 7]
    print(f"Numbers: {numbers}")
    print(f"Max/Min: {utils.find_max_min(numbers)}")
    print()

    print("--- Data Validation ---")
    print(f"Is 'test@example.com' valid email? {utils.is_email_valid('test@example.com')}")
    print(f"Is 'invalid.email' valid email? {utils.is_email_valid('invalid.email')}")
    print(f"Is '555-123-4567' valid phone? {utils.validate_phone_number('555-123-4567')}")
    print()

    print("--- Dictionary Operations ---")
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    print(f"Dict1: {dict1}")
    print(f"Dict2: {dict2}")
    print(f"Merged: {utils.merge_dicts(dict1, dict2)}")
    full_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
    print(f"Full dict: {full_dict}")
    print(f"Filtered by keys ['a', 'c']: {utils.filter_dict_by_keys(full_dict, ['a', 'c'])}")
    print()

    print("=" * 60)
    print("Decorator Demonstrations")
    print("=" * 60)
    print()

    print("--- Timer Decorator ---")
    @timer
    def slow_calculation(n):
        """Calculate sum of squares up to n."""
        return sum(i**2 for i in range(n))

    result = slow_calculation(10000)
    print(f"Result: {result}")
    print()

    print("--- Logging Decorator ---")
    @log_calls
    def greet(name, greeting="Hello"):
        """Return a greeting message."""
        return f"{greeting}, {name}!"

    message = greet("World")
    print(f"Message: {message}")
    print()

    print("--- Memoization Decorator ---")
    @memoize
    def fibonacci_memo(n):
        """Calculate Fibonacci with memoization."""
        if n <= 1:
            return n
        return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

    print("First call (cache miss):")
    fibonacci_memo(5)
    print("Second call (cache hit):")
    fibonacci_memo(5)
    print()

    print("--- Type Validation Decorator ---")
    @validate_types(x=int, y=int)
    def add_integers(x, y):
        """Add two integers."""
        return x + y

    try:
        print(f"add_integers(5, 3) = {add_integers(5, 3)}")
        print("Attempting with wrong types:")
        add_integers(5, "3")
    except TypeError as e:
        print(f"Type error caught: {e}")
    print()

    print("--- Retry Decorator ---")
    attempt_counter = {"count": 0}

    @retry(max_attempts=3, delay=0.5)
    def flaky_function():
        """Function that fails twice then succeeds."""
        attempt_counter["count"] += 1
        if attempt_counter["count"] < 3:
            raise ValueError(f"Simulated failure {attempt_counter['count']}")
        return "Success!"

    try:
        result = flaky_function()
        print(f"Function result: {result}")
    except Exception as e:
        print(f"Function failed: {e}")
    print()

    print("=" * 60)
    print("Demonstration Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
