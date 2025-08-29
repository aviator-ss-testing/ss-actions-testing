# Test Execution Guide

This document provides instructions for running the test suite with various methods.

## Available Test Execution Methods

### 1. Using the Custom Test Runner (Recommended)
```bash
python run_tests.py
```
This script provides:
- Comprehensive test execution with detailed reporting
- Basic test coverage analysis
- Execution time tracking
- Detailed failure and error reporting
- Success rate calculation

### 2. Using Python's Built-in Test Discovery
```bash
python -m unittest discover tests/ -v
```
This method uses Python's standard unittest discovery to run all tests in the tests/ directory.

### 3. Using the Complete Test Suite Module
```bash
python tests/test_all.py
```
This runs all tests through the unified test_all.py module.

### 4. Using Test Configuration Script
```bash
python test_config.py
```
This uses the test configuration file for consistent test execution.

### 5. Running Individual Test Modules
```bash
python -m unittest tests.test_math_operations -v
python -m unittest tests.test_string_utilities -v
python -m unittest tests.test_data_processing -v
```

## Expected Output

All methods should show:
- Total number of tests run
- Success/failure status for each test
- Overall execution summary
- Any failures or errors with detailed tracebacks

## Test Coverage

The test suite covers:
- **Mathematical Operations**: `utils.math_operations`
- **String Utilities**: `utils.string_utilities`
- **Data Processing**: `utils.data_processing`

Each module has comprehensive test coverage including:
- Normal operation test cases
- Edge cases (empty inputs, boundary values)
- Error conditions and exception handling
- Input validation testing