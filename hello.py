import math_operations
import string_utils
import list_operations

print("Hello, Aviator! Ok I saw webhook arrive but nothing happened?")

print("\n=== Module Functionality Demonstration ===")

print("\n--- Math Operations ---")
print(f"Addition: 5 + 3 = {math_operations.add(5, 3)}")
print(f"Subtraction: 10 - 4 = {math_operations.subtract(10, 4)}")
print(f"Multiplication: 7 * 6 = {math_operations.multiply(7, 6)}")
print(f"Division: 20 / 4 = {math_operations.divide(20, 4)}")
print(f"Power: 2^3 = {math_operations.power(2, 3)}")
print(f"Factorial: 5! = {math_operations.factorial(5)}")

print("\n--- String Utilities ---")
sample_text = "Hello World"
print(f"Original: '{sample_text}'")
print(f"Reversed: '{string_utils.reverse_string(sample_text)}'")
print(f"Vowel count: {string_utils.count_vowels(sample_text)}")
print(f"Is palindrome: {string_utils.is_palindrome('racecar')}")
print(f"Capitalized: '{string_utils.capitalize_words('hello aviator testing')}'")

print("\n--- List Operations ---")
sample_list = [5, 2, 8, 1, 9, 3]
print(f"Original list: {sample_list}")
print(f"Maximum: {list_operations.find_max(sample_list)}")
print(f"Minimum: {list_operations.find_min(sample_list)}")
print(f"Average: {list_operations.calculate_average(sample_list)}")
print(f"Sorted: {list_operations.sort_list(sample_list.copy())}")
duplicates_list = [1, 2, 2, 3, 3, 4, 5]
print(f"Remove duplicates from {duplicates_list}: {list_operations.remove_duplicates(duplicates_list)}")

print("\n=== End of Demonstration ===")
