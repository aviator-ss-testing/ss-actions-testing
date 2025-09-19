#!/usr/bin/env python3
"""
Test runner script to execute all tests with proper reporting and coverage.
Supports running unit tests, integration tests, or both with different verbosity levels.
"""

import unittest
import sys
import argparse
import os
from io import StringIO


def discover_tests(test_pattern='test_*.py'):
    """Discover and return test suite for given pattern."""
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir, pattern=test_pattern)
    return suite


def create_test_suite(test_category='all'):
    """Create test suite based on category selection."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    if test_category == 'unit' or test_category == 'all':
        try:
            import test_hello
            unit_suite = loader.loadTestsFromModule(test_hello)
            suite.addTest(unit_suite)
        except ImportError:
            print("Warning: Could not import test_hello module")

    if test_category == 'integration' or test_category == 'all':
        try:
            import test_integration
            integration_suite = loader.loadTestsFromModule(test_integration)
            suite.addTest(integration_suite)
        except ImportError:
            print("Warning: Could not import test_integration module")

    return suite


def run_tests_with_reporting(suite, verbosity=1):
    """Run tests with enhanced reporting including pass/fail counts."""

    # Capture test output
    stream = StringIO()
    runner = unittest.TextTestRunner(
        stream=stream,
        verbosity=verbosity,
        buffer=True
    )

    print("Running test suite...")
    print("=" * 50)

    result = runner.run(suite)

    # Print captured output
    output = stream.getvalue()
    print(output)

    # Print summary
    print("=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped) if hasattr(result, 'skipped') else 0}")

    success_count = result.testsRun - len(result.failures) - len(result.errors)
    print(f"Successful: {success_count}")

    if result.failures:
        print("\nFAILURES:")
        print("-" * 20)
        for test, traceback in result.failures:
            print(f"FAIL: {test}")
            if verbosity > 1:
                print(traceback)
                print("-" * 20)

    if result.errors:
        print("\nERRORS:")
        print("-" * 20)
        for test, traceback in result.errors:
            print(f"ERROR: {test}")
            if verbosity > 1:
                print(traceback)
                print("-" * 20)

    print("=" * 50)

    # Return success status
    return len(result.failures) == 0 and len(result.errors) == 0


def main():
    """Main function with CLI interface for test execution."""
    parser = argparse.ArgumentParser(
        description='Run Python utility function tests with reporting',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_tests.py                    # Run all tests with normal verbosity
  python run_tests.py --unit             # Run only unit tests
  python run_tests.py --integration      # Run only integration tests
  python run_tests.py -v                 # Run all tests with high verbosity
  python run_tests.py --quiet            # Run all tests with minimal output
  python run_tests.py --discover         # Use test discovery instead of imports
        """
    )

    # Test category options
    test_group = parser.add_mutually_exclusive_group()
    test_group.add_argument(
        '--unit',
        action='store_true',
        help='Run only unit tests (test_hello.py)'
    )
    test_group.add_argument(
        '--integration',
        action='store_true',
        help='Run only integration tests (test_integration.py)'
    )

    # Verbosity options
    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Verbose output (verbosity level 2)'
    )
    verbosity_group.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Quiet output (verbosity level 0)'
    )

    # Discovery option
    parser.add_argument(
        '--discover',
        action='store_true',
        help='Use test discovery to find all test files automatically'
    )

    # Pattern for discovery
    parser.add_argument(
        '--pattern',
        default='test_*.py',
        help='Pattern for test discovery (default: test_*.py)'
    )

    args = parser.parse_args()

    # Determine verbosity level
    if args.verbose:
        verbosity = 2
    elif args.quiet:
        verbosity = 0
    else:
        verbosity = 1

    # Determine test category
    if args.unit:
        test_category = 'unit'
    elif args.integration:
        test_category = 'integration'
    else:
        test_category = 'all'

    try:
        if args.discover:
            print(f"Using test discovery with pattern: {args.pattern}")
            suite = discover_tests(args.pattern)
        else:
            print(f"Running {test_category} tests...")
            suite = create_test_suite(test_category)

        if suite.countTestCases() == 0:
            print("No tests found!")
            return 1

        print(f"Found {suite.countTestCases()} test(s)")

        success = run_tests_with_reporting(suite, verbosity)

        if success:
            print("All tests passed!")
            return 0
        else:
            print("Some tests failed!")
            return 1

    except Exception as e:
        print(f"Error running tests: {e}")
        return 1


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)