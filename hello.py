"""
Comprehensive utilities module containing mathematical and string processing functions.
"""


def calculate_factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): Non-negative integer to calculate factorial for

    Returns:
        int: Factorial of n

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime_number(n):
    """
    Check if a number is prime.

    Args:
        n (int): Integer to check for primality

    Returns:
        bool: True if n is prime, False otherwise

    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci_sequence(n):
    """
    Generate the first n numbers in the Fibonacci sequence.

    Args:
        n (int): Number of Fibonacci numbers to generate

    Returns:
        list: List containing the first n Fibonacci numbers

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])

    return sequence


def reverse_words(text):
    """
    Reverse the order of words in a string.

    Args:
        text (str): Input string to reverse words

    Returns:
        str: String with words in reverse order

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    if not text.strip():
        return text

    words = text.split()
    return ' '.join(reversed(words))


def count_vowels(text):
    """
    Count the number of vowels in a string (case-insensitive).

    Args:
        text (str): Input string to count vowels

    Returns:
        int: Number of vowels in the string

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)


def capitalize_words(text):
    """
    Capitalize the first letter of each word in a string.

    Args:
        text (str): Input string to capitalize

    Returns:
        str: String with each word capitalized

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    if not text:
        return text

    return ' '.join(word.capitalize() for word in text.split())