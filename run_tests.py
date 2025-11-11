#!/usr/bin/env python3
"""
Test runner script for Python utilities test suite.

This script provides an easy entry point for running all tests in the project.
Run with: python run_tests.py
"""

import sys
import unittest


def run_tests(verbosity=2):
    """
    Discover and run all tests in the tests/ directory.

    Args:
        verbosity (int): Level of test output detail (0=quiet, 1=normal, 2=verbose)

    Returns:
        unittest.TestResult: Results of the test run
    """
    loader = unittest.TestLoader()

    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')

    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)

    return result


if __name__ == '__main__':
    verbosity = 2

    if len(sys.argv) > 1:
        if sys.argv[1] in ['-v', '--verbose']:
            verbosity = 2
        elif sys.argv[1] in ['-q', '--quiet']:
            verbosity = 0
        elif sys.argv[1] in ['-h', '--help']:
            print("Usage: python run_tests.py [options]")
            print("Options:")
            print("  -v, --verbose    Verbose output (default)")
            print("  -q, --quiet      Minimal output")
            print("  -h, --help       Show this help message")
            sys.exit(0)

    print("Running Python utilities test suite...")
    print("=" * 70)

    result = run_tests(verbosity=verbosity)

    print("=" * 70)
    print(f"\nTests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")

    if result.wasSuccessful():
        print("\n✓ All tests passed successfully!")
        sys.exit(0)
    else:
        print("\n✗ Some tests failed.")
        sys.exit(1)
