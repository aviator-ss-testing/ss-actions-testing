"""
Main entry point for running all tests.

This test runner uses unittest's test discovery to automatically find and run
all test files matching the pattern 'test_*.py' in the current directory.
"""

import sys
import unittest


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    sys.exit(not result.wasSuccessful())
