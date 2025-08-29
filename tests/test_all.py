"""
Complete Test Suite Runner

This module provides a unified interface to run all test cases
from all test modules in the test suite.
"""

import unittest
import sys
import os

# Add the parent directory to the path to import utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import all test modules
from tests.test_math_operations import TestMathOperations
from tests.test_string_utilities import TestStringUtilities  
from tests.test_data_processing import TestDataProcessing


class TestAll(unittest.TestCase):
    """Test case that runs all other test suites."""
    
    def test_run_all_suites(self):
        """Run all test suites and ensure they complete successfully."""
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        
        # Add all test cases
        suite.addTests(loader.loadTestsFromTestCase(TestMathOperations))
        suite.addTests(loader.loadTestsFromTestCase(TestStringUtilities))
        suite.addTests(loader.loadTestsFromTestCase(TestDataProcessing))
        
        # Run the tests
        runner = unittest.TextTestRunner(verbosity=0, stream=open(os.devnull, 'w'))
        result = runner.run(suite)
        
        # Assert that all tests passed
        self.assertTrue(result.wasSuccessful(), 
                       f"Test suite failed with {len(result.failures)} failures and {len(result.errors)} errors")


def create_test_suite():
    """Create a complete test suite with all test cases."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases from all modules
    suite.addTests(loader.loadTestsFromTestCase(TestMathOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestStringUtilities))
    suite.addTests(loader.loadTestsFromTestCase(TestDataProcessing))
    
    return suite


def run_all_tests():
    """Run all tests with detailed output."""
    print("Running complete test suite...")
    print("=" * 50)
    
    suite = create_test_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 50)
    print("COMPLETE TEST SUITE RESULTS")
    print("=" * 50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("✓ All tests passed successfully!")
    else:
        print("✗ Some tests failed")
        
    return result.wasSuccessful()


if __name__ == '__main__':
    # If run directly, execute all tests with detailed output
    success = run_all_tests()
    sys.exit(0 if success else 1)