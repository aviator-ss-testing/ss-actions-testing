#!/usr/bin/env python3
"""
Examples demonstrating how to use utility functions in integration scenarios.

This module provides practical examples of:
- Individual function usage
- Function chaining and composition
- Error handling patterns
- Sample data processing workflows
- Real-world integration testing scenarios

Note: This assumes the utility functions are implemented in hello.py
"""

import json
import tempfile
import os
from pathlib import Path


def demonstrate_math_functions():
    """Examples of mathematical function usage."""
    print("=== Mathematical Functions Examples ===")

    # Note: These would import from hello.py once implemented
    # from hello import calculate_factorial, is_prime_number, fibonacci_sequence

    print("1. Factorial calculations:")
    test_values = [0, 1, 5, 10]
    for val in test_values:
        # result = calculate_factorial(val)
        print(f"   factorial({val}) = {val}! (would calculate actual result)")

    print("\n2. Prime number checking:")
    test_numbers = [2, 4, 17, 25, 97]
    for num in test_numbers:
        # is_prime = is_prime_number(num)
        print(f"   is_prime({num}) = {'Prime' if num in [2, 17, 97] else 'Not Prime'}")

    print("\n3. Fibonacci sequence generation:")
    lengths = [5, 8, 10]
    for length in lengths:
        # sequence = fibonacci_sequence(length)
        print(f"   fibonacci({length}) = [0, 1, 1, 2, 3, ...] (first {length} numbers)")
    print()


def demonstrate_string_functions():
    """Examples of string processing function usage."""
    print("=== String Processing Functions Examples ===")

    # Note: These would import from hello.py once implemented
    # from hello import reverse_words, count_vowels, capitalize_words

    sample_texts = [
        "hello world",
        "The quick brown fox",
        "Integration Testing Made Easy",
        ""
    ]

    print("1. Word reversal:")
    for text in sample_texts:
        # reversed_text = reverse_words(text)
        words = text.split()
        reversed_words = ' '.join(word[::-1] for word in words) if words else ""
        print(f"   '{text}' -> '{reversed_words}'")

    print("\n2. Vowel counting:")
    for text in sample_texts:
        # vowel_count = count_vowels(text)
        vowel_count = sum(1 for char in text.lower() if char in 'aeiou')
        print(f"   '{text}' has {vowel_count} vowels")

    print("\n3. Word capitalization:")
    for text in sample_texts:
        # capitalized = capitalize_words(text)
        capitalized = ' '.join(word.capitalize() for word in text.split())
        print(f"   '{text}' -> '{capitalized}'")
    print()


def demonstrate_data_processing():
    """Examples of data manipulation functions."""
    print("=== Data Processing Functions Examples ===")

    # Note: These would import from hello.py once implemented
    # from hello import filter_even_numbers, find_duplicates, merge_sorted_lists
    # from hello import invert_dictionary, merge_dictionaries, filter_by_value

    print("1. List processing:")
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # even_numbers = filter_even_numbers(sample_list)
    even_numbers = [n for n in sample_list if n % 2 == 0]
    print(f"   Even numbers from {sample_list}: {even_numbers}")

    duplicate_list = [1, 2, 2, 3, 4, 4, 5]
    # duplicates = find_duplicates(duplicate_list)
    seen = set()
    duplicates = list(set(x for x in duplicate_list if x in seen or seen.add(x)))
    print(f"   Duplicates in {duplicate_list}: {duplicates}")

    print("\n2. Dictionary operations:")
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    # inverted = invert_dictionary(sample_dict)
    inverted = {v: k for k, v in sample_dict.items()}
    print(f"   Original: {sample_dict}")
    print(f"   Inverted: {inverted}")

    dict1 = {'x': 10, 'y': 20}
    dict2 = {'y': 30, 'z': 40}
    # merged = merge_dictionaries(dict1, dict2)
    merged = {**dict1, **dict2}
    print(f"   Merged {dict1} + {dict2} = {merged}")
    print()


