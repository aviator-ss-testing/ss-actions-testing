#!/usr/bin/env python3
"""
Main entry point demonstrating various function combinations with decorators.
"""

from utils import (
    fibonacci, factorial, is_prime, reverse_string,
    capitalize_words, flatten_list, unique_elements
)
from decorators import (
    timing, retry, cache,
    validate_types, log_calls
)
from data_processing import (
    parse_json_string, validate_json, parse_csv_string,
    deep_merge, filter_keys, format_datetime
)


def demonstrate_basic_functions():
    """Demonstrate basic utility functions."""
    print("=== Basic Function Demonstrations ===")

    # String operations
    text = "hello world python programming"
    print(f"Original: {text}")
    print(f"Reversed: {reverse_string(text)}")
    print(f"Capitalized: {capitalize_words(text)}")

    # Numeric operations
    numbers = [5, 8, 13, 21]
    for n in numbers:
        print(f"Fibonacci({n}): {fibonacci(n)}")
        print(f"Factorial({n}): {factorial(n)}")
        print(f"Is {n} prime: {is_prime(n)}")

    # List operations
    nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    flat = flatten_list(nested_list)
    unique = unique_elements([1, 2, 2, 3, 3, 4])
    print(f"Flattened: {flat}")
    print(f"Unique elements: {unique}")
    print()


def demonstrate_decorated_functions():
    """Demonstrate functions with various decorators."""
    print("=== Decorated Function Demonstrations ===")

    # Timing decorator
    @timing
    def expensive_operation():
        return sum(range(10000))

    # Cached decorator
    @cache()
    def cached_fibonacci(n):
        if n <= 1:
            return n
        return cached_fibonacci(n-1) + cached_fibonacci(n-2)

    # Retry decorator
    @retry(max_attempts=3)
    def potentially_failing_function():
        import random
        if random.random() > 0.7:
            return "Success!"
        raise ValueError("Random failure")

    # Validation decorator
    @validate_types(x=int, y=str)
    def validated_function(x: int, y: str):
        return f"{y}: {x * 2}"

    # Logging decorator
    @log_calls()
    def logged_function(message):
        return f"Processed: {message}"

    print("Running timed expensive operation:")
    result = expensive_operation()
    print(f"Result: {result}")

    print("\nRunning cached fibonacci:")
    for i in [10, 15, 10]:  # 10 should be cached on second call
        print(f"Fibonacci({i}): {cached_fibonacci(i)}")

    print("\nRunning function with retry logic:")
    try:
        retry_result = potentially_failing_function()
        print(f"Retry result: {retry_result}")
    except Exception as e:
        print(f"Function failed after retries: {e}")

    print("\nRunning validated function:")
    try:
        valid_result = validated_function(42, "Answer")
        print(f"Validation result: {valid_result}")
    except Exception as e:
        print(f"Validation error: {e}")

    print("\nRunning logged function:")
    log_result = logged_function("test message")
    print(f"Logged result: {log_result}")
    print()


def demonstrate_data_processing():
    """Demonstrate data processing functions."""
    print("=== Data Processing Demonstrations ===")

    # JSON operations
    json_data = '{"name": "John", "age": 30, "skills": ["Python", "JavaScript"]}'
    parsed = parse_json_string(json_data)
    is_valid = validate_json(json_data)
    print(f"Parsed JSON: {parsed}")
    print(f"Is valid JSON: {is_valid}")

    # CSV operations
    csv_data = "name,age,city\nJohn,30,NYC\nJane,25,LA"
    parsed_csv = parse_csv_string(csv_data)
    print(f"Parsed CSV: {parsed_csv}")

    # Dictionary operations
    dict1 = {"a": 1, "b": {"c": 2}}
    dict2 = {"b": {"d": 3}, "e": 4}
    merged = deep_merge(dict1, dict2)
    filtered = filter_keys(merged, lambda k: k in ['a', 'e'])
    print(f"Deep merged: {merged}")
    print(f"Filtered keys: {filtered}")

    # DateTime operations
    from datetime import datetime
    now = datetime.now()
    formatted = format_datetime(now, "%Y-%m-%d %H:%M:%S")
    print(f"Formatted datetime: {formatted}")
    print()


def demonstrate_combined_usage():
    """Demonstrate combining multiple functions and decorators."""
    print("=== Combined Usage Demonstrations ===")

    @timing
    @cache()
    @log_calls()
    def complex_data_processor(data_list):
        """Process a list of data with multiple operations."""
        # Flatten if nested
        flat_data = flatten_list(data_list) if any(isinstance(x, list) for x in data_list) else data_list

        # Get unique elements
        unique_data = unique_elements(flat_data)

        # Process each element
        processed = []
        for item in unique_data:
            if isinstance(item, str):
                processed.append(capitalize_words(item))
            elif isinstance(item, int):
                processed.append(fibonacci(min(item, 20)))  # Limit to prevent long computation

        return processed

    # Test with mixed data
    test_data = [["hello world", 5], [8, "python programming"], [5, "data science"]]
    print("Processing complex mixed data:")
    result = complex_data_processor(test_data)
    print(f"Processed result: {result}")

    # Demonstrate decorator chaining with data processing
    @timing
    def process_json_data(json_string):
        parsed = parse_json_string(json_string)
        if isinstance(parsed, dict):
            filtered = filter_keys(parsed, lambda k: len(k) > 2)
            return filtered
        return parsed

    sample_json = '{"id": 1, "name": "test", "description": "sample data", "x": 5}'
    print("\nProcessing JSON with timing:")
    json_result = process_json_data(sample_json)
    print(f"JSON processing result: {json_result}")
    print()


def main():
    """Main function orchestrating all demonstrations."""
    print("Python Functions with Decorators - Integration Testing Demo")
    print("=" * 60)

    try:
        demonstrate_basic_functions()
        demonstrate_decorated_functions()
        demonstrate_data_processing()
        demonstrate_combined_usage()

        print("All demonstrations completed successfully!")

    except Exception as e:
        print(f"Error during demonstration: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())