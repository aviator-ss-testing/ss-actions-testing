import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from string_utils import reverse_words, count_vowels, is_palindrome, truncate, memoize


class TestReverseWords(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(reverse_words("hello"), "hello")
        self.assertEqual(reverse_words("Python"), "Python")

    def test_multiple_words(self):
        self.assertEqual(reverse_words("hello world"), "world hello")
        self.assertEqual(reverse_words("the quick brown fox"), "fox brown quick the")
        self.assertEqual(reverse_words("one two three four five"), "five four three two one")

    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_multiple_spaces(self):
        self.assertEqual(reverse_words("hello  world"), "world hello")
        self.assertEqual(reverse_words("  spaces  everywhere  "), "everywhere spaces")

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            reverse_words(123)
        with self.assertRaises(TypeError):
            reverse_words(None)
        with self.assertRaises(TypeError):
            reverse_words(["list", "of", "words"])


class TestCountVowels(unittest.TestCase):
    def test_mixed_case(self):
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)
        self.assertEqual(count_vowels("The Quick Brown Fox"), 5)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("xyz"), 0)
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("123"), 0)

    def test_all_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("aaa"), 3)

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_special_characters(self):
        self.assertEqual(count_vowels("Hello! How are you?"), 7)
        self.assertEqual(count_vowels("@#$%^&*"), 0)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            count_vowels(123)
        with self.assertRaises(TypeError):
            count_vowels(None)


class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("noon"))

    def test_palindromes_with_spaces(self):
        self.assertTrue(is_palindrome("race car"))
        self.assertTrue(is_palindrome("nurses run"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_case_insensitive_palindromes(self):
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("Was it a rat I saw"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            is_palindrome(12321)
        with self.assertRaises(TypeError):
            is_palindrome(None)


class TestTruncate(unittest.TestCase):
    def test_text_longer_than_limit(self):
        self.assertEqual(truncate("Hello World", 5), "Hello...")
        self.assertEqual(truncate("The quick brown fox", 9), "The quick...")
        self.assertEqual(truncate("Python programming", 6), "Python...")

    def test_text_shorter_than_limit(self):
        self.assertEqual(truncate("Hello", 10), "Hello")
        self.assertEqual(truncate("Short", 20), "Short")
        self.assertEqual(truncate("", 5), "")

    def test_text_equal_to_limit(self):
        self.assertEqual(truncate("Hello", 5), "Hello")
        self.assertEqual(truncate("Exact", 5), "Exact")

    def test_custom_suffix(self):
        self.assertEqual(truncate("Hello World", 5, suffix="..."), "Hello...")
        self.assertEqual(truncate("Hello World", 5, suffix=">>"), "Hello>>")
        self.assertEqual(truncate("Hello World", 5, suffix=""), "Hello")

    def test_zero_length(self):
        self.assertEqual(truncate("Hello", 0), "...")
        self.assertEqual(truncate("Hello", 0, suffix=">>"), ">>")

    def test_invalid_text_type(self):
        with self.assertRaises(TypeError):
            truncate(123, 5)
        with self.assertRaises(TypeError):
            truncate(None, 5)

    def test_invalid_length_type(self):
        with self.assertRaises(TypeError):
            truncate("Hello", "5")
        with self.assertRaises(TypeError):
            truncate("Hello", 5.5)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            truncate("Hello", -1)


class TestMemoizeDecorator(unittest.TestCase):
    def test_caching_behavior(self):
        call_count = {'count': 0}

        @memoize
        def expensive_function(n):
            call_count['count'] += 1
            return n * 2

        result1 = expensive_function(5)
        self.assertEqual(result1, 10)
        self.assertEqual(call_count['count'], 1)

        result2 = expensive_function(5)
        self.assertEqual(result2, 10)
        self.assertEqual(call_count['count'], 1)

        result3 = expensive_function(10)
        self.assertEqual(result3, 20)
        self.assertEqual(call_count['count'], 2)

        result4 = expensive_function(5)
        self.assertEqual(result4, 10)
        self.assertEqual(call_count['count'], 2)

    def test_multiple_function_calls_with_different_args(self):
        call_count = {'count': 0}

        @memoize
        def add(a, b):
            call_count['count'] += 1
            return a + b

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(call_count['count'], 1)

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(call_count['count'], 1)

        self.assertEqual(add(2, 3), 5)
        self.assertEqual(call_count['count'], 2)

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(call_count['count'], 2)

    def test_count_vowels_memoization(self):
        result1 = count_vowels("hello")
        result2 = count_vowels("hello")
        self.assertEqual(result1, result2)
        self.assertEqual(result1, 2)

        result3 = count_vowels("world")
        self.assertEqual(result3, 1)

    def test_preserves_function_metadata(self):
        @memoize
        def documented_function(x):
            return x * 2

        self.assertEqual(documented_function.__name__, "documented_function")


if __name__ == '__main__':
    unittest.main()
