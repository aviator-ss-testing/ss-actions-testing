#!/usr/bin/env python3
"""
Test Runner - Main entry point for running all unit tests.

This module provides a unified entry point for discovering and running all test files.
Uses unittest's test discovery to automatically find all test_*.py files and execute them.

Usage:
    python test_runner.py              # Run all tests
    python -m unittest discover -v     # Alternative method
"""

import sys
import unittest


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    sys.exit(not result.wasSuccessful())
