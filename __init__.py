"""
Python Utilities Package

A comprehensive collection of mathematical operations, utility functions, and decorators
for common programming tasks. This package demonstrates proper Python module structure,
comprehensive testing, and decorator usage patterns.

Modules:
    math_ops: Mathematical operations including basic arithmetic and advanced functions
    utils: String manipulation, list processing, and data validation utilities
    decorators: Function decorators for timing, logging, retry, validation, and caching

Example:
    >>> import math_ops
    >>> math_ops.factorial(5)
    120

    >>> from utils import is_palindrome
    >>> is_palindrome('racecar')
    True

    >>> from decorators import timer
    >>> @timer
    ... def my_function():
    ...     return sum(range(1000))
"""

__version__ = "1.0.0"
__author__ = "Aviator"

# Expose key modules for easier importing
__all__ = [
    "math_ops",
    "utils",
    "decorators",
]
