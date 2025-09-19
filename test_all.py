#!/usr/bin/env python3
"""
Sequential test suite runner.
Imports and runs all test suites individually with detailed reporting.
"""

import unittest
import sys
import time


def run_test_module(module_name):
    """
    Run a specific test module and return results.

    Args:
        module_name (str): Name of the test module to run

    Returns:
        tuple: (success, tests_run, failures, errors, duration)
    """
    print(f"\n{'='*50}")
    print(f"RUNNING: {module_name}")
    print(f"{'='*50}")

    start_time = time.time()

    try:
        # Import the test module
        test_module = __import__(module_name)

        # Create test suite from the module
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(test_module)

        # Run the tests
        runner = unittest.TextTestRunner(
            verbosity=2,
            stream=sys.stdout
        )
        result = runner.run(suite)

        end_time = time.time()
        duration = end_time - start_time

        # Print module summary
        print(f"\n{'-'*50}")
        print(f"MODULE SUMMARY: {module_name}")
        print(f"Tests run: {result.testsRun}")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        print(f"Duration: {duration:.3f} seconds")
        print(f"Status: {'PASSED' if result.wasSuccessful() else 'FAILED'}")
        print(f"{'-'*50}")

        return (
            result.wasSuccessful(),
            result.testsRun,
            len(result.failures),
            len(result.errors),
            duration
        )

    except ImportError as e:
        print(f"ERROR: Could not import {module_name}: {e}")
        return False, 0, 0, 1, 0
    except Exception as e:
        print(f"ERROR: Unexpected error running {module_name}: {e}")
        return False, 0, 0, 1, 0


def main():
    """Main function to run all test suites sequentially."""
    print("SEQUENTIAL TEST SUITE RUNNER")
    print("="*70)
    print("Running all test modules in sequence...")

    # List of test modules to run
    test_modules = [
        'test_math_ops',
        'test_utils'
    ]

    # Track overall results
    overall_start_time = time.time()
    total_tests = 0
    total_failures = 0
    total_errors = 0
    failed_modules = []
    module_results = []

    # Run each test module
    for module in test_modules:
        success, tests_run, failures, errors, duration = run_test_module(module)

        total_tests += tests_run
        total_failures += failures
        total_errors += errors

        module_results.append({
            'name': module,
            'success': success,
            'tests_run': tests_run,
            'failures': failures,
            'errors': errors,
            'duration': duration
        })

        if not success:
            failed_modules.append(module)

    overall_end_time = time.time()
    overall_duration = overall_end_time - overall_start_time

    # Print final summary
    print(f"\n{'='*70}")
    print("FINAL TEST EXECUTION SUMMARY")
    print(f"{'='*70}")

    print(f"Total modules tested: {len(test_modules)}")
    print(f"Total tests run: {total_tests}")
    print(f"Total failures: {total_failures}")
    print(f"Total errors: {total_errors}")
    print(f"Total duration: {overall_duration:.3f} seconds")

    # Print per-module results
    print(f"\nPER-MODULE RESULTS:")
    print(f"{'-'*70}")
    for result in module_results:
        status = "PASS" if result['success'] else "FAIL"
        print(f"{result['name']:<20} | {status:<4} | "
              f"Tests: {result['tests_run']:<3} | "
              f"Failures: {result['failures']:<2} | "
              f"Errors: {result['errors']:<2} | "
              f"Time: {result['duration']:.3f}s")

    # Print failed modules if any
    if failed_modules:
        print(f"\nFAILED MODULES:")
        print(f"{'-'*70}")
        for module in failed_modules:
            print(f"✗ {module}")

    # Print overall status
    print(f"\n{'='*70}")
    if len(failed_modules) == 0:
        print("OVERALL RESULT: ✓ ALL TEST MODULES PASSED")
        success_rate = 100.0
    else:
        print(f"OVERALL RESULT: ✗ {len(failed_modules)} MODULE(S) FAILED")
        success_rate = ((len(test_modules) - len(failed_modules)) / len(test_modules)) * 100

    if total_tests > 0:
        test_success_rate = ((total_tests - total_failures - total_errors) / total_tests) * 100
        print(f"Module success rate: {success_rate:.1f}%")
        print(f"Test success rate: {test_success_rate:.1f}%")

    print(f"{'='*70}")

    # Exit with appropriate code
    sys.exit(0 if len(failed_modules) == 0 else 1)


if __name__ == '__main__':
    main()