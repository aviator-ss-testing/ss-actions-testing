"""
Test runner for executing all unit tests.

This module provides a main entry point for discovering and running all test_*.py
files in the project. It configures unittest with verbosity level 2 for detailed
output and supports running either specific test modules or all tests.

Usage:
    Run all tests:
        python test_runner.py

    Run specific test module:
        python test_runner.py test_math_utils
"""

import sys
import unittest


if __name__ == '__main__':
    loader = unittest.TestLoader()
    start_dir = '.'
    pattern = 'test_*.py'

    suite = loader.discover(start_dir, pattern=pattern)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    sys.exit(not result.wasSuccessful())
