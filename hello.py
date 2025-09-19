"""
Main demonstration script showcasing math_ops and utils modules functionality.
"""

import math_ops
import utils
import datetime

def main():
    print("Hello, Aviator! Demonstrating math and utility functions:")
    print("=" * 60)

    # Math operations demonstrations
    print("\n📊 MATH OPERATIONS:")
    print("-" * 30)

    # Basic arithmetic
    print(f"Addition: 15 + 25 = {math_ops.add(15, 25)}")
    print(f"Subtraction: 100 - 33 = {math_ops.subtract(100, 33)}")
    print(f"Multiplication: 7 * 8 = {math_ops.multiply(7, 8)}")
    print(f"Division: 144 / 12 = {math_ops.divide(144, 12)}")

    # Advanced math
    print(f"Factorial of 5: {math_ops.factorial(5)}")
    print(f"10th Fibonacci number: {math_ops.fibonacci(10)}")
    print(f"Is 17 prime? {math_ops.prime_checker(17)}")
    print(f"GCD of 48 and 18: {math_ops.gcd(48, 18)}")

    # Statistics
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Mean of {sample_data}: {math_ops.mean(sample_data)}")
    print(f"Median of {sample_data}: {math_ops.median(sample_data)}")

    # Geometry
    print(f"Area of circle (radius=5): {math_ops.area_circle(5):.2f}")
    print(f"Rectangle area (10x6): {math_ops.area_rectangle(10, 6)}")

    # Utility functions demonstrations
    print("\n🔧 UTILITY FUNCTIONS:")
    print("-" * 30)

    # String manipulation
    test_string = "racecar"
    print(f"Reverse of '{test_string}': {utils.reverse_string(test_string)}")
    print(f"Is '{test_string}' a palindrome? {utils.is_palindrome(test_string)}")
    print(f"Vowel count in '{test_string}': {utils.count_vowels(test_string)}")

    # List operations
    nested = [1, [2, 3], [4, [5, 6]], 7]
    print(f"Flatten {nested}: {utils.flatten_list(nested)}")
    duplicates = [1, 2, 2, 3, 3, 3, 4]
    print(f"Remove duplicates from {duplicates}: {utils.remove_duplicates(duplicates)}")

    # Validation
    print(f"Is 'user@example.com' valid email? {utils.is_email_valid('user@example.com')}")
    print(f"Is '(555) 123-4567' valid phone? {utils.is_phone_valid('(555) 123-4567')}")

    # Date utilities
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    print(f"Days between {yesterday} and {today}: {utils.days_between(yesterday, today)}")
    print(f"Is today a weekend? {utils.is_weekend(today)}")

    # File utilities
    print(f"Extension of 'document.pdf': {utils.get_file_extension('document.pdf')}")

    # Error handling demonstrations
    print("\n⚠️  ERROR HANDLING DEMONSTRATIONS:")
    print("-" * 40)

    # Division by zero
    try:
        result = math_ops.divide(10, 0)
    except ValueError as e:
        print(f"Division by zero caught: {e}")

    # Invalid factorial
    try:
        result = math_ops.factorial(-5)
    except ValueError as e:
        print(f"Negative factorial caught: {e}")

    # Empty list statistics
    try:
        result = math_ops.mean([])
    except ValueError as e:
        print(f"Empty list mean caught: {e}")

    # Invalid email
    invalid_email = "not-an-email"
    print(f"Is '{invalid_email}' valid email? {utils.is_email_valid(invalid_email)}")

    print("\n✅ All demonstrations completed successfully!")

if __name__ == "__main__":
    main()
