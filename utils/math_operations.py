"""
Mathematical utility functions module.

This module provides various mathematical operations and calculations
that are commonly used in testing and data processing scenarios.
"""


def calculate_factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer to calculate the factorial for.
        
    Returns:
        int: The factorial of n (n!).
        
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
        
    Examples:
        >>> calculate_factorial(0)
        1
        >>> calculate_factorial(5)
        120
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check for primality.
        
    Returns:
        bool: True if the number is prime, False otherwise.
        
    Raises:
        TypeError: If n is not an integer.
        
    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
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
        n (int): The number of Fibonacci numbers to generate.
        
    Returns:
        list: A list containing the first n Fibonacci numbers.
        
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
        
    Examples:
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci_sequence(0)
        []
        >>> fibonacci_sequence(1)
        [0]
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Number of terms cannot be negative")
    
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


def greatest_common_divisor(a, b):
    """
    Calculate the greatest common divisor (GCD) of two integers using Euclidean algorithm.
    
    Args:
        a (int): First integer.
        b (int): Second integer.
        
    Returns:
        int: The greatest common divisor of a and b.
        
    Raises:
        TypeError: If either a or b is not an integer.
        ValueError: If both a and b are zero.
        
    Examples:
        >>> greatest_common_divisor(48, 18)
        6
        >>> greatest_common_divisor(17, 13)
        1
        >>> greatest_common_divisor(0, 5)
        5
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    if a == 0 and b == 0:
        raise ValueError("GCD is not defined when both numbers are zero")
    
    a, b = abs(a), abs(b)
    
    while b:
        a, b = b, a % b
    
    return a


def least_common_multiple(a, b):
    """
    Calculate the least common multiple (LCM) of two integers.
    
    Args:
        a (int): First integer.
        b (int): Second integer.
        
    Returns:
        int: The least common multiple of a and b.
        
    Raises:
        TypeError: If either a or b is not an integer.
        ValueError: If either a or b is zero.
        
    Examples:
        >>> least_common_multiple(12, 18)
        36
        >>> least_common_multiple(7, 5)
        35
        >>> least_common_multiple(4, 6)
        12
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    if a == 0 or b == 0:
        raise ValueError("LCM is not defined when either number is zero")
    
    a, b = abs(a), abs(b)
    gcd = greatest_common_divisor(a, b)
    
    return (a * b) // gcd


def calculate_mean(numbers):
    """
    Calculate the arithmetic mean (average) of a list of numbers.
    
    Args:
        numbers (list): A list of numerical values.
        
    Returns:
        float: The arithmetic mean of the numbers.
        
    Raises:
        TypeError: If numbers is not a list.
        ValueError: If the list is empty or contains non-numeric values.
        
    Examples:
        >>> calculate_mean([1, 2, 3, 4, 5])
        3.0
        >>> calculate_mean([10, 20, 30])
        20.0
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be numeric")
    
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """
    Calculate the median value of a list of numbers.
    
    Args:
        numbers (list): A list of numerical values.
        
    Returns:
        float: The median value of the numbers.
        
    Raises:
        TypeError: If numbers is not a list.
        ValueError: If the list is empty or contains non-numeric values.
        
    Examples:
        >>> calculate_median([1, 2, 3, 4, 5])
        3.0
        >>> calculate_median([1, 2, 3, 4])
        2.5
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be numeric")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return float(sorted_numbers[n // 2])


def calculate_mode(numbers):
    """
    Calculate the mode (most frequent value) of a list of numbers.
    
    Args:
        numbers (list): A list of numerical values.
        
    Returns:
        list: A list of the most frequent values (can be multiple values).
        
    Raises:
        TypeError: If numbers is not a list.
        ValueError: If the list is empty or contains non-numeric values.
        
    Examples:
        >>> calculate_mode([1, 2, 2, 3, 4])
        [2]
        >>> calculate_mode([1, 1, 2, 2, 3])
        [1, 2]
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be numeric")
    
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    max_frequency = max(frequency.values())
    mode_values = [num for num, freq in frequency.items() if freq == max_frequency]
    
    return sorted(mode_values)


def calculate_variance(numbers):
    """
    Calculate the variance of a list of numbers.
    
    Args:
        numbers (list): A list of numerical values.
        
    Returns:
        float: The variance of the numbers.
        
    Raises:
        TypeError: If numbers is not a list.
        ValueError: If the list is empty, has only one element, or contains non-numeric values.
        
    Examples:
        >>> calculate_variance([1, 2, 3, 4, 5])
        2.0
        >>> calculate_variance([10, 12, 14, 16, 18])
        8.0
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not numbers:
        raise ValueError("Cannot calculate variance of empty list")
    if len(numbers) == 1:
        raise ValueError("Cannot calculate variance with only one data point")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be numeric")
    
    mean = calculate_mean(numbers)
    squared_differences = [(num - mean) ** 2 for num in numbers]
    
    return sum(squared_differences) / (len(numbers) - 1)


def calculate_standard_deviation(numbers):
    """
    Calculate the standard deviation of a list of numbers.
    
    Args:
        numbers (list): A list of numerical values.
        
    Returns:
        float: The standard deviation of the numbers.
        
    Raises:
        TypeError: If numbers is not a list.
        ValueError: If the list is empty, has only one element, or contains non-numeric values.
        
    Examples:
        >>> round(calculate_standard_deviation([1, 2, 3, 4, 5]), 6)
        1.581139
        >>> round(calculate_standard_deviation([10, 12, 14, 16, 18]), 6)
        2.828427
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of empty list")
    if len(numbers) == 1:
        raise ValueError("Cannot calculate standard deviation with only one data point")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be numeric")
    
    variance = calculate_variance(numbers)
    
    return variance ** 0.5


def sum_of_divisors(n):
    """
    Calculate the sum of all proper divisors of a positive integer.
    Proper divisors are all divisors of n except n itself.
    
    Args:
        n (int): A positive integer to find the sum of divisors for.
        
    Returns:
        int: The sum of all proper divisors of n.
        
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not positive.
        
    Examples:
        >>> sum_of_divisors(6)
        6
        >>> sum_of_divisors(12)
        16
        >>> sum_of_divisors(1)
        0
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    if n == 1:
        return 0
    
    divisors_sum = 1
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    
    return divisors_sum


def is_perfect_number(n):
    """
    Check if a positive integer is a perfect number.
    A perfect number is equal to the sum of its proper divisors.
    
    Args:
        n (int): A positive integer to check.
        
    Returns:
        bool: True if the number is perfect, False otherwise.
        
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not positive.
        
    Examples:
        >>> is_perfect_number(6)
        True
        >>> is_perfect_number(28)
        True
        >>> is_perfect_number(12)
        False
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    return sum_of_divisors(n) == n