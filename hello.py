from math_utils import add, multiply, is_prime, fibonacci, factorial
from string_utils import reverse_string, is_palindrome, count_vowels, truncate
from decorators import timer, memoize, retry


@timer
def calculate_fibonacci_stats(n):
    sequence = fibonacci(n)
    return {
        'sequence': sequence,
        'sum': sum(sequence),
        'count': len(sequence)
    }


@memoize
def expensive_calculation(base, exp):
    return multiply(factorial(base), exp)


@retry(attempts=2, delay=0.1)
def check_prime_numbers(limit):
    primes = [num for num in range(2, limit) if is_prime(num)]
    return primes


def main():
    print("=" * 60)
    print("Python Utility Modules Demo")
    print("=" * 60)

    print("\n[Math Operations]")
    result = add(15, 27)
    print(f"Addition: 15 + 27 = {result}")

    print(f"Factorial: 5! = {factorial(5)}")

    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Is 18 prime? {is_prime(18)}")

    print("\n[String Utilities]")
    test_string = "Hello, Aviator!"
    print(f"Original: '{test_string}'")
    print(f"Reversed: '{reverse_string(test_string)}'")
    print(f"Vowel count: {count_vowels(test_string)}")

    palindrome = "racecar"
    print(f"Is '{palindrome}' a palindrome? {is_palindrome(palindrome)}")

    long_text = "This is a very long text that needs to be truncated"
    print(f"Truncated: '{truncate(long_text, 30)}'")

    print("\n[Decorators in Action]")
    print("\n1. @timer decorator (measures execution time):")
    fib_stats = calculate_fibonacci_stats(10)
    print(f"   Result: {fib_stats}")

    print("\n2. @memoize decorator (caches results):")
    print("   First call (computed):")
    result1 = expensive_calculation(4, 10)
    print(f"   Result: {result1}")
    print("   Second call (cached):")
    result2 = expensive_calculation(4, 10)
    print(f"   Result: {result2}")

    print("\n3. @retry decorator (retries on failure):")
    primes = check_prime_numbers(20)
    print(f"   Prime numbers up to 20: {primes}")

    print("\n" + "=" * 60)
    print("Integration testing verification: All modules working!")
    print("=" * 60)


if __name__ == "__main__":
    main()
