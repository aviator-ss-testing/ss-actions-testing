#!/usr/bin/env python3
"""
Validation script to check that the test file is properly structured and importable.
"""

import sys
import os
import unittest

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

def validate_test_structure():
    """Validate that the test file is properly structured."""
    try:
        # Import the test module
        from tests import test_math_operations
        print("✓ Successfully imported test_math_operations module")
        
        # Check that TestMathOperations class exists
        test_class = test_math_operations.TestMathOperations
        print("✓ TestMathOperations class found")
        
        # Count test methods
        test_methods = [method for method in dir(test_class) if method.startswith('test_')]
        print(f"✓ Found {len(test_methods)} test methods")
        
        # Check that all mathematical functions are tested
        expected_functions = [
            'calculate_factorial',
            'is_prime', 
            'fibonacci_sequence',
            'greatest_common_divisor',
            'least_common_multiple',
            'calculate_mean',
            'calculate_median',
            'calculate_mode',
            'calculate_variance',
            'calculate_standard_deviation',
            'sum_of_divisors',
            'is_perfect_number'
        ]
        
        functions_covered = set()
        for method in test_methods:
            for func in expected_functions:
                if func in method:
                    functions_covered.add(func)
                    break
        
        print(f"✓ Functions with test coverage: {len(functions_covered)}/{len(expected_functions)}")
        
        if len(functions_covered) == len(expected_functions):
            print("✓ All mathematical functions have test coverage")
        else:
            missing = set(expected_functions) - functions_covered
            print(f"⚠ Missing coverage for: {missing}")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Validation error: {e}")
        return False

def count_test_cases():
    """Count the number of test cases for coverage analysis."""
    try:
        # Load and run the test suite to count tests
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromName('tests.test_math_operations')
        
        test_count = suite.countTestCases()
        print(f"✓ Total test cases: {test_count}")
        
        return test_count > 0
        
    except Exception as e:
        print(f"✗ Error counting test cases: {e}")
        return False

if __name__ == "__main__":
    print("Validating test_math_operations.py structure...")
    print("=" * 50)
    
    structure_ok = validate_test_structure()
    count_ok = count_test_cases()
    
    print("=" * 50)
    if structure_ok and count_ok:
        print("✓ Validation successful - test file is properly structured")
    else:
        print("✗ Validation failed - check errors above")