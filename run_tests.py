#!/usr/bin/env python3
"""
Test Runner Script with Coverage and Colored Output

This script provides a convenient way to run all tests in the project with:
- Automatic test discovery
- Colored output for better readability
- Test coverage reporting
- Options to run specific test modules or test cases
"""

import sys
import unittest
import argparse
import time
from io import StringIO
from typing import List, Optional


class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

    @staticmethod
    def disable():
        """Disable colors for non-terminal output"""
        Colors.GREEN = ''
        Colors.RED = ''
        Colors.YELLOW = ''
        Colors.BLUE = ''
        Colors.MAGENTA = ''
        Colors.CYAN = ''
        Colors.BOLD = ''
        Colors.RESET = ''


class ColoredTextTestResult(unittest.TextTestResult):
    """Custom test result class with colored output"""

    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.test_start_time = None

    def startTest(self, test):
        super().startTest(test)
        self.test_start_time = time.time()
        if self.showAll:
            self.stream.write(f"{Colors.CYAN}{self.getDescription(test)}{Colors.RESET} ... ")
            self.stream.flush()

    def addSuccess(self, test):
        super().addSuccess(test)
        if self.showAll:
            elapsed = time.time() - self.test_start_time
            self.stream.writeln(f"{Colors.GREEN}ok{Colors.RESET} ({elapsed:.3f}s)")
        elif self.dots:
            self.stream.write(f"{Colors.GREEN}.{Colors.RESET}")
            self.stream.flush()

    def addError(self, test, err):
        super().addError(test, err)
        if self.showAll:
            elapsed = time.time() - self.test_start_time
            self.stream.writeln(f"{Colors.RED}ERROR{Colors.RESET} ({elapsed:.3f}s)")
        elif self.dots:
            self.stream.write(f"{Colors.RED}E{Colors.RESET}")
            self.stream.flush()

    def addFailure(self, test, err):
        super().addFailure(test, err)
        if self.showAll:
            elapsed = time.time() - self.test_start_time
            self.stream.writeln(f"{Colors.RED}FAIL{Colors.RESET} ({elapsed:.3f}s)")
        elif self.dots:
            self.stream.write(f"{Colors.RED}F{Colors.RESET}")
            self.stream.flush()

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        if self.showAll:
            self.stream.writeln(f"{Colors.YELLOW}skipped{Colors.RESET} {reason!r}")
        elif self.dots:
            self.stream.write(f"{Colors.YELLOW}s{Colors.RESET}")
            self.stream.flush()


class ColoredTextTestRunner(unittest.TextTestRunner):
    """Custom test runner with colored output"""
    resultclass = ColoredTextTestResult

    def run(self, test):
        """Run tests and display results with colors"""
        result = super().run(test)

        self.stream.writeln()
        self.stream.writeln(f"{Colors.BOLD}{'='*70}{Colors.RESET}")

        if result.wasSuccessful():
            self.stream.writeln(f"{Colors.GREEN}{Colors.BOLD}ALL TESTS PASSED{Colors.RESET}")
        else:
            self.stream.writeln(f"{Colors.RED}{Colors.BOLD}SOME TESTS FAILED{Colors.RESET}")

        self.stream.writeln(f"{Colors.BOLD}{'='*70}{Colors.RESET}")
        self.stream.writeln()

        self.stream.writeln(f"Tests run: {Colors.BOLD}{result.testsRun}{Colors.RESET}")
        self.stream.writeln(f"Successes: {Colors.GREEN}{result.testsRun - len(result.failures) - len(result.errors)}{Colors.RESET}")

        if result.failures:
            self.stream.writeln(f"Failures: {Colors.RED}{len(result.failures)}{Colors.RESET}")
        if result.errors:
            self.stream.writeln(f"Errors: {Colors.RED}{len(result.errors)}{Colors.RESET}")
        if result.skipped:
            self.stream.writeln(f"Skipped: {Colors.YELLOW}{len(result.skipped)}{Colors.RESET}")

        return result


