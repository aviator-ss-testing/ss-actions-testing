"""Unit tests for string utility functions."""

import unittest
from string_utils import (
    reverse_string,
    is_palindrome,
    count_vowels,
    title_case,
    remove_whitespace,
    truncate
)


class TestReverseString(unittest.TestCase):
    """Test cases for reverse_string function."""

    def test_reverse_empty_string(self):
        """Test reversing an empty string returns empty string."""
        self.assertEqual(reverse_string(""), "")

    def test_reverse_single_character(self):
        """Test reversing a single character returns the same character."""
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("Z"), "Z")

    def test_reverse_basic_string(self):
        """Test reversing a basic string."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_reverse_long_string(self):
        """Test reversing a long string."""
        long_string = "The quick brown fox jumps over the lazy dog"
        expected = "god yzal eht revo spmuj xof nworb kciuq ehT"
        self.assertEqual(reverse_string(long_string), expected)

    def test_reverse_with_special_characters(self):
        """Test reversing strings with special characters."""
        self.assertEqual(reverse_string("hello!"), "!olleh")
        self.assertEqual(reverse_string("a@b#c$"), "$c#b@a")
        self.assertEqual(reverse_string("123-456"), "654-321")

    def test_reverse_with_unicode(self):
        """Test reversing strings with unicode characters."""
        self.assertEqual(reverse_string("café"), "éfac")
        self.assertEqual(reverse_string("你好"), "好你")
        self.assertEqual(reverse_string("🚀🌟"), "🌟🚀")

    def test_reverse_with_whitespace(self):
        """Test reversing strings with whitespace."""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string("  spaces  "), "  secaps  ")

    def test_reverse_non_string_raises_type_error(self):
        """Test that passing non-string raises TypeError."""
        with self.assertRaises(TypeError):
            reverse_string(123)
        with self.assertRaises(TypeError):
            reverse_string(None)
        with self.assertRaises(TypeError):
            reverse_string(["list"])


class TestIsPalindrome(unittest.TestCase):
    """Test cases for is_palindrome function."""

    def test_palindrome_empty_string(self):
        """Test that empty string is considered a palindrome."""
        self.assertTrue(is_palindrome(""))

    def test_palindrome_single_character(self):
        """Test that single character is a palindrome."""
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))

    def test_palindrome_simple_palindromes(self):
        """Test simple palindrome strings."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("noon"))
        self.assertTrue(is_palindrome("civic"))
        self.assertTrue(is_palindrome("radar"))

    def test_palindrome_case_insensitive(self):
        """Test that palindrome check is case-insensitive."""
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("NoOn"))
        self.assertTrue(is_palindrome("Aa"))

    def test_palindrome_with_spaces(self):
        """Test palindromes with spaces (spaces ignored)."""
        self.assertTrue(is_palindrome("race car"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("was it a car or a cat I saw"))

    def test_not_palindrome(self):
        """Test strings that are not palindromes."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("Python"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("ab"))

    def test_palindrome_with_special_characters(self):
        """Test palindromes with special characters (not ignored)."""
        self.assertTrue(is_palindrome("!!"))
        self.assertFalse(is_palindrome("hello!"))

    def test_palindrome_non_string_raises_type_error(self):
        """Test that passing non-string raises TypeError."""
        with self.assertRaises(TypeError):
            is_palindrome(12321)
        with self.assertRaises(TypeError):
            is_palindrome(None)


class TestCountVowels(unittest.TestCase):
    """Test cases for count_vowels function."""

    def test_count_vowels_empty_string(self):
        """Test counting vowels in empty string returns 0."""
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_no_vowels(self):
        """Test strings with no vowels."""
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("xyz"), 0)
        self.assertEqual(count_vowels("123"), 0)
        self.assertEqual(count_vowels("!@#$%"), 0)

    def test_count_vowels_all_vowels(self):
        """Test strings with all vowels."""
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("aEiOu"), 5)

    def test_count_vowels_mixed_string(self):
        """Test counting vowels in mixed strings."""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("beautiful"), 5)
        self.assertEqual(count_vowels("The quick brown fox"), 5)

    def test_count_vowels_case_insensitive(self):
        """Test that vowel counting is case-insensitive."""
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)
        self.assertEqual(count_vowels("HELLO"), 2)

    def test_count_vowels_with_special_characters(self):
        """Test counting vowels in strings with special characters."""
        self.assertEqual(count_vowels("hello!"), 2)
        self.assertEqual(count_vowels("a@e#i$o%u"), 5)

    def test_count_vowels_with_unicode(self):
        """Test counting vowels with unicode characters (standard vowels only)."""
        self.assertEqual(count_vowels("café"), 1)
        self.assertEqual(count_vowels("hello 你好"), 2)

    def test_count_vowels_repeated_vowels(self):
        """Test strings with repeated vowels."""
        self.assertEqual(count_vowels("aaa"), 3)
        self.assertEqual(count_vowels("eee"), 3)
        self.assertEqual(count_vowels("oooo"), 4)

    def test_count_vowels_non_string_raises_type_error(self):
        """Test that passing non-string raises TypeError."""
        with self.assertRaises(TypeError):
            count_vowels(123)
        with self.assertRaises(TypeError):
            count_vowels(None)


class TestTitleCase(unittest.TestCase):
    """Test cases for title_case function."""

    def test_title_case_empty_string(self):
        """Test title case of empty string."""
        self.assertEqual(title_case(""), "")

    def test_title_case_single_word(self):
        """Test title case with single word."""
        self.assertEqual(title_case("hello"), "Hello")
        self.assertEqual(title_case("WORLD"), "World")
        self.assertEqual(title_case("PyThOn"), "Python")

    def test_title_case_multiple_words(self):
        """Test title case with multiple words."""
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("the quick brown fox"), "The Quick Brown Fox")

    def test_title_case_already_title_case(self):
        """Test title case on already title-cased string."""
        self.assertEqual(title_case("Hello World"), "Hello World")

    def test_title_case_non_string_raises_type_error(self):
        """Test that passing non-string raises TypeError."""
        with self.assertRaises(TypeError):
            title_case(123)


class TestRemoveWhitespace(unittest.TestCase):
    """Test cases for remove_whitespace function."""

    def test_remove_all_whitespace(self):
        """Test removing all whitespace from string."""
        self.assertEqual(remove_whitespace("hello world", "all"), "helloworld")
        self.assertEqual(remove_whitespace("  a  b  c  ", "all"), "abc")
        self.assertEqual(remove_whitespace("hello\nworld\ttab", "all"), "helloworldtab")

    def test_remove_leading_whitespace(self):
        """Test removing leading whitespace."""
        self.assertEqual(remove_whitespace("  hello", "leading"), "hello")
        self.assertEqual(remove_whitespace("  hello  ", "leading"), "hello  ")
        self.assertEqual(remove_whitespace("hello", "leading"), "hello")

    def test_remove_trailing_whitespace(self):
        """Test removing trailing whitespace."""
        self.assertEqual(remove_whitespace("hello  ", "trailing"), "hello")
        self.assertEqual(remove_whitespace("  hello  ", "trailing"), "  hello")
        self.assertEqual(remove_whitespace("hello", "trailing"), "hello")

    def test_remove_both_whitespace(self):
        """Test removing leading and trailing whitespace."""
        self.assertEqual(remove_whitespace("  hello  ", "both"), "hello")
        self.assertEqual(remove_whitespace("  hello world  ", "both"), "hello world")
        self.assertEqual(remove_whitespace("hello", "both"), "hello")

    def test_remove_whitespace_default_mode(self):
        """Test that default mode is 'all'."""
        self.assertEqual(remove_whitespace("hello world"), "helloworld")

    def test_remove_whitespace_empty_string(self):
        """Test removing whitespace from empty string."""
        self.assertEqual(remove_whitespace("", "all"), "")
        self.assertEqual(remove_whitespace("   ", "all"), "")

    def test_remove_whitespace_invalid_mode(self):
        """Test that invalid mode raises ValueError."""
        with self.assertRaises(ValueError) as context:
            remove_whitespace("hello", "invalid")
        self.assertIn("Invalid mode", str(context.exception))

    def test_remove_whitespace_non_string_raises_type_error(self):
        """Test that passing non-string raises TypeError."""
        with self.assertRaises(TypeError):
            remove_whitespace(123)


class TestTruncate(unittest.TestCase):
    """Test cases for truncate function."""

    def test_truncate_string_shorter_than_limit(self):
        """Test that strings shorter than limit are not truncated."""
        self.assertEqual(truncate("hello", 10), "hello")
        self.assertEqual(truncate("hi", 5), "hi")

    def test_truncate_string_equal_to_limit(self):
        """Test that strings equal to limit are not truncated."""
        self.assertEqual(truncate("hello", 5), "hello")

    def test_truncate_string_longer_than_limit_with_ellipsis(self):
        """Test truncating strings longer than limit with ellipsis."""
        self.assertEqual(truncate("hello world", 8), "hello...")
        self.assertEqual(truncate("The quick brown fox", 10), "The qui...")
        self.assertEqual(truncate("abcdefghij", 7), "abcd...")

    def test_truncate_string_longer_than_limit_without_ellipsis(self):
        """Test truncating strings longer than limit without ellipsis."""
        self.assertEqual(truncate("hello world", 8, ellipsis=False), "hello wo")
        self.assertEqual(truncate("The quick brown fox", 10, ellipsis=False), "The quick ")

    def test_truncate_very_short_limit_with_ellipsis(self):
        """Test truncating with limit less than 3 (no room for ellipsis)."""
        self.assertEqual(truncate("hello", 2), "he")
        self.assertEqual(truncate("hello", 1), "h")
        self.assertEqual(truncate("hello", 0), "")

    def test_truncate_empty_string(self):
        """Test truncating empty string."""
        self.assertEqual(truncate("", 5), "")
        self.assertEqual(truncate("", 0), "")

    def test_truncate_exact_ellipsis_boundary(self):
        """Test truncating at exact ellipsis boundary (length 3)."""
        self.assertEqual(truncate("hello", 3), "...")
        self.assertEqual(truncate("hi", 3), "hi")

    def test_truncate_special_characters(self):
        """Test truncating strings with special characters."""
        self.assertEqual(truncate("hello!@#$%", 8), "hello...")
        self.assertEqual(truncate("test@example.com", 10), "test@ex...")

    def test_truncate_unicode_characters(self):
        """Test truncating strings with unicode characters."""
        self.assertEqual(truncate("café world", 8), "café ...")
        self.assertEqual(truncate("你好世界", 3), "...")

    def test_truncate_negative_length_raises_value_error(self):
        """Test that negative length raises ValueError."""
        with self.assertRaises(ValueError) as context:
            truncate("hello", -1)
        self.assertIn("non-negative", str(context.exception))

    def test_truncate_non_string_raises_type_error(self):
        """Test that passing non-string raises TypeError."""
        with self.assertRaises(TypeError):
            truncate(123, 5)

    def test_truncate_non_integer_length_raises_type_error(self):
        """Test that passing non-integer length raises TypeError."""
        with self.assertRaises(TypeError):
            truncate("hello", 5.5)
        with self.assertRaises(TypeError):
            truncate("hello", "5")


if __name__ == "__main__":
    unittest.main()
