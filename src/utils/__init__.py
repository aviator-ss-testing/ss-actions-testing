"""
Utility functions package.

This package provides various utility functions for common operations
including string manipulation, data processing, and mathematical operations.
"""

from .string_utils import (
    reverse_string,
    is_palindrome,
    title_case,
    count_words,
)

from .data_utils import (
    flatten_list,
    remove_duplicates,
    group_by_key,
    filter_none,
)

from .math_utils import (
    fibonacci,
    is_prime,
    factorial,
    gcd,
)

__all__ = [
    "reverse_string",
    "is_palindrome",
    "title_case",
    "count_words",
    "flatten_list",
    "remove_duplicates",
    "group_by_key",
    "filter_none",
    "fibonacci",
    "is_prime",
    "factorial",
    "gcd",
]
