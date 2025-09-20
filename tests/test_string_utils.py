"""
Comprehensive test suite for string_utils module.

Tests all string manipulation functions including edge cases, error conditions,
unicode handling, and special characters.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from string_utils import (
    reverse_string, count_vowels, is_palindrome,
    capitalize_words, remove_duplicates
)


class TestReverseString(unittest.TestCase):
    """Test cases for reverse_string function."""

    def test_simple_strings(self):
        """Test reversal of simple strings."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string("a"), "a")

    def test_empty_string(self):
        """Test reversal of empty string."""
        self.assertEqual(reverse_string(""), "")

    def test_numbers_and_symbols(self):
        """Test reversal of strings with numbers and symbols."""
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertEqual(reverse_string("!@#$%"), "%$#@!")
        self.assertEqual(reverse_string("abc123!@#"), "#@!321cba")

    def test_whitespace(self):
        """Test reversal of strings with whitespace."""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string("  spaces  "), "  secaps  ")
        self.assertEqual(reverse_string("\t\n"), "\n\t")

    def test_unicode_characters(self):
        """Test reversal of strings with unicode characters."""
        self.assertEqual(reverse_string("café"), "éfac")
        self.assertEqual(reverse_string("你好"), "好你")
        self.assertEqual(reverse_string("🎉🎊"), "🎊🎉")

    def test_palindromes(self):
        """Test reversal of palindromic strings."""
        self.assertEqual(reverse_string("racecar"), "racecar")
        self.assertEqual(reverse_string("madam"), "madam")

    def test_type_error(self):
        """Test type error for non-string input."""
        with self.assertRaises(TypeError):
            reverse_string(123)
        with self.assertRaises(TypeError):
            reverse_string(None)
        with self.assertRaises(TypeError):
            reverse_string([1, 2, 3])


class TestCountVowels(unittest.TestCase):
    """Test cases for count_vowels function."""

    def test_simple_strings(self):
        """Test vowel counting in simple strings."""
        self.assertEqual(count_vowels("hello world"), 3)
        self.assertEqual(count_vowels("programming"), 3)
        self.assertEqual(count_vowels("Python"), 1)

    def test_case_insensitive_default(self):
        """Test case-insensitive vowel counting (default)."""
        self.assertEqual(count_vowels("HELLO WORLD"), 3)
        self.assertEqual(count_vowels("AeIoU"), 5)
        self.assertEqual(count_vowels("MiXeD cAsE"), 4)

    def test_case_sensitive(self):
        """Test case-sensitive vowel counting."""
        self.assertEqual(count_vowels("HELLO", case_sensitive=True), 1)  # Only E
        self.assertEqual(count_vowels("hello", case_sensitive=True), 2)  # e and o
        self.assertEqual(count_vowels("AeIoU", case_sensitive=True), 3)  # e, o, and U are lowercase vowels

    def test_no_vowels(self):
        """Test strings with no vowels."""
        self.assertEqual(count_vowels("xyz"), 0)
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("123!@#"), 0)

    def test_all_vowels(self):
        """Test strings with all vowels."""
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("aaeeiiiooouuu"), 13)

    def test_empty_string(self):
        """Test vowel counting in empty string."""
        self.assertEqual(count_vowels(""), 0)

    def test_whitespace_and_numbers(self):
        """Test vowel counting with whitespace and numbers."""
        self.assertEqual(count_vowels("hello 123"), 2)
        self.assertEqual(count_vowels("   a e i o u   "), 5)

    def test_unicode_vowels(self):
        """Test vowel counting with unicode characters."""
        self.assertEqual(count_vowels("café"), 2)  # a and e
        self.assertEqual(count_vowels("naïve"), 3)  # a, i, and e

    def test_type_error(self):
        """Test type error for non-string input."""
        with self.assertRaises(TypeError):
            count_vowels(123)
        with self.assertRaises(TypeError):
            count_vowels(None)


