# ss-actions-testing

A Python integration testing repository demonstrating modular package structure with mathematical operations, utility functions, and comprehensive test coverage.

## Project Structure

```
.
├── src/
│   ├── mathops/
│   │   ├── __init__.py
│   │   └── operations.py      # Mathematical operations (factorial, fibonacci, GCD, etc.)
│   └── utils/
│       ├── __init__.py
│       ├── decorators.py      # Function decorators (timer, memoize, validate_positive)
│       ├── strings.py         # String manipulation utilities
│       └── lists.py           # List manipulation utilities
├── tests/
│   ├── __init__.py
│   ├── test_mathops.py        # Tests for mathematical operations
│   ├── test_decorators.py     # Tests for decorators
│   ├── test_strings.py        # Tests for string utilities
│   └── test_lists.py          # Tests for list utilities
└── run_tests.py               # Test runner script
```

## Usage Examples

### Mathematical Operations

```python
from src.mathops.operations import factorial, fibonacci, is_prime, gcd, lcm, power

# Compute factorial
result = factorial(5)  # Returns: 120

# Get nth Fibonacci number
fib = fibonacci(10)  # Returns: 55

# Check if number is prime
is_prime(7)  # Returns: True
is_prime(9)  # Returns: False

# Greatest common divisor
gcd(48, 18)  # Returns: 6

# Least common multiple
lcm(12, 15)  # Returns: 60

# Power function
power(2, 10)  # Returns: 1024
power(5, -2)  # Returns: 0.04
```

### String Utilities

```python
from src.utils.strings import reverse_words, is_palindrome, count_vowels, title_case, remove_duplicates

# Reverse word order
reverse_words("Hello World")  # Returns: "World Hello"

# Check palindrome
is_palindrome("A man a plan a canal Panama")  # Returns: True

# Count vowels
count_vowels("Hello World")  # Returns: 3

# Convert to title case
title_case("hello world")  # Returns: "Hello World"

# Remove duplicate characters
remove_duplicates("hello")  # Returns: "helo"
```

### List Utilities

```python
from src.utils.lists import flatten, chunk, rotate, find_duplicates, merge_sorted

# Flatten nested lists
flatten([1, [2, [3, 4]], 5])  # Returns: [1, 2, 3, 4, 5]

# Split list into chunks
chunk([1, 2, 3, 4, 5], 2)  # Returns: [[1, 2], [3, 4], [5]]

# Rotate list elements
rotate([1, 2, 3, 4, 5], 2)  # Returns: [4, 5, 1, 2, 3]

# Find duplicates
find_duplicates([1, 2, 2, 3, 3, 4])  # Returns: [2, 3]

# Merge sorted lists
merge_sorted([1, 3, 5], [2, 4, 6])  # Returns: [1, 2, 3, 4, 5, 6]
```

### Decorator Usage

```python
from src.utils.decorators import timer, memoize, validate_positive

# Time function execution
@timer
def slow_function():
    # Function execution time will be printed
    pass

# Cache expensive computations
@memoize
def expensive_calculation(n):
    # Subsequent calls with same argument return cached result
    return sum(range(n))

# Validate positive arguments
@validate_positive
def process_positive(x, y):
    # Raises ValueError if arguments are not positive
    return x + y

# Chain decorators
@timer
@memoize
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)
```

## Running Tests

Execute all tests using the test runner:

```bash
python run_tests.py
```

The test suite includes 169 comprehensive tests covering:
- Mathematical operations with edge cases
- Decorator functionality and behavior
- String manipulation with Unicode handling
- List operations with various input patterns

All tests use Python's built-in `unittest` framework, requiring no external dependencies.

## Requirements

- Python 3.11+
- No external dependencies (uses standard library only)

## Development

This repository demonstrates:
- Clean package structure with `src/` directory pattern
- Modular organization by functionality
- Comprehensive input validation with appropriate exceptions
- Efficient algorithms with documented time complexity
- Complete test coverage using `unittest`
- Decorator patterns for function enhancement
