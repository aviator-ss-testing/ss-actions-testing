"""
Python utility functions package.

This package provides various utility functions for mathematical operations,
string manipulation, and data processing.
"""

__version__ = "1.0.0"
__author__ = "Utility Functions Package"
__description__ = "A comprehensive collection of utility functions for mathematical operations, string manipulation, and data processing"

# Import individual modules
from . import math_operations
from . import string_utilities
from . import data_processing

# Import all public functions from each module for direct access
from .math_operations import (
    calculate_factorial,
    is_prime,
    fibonacci_sequence,
    greatest_common_divisor,
    least_common_multiple,
    calculate_mean,
    calculate_median,
    calculate_mode,
    calculate_variance,
    calculate_standard_deviation,
    sum_of_divisors,
    is_perfect_number
)

from .string_utilities import (
    reverse_string,
    is_palindrome,
    remove_duplicates,
    capitalize_words,
    count_vowels,
    count_consonants,
    extract_numbers,
    is_valid_email,
    is_valid_phone,
    count_word_frequency,
    longest_common_substring,
    sanitize_string
)

from .data_processing import (
    flatten_list,
    merge_dictionaries,
    remove_duplicates_preserve_order,
    find_common_elements,
    csv_string_to_dict,
    dict_to_csv_string,
    normalize_data,
    chunk_list
)

# Define what gets imported when using "from utils import *"
__all__ = [
    # Module exports
    'math_operations',
    'string_utilities',
    'data_processing',
    
    # Mathematical operations
    'calculate_factorial',
    'is_prime',
    'fibonacci_sequence',
    'greatest_common_divisor',
    'least_common_multiple',
    'calculate_mean',
    'calculate_median',
    'calculate_mode',
    'calculate_variance',
    'calculate_standard_deviation',
    'sum_of_divisors',
    'is_perfect_number',
    
    # String utilities
    'reverse_string',
    'is_palindrome',
    'remove_duplicates',
    'capitalize_words',
    'count_vowels',
    'count_consonants',
    'extract_numbers',
    'is_valid_email',
    'is_valid_phone',
    'count_word_frequency',
    'longest_common_substring',
    'sanitize_string',
    
    # Data processing
    'flatten_list',
    'merge_dictionaries',
    'remove_duplicates_preserve_order',
    'find_common_elements',
    'csv_string_to_dict',
    'dict_to_csv_string',
    'normalize_data',
    'chunk_list'
]