def demonstrate_function_chaining():
    """Examples of chaining functions together for complex operations."""
    print("=== Function Chaining and Composition Examples ===")

    print("1. Text processing pipeline:")
    original_text = "the quick brown fox jumps"

    # Step 1: Capitalize words
    # capitalized = capitalize_words(original_text)
    capitalized = ' '.join(word.capitalize() for word in original_text.split())

    # Step 2: Count vowels in capitalized text
    # vowel_count = count_vowels(capitalized)
    vowel_count = sum(1 for char in capitalized.lower() if char in 'aeiou')

    # Step 3: Reverse words
    # final_text = reverse_words(capitalized)
    words = capitalized.split()
    final_text = ' '.join(word[::-1] for word in words)

    print(f"   Original: '{original_text}'")
    print(f"   Capitalized: '{capitalized}'")
    print(f"   Vowel count: {vowel_count}")
    print(f"   Words reversed: '{final_text}'")

    print("\n2. Mathematical computation chain:")
    numbers = [3, 4, 5]
    print(f"   Computing factorials and checking primality for {numbers}:")

    for num in numbers:
        # factorial_result = calculate_factorial(num)
        factorial_result = 1
        for i in range(1, num + 1):
            factorial_result *= i

        # is_prime = is_prime_number(factorial_result)
        is_prime = factorial_result > 1 and all(factorial_result % i != 0 for i in range(2, int(factorial_result**0.5) + 1))

        print(f"   {num}! = {factorial_result}, is_prime = {is_prime}")
    print()


def demonstrate_error_handling():
    """Examples of proper error handling with utility functions."""
    print("=== Error Handling Examples ===")

    print("1. Handling invalid inputs:")
    invalid_inputs = [None, "", -1, "not_a_number", []]

    for invalid_input in invalid_inputs:
        print(f"   Testing with input: {repr(invalid_input)}")

        # Example of how functions should handle errors
        try:
            if invalid_input is None:
                raise ValueError("Input cannot be None")
            elif isinstance(invalid_input, str) and not invalid_input:
                print("   -> Empty string handled gracefully")
            elif isinstance(invalid_input, int) and invalid_input < 0:
                raise ValueError("Negative numbers not supported for factorial")
            else:
                print("   -> Input would be processed normally")
        except (ValueError, TypeError) as e:
            print(f"   -> Error handled: {e}")

    print("\n2. File operation error handling:")
    non_existent_file = "non_existent_file.txt"

    try:
        # This would use read_file_lines(non_existent_file)
        with open(non_existent_file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"   -> File '{non_existent_file}' not found - error handled gracefully")
    except PermissionError:
        print("   -> Permission denied - error handled gracefully")
    print()


def demonstrate_file_operations():
    """Examples of file and JSON processing workflows."""
    print("=== File and JSON Operations Examples ===")

    # Create temporary files for demonstration
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        print("1. File processing workflow:")

        # Create a sample text file
        sample_file = temp_path / "sample.txt"
        sample_content = """This is line 1
This is line 2 with more words
Final line here"""

        # This would use write_to_file(sample_file, sample_content)
        sample_file.write_text(sample_content)
        print(f"   Created sample file: {sample_file}")

        # This would use read_file_lines(sample_file)
        lines = sample_file.read_text().splitlines()
        print(f"   File has {len(lines)} lines")

        # This would use count_file_words(sample_file)
        word_count = len(sample_file.read_text().split())
        print(f"   Total word count: {word_count}")

        print("\n2. JSON processing workflow:")

        # Create sample JSON data
        sample_data = {
            "users": [
                {"name": "Alice", "age": 30, "active": True},
                {"name": "Bob", "age": 25, "active": False},
                {"name": "Charlie", "age": 35, "active": True}
            ],
            "metadata": {
                "version": "1.0",
                "created": "2024-01-01"
            }
        }

        json_file = temp_path / "data.json"
        # This would use functions to handle JSON operations
        json_file.write_text(json.dumps(sample_data, indent=2))

        # This would use parse_json_string() and extract_json_values()
        loaded_data = json.loads(json_file.read_text())
        active_users = [user for user in loaded_data["users"] if user["active"]]

        print(f"   Created JSON file with {len(loaded_data['users'])} users")
        print(f"   Found {len(active_users)} active users")

        print("\n3. CSV processing workflow:")
        csv_content = """name,age,city
John,25,New York
Jane,30,Los Angeles
Bob,35,Chicago"""

        csv_file = temp_path / "data.csv"
        csv_file.write_text(csv_content)

        # This would use parse_csv_data() and convert_to_csv_format()
        lines = csv_content.strip().split('\n')
        headers = lines[0].split(',')
        rows = [line.split(',') for line in lines[1:]]

        print(f"   CSV has {len(headers)} columns: {headers}")
        print(f"   CSV has {len(rows)} data rows")

        # Demonstrate converting back to CSV format
        processed_data = [dict(zip(headers, row)) for row in rows]
        print(f"   Processed {len(processed_data)} records")
    print()


