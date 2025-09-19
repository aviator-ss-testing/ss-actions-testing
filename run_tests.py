#!/usr/bin/env python3
"""
Test Runner for Python Math Functions and Testing Framework

This script provides comprehensive test execution capabilities with integration-friendly
reporting and selective test suite execution.
"""

import unittest
import sys
import os
import time
from io import StringIO
from typing import List, Optional, Dict, Any


class IntegrationTestResult(unittest.TextTestResult):
    """Custom test result class that provides integration-friendly output formatting."""

    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.test_results = []
        self.start_time = None
        self.end_time = None

    def startTest(self, test):
        super().startTest(test)
        self.start_time = time.time()

    def stopTest(self, test):
        super().stopTest(test)
        self.end_time = time.time()
        duration = self.end_time - self.start_time

        status = "PASS"
        error_message = None

        if self.failures:
            for failure_test, failure_message in self.failures:
                if failure_test == test:
                    status = "FAIL"
                    error_message = failure_message
                    break

        if self.errors:
            for error_test, error_message in self.errors:
                if error_test == test:
                    status = "ERROR"
                    error_message = error_message
                    break

        if self.skipped:
            for skip_test, skip_reason in self.skipped:
                if skip_test == test:
                    status = "SKIP"
                    error_message = skip_reason
                    break

        self.test_results.append({
            'test': str(test),
            'status': status,
            'duration': duration,
            'error_message': error_message
        })


class IntegrationTestRunner:
    """Test runner with integration-friendly reporting and selective execution."""

    def __init__(self, verbosity: int = 2):
        self.verbosity = verbosity
        self.test_results = []

    def discover_tests(self, test_dir: str = "tests", pattern: str = "test*.py") -> unittest.TestSuite:
        """Discover all tests in the specified directory."""
        loader = unittest.TestLoader()
        suite = loader.discover(test_dir, pattern=pattern)
        return suite

    def run_specific_module(self, module_name: str) -> unittest.TestResult:
        """Run tests for a specific module."""
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromName(f"tests.{module_name}")
        return self._run_suite(suite)

    def run_all_tests(self) -> unittest.TestResult:
        """Run all discovered tests."""
        suite = self.discover_tests()
        return self._run_suite(suite)

    def _run_suite(self, suite: unittest.TestSuite) -> unittest.TestResult:
        """Execute a test suite with custom result reporting."""
        stream = StringIO()
        runner = unittest.TextTestRunner(
            stream=stream,
            verbosity=self.verbosity,
            resultclass=IntegrationTestResult
        )
        result = runner.run(suite)
        return result

    def print_summary(self, result: unittest.TestResult) -> None:
        """Print a comprehensive test summary."""
        print("\n" + "="*70)
        print("TEST EXECUTION SUMMARY")
        print("="*70)

        total_tests = result.testsRun
        failures = len(result.failures)
        errors = len(result.errors)
        skipped = len(result.skipped) if hasattr(result, 'skipped') else 0
        passed = total_tests - failures - errors - skipped

        print(f"Total Tests:    {total_tests}")
        print(f"Passed:         {passed}")
        print(f"Failed:         {failures}")
        print(f"Errors:         {errors}")
        print(f"Skipped:        {skipped}")

        success_rate = (passed / total_tests * 100) if total_tests > 0 else 0
        print(f"Success Rate:   {success_rate:.1f}%")

        if hasattr(result, 'test_results'):
            total_duration = sum(r['duration'] for r in result.test_results)
            print(f"Total Duration: {total_duration:.3f}s")

        print("\nOVERALL STATUS:", end=" ")
        if failures == 0 and errors == 0:
            print("✅ ALL TESTS PASSED")
        else:
            print("❌ TESTS FAILED")

        print("="*70)

    def print_detailed_results(self, result: unittest.TestResult) -> None:
        """Print detailed test results for integration monitoring."""
        if not hasattr(result, 'test_results'):
            return

        print("\nDETAILED TEST RESULTS")
        print("-" * 70)

        for test_result in result.test_results:
            status_symbol = {
                'PASS': '✅',
                'FAIL': '❌',
                'ERROR': '💥',
                'SKIP': '⏭️'
            }.get(test_result['status'], '?')

            print(f"{status_symbol} {test_result['status']:<6} {test_result['test']:<50} {test_result['duration']:.3f}s")

            if test_result['error_message']:
                print(f"   Error: {test_result['error_message'].splitlines()[0]}")

        print("-" * 70)

    def run_with_reporting(self, test_selection: Optional[str] = None) -> bool:
        """Run tests with comprehensive reporting and return success status."""
        print("Python Math Functions Test Runner")
        print("=" * 50)

        if test_selection:
            print(f"Running tests for module: {test_selection}")
            result = self.run_specific_module(test_selection)
        else:
            print("Running all tests...")
            result = self.run_all_tests()

        # Print detailed results if available
        if hasattr(result, 'test_results') and self.verbosity >= 2:
            self.print_detailed_results(result)

        # Print summary
        self.print_summary(result)

        # Print failure details
        if result.failures:
            print("\nFAILURE DETAILS:")
            print("-" * 50)
            for test, traceback in result.failures:
                print(f"FAILED: {test}")
                print(traceback)
                print("-" * 50)

        if result.errors:
            print("\nERROR DETAILS:")
            print("-" * 50)
            for test, traceback in result.errors:
                print(f"ERROR: {test}")
                print(traceback)
                print("-" * 50)

        # Return success status for integration systems
        return len(result.failures) == 0 and len(result.errors) == 0


def main():
    """Main entry point for the test runner."""
    import argparse

    parser = argparse.ArgumentParser(description="Run tests with integration-friendly reporting")
    parser.add_argument(
        "--module", "-m",
        help="Run tests for specific module (e.g., test_math_operations)",
        default=None
    )
    parser.add_argument(
        "--verbosity", "-v",
        type=int,
        choices=[0, 1, 2],
        default=2,
        help="Test output verbosity (0=quiet, 1=normal, 2=verbose)"
    )
    parser.add_argument(
        "--list-tests", "-l",
        action="store_true",
        help="List all available tests without running them"
    )

    args = parser.parse_args()

    # Ensure we can import from the current directory
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

    runner = IntegrationTestRunner(verbosity=args.verbosity)

    if args.list_tests:
        print("Available test modules:")
        test_files = [f for f in os.listdir("tests") if f.startswith("test_") and f.endswith(".py")]
        for test_file in sorted(test_files):
            module_name = test_file[:-3]  # Remove .py extension
            print(f"  - {module_name}")
        return 0

    try:
        success = runner.run_with_reporting(args.module)
        return 0 if success else 1
    except Exception as e:
        print(f"Test runner failed with error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())