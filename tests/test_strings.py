"""Test cases for string manipulation utilities."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.strings import (
    reverse_words,
    is_palindrome,
    count_vowels,
    title_case,
    remove_duplicates
)


class TestReverseWords(unittest.TestCase):
    """Test cases for reverse_words function."""

    def test_reverse_words_multiple_words(self):
        """Test reversing order of multiple words."""
        self.assertEqual(reverse_words("hello world"), "world hello")
        self.assertEqual(reverse_words("one two three"), "three two one")
        self.assertEqual(reverse_words("the quick brown fox"), "fox brown quick the")

    def test_reverse_words_single_word(self):
        """Test reversing a single word returns same word."""
        self.assertEqual(reverse_words("hello"), "hello")
        self.assertEqual(reverse_words("single"), "single")

    def test_reverse_words_extra_spaces(self):
        """Test handling of extra spaces between words."""
        self.assertEqual(reverse_words("hello  world"), "world hello")
        self.assertEqual(reverse_words("  one   two  "), "two one")
        self.assertEqual(reverse_words("multiple    spaces    here"), "here spaces multiple")

    def test_reverse_words_empty_string(self):
        """Test reversing empty string."""
        self.assertEqual(reverse_words(""), "")
        self.assertEqual(reverse_words("   "), "")

    def test_reverse_words_type_error(self):
        """Test that non-string input raises TypeError."""
        with self.assertRaises(TypeError):
            reverse_words(123)
        with self.assertRaises(TypeError):
            reverse_words(None)


class TestIsPalindrome(unittest.TestCase):
    """Test cases for is_palindrome function."""

    def test_is_palindrome_true_cases(self):
        """Test strings that are palindromes."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("noon"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("a"))

    def test_is_palindrome_case_variations(self):
        """Test palindromes with different case variations."""
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("Noon"))
        self.assertTrue(is_palindrome("LEVEL"))
        self.assertTrue(is_palindrome("AbBa"))

    def test_is_palindrome_with_spaces(self):
        """Test palindromes with spaces."""
        self.assertTrue(is_palindrome("race car"))
        self.assertTrue(is_palindrome("a man a plan a canal panama"))
        self.assertTrue(is_palindrome("taco cat"))

    def test_is_palindrome_false_cases(self):
        """Test strings that are not palindromes."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))

    def test_is_palindrome_empty_string(self):
        """Test empty string is considered palindrome."""
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_single_character(self):
        """Test single characters are palindromes."""
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))

    def test_is_palindrome_unicode(self):
        """Test palindromes with Unicode characters."""
        self.assertTrue(is_palindrome("été"))
        self.assertTrue(is_palindrome("aña"))

    def test_is_palindrome_type_error(self):
        """Test that non-string input raises TypeError."""
        with self.assertRaises(TypeError):
            is_palindrome(12321)
        with self.assertRaises(TypeError):
            is_palindrome(None)


class TestCountVowels(unittest.TestCase):
    """Test cases for count_vowels function."""

    def test_count_vowels_mixed_case(self):
        """Test counting vowels with mixed case."""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("HELLO"), 2)
        self.assertEqual(count_vowels("HeLLo"), 2)
        self.assertEqual(count_vowels("Programming"), 3)

    def test_count_vowels_all_vowels(self):
        """Test strings with all vowels."""
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("AeIoU"), 5)

    def test_count_vowels_no_vowels(self):
        """Test strings with no vowels."""
        self.assertEqual(count_vowels("rhythm"), 0)
        self.assertEqual(count_vowels("fly"), 0)
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("xyz"), 0)

    def test_count_vowels_empty_string(self):
        """Test counting vowels in empty string."""
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_with_spaces_and_punctuation(self):
        """Test counting vowels with spaces and punctuation."""
        self.assertEqual(count_vowels("Hello, World!"), 3)
        self.assertEqual(count_vowels("a e i o u"), 5)
        self.assertEqual(count_vowels("Test! 123"), 1)

    def test_count_vowels_unicode(self):
        """Test vowel counting with Unicode characters (counts only ASCII vowels)."""
        self.assertEqual(count_vowels("café"), 1)
        self.assertEqual(count_vowels("naïve"), 2)

    def test_count_vowels_type_error(self):
        """Test that non-string input raises TypeError."""
        with self.assertRaises(TypeError):
            count_vowels(12345)
        with self.assertRaises(TypeError):
            count_vowels(None)


class TestTitleCase(unittest.TestCase):
    """Test cases for title_case function."""

    def test_title_case_basic(self):
        """Test basic title case conversion."""
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("python programming"), "Python Programming")

    def test_title_case_all_lowercase(self):
        """Test converting all lowercase to title case."""
        self.assertEqual(title_case("the quick brown fox"), "The Quick Brown Fox")
        self.assertEqual(title_case("once upon a time"), "Once Upon A Time")

    def test_title_case_all_uppercase(self):
        """Test converting all uppercase to title case."""
        self.assertEqual(title_case("HELLO WORLD"), "Hello World")
        self.assertEqual(title_case("ALREADY UPPERCASE"), "Already Uppercase")

    def test_title_case_mixed_capitalization(self):
        """Test converting mixed capitalization to title case."""
        self.assertEqual(title_case("hElLo WoRlD"), "Hello World")
        self.assertEqual(title_case("PyThOn PrOgRaMmInG"), "Python Programming")

    def test_title_case_with_punctuation(self):
        """Test title case with punctuation."""
        self.assertEqual(title_case("hello, world!"), "Hello, World!")
        self.assertEqual(title_case("it's a beautiful day"), "It's A Beautiful Day")

    def test_title_case_with_numbers(self):
        """Test title case with numbers."""
        self.assertEqual(title_case("hello 123 world"), "Hello 123 World")
        self.assertEqual(title_case("test 1 2 3"), "Test 1 2 3")

    def test_title_case_empty_string(self):
        """Test title case on empty string."""
        self.assertEqual(title_case(""), "")

    def test_title_case_single_word(self):
        """Test title case on single word."""
        self.assertEqual(title_case("hello"), "Hello")
        self.assertEqual(title_case("WORLD"), "World")

    def test_title_case_extra_spaces(self):
        """Test title case with extra spaces."""
        self.assertEqual(title_case("hello  world"), "Hello World")
        self.assertEqual(title_case("  multiple   spaces  "), "Multiple Spaces")

    def test_title_case_type_error(self):
        """Test that non-string input raises TypeError."""
        with self.assertRaises(TypeError):
            title_case(123)
        with self.assertRaises(TypeError):
            title_case(None)


class TestRemoveDuplicates(unittest.TestCase):
    """Test cases for remove_duplicates function."""

    def test_remove_duplicates_with_duplicates(self):
        """Test removing duplicate characters."""
        self.assertEqual(remove_duplicates("hello"), "helo")
        self.assertEqual(remove_duplicates("aabbcc"), "abc")
        self.assertEqual(remove_duplicates("mississippi"), "misp")

    def test_remove_duplicates_no_duplicates(self):
        """Test string with no duplicates."""
        self.assertEqual(remove_duplicates("abcdef"), "abcdef")
        self.assertEqual(remove_duplicates("world"), "world")

    def test_remove_duplicates_empty_string(self):
        """Test removing duplicates from empty string."""
        self.assertEqual(remove_duplicates(""), "")

    def test_remove_duplicates_preserves_order(self):
        """Test that first occurrence is preserved in order."""
        self.assertEqual(remove_duplicates("banana"), "ban")
        self.assertEqual(remove_duplicates("bookkeeper"), "bokepr")
        self.assertEqual(remove_duplicates("programming"), "progamin")

    def test_remove_duplicates_all_same_character(self):
        """Test string with all same characters."""
        self.assertEqual(remove_duplicates("aaaa"), "a")
        self.assertEqual(remove_duplicates("zzzzzz"), "z")

    def test_remove_duplicates_case_sensitive(self):
        """Test that removal is case-sensitive."""
        self.assertEqual(remove_duplicates("AaBbCc"), "AaBbCc")
        self.assertEqual(remove_duplicates("AAaa"), "Aa")

    def test_remove_duplicates_with_spaces(self):
        """Test removing duplicates with spaces."""
        self.assertEqual(remove_duplicates("hello world"), "helo wrd")
        self.assertEqual(remove_duplicates("a b c a b c"), "a bc")

    def test_remove_duplicates_unicode(self):
        """Test removing duplicates with Unicode characters."""
        self.assertEqual(remove_duplicates("café"), "café")
        self.assertEqual(remove_duplicates("naïve"), "naïve")
        self.assertEqual(remove_duplicates("ééé"), "é")

    def test_remove_duplicates_type_error(self):
        """Test that non-string input raises TypeError."""
        with self.assertRaises(TypeError):
            remove_duplicates(123)
        with self.assertRaises(TypeError):
            remove_duplicates(None)


if __name__ == '__main__':
    unittest.main()
