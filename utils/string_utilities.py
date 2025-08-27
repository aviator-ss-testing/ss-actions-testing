"""
String manipulation and processing utility functions module.

This module provides various string manipulation functions including
validation, transformation, and analysis utilities.
"""

import re


def reverse_string(s):
    """
    Reverse a string.
    
    Args:
        s (str or None): The string to reverse
        
    Returns:
        str: Reversed string, empty string if input is None
    """
    if s is None:
        return ""
    return s[::-1]


def is_palindrome(s):
    """
    Check if a string is a palindrome (reads same forwards and backwards).
    
    Args:
        s (str or None): The string to check
        
    Returns:
        bool: True if string is a palindrome, False otherwise
    """
    if s is None:
        return False
    
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]


def remove_duplicates(s):
    """
    Remove duplicate characters from a string while preserving order.
    
    Args:
        s (str or None): The string to process
        
    Returns:
        str: String with duplicates removed, empty string if input is None
    """
    if s is None:
        return ""
    
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)


def capitalize_words(s):
    """
    Capitalize the first letter of each word in a string.
    
    Args:
        s (str or None): The string to capitalize
        
    Returns:
        str: String with each word capitalized, empty string if input is None
    """
    if s is None:
        return ""
    
    return ' '.join(word.capitalize() for word in s.split())


def count_vowels(s):
    """
    Count the number of vowels in a string.
    
    Args:
        s (str or None): The string to analyze
        
    Returns:
        int: Number of vowels (a, e, i, o, u) in the string, 0 if input is None
    """
    if s is None:
        return 0
    
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


def count_consonants(s):
    """
    Count the number of consonants in a string.
    
    Args:
        s (str or None): The string to analyze
        
    Returns:
        int: Number of consonants (alphabetic characters that are not vowels), 0 if input is None
    """
    if s is None:
        return 0
    
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)


def extract_numbers(s):
    """
    Extract all numeric values from a string.
    
    Args:
        s (str or None): The string to extract numbers from
        
    Returns:
        list: List of float values found in the string, empty list if input is None
    """
    if s is None:
        return []
    
    # Find all number patterns including integers and floats
    number_pattern = r'-?\d+\.?\d*'
    matches = re.findall(number_pattern, s)
    
    # Convert to float, handling integers and floats
    numbers = []
    for match in matches:
        if '.' in match:
            numbers.append(float(match))
        else:
            numbers.append(float(match))
    
    return numbers