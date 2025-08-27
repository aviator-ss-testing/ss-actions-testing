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


def is_valid_email(email):
    """
    Validate an email address using a basic regex pattern.
    
    Args:
        email (str or None): The email address to validate
        
    Returns:
        bool: True if email is valid, False otherwise
    """
    if email is None or not isinstance(email, str):
        return False
    
    # Basic email regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email.strip()) is not None


def is_valid_phone(phone):
    """
    Validate a phone number using a basic regex pattern.
    Supports formats like: (123) 456-7890, 123-456-7890, 1234567890, +1-123-456-7890
    
    Args:
        phone (str or None): The phone number to validate
        
    Returns:
        bool: True if phone number is valid, False otherwise
    """
    if phone is None or not isinstance(phone, str):
        return False
    
    # Basic phone regex pattern - supports common US formats
    phone_pattern = r'^(\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})$'
    return re.match(phone_pattern, phone.strip()) is not None


def count_word_frequency(text):
    """
    Count the frequency of each word in a text string.
    
    Args:
        text (str or None): The text to analyze
        
    Returns:
        dict: Dictionary with words as keys and their frequencies as values
    """
    if text is None or not isinstance(text, str):
        return {}
    
    # Convert to lowercase and split into words, removing punctuation
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency


def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two strings.
    
    Args:
        str1 (str or None): First string
        str2 (str or None): Second string
        
    Returns:
        str: The longest common substring, empty string if no common substring or if inputs are None
    """
    if str1 is None or str2 is None or not isinstance(str1, str) or not isinstance(str2, str):
        return ""
    
    if not str1 or not str2:
        return ""
    
    # Dynamic programming approach
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    max_length = 0
    ending_pos = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    ending_pos = i
            else:
                dp[i][j] = 0
    
    if max_length == 0:
        return ""
    
    return str1[ending_pos - max_length:ending_pos]


def sanitize_string(s):
    """
    Perform basic string cleaning operations.
    Removes leading/trailing whitespace, reduces multiple spaces to single space,
    and removes non-printable characters.
    
    Args:
        s (str or None): The string to sanitize
        
    Returns:
        str: Sanitized string, empty string if input is None
    """
    if s is None:
        return ""
    
    if not isinstance(s, str):
        s = str(s)
    
    # Remove non-printable characters (except newlines and tabs)
    s = re.sub(r'[^\x20-\x7E\n\t]', '', s)
    
    # Replace multiple whitespace characters with single space
    s = re.sub(r'\s+', ' ', s)
    
    # Strip leading and trailing whitespace
    return s.strip()