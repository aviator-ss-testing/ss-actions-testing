import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from io import StringIO
from unittest.mock import patch
from list_utils import flatten, chunk, unique_elements, running_average, timer


class TestFlatten(unittest.TestCase):

    def test_flatten_empty_list(self):
        self.assertEqual(flatten([]), [])

    def test_flatten_single_level(self):
        self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])

    def test_flatten_two_levels(self):
        self.assertEqual(flatten([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_flatten_deeply_nested(self):
        self.assertEqual(flatten([1, [2, [3, [4, [5]]]]]), [1, 2, 3, 4, 5])

    def test_flatten_multiple_nested_lists(self):
        self.assertEqual(flatten([[1, 2], [3, 4], [5, 6]]), [1, 2, 3, 4, 5, 6])

    def test_flatten_mixed_nesting(self):
        self.assertEqual(flatten([1, [2, 3], 4, [5, [6, 7]], 8]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_flatten_with_empty_nested_lists(self):
        self.assertEqual(flatten([1, [], [2, []], 3]), [1, 2, 3])

    def test_flatten_all_empty_nested_lists(self):
        self.assertEqual(flatten([[], [[]], [[[]]]]), [])

    def test_flatten_non_list_raises_type_error(self):
        with self.assertRaises(TypeError):
            flatten("not a list")

    def test_flatten_none_raises_type_error(self):
        with self.assertRaises(TypeError):
            flatten(None)


class TestChunk(unittest.TestCase):

    def test_chunk_empty_list(self):
        self.assertEqual(chunk([], 2), [])

    def test_chunk_size_one(self):
        self.assertEqual(chunk([1, 2, 3, 4], 1), [[1], [2], [3], [4]])

    def test_chunk_size_two(self):
        self.assertEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_chunk_size_three(self):
        self.assertEqual(chunk([1, 2, 3, 4, 5, 6, 7], 3), [[1, 2, 3], [4, 5, 6], [7]])

    def test_chunk_size_equals_list_length(self):
        self.assertEqual(chunk([1, 2, 3], 3), [[1, 2, 3]])

    def test_chunk_size_larger_than_list(self):
        self.assertEqual(chunk([1, 2], 5), [[1, 2]])

    def test_chunk_single_element_list(self):
        self.assertEqual(chunk([1], 2), [[1]])

    def test_chunk_size_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            chunk([1, 2, 3], 0)

    def test_chunk_negative_size_raises_value_error(self):
        with self.assertRaises(ValueError):
            chunk([1, 2, 3], -1)

    def test_chunk_non_list_raises_type_error(self):
        with self.assertRaises(TypeError):
            chunk("not a list", 2)

    def test_chunk_non_integer_size_raises_type_error(self):
        with self.assertRaises(TypeError):
            chunk([1, 2, 3], 2.5)

    def test_chunk_string_size_raises_type_error(self):
        with self.assertRaises(TypeError):
            chunk([1, 2, 3], "2")


class TestUniqueElements(unittest.TestCase):

    def test_unique_elements_empty_list(self):
        self.assertEqual(unique_elements([]), [])

    def test_unique_elements_no_duplicates(self):
        self.assertEqual(unique_elements([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_unique_elements_all_duplicates(self):
        self.assertEqual(unique_elements([1, 1, 1, 1]), [1])

    def test_unique_elements_some_duplicates(self):
        self.assertEqual(unique_elements([1, 2, 2, 3, 3, 3, 4]), [1, 2, 3, 4])

    def test_unique_elements_maintains_order(self):
        self.assertEqual(unique_elements([3, 1, 2, 1, 3, 2]), [3, 1, 2])

    def test_unique_elements_maintains_first_occurrence(self):
        self.assertEqual(unique_elements([5, 2, 3, 2, 5, 1]), [5, 2, 3, 1])

    def test_unique_elements_single_element(self):
        self.assertEqual(unique_elements([42]), [42])

    def test_unique_elements_with_strings(self):
        self.assertEqual(unique_elements(['a', 'b', 'a', 'c', 'b']), ['a', 'b', 'c'])

    def test_unique_elements_mixed_types(self):
        self.assertEqual(unique_elements([1, 'a', 2, 'a', 1]), [1, 'a', 2])

    def test_unique_elements_non_list_raises_type_error(self):
        with self.assertRaises(TypeError):
            unique_elements("not a list")

    def test_unique_elements_none_raises_type_error(self):
        with self.assertRaises(TypeError):
            unique_elements(None)


class TestRunningAverage(unittest.TestCase):

    def test_running_average_empty_list(self):
        self.assertEqual(running_average([]), [])

    def test_running_average_single_element(self):
        self.assertEqual(running_average([5]), [5.0])

    def test_running_average_positive_integers(self):
        result = running_average([1, 2, 3, 4, 5])
        expected = [1.0, 1.5, 2.0, 2.5, 3.0]
        self.assertEqual(result, expected)

    def test_running_average_negative_integers(self):
        result = running_average([-1, -2, -3, -4])
        expected = [-1.0, -1.5, -2.0, -2.5]
        self.assertEqual(result, expected)

    def test_running_average_mixed_positive_negative(self):
        result = running_average([10, -5, 5, -10])
        expected = [10.0, 2.5, 10/3, 0.0]
        self.assertEqual(len(result), len(expected))
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=7)

    def test_running_average_with_floats(self):
        result = running_average([1.5, 2.5, 3.5])
        expected = [1.5, 2.0, 2.5]
        self.assertEqual(result, expected)

    def test_running_average_mixed_int_float(self):
        result = running_average([1, 2.0, 3, 4.0])
        expected = [1.0, 1.5, 2.0, 2.5]
        self.assertEqual(result, expected)

    def test_running_average_with_zeros(self):
        result = running_average([0, 0, 0, 0])
        expected = [0.0, 0.0, 0.0, 0.0]
        self.assertEqual(result, expected)

    def test_running_average_zeros_and_numbers(self):
        result = running_average([5, 0, 5, 0])
        expected = [5.0, 2.5, 10/3, 2.5]
        self.assertEqual(len(result), len(expected))
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=7)

    def test_running_average_non_list_raises_type_error(self):
        with self.assertRaises(TypeError):
            running_average("not a list")

    def test_running_average_non_numeric_element_raises_type_error(self):
        with self.assertRaises(TypeError):
            running_average([1, 2, "3", 4])

    def test_running_average_string_element_raises_type_error(self):
        with self.assertRaises(TypeError):
            running_average([1, 2, "three"])

    def test_running_average_none_element_raises_type_error(self):
        with self.assertRaises(TypeError):
            running_average([1, None, 3])


class TestTimerDecorator(unittest.TestCase):

    def test_timer_returns_correct_result(self):
        @timer
        def add(a, b):
            return a + b

        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_timer_preserves_function_name(self):
        @timer
        def sample_function():
            return 42

        self.assertEqual(sample_function.__name__, 'sample_function')

    def test_timer_executes_function(self):
        @timer
        def multiply(a, b):
            return a * b

        result = multiply(4, 5)
        self.assertEqual(result, 20)

    def test_timer_handles_multiple_arguments(self):
        @timer
        def sum_all(*args):
            return sum(args)

        result = sum_all(1, 2, 3, 4, 5)
        self.assertEqual(result, 15)

    def test_timer_handles_keyword_arguments(self):
        @timer
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}"

        result = greet("Alice", greeting="Hi")
        self.assertEqual(result, "Hi, Alice")

    @patch('sys.stdout', new_callable=StringIO)
    def test_timer_prints_execution_time(self, mock_stdout):
        @timer
        def quick_function():
            return 1 + 1

        result = quick_function()
        output = mock_stdout.getvalue()

        self.assertEqual(result, 2)
        self.assertIn("quick_function executed in", output)
        self.assertIn("seconds", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_timer_output_format(self, mock_stdout):
        @timer
        def test_func():
            return "done"

        test_func()
        output = mock_stdout.getvalue()

        self.assertTrue(output.startswith("test_func executed in"))
        self.assertTrue("seconds" in output)

    def test_timer_does_not_break_function_with_no_args(self):
        @timer
        def no_args():
            return "success"

        result = no_args()
        self.assertEqual(result, "success")

    def test_timer_handles_exceptions(self):
        @timer
        def failing_function():
            raise ValueError("test error")

        with self.assertRaises(ValueError):
            failing_function()


if __name__ == '__main__':
    unittest.main()
