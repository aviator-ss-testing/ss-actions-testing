"""
Test runner configuration for discovering and running all test modules.

This module serves as the main entry point for running the test suite.
It uses unittest's test discovery to automatically find and run all test_*.py files.
"""

import sys
import unittest


if __name__ == '__main__':
    loader = unittest.TestLoader()
    start_dir = '.'
    suite = loader.discover(start_dir, pattern='test_*.py')

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    sys.exit(not result.wasSuccessful())
