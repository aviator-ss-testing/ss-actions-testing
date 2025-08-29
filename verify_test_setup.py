#!/usr/bin/env python3
"""
Test Setup Verification Script

This script verifies that all test execution methods are properly configured
and can discover and run the test suite successfully.
"""

import sys
import os
import unittest
import importlib.util


def verify_test_modules():
    """Verify that all test modules can be imported."""
    test_modules = [
        'tests.test_math_operations',
        'tests.test_string_utilities', 
        'tests.test_data_processing',
        'tests.test_all'
    ]
    
    print("Verifying test module imports...")
    for module_name in test_modules:
        try:
            module = __import__(module_name, fromlist=[''])
            print(f"  ✓ {module_name}")
        except ImportError as e:
            print(f"  ✗ {module_name}: {e}")
            return False
    
    return True


def verify_utils_modules():
    """Verify that all utils modules can be imported."""
    utils_modules = [
        'utils.math_operations',
        'utils.string_utilities',
        'utils.data_processing'
    ]
    
    print("\nVerifying utils module imports...")
    for module_name in utils_modules:
        try:
            module = __import__(module_name, fromlist=[''])
            print(f"  ✓ {module_name}")
        except ImportError as e:
            print(f"  ✗ {module_name}: {e}")
            return False
    
    return True


def verify_test_discovery():
    """Verify that unittest discovery can find all test cases."""
    print("\nVerifying test discovery...")
    
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')
    
    test_count = suite.countTestCases()
    print(f"  Total test cases discovered: {test_count}")
    
    if test_count == 0:
        print("  ✗ No tests discovered!")
        return False
    else:
        print("  ✓ Test discovery successful")
        return True


def verify_test_runner_script():
    """Verify that the custom test runner script exists and is properly formatted."""
    print("\nVerifying test runner script...")
    
    script_path = 'run_tests.py'
    if not os.path.exists(script_path):
        print(f"  ✗ {script_path} not found!")
        return False
    
    try:
        with open(script_path, 'r') as f:
            content = f.read()
            if 'run_tests_with_coverage' in content and 'main' in content:
                print("  ✓ run_tests.py is properly structured")
                return True
            else:
                print("  ✗ run_tests.py missing required functions")
                return False
    except Exception as e:
        print(f"  ✗ Error reading {script_path}: {e}")
        return False


def main():
    """Run all verification checks."""
    print("=" * 60)
    print("TEST SETUP VERIFICATION")
    print("=" * 60)
    
    # Add current directory to Python path
    sys.path.insert(0, '.')
    
    checks = [
        ("Utils Modules", verify_utils_modules),
        ("Test Modules", verify_test_modules),
        ("Test Discovery", verify_test_discovery), 
        ("Test Runner Script", verify_test_runner_script)
    ]
    
    all_passed = True
    for check_name, check_func in checks:
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ ALL VERIFICATION CHECKS PASSED")
        print("Test setup is properly configured and ready to use.")
    else:
        print("✗ SOME VERIFICATION CHECKS FAILED")
        print("Please review the errors above and fix the issues.")
    
    print("=" * 60)
    return 0 if all_passed else 1


if __name__ == '__main__':
    sys.exit(main())