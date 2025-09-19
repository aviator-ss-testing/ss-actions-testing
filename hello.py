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


# Data Processing Functions

def filter_even_numbers(numbers):
    """
    Filter even numbers from a list of integers.

    Args:
        numbers (list): List of integers to filter

    Returns:
        list: List containing only even numbers

    Raises:
        TypeError: If input is not a list or contains non-integers
    """
    if numbers is None:
        return []
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not numbers:
        return []

    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")

    return [num for num in numbers if num % 2 == 0]


def find_duplicates(items):
    """
    Find duplicate items in a list.

    Args:
        items (list): List of items to check for duplicates

    Returns:
        list: List of duplicate items (without duplicates in the result)

    Raises:
        TypeError: If input is not a list
    """
    if items is None:
        return []
    if not isinstance(items, list):
        raise TypeError("Input must be a list")
    if not items:
        return []

    seen = set()
    duplicates = set()

    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)


def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into a single sorted list.

    Args:
        list1 (list): First sorted list
        list2 (list): Second sorted list

    Returns:
        list: Merged sorted list

    Raises:
        TypeError: If inputs are not lists
    """
    if list1 is None:
        list1 = []
    if list2 is None:
        list2 = []
    if not isinstance(list1, list):
        raise TypeError("First input must be a list")
    if not isinstance(list2, list):
        raise TypeError("Second input must be a list")

    result = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result


def invert_dictionary(dictionary):
    """
    Invert a dictionary by swapping keys and values.

    Args:
        dictionary (dict): Dictionary to invert

    Returns:
        dict: Dictionary with keys and values swapped

    Raises:
        TypeError: If input is not a dictionary
        ValueError: If values are not hashable
    """
    if dictionary is None:
        return {}
    if not isinstance(dictionary, dict):
        raise TypeError("Input must be a dictionary")
    if not dictionary:
        return {}

    try:
        return {value: key for key, value in dictionary.items()}
    except TypeError as e:
        raise ValueError("Dictionary values must be hashable") from e


def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries, with dict2 values taking precedence.

    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: Merged dictionary

    Raises:
        TypeError: If inputs are not dictionaries
    """
    if dict1 is None:
        dict1 = {}
    if dict2 is None:
        dict2 = {}
    if not isinstance(dict1, dict):
        raise TypeError("First input must be a dictionary")
    if not isinstance(dict2, dict):
        raise TypeError("Second input must be a dictionary")

    result = dict1.copy()
    result.update(dict2)
    return result


def filter_by_value(dictionary, threshold):
    """
    Filter dictionary items by value using a threshold.

    Args:
        dictionary (dict): Dictionary to filter
        threshold: Threshold value for comparison

    Returns:
        dict: Dictionary containing only items with values >= threshold

    Raises:
        TypeError: If input is not a dictionary
    """
    if dictionary is None:
        return {}
    if not isinstance(dictionary, dict):
        raise TypeError("Input must be a dictionary")
    if not dictionary:
        return {}

    return {key: value for key, value in dictionary.items() if value >= threshold}


def find_common_elements(set1, set2):
    """
    Find common elements between two sets.

    Args:
        set1 (set): First set
        set2 (set): Second set

    Returns:
        set: Set of common elements

    Raises:
        TypeError: If inputs are not sets
    """
    if set1 is None:
        set1 = set()
    if set2 is None:
        set2 = set()
    if not isinstance(set1, set):
        raise TypeError("First input must be a set")
    if not isinstance(set2, set):
        raise TypeError("Second input must be a set")

    return set1.intersection(set2)


def calculate_set_difference(set1, set2):
    """
    Calculate the difference between two sets (elements in set1 but not in set2).

    Args:
        set1 (set): First set
        set2 (set): Second set

    Returns:
        set: Set containing elements in set1 but not in set2

    Raises:
        TypeError: If inputs are not sets
    """
    if set1 is None:
        set1 = set()
    if set2 is None:
        set2 = set()
    if not isinstance(set1, set):
        raise TypeError("First input must be a set")
    if not isinstance(set2, set):
        raise TypeError("Second input must be a set")

    return set1.difference(set2)