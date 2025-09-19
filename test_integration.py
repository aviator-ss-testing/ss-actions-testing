"""
Integration test suite for testing function combinations and real-world scenarios.
"""

import unittest
import os
import tempfile
import shutil
import time
import json
from hello import (
    # Math functions
    calculate_factorial, is_prime_number, fibonacci_sequence,
    # String functions
    reverse_words, count_vowels, capitalize_words,
    # Data processing functions
    filter_even_numbers, find_duplicates, merge_sorted_lists,
    # Dictionary functions
    invert_dictionary, merge_dictionaries, filter_by_value,
    # Set functions
    find_common_elements, calculate_set_difference,
    # File operations
    read_file_lines, write_to_file, count_file_words,
    # JSON functions
    parse_json_string, validate_json_structure, extract_json_values,
    # CSV functions
    parse_csv_data, convert_to_csv_format
)


class TestIntegrationScenarios(unittest.TestCase):
    """Integration test class for testing function combinations and real-world scenarios."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_files = []

    def tearDown(self):
        """Clean up after each test method."""
        # Clean up all temporary files and directories
        shutil.rmtree(self.temp_dir, ignore_errors=True)

        # Clean up any additional test files created
        for file_path in self.test_files:
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
            except:
                pass

    def _create_test_file(self, filename, content):
        """Helper method to create test files and track them for cleanup."""
        file_path = os.path.join(self.temp_dir, filename)
        self.test_files.append(file_path)
        write_to_file(file_path, content)
        return file_path

    # Function Chaining and Composition Tests

    def test_math_string_integration(self):
        """Test chaining mathematical and string processing functions."""
        # Generate Fibonacci sequence, convert to string, then process
        fib_numbers = fibonacci_sequence(5)  # [0, 1, 1, 2, 3]
        fib_string = ' '.join(map(str, fib_numbers))  # "0 1 1 2 3"

        # Apply string transformations
        capitalized = capitalize_words(fib_string)
        reversed_words = reverse_words(capitalized)
        vowel_count = count_vowels(reversed_words)

        self.assertEqual(fib_numbers, [0, 1, 1, 2, 3])
        self.assertEqual(capitalized, "0 1 1 2 3")
        self.assertEqual(reversed_words, "3 2 1 1 0")
        self.assertEqual(vowel_count, 0)  # No vowels in numbers

    def test_data_processing_pipeline(self):
        """Test a complete data processing pipeline."""
        # Start with raw data
        raw_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6]

        # Find duplicates first
        duplicates = find_duplicates(raw_numbers)
        self.assertEqual(set(duplicates), {2, 4, 6})

        # Filter even numbers
        even_numbers = filter_even_numbers(raw_numbers)
        self.assertEqual(even_numbers, [2, 4, 6, 8, 10, 2, 4, 6])

        # Create two sorted lists and merge them
        list1 = [2, 6, 10]
        list2 = [4, 8, 12]
        merged = merge_sorted_lists(list1, list2)
        self.assertEqual(merged, [2, 4, 6, 8, 10, 12])

        # Process prime numbers from original data
        primes = [num for num in raw_numbers if is_prime_number(num)]
        self.assertEqual(primes, [2, 3, 5, 7, 2])

    def test_file_processing_workflow(self):
        """Test file operations with data processing."""
        # Create test data
        test_data = "apple banana cherry\ndog elephant fox\ngrape honey ice"
        test_file = self._create_test_file("test_words.txt", test_data)

        # Read and process file content
        lines = read_file_lines(test_file)
        self.assertEqual(len(lines), 3)

        # Process each line
        processed_lines = []
        total_vowels = 0

        for line in lines:
            # Reverse words in each line
            reversed_line = reverse_words(line)
            processed_lines.append(reversed_line)

            # Count vowels in original line
            vowels = count_vowels(line)
            total_vowels += vowels

        self.assertEqual(processed_lines, [
            "cherry banana apple",
            "fox elephant dog",
            "ice honey grape"
        ])
        self.assertEqual(total_vowels, 19)  # Count all vowels in the text

        # Write processed data back to a new file
        processed_content = '\n'.join(processed_lines)
        output_file = self._create_test_file("processed_output.txt", processed_content)

        # Verify the output
        word_count = count_file_words(output_file)
        self.assertEqual(word_count, 9)  # Same number of words

    def test_json_csv_conversion_pipeline(self):
        """Test JSON to CSV conversion with data processing."""
        # Create JSON data
        json_data = [
            {"name": "alice johnson", "age": 30, "score": 85},
            {"name": "bob smith", "age": 25, "score": 92},
            {"name": "charlie brown", "age": 35, "score": 78}
        ]

        # Process names: capitalize words
        for person in json_data:
            person["name"] = capitalize_words(person["name"])
            person["vowel_count"] = count_vowels(person["name"])

        # Filter by age threshold
        filtered_data = [p for p in json_data if p["age"] >= 30]
        self.assertEqual(len(filtered_data), 2)

        # Convert to CSV
        csv_content = convert_to_csv_format(filtered_data)

        # Parse the CSV back
        parsed_csv = parse_csv_data(csv_content)

        # Verify the round-trip conversion
        self.assertEqual(len(parsed_csv), 2)
        self.assertEqual(parsed_csv[0]["name"], "Alice Johnson")
        self.assertEqual(parsed_csv[1]["name"], "Charlie Brown")

        # Verify vowel counts were calculated correctly
        alice_vowels = int(parsed_csv[0]["vowel_count"])
        charlie_vowels = int(parsed_csv[1]["vowel_count"])
        self.assertEqual(alice_vowels, 6)  # Alice Johnson
        self.assertEqual(charlie_vowels, 6)  # Charlie Brown

    def test_set_operations_with_file_data(self):
        """Test set operations using data from files."""
        # Create two files with different word sets
        file1_content = "apple banana cherry date elderberry"
        file2_content = "cherry date fig grape honey elderberry"

        file1 = self._create_test_file("words1.txt", file1_content)
        file2 = self._create_test_file("words2.txt", file2_content)

        # Read and process file contents
        words1 = set(read_file_lines(file1)[0].split())
        words2 = set(read_file_lines(file2)[0].split())

        # Perform set operations
        common = find_common_elements(words1, words2)
        difference = calculate_set_difference(words1, words2)

        self.assertEqual(common, {"cherry", "date", "elderberry"})
        self.assertEqual(difference, {"apple", "banana"})

        # Process the results with string functions
        common_words = list(common)
        common_words.sort()  # Ensure consistent order
        common_string = ' '.join(common_words)
        capitalized_common = capitalize_words(common_string)

        self.assertEqual(capitalized_common, "Cherry Date Elderberry")

    # Performance Tests for Large Datasets

    def test_large_dataset_fibonacci_performance(self):
        """Test Fibonacci generation with larger datasets."""
        start_time = time.time()
        large_fib = fibonacci_sequence(1000)
        end_time = time.time()

        # Should complete within reasonable time (adjust as needed)
        self.assertLess(end_time - start_time, 1.0)
        self.assertEqual(len(large_fib), 1000)
        self.assertEqual(large_fib[0], 0)
        self.assertEqual(large_fib[1], 1)

        # Test that the sequence follows Fibonacci rules for first few numbers
        for i in range(2, 10):
            self.assertEqual(large_fib[i], large_fib[i-1] + large_fib[i-2])

    def test_large_list_operations_performance(self):
        """Test list operations with large datasets."""
        # Generate large dataset
        large_list = list(range(10000)) * 2  # 20,000 items with duplicates

        start_time = time.time()
        duplicates = find_duplicates(large_list)
        end_time = time.time()

        # Should find all duplicates efficiently
        self.assertLess(end_time - start_time, 1.0)
        self.assertEqual(len(duplicates), 10000)  # All numbers 0-9999 are duplicates

        # Test even number filtering on large dataset
        start_time = time.time()
        evens = filter_even_numbers(large_list)
        end_time = time.time()

        self.assertLess(end_time - start_time, 1.0)
        self.assertEqual(len(evens), 10000)  # Half the numbers are even

    def test_large_file_processing_performance(self):
        """Test file operations with larger files."""
        # Create a large text file
        lines = []
        for i in range(1000):
            # Create lines with varying content
            line = f"line {i} with some random words and numbers {i*2} {i*3}"
            lines.append(line)

        large_content = '\n'.join(lines)
        large_file = self._create_test_file("large_file.txt", large_content)

        # Test reading performance
        start_time = time.time()
        read_lines = read_file_lines(large_file)
        end_time = time.time()

        self.assertLess(end_time - start_time, 1.0)
        self.assertEqual(len(read_lines), 1000)

        # Test word counting performance
        start_time = time.time()
        word_count = count_file_words(large_file)
        end_time = time.time()

        self.assertLess(end_time - start_time, 1.0)
        self.assertGreater(word_count, 8000)  # Each line has ~8-9 words

    # Real-world Integration Testing Scenarios

    def test_user_data_processing_scenario(self):
        """Simulate processing user data from multiple sources."""
        # Simulate user registration data from JSON API
        json_users = '''[
            {"id": 1, "full_name": "john doe", "email": "john@example.com", "age": 28},
            {"id": 2, "full_name": "jane smith", "email": "jane@example.com", "age": 32},
            {"id": 3, "full_name": "bob johnson", "email": "bob@example.com", "age": 45}
        ]'''

        users = parse_json_string(json_users)

        # Process user data
        for user in users:
            # Normalize names
            user["full_name"] = capitalize_words(user["full_name"])
            user["name_length"] = len(user["full_name"])
            user["vowel_count"] = count_vowels(user["full_name"])

        # Validate data structure
        required_fields = ["id", "full_name", "email", "age"]
        for user in users:
            self.assertTrue(validate_json_structure(user, required_fields))

        # Filter adult users and extract specific data
        adults = [u for u in users if u["age"] >= 30]
        adult_data = []
        for user in adults:
            extracted = extract_json_values(user, ["full_name", "age", "vowel_count"])
            adult_data.append(extracted)

        # Convert to CSV for export
        csv_output = convert_to_csv_format(adult_data)

        # Verify the processing results
        self.assertEqual(len(adults), 2)
        self.assertIn("Jane Smith", csv_output)
        self.assertIn("Bob Johnson", csv_output)

    def test_data_analysis_workflow(self):
        """Simulate a data analysis workflow."""
        # Create sample sales data
        sales_data = [
            {"product": "apple pie", "sales": 150, "region": "north"},
            {"product": "banana bread", "sales": 200, "region": "south"},
            {"product": "cherry cake", "sales": 175, "region": "north"},
            {"product": "date cookies", "sales": 125, "region": "east"},
            {"product": "elderberry tart", "sales": 225, "region": "west"}
        ]

        # Process product names
        for item in sales_data:
            item["product"] = capitalize_words(item["product"])
            item["product_vowels"] = count_vowels(item["product"])

        # Analyze sales performance
        all_sales = [item["sales"] for item in sales_data]
        total_sales = sum(all_sales)

        # Group by performance (high vs low sales)
        high_performers = [item for item in sales_data if item["sales"] >= 175]
        low_performers = [item for item in sales_data if item["sales"] < 175]

        # Extract regions for set analysis
        high_regions = set(item["region"] for item in high_performers)
        low_regions = set(item["region"] for item in low_performers)

        common_regions = find_common_elements(high_regions, low_regions)
        high_only_regions = calculate_set_difference(high_regions, low_regions)

        # Export analysis results
        analysis_results = {
            "total_sales": total_sales,
            "high_performers": len(high_performers),
            "low_performers": len(low_performers),
            "common_regions": list(common_regions),
            "high_only_regions": list(high_only_regions)
        }

        # Write analysis to file
        analysis_json = json.dumps(analysis_results, indent=2)
        analysis_file = self._create_test_file("analysis_results.json", analysis_json)

        # Verify file was created and contains expected data
        self.assertTrue(os.path.exists(analysis_file))

        # Read back and verify
        file_lines = read_file_lines(analysis_file)
        file_content = '\n'.join(file_lines)
        parsed_results = parse_json_string(file_content)

        self.assertEqual(parsed_results["total_sales"], 875)
        self.assertEqual(parsed_results["high_performers"], 3)
        self.assertEqual(parsed_results["low_performers"], 2)

    def test_configuration_management_scenario(self):
        """Simulate configuration file processing and validation."""
        # Create configuration files in different formats

        # JSON config
        json_config = {
            "database": {"host": "localhost", "port": 5432, "name": "testdb"},
            "api": {"timeout": 30, "retries": 3, "base_url": "https://api.example.com"},
            "logging": {"level": "info", "file": "app.log"}
        }

        json_file = self._create_test_file("config.json", json.dumps(json_config))

        # CSV config (key-value pairs)
        csv_config = "key,value,type\ndatabase_host,localhost,string\ndatabase_port,5432,integer\napi_timeout,30,integer"
        csv_file = self._create_test_file("config.csv", csv_config)

        # Process JSON config
        json_content = '\n'.join(read_file_lines(json_file))
        parsed_json = parse_json_string(json_content)

        # Validate required sections
        required_sections = ["database", "api", "logging"]
        self.assertTrue(validate_json_structure(parsed_json, required_sections))

        # Extract database config
        db_config = extract_json_values(parsed_json, ["database"])

        # Process CSV config
        csv_content = '\n'.join(read_file_lines(csv_file))
        csv_data = parse_csv_data(csv_content)

        # Merge configurations (CSV overrides JSON for conflicting keys)
        merged_config = {}
        for row in csv_data:
            key_parts = row["key"].split("_")
            if len(key_parts) == 2:
                section, key = key_parts
                if section not in merged_config:
                    merged_config[section] = {}

                # Convert value based on type
                value = row["value"]
                if row["type"] == "integer":
                    value = int(value)
                merged_config[section][key] = value

        # Verify merged configuration
        self.assertIn("database", merged_config)
        self.assertEqual(merged_config["database"]["host"], "localhost")
        self.assertEqual(merged_config["database"]["port"], 5432)

        # Export final config
        final_config_json = json.dumps(merged_config, indent=2)
        final_file = self._create_test_file("final_config.json", final_config_json)

        # Verify export
        word_count = count_file_words(final_file)
        self.assertGreater(word_count, 5)


if __name__ == '__main__':
    unittest.main()