class TestIsPalindrome(unittest.TestCase):
    """Test cases for is_palindrome function."""

    def test_simple_palindromes(self):
        """Test simple palindromic strings."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("level"))

    def test_simple_non_palindromes(self):
        """Test simple non-palindromic strings."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("programming"))

    def test_single_character(self):
        """Test single character strings."""
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))
        self.assertTrue(is_palindrome("1"))

    def test_empty_string(self):
        """Test empty string."""
        self.assertTrue(is_palindrome(""))

    def test_case_sensitivity(self):
        """Test case sensitivity options."""
        self.assertTrue(is_palindrome("Aa", ignore_case=True))
        self.assertFalse(is_palindrome("Aa", ignore_case=False))
        self.assertTrue(is_palindrome("RaceCar", ignore_case=True))
        self.assertFalse(is_palindrome("RaceCar", ignore_case=False))

    def test_with_spaces_default(self):
        """Test palindromes with spaces (default behavior)."""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("race a car", ignore_spaces=True))
        self.assertFalse(is_palindrome("race a car", ignore_spaces=False))

    def test_with_punctuation(self):
        """Test palindromes with punctuation."""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("Madam, I'm Adam"))

    def test_numbers_and_symbols(self):
        """Test palindromes with numbers and symbols."""
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("1a2b2a1", ignore_spaces=True))
        self.assertFalse(is_palindrome("1a2b3a1", ignore_spaces=True))

    def test_combined_options(self):
        """Test various combinations of options."""
        test_string = "A man, A plan, A canal: Panama!"
        self.assertTrue(is_palindrome(test_string, ignore_case=True, ignore_spaces=True))
        self.assertFalse(is_palindrome(test_string, ignore_case=False, ignore_spaces=True))
        self.assertFalse(is_palindrome(test_string, ignore_case=True, ignore_spaces=False))

    def test_unicode_palindromes(self):
        """Test palindromes with unicode characters."""
        self.assertTrue(is_palindrome("上海海上"))  # Chinese palindrome
        self.assertTrue(is_palindrome("А роза упала на лапу Азора", ignore_case=True))  # Russian palindrome

    def test_type_error(self):
        """Test type error for non-string input."""
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome(None)


class TestCapitalizeWords(unittest.TestCase):
    """Test cases for capitalize_words function."""

    def test_simple_strings(self):
        """Test capitalization of simple strings."""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python programming"), "Python Programming")
        self.assertEqual(capitalize_words("the quick brown fox"), "The Quick Brown Fox")

    def test_already_capitalized(self):
        """Test strings that are already capitalized."""
        self.assertEqual(capitalize_words("Hello World"), "Hello World")
        self.assertEqual(capitalize_words("HELLO WORLD"), "Hello World")

    def test_single_word(self):
        """Test single word strings."""
        self.assertEqual(capitalize_words("hello"), "Hello")
        self.assertEqual(capitalize_words("python"), "Python")
        self.assertEqual(capitalize_words("a"), "A")

    def test_empty_string(self):
        """Test empty string."""
        self.assertEqual(capitalize_words(""), "")

    def test_multiple_spaces(self):
        """Test strings with multiple spaces."""
        self.assertEqual(capitalize_words("hello  world"), "Hello  World")
        self.assertEqual(capitalize_words("  hello world  "), "  Hello World  ")

    def test_custom_separator(self):
        """Test with custom separators."""
        self.assertEqual(capitalize_words("hello-world", separator="-"), "Hello-World")
        self.assertEqual(capitalize_words("hello_world_test", separator="_"), "Hello_World_Test")
        self.assertEqual(capitalize_words("hello|world|test", separator="|"), "Hello|World|Test")

    def test_numbers_and_symbols(self):
        """Test strings with numbers and symbols."""
        self.assertEqual(capitalize_words("hello123 world456"), "Hello123 World456")
        self.assertEqual(capitalize_words("test@email.com test"), "Test@Email.Com Test")

    def test_special_cases(self):
        """Test special edge cases."""
        self.assertEqual(capitalize_words("hello world", separator=""), "Hello world")
        self.assertEqual(capitalize_words("a b c d"), "A B C D")

    def test_unicode_strings(self):
        """Test capitalization with unicode characters."""
        self.assertEqual(capitalize_words("café restaurant"), "Café Restaurant")
        self.assertEqual(capitalize_words("naïve approach"), "Naïve Approach")

    def test_type_errors(self):
        """Test type errors for invalid inputs."""
        with self.assertRaises(TypeError):
            capitalize_words(123)
        with self.assertRaises(TypeError):
            capitalize_words("hello", separator=123)
        with self.assertRaises(TypeError):
            capitalize_words(None)