def demonstrate_integration_scenarios():
    """Examples simulating real-world integration testing scenarios."""
    print("=== Real-World Integration Testing Scenarios ===")

    print("1. User Data Validation Pipeline:")
    # Simulate processing user registration data
    user_inputs = [
        {"name": "john doe", "email": "john@example.com", "age": "25"},
        {"name": "JANE SMITH", "email": "jane@test.com", "age": "30"},
        {"name": "", "email": "invalid-email", "age": "-5"}
    ]

    for i, user_data in enumerate(user_inputs, 1):
        print(f"   Processing user {i}: {user_data}")

        # This would use multiple utility functions in sequence
        try:
            # Normalize name using capitalize_words
            if user_data["name"]:
                normalized_name = ' '.join(word.capitalize() for word in user_data["name"].split())
            else:
                raise ValueError("Name cannot be empty")

            # Validate email (basic check)
            if "@" not in user_data["email"] or "." not in user_data["email"]:
                raise ValueError("Invalid email format")

            # Validate age
            age = int(user_data["age"])
            if age < 0:
                raise ValueError("Age cannot be negative")

            print(f"   -> Valid user: {normalized_name}, {user_data['email']}, age {age}")

        except (ValueError, TypeError) as e:
            print(f"   -> Invalid user data: {e}")

    print("\n2. Data Processing and Analysis Workflow:")
    # Simulate analyzing test results
    test_results = [
        {"test_name": "login_test", "duration": 1.5, "status": "passed"},
        {"test_name": "checkout_test", "duration": 3.2, "status": "failed"},
        {"test_name": "search_test", "duration": 0.8, "status": "passed"},
        {"test_name": "payment_test", "duration": 2.1, "status": "passed"}
    ]

    print(f"   Analyzing {len(test_results)} test results:")

    # This would use filter and statistical functions
    passed_tests = [t for t in test_results if t["status"] == "passed"]
    failed_tests = [t for t in test_results if t["status"] == "failed"]

    total_duration = sum(t["duration"] for t in test_results)
    avg_duration = total_duration / len(test_results)

    print(f"   -> Passed: {len(passed_tests)}, Failed: {len(failed_tests)}")
    print(f"   -> Total duration: {total_duration:.1f}s, Average: {avg_duration:.1f}s")

    # Find longest running tests
    sorted_tests = sorted(test_results, key=lambda x: x["duration"], reverse=True)
    print(f"   -> Slowest test: {sorted_tests[0]['test_name']} ({sorted_tests[0]['duration']}s)")

    print("\n3. Configuration File Processing:")
    # Simulate processing configuration files for different environments
    configs = {
        "development": {
            "database_url": "localhost:5432",
            "debug": True,
            "log_level": "DEBUG"
        },
        "staging": {
            "database_url": "staging-db:5432",
            "debug": False,
            "log_level": "INFO"
        },
        "production": {
            "database_url": "prod-db:5432",
            "debug": False,
            "log_level": "ERROR"
        }
    }

    print("   Environment configurations:")
    for env, config in configs.items():
        # This would use dictionary manipulation functions
        debug_status = "enabled" if config.get("debug", False) else "disabled"
        print(f"   -> {env.capitalize()}: Debug {debug_status}, Log level {config['log_level']}")

        # Validate required settings
        required_keys = ["database_url", "log_level"]
        missing_keys = [key for key in required_keys if key not in config]

        if missing_keys:
            print(f"      WARNING: Missing required keys: {missing_keys}")
        else:
            print("      Configuration is complete")
    print()


def main():
    """Run all demonstration examples."""
    print("Python Utility Functions - Integration Examples")
    print("=" * 50)
    print()

    # Run all demonstration functions
    demonstrate_math_functions()
    demonstrate_string_functions()
    demonstrate_data_processing()
    demonstrate_function_chaining()
    demonstrate_error_handling()
    demonstrate_file_operations()
    demonstrate_integration_scenarios()

    print("=" * 50)
    print("All examples completed successfully!")
    print("\nNote: These examples show intended usage patterns.")
    print("Actual utility functions should be implemented in hello.py")
    print("for full functionality.")


if __name__ == "__main__":
    main()