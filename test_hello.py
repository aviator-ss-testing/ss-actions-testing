"""
Comprehensive unit tests for all utility functions in hello.py.
"""

import unittest
import os
import tempfile
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


class TestUtilityFunctions(unittest.TestCase):
    """Test class for all utility functions."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Clean up after each test method."""
        # Clean up temporary files
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    # Math Functions Tests

    def test_calculate_factorial_normal_cases(self):
        """Test factorial calculation for normal cases."""
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(10), 3628800)

    def test_calculate_factorial_edge_cases(self):
        """Test factorial calculation for edge cases."""
        with self.assertRaises(TypeError):
            calculate_factorial("5")
        with self.assertRaises(TypeError):
            calculate_factorial(5.5)
        with self.assertRaises(TypeError):
            calculate_factorial(None)
        with self.assertRaises(ValueError):
            calculate_factorial(-1)
        with self.assertRaises(ValueError):
            calculate_factorial(-10)

    def test_is_prime_number_normal_cases(self):
        """Test prime number detection for normal cases."""
        self.assertTrue(is_prime_number(2))
        self.assertTrue(is_prime_number(3))
        self.assertTrue(is_prime_number(5))
        self.assertTrue(is_prime_number(17))
        self.assertTrue(is_prime_number(97))
        self.assertFalse(is_prime_number(1))
        self.assertFalse(is_prime_number(4))
        self.assertFalse(is_prime_number(9))
        self.assertFalse(is_prime_number(15))
        self.assertFalse(is_prime_number(100))

    def test_is_prime_number_edge_cases(self):
        """Test prime number detection for edge cases."""
        self.assertFalse(is_prime_number(0))
        self.assertFalse(is_prime_number(-5))
        with self.assertRaises(TypeError):
            is_prime_number("7")
        with self.assertRaises(TypeError):
            is_prime_number(7.5)
        with self.assertRaises(TypeError):
            is_prime_number(None)

    def test_fibonacci_sequence_normal_cases(self):
        """Test Fibonacci sequence generation for normal cases."""
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(1), [0])
        self.assertEqual(fibonacci_sequence(2), [0, 1])
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_sequence(8), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_fibonacci_sequence_edge_cases(self):
        """Test Fibonacci sequence generation for edge cases."""
        with self.assertRaises(TypeError):
            fibonacci_sequence("5")
        with self.assertRaises(TypeError):
            fibonacci_sequence(5.5)
        with self.assertRaises(TypeError):
            fibonacci_sequence(None)
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)

    # String Functions Tests

    def test_reverse_words_normal_cases(self):
        """Test word reversal for normal cases."""
        self.assertEqual(reverse_words("hello world"), "world hello")
        self.assertEqual(reverse_words("the quick brown fox"), "fox brown quick the")
        self.assertEqual(reverse_words("Python is awesome"), "awesome is Python")

    def test_reverse_words_edge_cases(self):
        """Test word reversal for edge cases."""
        self.assertEqual(reverse_words(""), "")
        self.assertEqual(reverse_words("   "), "   ")
        self.assertEqual(reverse_words("single"), "single")
        self.assertEqual(reverse_words("  hello   world  "), "world hello")
        with self.assertRaises(TypeError):
            reverse_words(123)
        with self.assertRaises(TypeError):
            reverse_words(None)

    def test_count_vowels_normal_cases(self):
        """Test vowel counting for normal cases."""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("Programming"), 3)
        self.assertEqual(count_vowels("xyz"), 0)

    def test_count_vowels_edge_cases(self):
        """Test vowel counting for edge cases."""
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("123456"), 0)
        self.assertEqual(count_vowels("!@#$%"), 0)
        with self.assertRaises(TypeError):
            count_vowels(123)
        with self.assertRaises(TypeError):
            count_vowels(None)

    def test_capitalize_words_normal_cases(self):
        """Test word capitalization for normal cases."""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python is great"), "Python Is Great")
        self.assertEqual(capitalize_words("HELLO WORLD"), "Hello World")

    def test_capitalize_words_edge_cases(self):
        """Test word capitalization for edge cases."""
        self.assertEqual(capitalize_words(""), "")
        self.assertEqual(capitalize_words("single"), "Single")
        self.assertEqual(capitalize_words("  hello   world  "), "Hello World")
        with self.assertRaises(TypeError):
            capitalize_words(123)
        with self.assertRaises(TypeError):
            capitalize_words(None)

    # Data Processing Functions Tests

    def test_filter_even_numbers_normal_cases(self):
        """Test even number filtering for normal cases."""
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(filter_even_numbers([1, 3, 5, 7]), [])
        self.assertEqual(filter_even_numbers([2, 4, 6, 8]), [2, 4, 6, 8])
        self.assertEqual(filter_even_numbers([0, -2, -4, 3]), [0, -2, -4])

    def test_filter_even_numbers_edge_cases(self):
        """Test even number filtering for edge cases."""
        self.assertEqual(filter_even_numbers([]), [])
        self.assertEqual(filter_even_numbers(None), [])
        with self.assertRaises(TypeError):
            filter_even_numbers("123")
        with self.assertRaises(TypeError):
            filter_even_numbers([1, 2, "3", 4])
        with self.assertRaises(TypeError):
            filter_even_numbers([1, 2.5, 3])

    def test_find_duplicates_normal_cases(self):
        """Test duplicate finding for normal cases."""
        self.assertEqual(set(find_duplicates([1, 2, 3, 2, 4, 3])), {2, 3})
        self.assertEqual(find_duplicates([1, 2, 3, 4, 5]), [])
        self.assertEqual(set(find_duplicates(["a", "b", "a", "c", "b"])), {"a", "b"})

    def test_find_duplicates_edge_cases(self):
        """Test duplicate finding for edge cases."""
        self.assertEqual(find_duplicates([]), [])
        self.assertEqual(find_duplicates(None), [])
        self.assertEqual(find_duplicates([1]), [])
        self.assertEqual(find_duplicates([1, 1, 1]), [1])
        with self.assertRaises(TypeError):
            find_duplicates("abc")

    def test_merge_sorted_lists_normal_cases(self):
        """Test sorted list merging for normal cases."""
        self.assertEqual(merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_lists([4, 5, 6], [1, 2, 3]), [1, 2, 3, 4, 5, 6])

    def test_merge_sorted_lists_edge_cases(self):
        """Test sorted list merging for edge cases."""
        self.assertEqual(merge_sorted_lists([], []), [])
        self.assertEqual(merge_sorted_lists([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(merge_sorted_lists([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge_sorted_lists(None, [1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge_sorted_lists([1, 2, 3], None), [1, 2, 3])
        self.assertEqual(merge_sorted_lists(None, None), [])
        with self.assertRaises(TypeError):
            merge_sorted_lists("123", [1, 2, 3])

    # Dictionary Functions Tests

    def test_invert_dictionary_normal_cases(self):
        """Test dictionary inversion for normal cases."""
        self.assertEqual(invert_dictionary({"a": 1, "b": 2}), {1: "a", 2: "b"})
        self.assertEqual(invert_dictionary({1: "x", 2: "y"}), {"x": 1, "y": 2})

    def test_invert_dictionary_edge_cases(self):
        """Test dictionary inversion for edge cases."""
        self.assertEqual(invert_dictionary({}), {})
        self.assertEqual(invert_dictionary(None), {})
        with self.assertRaises(TypeError):
            invert_dictionary("abc")
        with self.assertRaises(ValueError):
            invert_dictionary({"a": [1, 2], "b": [3, 4]})  # Non-hashable values

    def test_merge_dictionaries_normal_cases(self):
        """Test dictionary merging for normal cases."""
        result = merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4})
        self.assertEqual(result, {"a": 1, "b": 3, "c": 4})

    def test_merge_dictionaries_edge_cases(self):
        """Test dictionary merging for edge cases."""
        self.assertEqual(merge_dictionaries({}, {}), {})
        self.assertEqual(merge_dictionaries({"a": 1}, {}), {"a": 1})
        self.assertEqual(merge_dictionaries({}, {"a": 1}), {"a": 1})
        self.assertEqual(merge_dictionaries(None, {"a": 1}), {"a": 1})
        self.assertEqual(merge_dictionaries({"a": 1}, None), {"a": 1})
        self.assertEqual(merge_dictionaries(None, None), {})
        with self.assertRaises(TypeError):
            merge_dictionaries("abc", {"a": 1})

    def test_filter_by_value_normal_cases(self):
        """Test value-based dictionary filtering for normal cases."""
        data = {"a": 10, "b": 5, "c": 15, "d": 3}
        self.assertEqual(filter_by_value(data, 10), {"a": 10, "c": 15})
        self.assertEqual(filter_by_value(data, 20), {})
        self.assertEqual(filter_by_value(data, 0), {"a": 10, "b": 5, "c": 15, "d": 3})

    def test_filter_by_value_edge_cases(self):
        """Test value-based dictionary filtering for edge cases."""
        self.assertEqual(filter_by_value({}, 5), {})
        self.assertEqual(filter_by_value(None, 5), {})
        with self.assertRaises(TypeError):
            filter_by_value("abc", 5)

    # Set Functions Tests

    def test_find_common_elements_normal_cases(self):
        """Test finding common elements for normal cases."""
        self.assertEqual(find_common_elements({1, 2, 3}, {2, 3, 4}), {2, 3})
        self.assertEqual(find_common_elements({1, 2}, {3, 4}), set())
        self.assertEqual(find_common_elements({"a", "b"}, {"b", "c"}), {"b"})

    def test_find_common_elements_edge_cases(self):
        """Test finding common elements for edge cases."""
        self.assertEqual(find_common_elements(set(), set()), set())
        self.assertEqual(find_common_elements({1, 2}, set()), set())
        self.assertEqual(find_common_elements(set(), {1, 2}), set())
        self.assertEqual(find_common_elements(None, {1, 2}), set())
        self.assertEqual(find_common_elements({1, 2}, None), set())
        self.assertEqual(find_common_elements(None, None), set())
        with self.assertRaises(TypeError):
            find_common_elements([1, 2], {1, 2})

    def test_calculate_set_difference_normal_cases(self):
        """Test set difference calculation for normal cases."""
        self.assertEqual(calculate_set_difference({1, 2, 3}, {2, 3, 4}), {1})
        self.assertEqual(calculate_set_difference({1, 2}, {3, 4}), {1, 2})
        self.assertEqual(calculate_set_difference({"a", "b"}, {"b", "c"}), {"a"})

    def test_calculate_set_difference_edge_cases(self):
        """Test set difference calculation for edge cases."""
        self.assertEqual(calculate_set_difference(set(), set()), set())
        self.assertEqual(calculate_set_difference({1, 2}, set()), {1, 2})
        self.assertEqual(calculate_set_difference(set(), {1, 2}), set())
        self.assertEqual(calculate_set_difference(None, {1, 2}), set())
        self.assertEqual(calculate_set_difference({1, 2}, None), {1, 2})
        self.assertEqual(calculate_set_difference(None, None), set())
        with self.assertRaises(TypeError):
            calculate_set_difference([1, 2], {1, 2})

    # File Operations Tests

    def test_read_file_lines_normal_cases(self):
        """Test file reading for normal cases."""
        # Create a test file
        test_file = os.path.join(self.temp_dir, "test.txt")
        with open(test_file, 'w') as f:
            f.write("line 1\nline 2\nline 3")

        lines = read_file_lines(test_file)
        self.assertEqual(lines, ["line 1", "line 2", "line 3"])

    def test_read_file_lines_edge_cases(self):
        """Test file reading for edge cases."""
        # Test empty file
        empty_file = os.path.join(self.temp_dir, "empty.txt")
        with open(empty_file, 'w') as f:
            pass
        self.assertEqual(read_file_lines(empty_file), [])

        # Test non-existent file
        with self.assertRaises(FileNotFoundError):
            read_file_lines("non_existent_file.txt")

        # Test invalid input types
        with self.assertRaises(TypeError):
            read_file_lines(123)
        with self.assertRaises(TypeError):
            read_file_lines(None)
        with self.assertRaises(ValueError):
            read_file_lines("")
        with self.assertRaises(ValueError):
            read_file_lines("   ")

    def test_write_to_file_normal_cases(self):
        """Test file writing for normal cases."""
        test_file = os.path.join(self.temp_dir, "write_test.txt")
        result = write_to_file(test_file, "Hello, World!")
        self.assertTrue(result)

        # Verify the content was written
        with open(test_file, 'r') as f:
            self.assertEqual(f.read(), "Hello, World!")

    def test_write_to_file_edge_cases(self):
        """Test file writing for edge cases."""
        # Test creating nested directories
        nested_file = os.path.join(self.temp_dir, "nested", "dir", "test.txt")
        result = write_to_file(nested_file, "nested content")
        self.assertTrue(result)
        self.assertTrue(os.path.exists(nested_file))

        # Test invalid input types
        with self.assertRaises(TypeError):
            write_to_file(123, "content")
        with self.assertRaises(TypeError):
            write_to_file("file.txt", 123)
        with self.assertRaises(ValueError):
            write_to_file("", "content")
        with self.assertRaises(ValueError):
            write_to_file("   ", "content")

    def test_count_file_words_normal_cases(self):
        """Test word counting for normal cases."""
        test_file = os.path.join(self.temp_dir, "words_test.txt")
        with open(test_file, 'w') as f:
            f.write("Hello world this is a test file with multiple words")

        word_count = count_file_words(test_file)
        self.assertEqual(word_count, 11)

    def test_count_file_words_edge_cases(self):
        """Test word counting for edge cases."""
        # Test empty file
        empty_file = os.path.join(self.temp_dir, "empty_words.txt")
        with open(empty_file, 'w') as f:
            pass
        self.assertEqual(count_file_words(empty_file), 0)

        # Test file with only whitespace
        whitespace_file = os.path.join(self.temp_dir, "whitespace.txt")
        with open(whitespace_file, 'w') as f:
            f.write("   \n  \t  \n  ")
        self.assertEqual(count_file_words(whitespace_file), 0)

        # Test non-existent file
        with self.assertRaises(FileNotFoundError):
            count_file_words("non_existent_file.txt")

        # Test invalid input types
        with self.assertRaises(TypeError):
            count_file_words(123)
        with self.assertRaises(TypeError):
            count_file_words(None)

    # JSON Functions Tests

    def test_parse_json_string_normal_cases(self):
        """Test JSON parsing for normal cases."""
        self.assertEqual(parse_json_string('{"key": "value"}'), {"key": "value"})
        self.assertEqual(parse_json_string('[1, 2, 3]'), [1, 2, 3])
        self.assertEqual(parse_json_string('42'), 42)
        self.assertEqual(parse_json_string('true'), True)
        self.assertEqual(parse_json_string('null'), None)

    def test_parse_json_string_edge_cases(self):
        """Test JSON parsing for edge cases."""
        with self.assertRaises(ValueError):
            parse_json_string('{"invalid": json}')
        with self.assertRaises(ValueError):
            parse_json_string('')
        with self.assertRaises(ValueError):
            parse_json_string('   ')
        with self.assertRaises(TypeError):
            parse_json_string(123)
        with self.assertRaises(TypeError):
            parse_json_string(None)

    def test_validate_json_structure_normal_cases(self):
        """Test JSON structure validation for normal cases."""
        data = {"name": "John", "age": 30, "city": "New York"}
        self.assertTrue(validate_json_structure(data, ["name", "age"]))
        self.assertTrue(validate_json_structure(data, []))

    def test_validate_json_structure_edge_cases(self):
        """Test JSON structure validation for edge cases."""
        data = {"name": "John", "age": 30}
        with self.assertRaises(ValueError):
            validate_json_structure(data, ["name", "age", "missing_key"])
        with self.assertRaises(TypeError):
            validate_json_structure("not a dict", ["key"])
        with self.assertRaises(TypeError):
            validate_json_structure({}, "not a list")

    def test_extract_json_values_normal_cases(self):
        """Test JSON value extraction for normal cases."""
        data = {"name": "John", "age": 30, "city": "New York"}
        result = extract_json_values(data, ["name", "age"])
        self.assertEqual(result, {"name": "John", "age": 30})

    def test_extract_json_values_edge_cases(self):
        """Test JSON value extraction for edge cases."""
        data = {"name": "John", "age": 30}
        result = extract_json_values(data, ["name", "missing_key"])
        self.assertEqual(result, {"name": "John"})

        self.assertEqual(extract_json_values({}, []), {})
        self.assertEqual(extract_json_values(None, []), {})
        self.assertEqual(extract_json_values({}, None), {})

        with self.assertRaises(TypeError):
            extract_json_values("not a dict", ["key"])
        with self.assertRaises(TypeError):
            extract_json_values({}, "not a list")

    # CSV Functions Tests

    def test_parse_csv_data_normal_cases(self):
        """Test CSV parsing for normal cases."""
        csv_data = "name,age,city\nJohn,30,New York\nJane,25,Boston"
        result = parse_csv_data(csv_data)
        expected = [
            {"name": "John", "age": "30", "city": "New York"},
            {"name": "Jane", "age": "25", "city": "Boston"}
        ]
        self.assertEqual(result, expected)

    def test_parse_csv_data_edge_cases(self):
        """Test CSV parsing for edge cases."""
        self.assertEqual(parse_csv_data(""), [])
        self.assertEqual(parse_csv_data("   "), [])

        # Test custom delimiter
        csv_data = "name|age|city\nJohn|30|New York"
        result = parse_csv_data(csv_data, delimiter="|")
        expected = [{"name": "John", "age": "30", "city": "New York"}]
        self.assertEqual(result, expected)

        with self.assertRaises(TypeError):
            parse_csv_data(123)
        with self.assertRaises(TypeError):
            parse_csv_data("data", delimiter=123)

    def test_convert_to_csv_format_normal_cases(self):
        """Test CSV conversion for normal cases."""
        data = [
            {"name": "John", "age": 30},
            {"name": "Jane", "age": 25}
        ]
        result = convert_to_csv_format(data)
        self.assertIn("age,name", result)  # Headers (sorted)
        self.assertIn("30,John", result)
        self.assertIn("25,Jane", result)

    def test_convert_to_csv_format_edge_cases(self):
        """Test CSV conversion for edge cases."""
        # Test empty data with fieldnames
        result = convert_to_csv_format([], fieldnames=["name", "age"])
        self.assertEqual(result, "name,age")

        # Test empty data without fieldnames
        self.assertEqual(convert_to_csv_format([]), "")

        # Test custom delimiter
        data = [{"name": "John", "age": 30}]
        result = convert_to_csv_format(data, delimiter="|")
        self.assertIn("age|name", result)
        self.assertIn("30|John", result)

        with self.assertRaises(TypeError):
            convert_to_csv_format("not a list")
        with self.assertRaises(TypeError):
            convert_to_csv_format([{"name": "John"}, "not a dict"])
        with self.assertRaises(TypeError):
            convert_to_csv_format([], delimiter=123)


if __name__ == '__main__':
    unittest.main()