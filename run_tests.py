"""Test runner script for executing all tests in the tests/ directory."""

import sys
import unittest


def run_tests():
    """Discover and run all tests in the tests/ directory.

    Returns:
        int: Exit code (0 for success, 1 for failure)
    """
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(run_tests())
