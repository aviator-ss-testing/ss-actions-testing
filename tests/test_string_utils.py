import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.string_utils import (
    reverse_string,
    is_palindrome,
    word_count,
    title_case,
    remove_duplicates,
    truncate
)


class TestReverseString(unittest.TestCase):
    def test_reverse_normal_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("python"), "nohtyp")

    def test_reverse_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_single_character(self):
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("Z"), "Z")

    def test_reverse_string_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_reverse_string_type_error(self):
        with self.assertRaises(TypeError):
            reverse_string(123)
        with self.assertRaises(TypeError):
            reverse_string(None)


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_simple(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("noon"))
        self.assertTrue(is_palindrome("level"))

    def test_palindrome_case_variations(self):
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("Noon"))
        self.assertTrue(is_palindrome("LEVEL"))

    def test_palindrome_single_character(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("world"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_palindrome_type_error(self):
        with self.assertRaises(TypeError):
            is_palindrome(12321)
        with self.assertRaises(TypeError):
            is_palindrome(None)


class TestWordCount(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(word_count("hello"), 1)
        self.assertEqual(word_count("python"), 1)

    def test_multiple_words(self):
        self.assertEqual(word_count("hello world"), 2)
        self.assertEqual(word_count("the quick brown fox"), 4)

    def test_extra_whitespace(self):
        self.assertEqual(word_count("hello  world"), 2)
        self.assertEqual(word_count("  hello   world  "), 2)
        self.assertEqual(word_count("one   two    three"), 3)

    def test_empty_string(self):
        self.assertEqual(word_count(""), 0)

    def test_only_whitespace(self):
        self.assertEqual(word_count("   "), 0)
        self.assertEqual(word_count("\t\n"), 0)

    def test_word_count_type_error(self):
        with self.assertRaises(TypeError):
            word_count(123)
        with self.assertRaises(TypeError):
            word_count(None)


class TestTitleCase(unittest.TestCase):
    def test_lowercase_string(self):
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("python programming"), "Python Programming")

    def test_uppercase_string(self):
        self.assertEqual(title_case("HELLO WORLD"), "Hello World")

    def test_mixed_case_string(self):
        self.assertEqual(title_case("hELLo WoRLD"), "Hello World")

    def test_special_characters(self):
        self.assertEqual(title_case("hello-world"), "Hello-World")
        self.assertEqual(title_case("hello_world"), "Hello_World")
        self.assertEqual(title_case("hello's world"), "Hello'S World")

    def test_empty_string(self):
        self.assertEqual(title_case(""), "")

    def test_single_word(self):
        self.assertEqual(title_case("hello"), "Hello")

    def test_title_case_type_error(self):
        with self.assertRaises(TypeError):
            title_case(123)
        with self.assertRaises(TypeError):
            title_case(None)


class TestRemoveDuplicates(unittest.TestCase):
    def test_consecutive_duplicates(self):
        self.assertEqual(remove_duplicates("hello"), "helo")
        self.assertEqual(remove_duplicates("bookkeeper"), "bokeper")
        self.assertEqual(remove_duplicates("aabbcc"), "abc")

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates("abcdef"), "abcdef")
        self.assertEqual(remove_duplicates("python"), "python")

    def test_all_same_character(self):
        self.assertEqual(remove_duplicates("aaaa"), "a")
        self.assertEqual(remove_duplicates("zzzz"), "z")

    def test_empty_string(self):
        self.assertEqual(remove_duplicates(""), "")

    def test_single_character(self):
        self.assertEqual(remove_duplicates("a"), "a")

    def test_mixed_duplicates(self):
        self.assertEqual(remove_duplicates("aabbccaabbcc"), "abcabc")

    def test_remove_duplicates_type_error(self):
        with self.assertRaises(TypeError):
            remove_duplicates(123)
        with self.assertRaises(TypeError):
            remove_duplicates(None)


class TestTruncate(unittest.TestCase):
    def test_short_string_no_truncation(self):
        self.assertEqual(truncate("hello", 10), "hello")
        self.assertEqual(truncate("hi", 5), "hi")

    def test_exact_length_no_truncation(self):
        self.assertEqual(truncate("hello", 5), "hello")

    def test_long_string_truncation(self):
        self.assertEqual(truncate("hello world", 5), "hello...")
        self.assertEqual(truncate("python programming", 6), "python...")

    def test_custom_suffix(self):
        self.assertEqual(truncate("hello world", 5, "!!!"), "hello!!!")
        self.assertEqual(truncate("hello world", 5, " [more]"), "hello [more]")

    def test_empty_suffix(self):
        self.assertEqual(truncate("hello world", 5, ""), "hello")

    def test_empty_string(self):
        self.assertEqual(truncate("", 5), "")

    def test_zero_length(self):
        self.assertEqual(truncate("hello", 0), "...")

    def test_truncate_type_errors(self):
        with self.assertRaises(TypeError):
            truncate(123, 5)
        with self.assertRaises(TypeError):
            truncate("hello", "5")
        with self.assertRaises(TypeError):
            truncate("hello", 5, 123)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            truncate("hello", -1)


if __name__ == '__main__':
    unittest.main()