class TestRemoveDuplicates(unittest.TestCase):
    """Test cases for remove_duplicates function."""

    def test_simple_duplicates(self):
        """Test removal of simple duplicate characters."""
        self.assertEqual(remove_duplicates("hello"), "helo")
        self.assertEqual(remove_duplicates("programming"), "progamin")
        self.assertEqual(remove_duplicates("aabbcc"), "abc")

    def test_no_duplicates(self):
        """Test strings with no duplicates."""
        self.assertEqual(remove_duplicates("abcd"), "abcd")
        self.assertEqual(remove_duplicates("python"), "python")
        self.assertEqual(remove_duplicates("xyz"), "xyz")

    def test_all_same_character(self):
        """Test strings with all same characters."""
        self.assertEqual(remove_duplicates("aaaa"), "a")
        self.assertEqual(remove_duplicates("bbbbbb"), "b")
        self.assertEqual(remove_duplicates("111"), "1")

    def test_preserve_order_true(self):
        """Test duplicate removal with order preservation (default)."""
        self.assertEqual(remove_duplicates("abcabc"), "abc")
        self.assertEqual(remove_duplicates("hello world"), "helo wrd")
        self.assertEqual(remove_duplicates("abccba"), "abc")

    def test_preserve_order_false(self):
        """Test duplicate removal without order preservation."""
        result = remove_duplicates("hello", preserve_order=False)
        self.assertEqual(sorted(result), sorted("helo"))
        self.assertEqual(len(result), 4)  # h, e, l, o

        result = remove_duplicates("programming", preserve_order=False)
        expected_chars = set("programming")
        self.assertEqual(set(result), expected_chars)

    def test_empty_string(self):
        """Test empty string."""
        self.assertEqual(remove_duplicates(""), "")
        self.assertEqual(remove_duplicates("", preserve_order=False), "")

    def test_single_character(self):
        """Test single character string."""
        self.assertEqual(remove_duplicates("a"), "a")
        self.assertEqual(remove_duplicates("z", preserve_order=False), "z")

    def test_whitespace_and_symbols(self):
        """Test strings with whitespace and symbols."""
        self.assertEqual(remove_duplicates("hello  world"), "helo wrd")
        self.assertEqual(remove_duplicates("a!b@c#a!b@c#"), "a!b@c#")
        self.assertEqual(remove_duplicates("123321"), "123")

    def test_case_sensitivity(self):
        """Test that function is case-sensitive."""
        self.assertEqual(remove_duplicates("AaBbCcAaBbCc"), "AaBbCc")
        self.assertEqual(remove_duplicates("Hello"), "Helo")

    def test_unicode_characters(self):
        """Test duplicate removal with unicode characters."""
        self.assertEqual(remove_duplicates("café café"), "café ")
        self.assertEqual(remove_duplicates("🎉🎊🎉🎊"), "🎉🎊")
        self.assertEqual(remove_duplicates("你好你好"), "你好")

    def test_complex_strings(self):
        """Test complex strings with mixed content."""
        input_str = "Hello123!Hello123!"
        expected = "Helo123!"
        self.assertEqual(remove_duplicates(input_str), expected)

    def test_type_error(self):
        """Test type error for non-string input."""
        with self.assertRaises(TypeError):
            remove_duplicates(123)
        with self.assertRaises(TypeError):
            remove_duplicates(None)
        with self.assertRaises(TypeError):
            remove_duplicates(['a', 'b', 'c'])


if __name__ == '__main__':
    unittest.main(verbosity=2)