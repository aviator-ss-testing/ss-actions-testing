#!/usr/bin/env python3
"""
Simple validation script to check that all test modules can be imported
and basic functionality works.
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def validate_imports():
    """Validate that all modules and test modules can be imported."""
    print("Validating module imports...")

    try:
        # Test core modules
        import math_operations
        import string_utils
        import data_utils
        print("✓ All core modules imported successfully")

        # Test test modules
        from tests import test_math_operations
        from tests import test_string_utils
        from tests import test_data_utils
        print("✓ All test modules imported successfully")

        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def validate_basic_functionality():
    """Test basic functionality of a few key functions."""
    print("\nValidating basic functionality...")

    try:
        # Test a few functions from each module
        from math_operations import add_numbers
        from string_utils import reverse_string
        from data_utils import flatten_list

        # Basic functionality tests
        assert add_numbers(2, 3) == 5
        assert reverse_string("hello") == "olleh"
        assert flatten_list([1, [2, 3]]) == [1, 2, 3]

        print("✓ Basic functionality validation passed")
        return True
    except Exception as e:
        print(f"✗ Functionality test failed: {e}")
        return False

def main():
    """Run all validation checks."""
    print("=" * 50)
    print("TEST VALIDATION SCRIPT")
    print("=" * 50)

    import_success = validate_imports()
    functionality_success = validate_basic_functionality()

    print("\n" + "=" * 50)
    if import_success and functionality_success:
        print("✓ ALL VALIDATIONS PASSED")
        print("Tests are ready to run!")
        return 0
    else:
        print("✗ VALIDATION FAILED")
        print("Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())