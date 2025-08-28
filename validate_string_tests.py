#!/usr/bin/env python3
"""
Validation script to check that the string utilities test file is properly structured and importable.
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

def validate_string_test_structure():
    """Validate that the string utilities test file is properly structured."""
    try:
        # Import the test module
        from tests import test_string_utilities
        print("✓ Successfully imported test_string_utilities module")
        
        # Check that TestStringUtilities class exists
        test_class = test_string_utilities.TestStringUtilities
        print("✓ TestStringUtilities class found")
        
        # Count test methods
        test_methods = [method for method in dir(test_class) if method.startswith('test_')]
        print(f"✓ Found {len(test_methods)} test methods")
        
        # Check that all string utility functions are tested
        expected_functions = [
            'reverse_string',
            'is_palindrome', 
            'remove_duplicates',
            'capitalize_words',
            'count_vowels',
            'count_consonants',
            'extract_numbers',
            'is_valid_email',
            'is_valid_phone',
            'count_word_frequency',
            'longest_common_substring',
            'sanitize_string'
        ]
        
        functions_covered = set()
        for method in test_methods:
            for func in expected_functions:
                if func in method:
                    functions_covered.add(func)
                    break
        
        print(f"✓ Functions with test coverage: {len(functions_covered)}/{len(expected_functions)}")
        
        if len(functions_covered) == len(expected_functions):
            print("✓ All string utility functions have test coverage")
        else:
            missing = set(expected_functions) - functions_covered
            print(f"⚠ Missing coverage for: {missing}")
        
        # Check for special test categories
        special_tests = ['performance', 'unicode', 'edge_cases']
        special_found = []
        for special in special_tests:
            if any(special in method for method in test_methods):
                special_found.append(special)
        
        print(f"✓ Special test categories found: {special_found}")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Validation error: {e}")
        return False

if __name__ == "__main__":
    print("Validating test_string_utilities.py structure...")
    print("=" * 50)
    
    structure_ok = validate_string_test_structure()
    
    print("=" * 50)
    if structure_ok:
        print("✓ Validation successful - string utilities test file is properly structured")
    else:
        print("✗ Validation failed - check errors above")