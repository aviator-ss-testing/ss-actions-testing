"""
Python Math Functions and Testing Framework

A modular Python project providing mathematical operations, string utilities, and list processing
functions with comprehensive test coverage. Designed for integration testing scenarios.

Modules:
    math_operations: Basic mathematical operations (add, subtract, multiply, divide, power, factorial)
    string_utils: String manipulation functions (reverse, count vowels, palindrome check, capitalize)
    list_operations: List processing functions (find max/min, average, remove duplicates, sort)
"""

from . import math_operations
from . import string_utils
from . import list_operations

__version__ = "1.0.0"
__all__ = ["math_operations", "string_utils", "list_operations"]