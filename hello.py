"""
Simple hello module demonstrating various Python functions and decorators.
"""
from utils import fibonacci, capitalize_words, flatten_list
from decorators import timing, retry
from data_processing import parse_json_string, deep_merge

print("Hello, Aviator! Demonstrating Python functions with decorators...")

# Demonstrate utility functions
print(f"Fibonacci(10): {fibonacci(10)}")
print(f"Capitalize words: {capitalize_words('hello world python')}")
print(f"Flatten list: {flatten_list([[1, 2], [3, 4], [5]])}")

# Demonstrate decorated functions
@timing
def sample_computation():
    return sum(range(1000))

print(f"Timed computation result: {sample_computation()}")

# Demonstrate data processing
json_data = '{"name": "test", "value": 42}'
parsed = parse_json_string(json_data)
print(f"Parsed JSON: {parsed}")

merged = deep_merge({"a": 1}, {"b": 2})
print(f"Deep merge result: {merged}")

print("Function demonstrations completed!")
