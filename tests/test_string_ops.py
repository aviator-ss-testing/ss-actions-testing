import unittest
import sys
import os
from io import StringIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.string_ops import reverse_words, count_vowels, is_palindrome, title_case, remove_duplicates


class TestStringOps(unittest.TestCase):

    def test_reverse_words_normal_sentence(self):
        """Test reverse_words with a normal sentence"""
        result = reverse_words("hello world")
        self.assertEqual(result, "world hello")

    def test_reverse_words_multiple_words(self):
        """Test reverse_words with multiple words"""
        captured_output = StringIO()
        sys.stdout = captured_output

        result = reverse_words("the quick brown fox")

        sys.stdout = sys.__stdout__

        self.assertEqual(result, "fox brown quick the")

    def test_reverse_words_single_word(self):
        """Test reverse_words with a single word"""
        captured_output = StringIO()
        sys.stdout = captured_output

        result = reverse_words("hello")

        sys.stdout = sys.__stdout__

        self.assertEqual(result, "hello")

    def test_reverse_words_empty_string(self):
        """Test reverse_words with an empty string"""
        captured_output = StringIO()
        sys.stdout = captured_output

        result = reverse_words("")

        sys.stdout = sys.__stdout__

        self.assertEqual(result, "")

    def test_reverse_words_with_extra_spaces(self):
        """Test reverse_words handles extra spaces correctly"""
        captured_output = StringIO()
        sys.stdout = captured_output

        result = reverse_words("hello   world")

        sys.stdout = sys.__stdout__

        self.assertEqual(result, "world hello")

    def test_reverse_words_with_special_characters(self):
        """Test reverse_words with special characters"""
        captured_output = StringIO()
        sys.stdout = captured_output

        result = reverse_words("hello! world?")

        sys.stdout = sys.__stdout__

        self.assertEqual(result, "world? hello!")

    def test_reverse_words_with_numbers(self):
        """Test reverse_words with numbers"""
        captured_output = StringIO()
        sys.stdout = captured_output

        result = reverse_words("test 123 abc 456")

        sys.stdout = sys.__stdout__

        self.assertEqual(result, "456 abc 123 test")

    def test_reverse_words_invalid_type(self):
        """Test reverse_words raises TypeError for non-string input"""
        with self.assertRaises(TypeError) as context:
            reverse_words(123)

        self.assertIn("must be of type str", str(context.exception))

    def test_count_vowels_normal_string(self):
        """Test count_vowels with a normal string"""
        result = count_vowels("hello world")
        self.assertEqual(result, 3)

    def test_count_vowels_all_vowels(self):
        """Test count_vowels with all vowels"""
        result = count_vowels("aeiou")
        self.assertEqual(result, 5)

    def test_count_vowels_no_vowels(self):
        """Test count_vowels with no vowels"""
        result = count_vowels("bcdfg")
        self.assertEqual(result, 0)

    def test_count_vowels_empty_string(self):
        """Test count_vowels with empty string"""
        result = count_vowels("")
        self.assertEqual(result, 0)

    def test_count_vowels_mixed_case(self):
        """Test count_vowels handles both uppercase and lowercase"""
        result = count_vowels("AEIOUaeiou")
        self.assertEqual(result, 10)

    def test_count_vowels_with_numbers_and_special_chars(self):
        """Test count_vowels ignores numbers and special characters"""
        result = count_vowels("h3llo! w0rld@")
        self.assertEqual(result, 1)

    def test_count_vowels_unicode(self):
        """Test count_vowels with unicode characters (accented vowels not counted as standard vowels)"""
        result = count_vowels("café résumé")
        self.assertEqual(result, 2)

    def test_count_vowels_long_string(self):
        """Test count_vowels with a long string"""
        long_text = "a" * 100 + "b" * 100 + "e" * 50
        result = count_vowels(long_text)
        self.assertEqual(result, 150)

    def test_count_vowels_invalid_type(self):
        """Test count_vowels raises TypeError for non-string input"""
        with self.assertRaises(TypeError) as context:
            count_vowels(12345)

        self.assertIn("must be of type str", str(context.exception))

    def test_is_palindrome_simple_palindrome(self):
        """Test is_palindrome with a simple palindrome"""
        result = is_palindrome("racecar")
        self.assertTrue(result)

    def test_is_palindrome_with_spaces(self):
        """Test is_palindrome ignores spaces"""
        result = is_palindrome("race car")
        self.assertTrue(result)

    def test_is_palindrome_with_mixed_case(self):
        """Test is_palindrome is case-insensitive"""
        result = is_palindrome("RaceCar")
        self.assertTrue(result)

    def test_is_palindrome_not_palindrome(self):
        """Test is_palindrome returns False for non-palindromes"""
        result = is_palindrome("hello")
        self.assertFalse(result)

    def test_is_palindrome_empty_string(self):
        """Test is_palindrome with empty string"""
        result = is_palindrome("")
        self.assertTrue(result)

    def test_is_palindrome_single_character(self):
        """Test is_palindrome with single character"""
        result = is_palindrome("a")
        self.assertTrue(result)

    def test_is_palindrome_phrase(self):
        """Test is_palindrome with a phrase"""
        result = is_palindrome("A man a plan a canal Panama")
        self.assertTrue(result)

    def test_is_palindrome_with_special_characters(self):
        """Test is_palindrome with special characters"""
        result = is_palindrome("a!b!a")
        self.assertTrue(result)

    def test_is_palindrome_caching(self):
        """Test is_palindrome memoization works correctly"""
        is_palindrome.cache_clear()

        result1 = is_palindrome("racecar")
        cache_size_1 = len(is_palindrome.cache)

        result2 = is_palindrome("racecar")
        cache_size_2 = len(is_palindrome.cache)

        self.assertTrue(result1)
        self.assertTrue(result2)
        self.assertEqual(cache_size_1, 1)
        self.assertEqual(cache_size_2, 1)

    def test_is_palindrome_invalid_type(self):
        """Test is_palindrome raises TypeError for non-string input"""
        with self.assertRaises(TypeError) as context:
            is_palindrome(12321)

        self.assertIn("must be of type str", str(context.exception))

    def test_title_case_lowercase_string(self):
        """Test title_case with lowercase string"""
        result = title_case("hello world")
        self.assertEqual(result, "Hello World")

    def test_title_case_uppercase_string(self):
        """Test title_case with uppercase string"""
        result = title_case("HELLO WORLD")
        self.assertEqual(result, "Hello World")

    def test_title_case_mixed_case(self):
        """Test title_case with mixed case string"""
        result = title_case("hELLo WoRLd")
        self.assertEqual(result, "Hello World")

    def test_title_case_empty_string(self):
        """Test title_case with empty string"""
        result = title_case("")
        self.assertEqual(result, "")

    def test_title_case_single_word(self):
        """Test title_case with single word"""
        result = title_case("python")
        self.assertEqual(result, "Python")

    def test_title_case_with_apostrophes(self):
        """Test title_case with apostrophes"""
        result = title_case("don't stop")
        self.assertEqual(result, "Don'T Stop")

    def test_title_case_with_numbers(self):
        """Test title_case with numbers"""
        result = title_case("python 3.9 programming")
        self.assertEqual(result, "Python 3.9 Programming")

    def test_title_case_invalid_type(self):
        """Test title_case raises TypeError for non-string input"""
        with self.assertRaises(TypeError) as context:
            title_case(123)

        self.assertIn("must be of type str", str(context.exception))

    def test_remove_duplicates_simple_string(self):
        """Test remove_duplicates with a simple string"""
        result = remove_duplicates("hello")
        self.assertEqual(result, "helo")

    def test_remove_duplicates_all_duplicates(self):
        """Test remove_duplicates with all duplicate characters"""
        result = remove_duplicates("aaaa")
        self.assertEqual(result, "a")

    def test_remove_duplicates_no_duplicates(self):
        """Test remove_duplicates with no duplicates"""
        result = remove_duplicates("abcd")
        self.assertEqual(result, "abcd")

    def test_remove_duplicates_empty_string(self):
        """Test remove_duplicates with empty string"""
        result = remove_duplicates("")
        self.assertEqual(result, "")

    def test_remove_duplicates_preserves_order(self):
        """Test remove_duplicates preserves character order"""
        result = remove_duplicates("programming")
        self.assertEqual(result, "progamin")

    def test_remove_duplicates_with_spaces(self):
        """Test remove_duplicates handles spaces"""
        result = remove_duplicates("hello  world")
        self.assertEqual(result, "helo wrd")

    def test_remove_duplicates_with_special_characters(self):
        """Test remove_duplicates with special characters"""
        result = remove_duplicates("a!b!c!")
        self.assertEqual(result, "a!bc")

    def test_remove_duplicates_case_sensitive(self):
        """Test remove_duplicates is case-sensitive"""
        result = remove_duplicates("AaBbCc")
        self.assertEqual(result, "AaBbCc")

    def test_remove_duplicates_long_string(self):
        """Test remove_duplicates with a long string"""
        long_text = "a" * 100 + "b" * 100 + "a" * 100
        result = remove_duplicates(long_text)
        self.assertEqual(result, "ab")

    def test_remove_duplicates_unicode(self):
        """Test remove_duplicates with unicode characters"""
        result = remove_duplicates("café café")
        self.assertEqual(result, "café ")

    def test_remove_duplicates_invalid_type(self):
        """Test remove_duplicates raises TypeError for non-string input"""
        with self.assertRaises(TypeError) as context:
            remove_duplicates(12345)

        self.assertIn("must be of type str", str(context.exception))


if __name__ == '__main__':
    unittest.main()
