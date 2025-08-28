#!/usr/bin/env python3
"""Simple import check for string utilities tests."""

try:
    import sys
    import os
    sys.path.insert(0, os.path.dirname(__file__))
    
    from tests.test_string_utilities import TestStringUtilities
    print("✓ Successfully imported TestStringUtilities")
    
    # Count test methods
    test_methods = [method for method in dir(TestStringUtilities) if method.startswith('test_')]
    print(f"✓ Found {len(test_methods)} test methods")
    
    # List some test categories
    categories = {
        'normal_cases': len([m for m in test_methods if 'normal_cases' in m]),
        'edge_cases': len([m for m in test_methods if 'edge_cases' in m]),
        'unicode': len([m for m in test_methods if 'unicode' in m]),
        'performance': len([m for m in test_methods if 'performance' in m])
    }
    
    for category, count in categories.items():
        print(f"✓ {category}: {count} tests")
    
    print("✓ Import validation successful")
    
except Exception as e:
    print(f"✗ Import failed: {e}")
    import traceback
    traceback.print_exc()