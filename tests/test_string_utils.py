"""
Comprehensive test suite for the string_utils module.

Tests cover all string manipulation functions with various scenarios including
Unicode characters, special characters, edge cases, and proper error handling.
"""

import unittest
import sys
import os

# Add parent directory to path to import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from string_utils import reverse_string, count_vowels, is_palindrome, capitalize_words


class TestStringUtils(unittest.TestCase):
    """Test cases for all string utility functions."""

    def setUp(self):
        """Set up test data for string operations tests."""
        # Common test strings for reuse across tests
        self.basic_string = "hello"
        self.empty_string = ""
        self.none_value = None
        self.single_char = "a"
        self.mixed_case = "Hello World"
        self.with_spaces = "hello world"
        self.with_punctuation = "Hello, World!"
        self.unicode_string = "café"
        self.emoji_string = "🙂😊🎉"
        self.numeric_string = "12321"
        self.palindrome = "racecar"
        self.non_palindrome = "hello"

        # Invalid input types for error testing
        self.invalid_int = 123
        self.invalid_list = []
        self.invalid_dict = {}

    def test_reverse_string_basic(self):
        """Test basic string reversal."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_string_empty(self):
        """Test string reversal with empty strings."""
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string(None), "")

    def test_reverse_string_whitespace(self):
        """Test string reversal with whitespace."""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string(" "), " ")
        self.assertEqual(reverse_string("  hello  "), "  olleh  ")

    def test_reverse_string_special_characters(self):
        """Test string reversal with special characters."""
        self.assertEqual(reverse_string("hello!@#"), "#@!olleh")
        self.assertEqual(reverse_string("123-456"), "654-321")
        self.assertEqual(reverse_string("a.b,c;d"), "d;c,b.a")

    def test_reverse_string_unicode(self):
        """Test string reversal with Unicode characters."""
        self.assertEqual(reverse_string("café"), "éfac")
        self.assertEqual(reverse_string("naïve"), "evïan")
        self.assertEqual(reverse_string("🙂😊🎉"), "🎉😊🙂")
        self.assertEqual(reverse_string("αβγδ"), "δγβα")

    def test_reverse_string_mixed_case(self):
        """Test string reversal with mixed case."""
        self.assertEqual(reverse_string("Hello World"), "dlroW olleH")
        self.assertEqual(reverse_string("PyThOn"), "nOhTyP")

    def test_reverse_string_type_error(self):
        """Test reverse_string raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            reverse_string(123)
        with self.assertRaises(TypeError):
            reverse_string([])
        with self.assertRaises(TypeError):
            reverse_string({})

    def test_count_vowels_basic(self):
        """Test basic vowel counting."""
        self.assertEqual(count_vowels("hello"), 2)  # e, o
        self.assertEqual(count_vowels("world"), 1)  # o
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_count_vowels_mixed_case(self):
        """Test vowel counting with mixed case."""
        self.assertEqual(count_vowels("Hello World"), 3)  # e, o, o
        self.assertEqual(count_vowels("PyThOn PrOgRaMmInG"), 5)  # y not counted, O, O, a, I

    def test_count_vowels_empty(self):
        """Test vowel counting with empty strings."""
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels(None), 0)

    def test_count_vowels_no_vowels(self):
        """Test vowel counting with no vowels."""
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("123456"), 0)
        self.assertEqual(count_vowels("xyz"), 0)

    def test_count_vowels_special_characters(self):
        """Test vowel counting with special characters."""
        self.assertEqual(count_vowels("hello!@#"), 2)  # e, o
        self.assertEqual(count_vowels("a-e-i-o-u"), 5)
        self.assertEqual(count_vowels("!@#$%"), 0)

    def test_count_vowels_unicode(self):
        """Test vowel counting with Unicode characters."""
        self.assertEqual(count_vowels("café"), 2)  # a, e
        self.assertEqual(count_vowels("naïve"), 3)  # a, i, e
        self.assertEqual(count_vowels("résumé"), 4)  # e, u, e, e

    def test_count_vowels_type_error(self):
        """Test count_vowels raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            count_vowels(123)
        with self.assertRaises(TypeError):
            count_vowels([])
        with self.assertRaises(TypeError):
            count_vowels({})

    def test_is_palindrome_basic(self):
        """Test basic palindrome detection."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("noon"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

    def test_is_palindrome_case_insensitive(self):
        """Test case-insensitive palindrome detection."""
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("Level"))
        self.assertTrue(is_palindrome("MadAm"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_is_palindrome_with_spaces_punctuation(self):
        """Test palindrome detection ignoring spaces and punctuation."""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("race a car"))  # False - "raceacar" != "racaecar"
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertFalse(is_palindrome("race a car"))  # "raceacar" is not a palindrome

    def test_is_palindrome_empty_and_single(self):
        """Test palindrome detection with empty and single character strings."""
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome(None))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("A"))

    def test_is_palindrome_numbers(self):
        """Test palindrome detection with numbers."""
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("1001"))
        self.assertFalse(is_palindrome("12345"))

    def test_is_palindrome_special_characters_only(self):
        """Test palindrome detection with only special characters."""
        self.assertTrue(is_palindrome("!@#@!"))
        self.assertTrue(is_palindrome(".,.,"))
        self.assertTrue(is_palindrome("   "))  # Only spaces

    def test_is_palindrome_unicode(self):
        """Test palindrome detection with Unicode characters."""
        self.assertTrue(is_palindrome("аргентина манит негра"))  # Cyrillic
        self.assertTrue(is_palindrome("А роза упала на лапу Азора"))  # Cyrillic

    def test_is_palindrome_type_error(self):
        """Test is_palindrome raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome([])
        with self.assertRaises(TypeError):
            is_palindrome({})

    def test_capitalize_words_basic(self):
        """Test basic word capitalization."""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python programming"), "Python Programming")
        self.assertEqual(capitalize_words("a"), "A")

    def test_capitalize_words_empty(self):
        """Test word capitalization with empty strings."""
        self.assertEqual(capitalize_words(""), "")
        self.assertEqual(capitalize_words(None), "")

    def test_capitalize_words_whitespace(self):
        """Test word capitalization with various whitespace."""
        self.assertEqual(capitalize_words("hello   world"), "Hello World")
        self.assertEqual(capitalize_words("  hello world  "), "Hello World")
        self.assertEqual(capitalize_words("   "), "   ")  # Only whitespace

    def test_capitalize_words_mixed_case(self):
        """Test word capitalization with mixed case input."""
        self.assertEqual(capitalize_words("hELLo WoRLd"), "Hello World")
        self.assertEqual(capitalize_words("pYtHoN pRoGrAmMiNg"), "Python Programming")

    def test_capitalize_words_special_characters(self):
        """Test word capitalization with special characters."""
        self.assertEqual(capitalize_words("hello-world"), "Hello-world")
        self.assertEqual(capitalize_words("hello.world"), "Hello.world")
        self.assertEqual(capitalize_words("hello,world!"), "Hello,world!")

    def test_capitalize_words_numbers(self):
        """Test word capitalization with numbers."""
        self.assertEqual(capitalize_words("hello 123 world"), "Hello 123 World")
        self.assertEqual(capitalize_words("123abc 456def"), "123abc 456def")

    def test_capitalize_words_unicode(self):
        """Test word capitalization with Unicode characters."""
        self.assertEqual(capitalize_words("café restaurant"), "Café Restaurant")
        self.assertEqual(capitalize_words("naïve approach"), "Naïve Approach")
        self.assertEqual(capitalize_words("résumé cover"), "Résumé Cover")

    def test_capitalize_words_single_letters(self):
        """Test word capitalization with single letters."""
        self.assertEqual(capitalize_words("a b c d"), "A B C D")
        self.assertEqual(capitalize_words("i am a programmer"), "I Am A Programmer")

    def test_capitalize_words_apostrophes(self):
        """Test word capitalization with contractions/apostrophes."""
        self.assertEqual(capitalize_words("don't can't won't"), "Don't Can't Won't")
        self.assertEqual(capitalize_words("it's a beautiful day"), "It's A Beautiful Day")

    def test_capitalize_words_type_error(self):
        """Test capitalize_words raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            capitalize_words(123)
        with self.assertRaises(TypeError):
            capitalize_words([])
        with self.assertRaises(TypeError):
            capitalize_words({})


if __name__ == '__main__':
    unittest.main()