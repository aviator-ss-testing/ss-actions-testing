"""
Test Configuration

Provides configuration settings for test discovery and execution.
This file helps ensure consistent test execution across different environments.
"""

import unittest
import sys
import os

# Test discovery settings
TEST_DIR = 'tests'
TEST_PATTERN = 'test_*.py'
TOP_LEVEL_DIR = '.'

# Coverage settings
COVERAGE_MODULES = [
    'utils.math_operations',
    'utils.string_utilities', 
    'utils.data_processing'
]

def get_test_suite():
    """Get the complete test suite using discovery."""
    loader = unittest.TestLoader()
    suite = loader.discover(TEST_DIR, pattern=TEST_PATTERN, top_level_dir=TOP_LEVEL_DIR)
    return suite

def run_tests_from_command_line():
    """Run tests when called from command line with proper configuration."""
    # Ensure current directory is in Python path
    if '.' not in sys.path:
        sys.path.insert(0, '.')
    
    # Use test discovery
    suite = get_test_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return appropriate exit code
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(run_tests_from_command_line())