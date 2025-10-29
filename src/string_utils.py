def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


def to_title_case(s):
    return ' '.join(word.capitalize() for word in s.split())
