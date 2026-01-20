#!/usr/bin/env python3
"""Test runner for discovering and executing all unittest test cases.

This module serves as the main entry point for running the complete test suite.
It automatically discovers all test files matching the pattern 'test_*.py' and
runs them with detailed output.

Usage:
    python test_runner.py              # Run all tests
    python -m unittest discover -v     # Alternative using unittest directly
"""

import sys
import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(not result.wasSuccessful())