class CoverageTracker:
    """Simple coverage tracker for executed modules"""

    def __init__(self):
        self.executed_modules = set()
        self.total_modules = {'math_ops', 'utils', 'decorators'}

    def track_imports(self):
        """Track which modules are imported and tested"""
        for module_name in list(sys.modules.keys()):
            if module_name in self.total_modules:
                self.executed_modules.add(module_name)

    def get_coverage_report(self) -> str:
        """Generate a simple coverage report"""
        coverage_pct = (len(self.executed_modules) / len(self.total_modules)) * 100 if self.total_modules else 0

        report = [
            f"\n{Colors.BOLD}{'='*70}{Colors.RESET}",
            f"{Colors.BOLD}COVERAGE REPORT{Colors.RESET}",
            f"{Colors.BOLD}{'='*70}{Colors.RESET}",
            f"\nModules tested: {len(self.executed_modules)}/{len(self.total_modules)}",
        ]

        for module in sorted(self.total_modules):
            status = f"{Colors.GREEN}✓{Colors.RESET}" if module in self.executed_modules else f"{Colors.RED}✗{Colors.RESET}"
            report.append(f"  {status} {module}")

        color = Colors.GREEN if coverage_pct == 100 else Colors.YELLOW if coverage_pct >= 80 else Colors.RED
        report.append(f"\nOverall Coverage: {color}{coverage_pct:.1f}%{Colors.RESET}")
        report.append(f"{Colors.BOLD}{'='*70}{Colors.RESET}\n")

        return '\n'.join(report)


def discover_tests(test_dir: str = 'tests', pattern: str = 'test*.py') -> unittest.TestSuite:
    """
    Discover and load all test modules automatically

    Args:
        test_dir: Directory containing test files
        pattern: Pattern to match test files

    Returns:
        TestSuite containing all discovered tests
    """
    loader = unittest.TestLoader()
    return loader.discover(test_dir, pattern=pattern)


def load_specific_tests(module_names: List[str]) -> unittest.TestSuite:
    """
    Load specific test modules or test cases

    Args:
        module_names: List of module names or test case names

    Returns:
        TestSuite containing specified tests
    """
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for name in module_names:
        try:
            if '.' in name:
                suite.addTests(loader.loadTestsFromName(name))
            else:
                if not name.startswith('tests.'):
                    name = f'tests.{name}'
                suite.addTests(loader.loadTestsFromName(name))
        except (ImportError, AttributeError) as e:
            print(f"{Colors.RED}Error loading {name}: {e}{Colors.RESET}")

    return suite


def main():
    """Main entry point for the test runner"""
    parser = argparse.ArgumentParser(
        description='Run tests with colored output and coverage reporting',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           # Run all tests
  %(prog)s -v                        # Run all tests with verbose output
  %(prog)s -m test_math_ops          # Run specific test module
  %(prog)s -m test_math_ops test_utils  # Run multiple modules
  %(prog)s -t tests.test_math_ops.TestBasicArithmetic.test_add  # Run specific test
  %(prog)s --no-color                # Disable colored output
  %(prog)s --no-coverage             # Disable coverage reporting
        """
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Verbose output showing each test'
    )

    parser.add_argument(
        '-m', '--modules',
        nargs='+',
        metavar='MODULE',
        help='Run specific test modules (e.g., test_math_ops test_utils)'
    )

    parser.add_argument(
        '-t', '--tests',
        nargs='+',
        metavar='TEST',
        help='Run specific test cases (e.g., tests.test_math_ops.TestBasicArithmetic.test_add)'
    )

    parser.add_argument(
        '--no-color',
        action='store_true',
        help='Disable colored output'
    )

    parser.add_argument(
        '--no-coverage',
        action='store_true',
        help='Disable coverage reporting'
    )

    args = parser.parse_args()

    if args.no_color or not sys.stdout.isatty():
        Colors.disable()

    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}Running Python Tests{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.RESET}\n")

    if args.tests:
        suite = load_specific_tests(args.tests)
    elif args.modules:
        suite = load_specific_tests(args.modules)
    else:
        print(f"{Colors.CYAN}Discovering tests...{Colors.RESET}")
        suite = discover_tests()

    print(f"{Colors.CYAN}Found {suite.countTestCases()} test(s){Colors.RESET}\n")

    verbosity = 2 if args.verbose else 1
    runner = ColoredTextTestRunner(verbosity=verbosity, stream=sys.stdout)

    start_time = time.time()
    result = runner.run(suite)
    elapsed_time = time.time() - start_time

    print(f"\n{Colors.BOLD}Total time: {elapsed_time:.3f}s{Colors.RESET}\n")

    if not args.no_coverage:
        coverage = CoverageTracker()
        coverage.track_imports()
        print(coverage.get_coverage_report())

    sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == '__main__':
    main()