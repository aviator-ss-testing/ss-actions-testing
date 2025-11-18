"""Integration tests for the utils package.

This module tests that all utility modules can be imported and work
together correctly in realistic scenarios.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest


class TestModuleImports:
    """Test that all modules can be imported successfully."""

    def test_import_string_utils(self):
        """Test that string_utils module can be imported."""
        from utils import string_utils
        assert hasattr(string_utils, "reverse_string")
        assert hasattr(string_utils, "is_palindrome")
        assert hasattr(string_utils, "title_case")
        assert hasattr(string_utils, "count_words")

    def test_import_data_utils(self):
        """Test that data_utils module can be imported."""
        from utils import data_utils
        assert hasattr(data_utils, "flatten_list")
        assert hasattr(data_utils, "remove_duplicates")
        assert hasattr(data_utils, "group_by_key")
        assert hasattr(data_utils, "filter_none")

    def test_import_math_utils(self):
        """Test that math_utils module can be imported."""
        from utils import math_utils
        assert hasattr(math_utils, "fibonacci")
        assert hasattr(math_utils, "is_prime")
        assert hasattr(math_utils, "factorial")
        assert hasattr(math_utils, "gcd")


class TestPackageLevelImports:
    """Test that package-level imports work correctly."""

    def test_all_string_functions_accessible(self):
        """Test that all string functions are accessible from package level."""
        from utils import reverse_string, is_palindrome, title_case, count_words

        assert callable(reverse_string)
        assert callable(is_palindrome)
        assert callable(title_case)
        assert callable(count_words)

    def test_all_data_functions_accessible(self):
        """Test that all data functions are accessible from package level."""
        from utils import flatten_list, remove_duplicates, group_by_key, filter_none

        assert callable(flatten_list)
        assert callable(remove_duplicates)
        assert callable(group_by_key)
        assert callable(filter_none)

    def test_all_math_functions_accessible(self):
        """Test that all math functions are accessible from package level."""
        from utils import fibonacci, is_prime, factorial, gcd

        assert callable(fibonacci)
        assert callable(is_prime)
        assert callable(factorial)
        assert callable(gcd)

    def test_public_api_completeness(self):
        """Test that __all__ contains all expected functions."""
        import utils

        expected_functions = [
            "reverse_string", "is_palindrome", "title_case", "count_words",
            "flatten_list", "remove_duplicates", "group_by_key", "filter_none",
            "fibonacci", "is_prime", "factorial", "gcd",
        ]

        for func_name in expected_functions:
            assert func_name in utils.__all__
            assert hasattr(utils, func_name)


class TestRealisticScenarios:
    """Test using multiple utility functions together in realistic scenarios."""

    def test_process_user_data(self):
        """Test processing user data with multiple utilities."""
        from utils import flatten_list, remove_duplicates, group_by_key, filter_none

        raw_data = [
            [{"name": "Alice", "age": 30, "role": "admin"}],
            [{"name": "Bob", "age": 25, "role": "user"}, {"name": "Charlie", "age": 30, "role": "user"}],
            [{"name": "Diana", "age": None, "role": "admin"}],
        ]

        flattened = flatten_list(raw_data)
        assert len(flattened) == 4

        grouped = group_by_key(flattened, "role")
        assert "admin" in grouped
        assert "user" in grouped
        assert len(grouped["admin"]) == 2
        assert len(grouped["user"]) == 2

        ages = [user.get("age") for user in flattened]
        filtered_ages = filter_none(ages)
        assert len(filtered_ages) == 3
        unique_ages = remove_duplicates(filtered_ages)
        assert unique_ages == [30, 25]

    def test_text_processing_pipeline(self):
        """Test text processing with string utilities."""
        from utils import reverse_string, is_palindrome, title_case, count_words

        text = "hello world"

        reversed_text = reverse_string(text)
        assert reversed_text == "dlrow olleh"

        titled = title_case(text)
        assert titled == "Hello World"
        assert count_words(titled) == 2

        test_words = ["racecar", "hello", "radar", "world"]
        palindromes = [word for word in test_words if is_palindrome(word)]
        assert palindromes == ["racecar", "radar"]

    def test_mathematical_operations_pipeline(self):
        """Test mathematical operations with math utilities."""
        from utils import fibonacci, is_prime, factorial, gcd

        fib_sequence = [fibonacci(i) for i in range(10)]
        assert fib_sequence == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        primes_in_fib = [n for n in fib_sequence if is_prime(n)]
        assert primes_in_fib == [2, 3, 5, 13]

        fact_5 = factorial(5)
        assert fact_5 == 120

        gcd_result = gcd(fact_5, 48)
        assert gcd_result == 24

    def test_mixed_utilities_data_processing(self):
        """Test mixing string, data, and math utilities for complex processing."""
        from utils import (
            title_case, count_words, flatten_list, remove_duplicates,
            filter_none, fibonacci, is_prime
        )

        sentences = [
            "the quick brown fox",
            "the lazy dog",
            "the quick cat"
        ]

        titled_sentences = [title_case(s) for s in sentences]
        word_counts = [count_words(s) for s in sentences]
        assert word_counts == [4, 3, 3]

        words = [s.split() for s in sentences]
        all_words = flatten_list(words)
        unique_words = remove_duplicates(all_words)
        assert len(unique_words) == 7

        first_n_fibs = [fibonacci(i) for i in range(10)]
        prime_fibs = [n for n in first_n_fibs if n > 0 and is_prime(n)]
        assert prime_fibs == [2, 3, 5, 13]

    def test_data_cleaning_workflow(self):
        """Test a realistic data cleaning workflow."""
        from utils import flatten_list, remove_duplicates, filter_none, group_by_key

        messy_data = [
            [
                {"id": 1, "value": "apple", "category": "fruit"},
                {"id": 2, "value": None, "category": "vegetable"},
            ],
            [
                {"id": 1, "value": "apple", "category": "fruit"},
                {"id": 3, "value": "banana", "category": "fruit"},
            ],
            [
                {"id": 4, "value": "carrot", "category": "vegetable"},
                {"id": 5, "value": None, "category": None},
            ]
        ]

        flattened = flatten_list(messy_data)
        assert len(flattened) == 6

        values = [item.get("value") for item in flattened]
        clean_values = filter_none(values)
        unique_values = remove_duplicates(clean_values)
        assert set(unique_values) == {"apple", "banana", "carrot"}

        items_with_category = [item for item in flattened if item.get("category")]
        grouped = group_by_key(items_with_category, "category")
        assert len(grouped.get("fruit", [])) == 3
        assert len(grouped.get("vegetable", [])) == 2

    def test_string_analysis_with_math(self):
        """Test analyzing strings using both string and math utilities."""
        from utils import (
            reverse_string, is_palindrome, count_words,
            factorial, gcd
        )

        words = ["hello", "racecar", "world", "radar", "python"]

        palindromes = [w for w in words if is_palindrome(w)]
        assert len(palindromes) == 2

        reversed_words = [reverse_string(w) for w in words]
        assert reversed_words[0] == "olleh"

        sentence = " ".join(words)
        word_count = count_words(sentence)
        assert word_count == 5

        fact_word_count = factorial(word_count)
        assert fact_word_count == 120

        gcd_result = gcd(fact_word_count, len(words))
        assert gcd_result == 5

    def test_nested_data_aggregation(self):
        """Test aggregating nested data structures."""
        from utils import flatten_list, remove_duplicates, group_by_key

        departments = [
            {
                "name": "Engineering",
                "teams": [
                    [
                        {"employee": "Alice", "level": 5},
                        {"employee": "Bob", "level": 3}
                    ],
                    [
                        {"employee": "Charlie", "level": 5}
                    ]
                ]
            },
            {
                "name": "Sales",
                "teams": [
                    [
                        {"employee": "Diana", "level": 3},
                        {"employee": "Eve", "level": 4}
                    ]
                ]
            }
        ]

        all_teams = [dept["teams"] for dept in departments]
        all_teams_flat = flatten_list(all_teams)
        all_employees = flatten_list(all_teams_flat)
        assert len(all_employees) == 5

        by_level = group_by_key(all_employees, "level")
        assert len(by_level[5]) == 2
        assert len(by_level[3]) == 2
        assert len(by_level[4]) == 1

        levels = [emp["level"] for emp in all_employees]
        unique_levels = remove_duplicates(levels)
        assert set(unique_levels) == {3, 4, 5}

    def test_numerical_sequence_processing(self):
        """Test processing numerical sequences with multiple utilities."""
        from utils import (
            fibonacci, is_prime, factorial, gcd,
            flatten_list, remove_duplicates, filter_none
        )

        fib_sequences = [
            [fibonacci(i) for i in range(5)],
            [fibonacci(i) for i in range(5, 8)],
            [None, fibonacci(8), fibonacci(9)]
        ]

        all_fibs = flatten_list(fib_sequences)
        clean_fibs = filter_none(all_fibs)
        unique_fibs = remove_duplicates(clean_fibs)

        prime_fibs = [n for n in unique_fibs if n > 1 and is_prime(n)]
        assert 2 in prime_fibs
        assert 3 in prime_fibs
        assert 5 in prime_fibs
        assert 13 in prime_fibs

        small_factorials = [factorial(i) for i in range(1, 6)]
        assert small_factorials == [1, 2, 6, 24, 120]

        gcd_pairs = gcd(small_factorials[-1], small_factorials[-2])
        assert gcd_pairs == 24


class TestErrorHandlingIntegration:
    """Test error handling across multiple utilities."""

    def test_math_functions_error_handling(self):
        """Test that math functions properly handle invalid inputs together."""
        from utils import fibonacci, factorial

        with pytest.raises(ValueError, match="n must be a non-negative integer"):
            fibonacci(-1)

        with pytest.raises(ValueError, match="n must be a non-negative integer"):
            factorial(-5)

    def test_empty_data_structures(self):
        """Test that utilities handle empty data structures gracefully."""
        from utils import (
            flatten_list, remove_duplicates, group_by_key, filter_none,
            count_words
        )

        assert flatten_list([]) == []
        assert remove_duplicates([]) == []
        assert group_by_key([], "any_key") == {}
        assert filter_none([]) == []
        assert count_words("") == 0

    def test_edge_cases_combined(self):
        """Test edge cases when using multiple utilities together."""
        from utils import (
            reverse_string, is_palindrome, flatten_list,
            fibonacci, gcd
        )

        empty_string = ""
        assert reverse_string(empty_string) == ""
        assert is_palindrome(empty_string) is True

        assert flatten_list([[]]) == []

        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

        assert gcd(0, 5) == 5
        assert gcd(7, 7) == 7
