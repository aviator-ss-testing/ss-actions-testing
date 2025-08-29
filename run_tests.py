#!/usr/bin/env python3
"""
Test Runner Script

Executes all tests with proper reporting and basic coverage analysis.
Provides a unified interface for running the complete test suite.
"""

import sys
import unittest
import os
import time
from io import StringIO


def run_tests_with_coverage():
    """Run all tests and provide basic coverage reporting."""
    print("=" * 60)
    print("PYTHON UTILITIES TEST RUNNER")
    print("=" * 60)
    
    # Add current directory to Python path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, current_dir)
    
    # Discover and run tests
    loader = unittest.TestLoader()
    start_dir = os.path.join(current_dir, 'tests')
    
    print(f"Discovering tests in: {start_dir}")
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Count total tests
    total_tests = suite.countTestCases()
    print(f"Total tests found: {total_tests}")
    print("-" * 60)
    
    # Run tests with detailed output
    stream = StringIO()
    runner = unittest.TextTestRunner(
        stream=stream,
        verbosity=2,
        failfast=False,
        buffer=True
    )
    
    start_time = time.time()
    result = runner.run(suite)
    end_time = time.time()
    
    # Print detailed results
    output = stream.getvalue()
    print(output)
    
    # Summary report
    print("=" * 60)
    print("TEST EXECUTION SUMMARY")
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped) if hasattr(result, 'skipped') else 0}")
    print(f"Execution time: {end_time - start_time:.2f} seconds")
    
    # Success rate
    success_rate = ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100) if result.testsRun > 0 else 0
    print(f"Success rate: {success_rate:.1f}%")
    
    # Show failures and errors if any
    if result.failures:
        print("\n" + "=" * 60)
        print("FAILURES:")
        print("=" * 60)
        for test, traceback in result.failures:
            print(f"\n{test}:")
            print(traceback)
    
    if result.errors:
        print("\n" + "=" * 60)
        print("ERRORS:")
        print("=" * 60)
        for test, traceback in result.errors:
            print(f"\n{test}:")
            print(traceback)
    
    # Basic coverage reporting
    print("\n" + "=" * 60)
    print("BASIC COVERAGE ANALYSIS")
    print("=" * 60)
    
    # Check which modules are being tested
    tested_modules = set()
    utils_dir = os.path.join(current_dir, 'utils')
    
    if os.path.exists(utils_dir):
        for filename in os.listdir(utils_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                tested_modules.add(module_name)
        
        print("Modules with test coverage:")
        for module in sorted(tested_modules):
            test_file = os.path.join(current_dir, 'tests', f'test_{module}.py')
            if os.path.exists(test_file):
                print(f"  ✓ {module}")
            else:
                print(f"  ✗ {module} (no test file found)")
    
    print("\n" + "=" * 60)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


def main():
    """Main entry point for the test runner."""
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help']:
            print("Usage: python run_tests.py [options]")
            print()
            print("Options:")
            print("  -h, --help     Show this help message")
            print("  --discover     Run test discovery only (same as default)")
            print()
            print("This script runs all tests in the tests/ directory with detailed reporting.")
            return 0
        elif sys.argv[1] == '--discover':
            pass  # Default behavior
    
    return run_tests_with_coverage()


if __name__ == '__main__':
    sys.exit(main())