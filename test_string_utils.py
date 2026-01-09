"""
Comprehensive test suite for string_utils module.
"""

import unittest
from string_utils import (
    reverse_words,
    is_palindrome,
    count_vowels,
    title_case,
    snake_to_camel,
    camel_to_snake
)


class TestStringUtils(unittest.TestCase):
    """Test cases for string utility functions."""

    def test_reverse_words_normal_cases(self):
        """Test reverse_words with typical strings."""
        self.assertEqual(reverse_words("hello world"), "world hello")
        self.assertEqual(reverse_words("the quick brown fox"), "fox brown quick the")
        self.assertEqual(reverse_words("Python is great"), "great is Python")

    def test_reverse_words_edge_cases(self):
        """Test reverse_words edge cases."""
        self.assertEqual(reverse_words(""), "")
        self.assertEqual(reverse_words("   "), "")
        self.assertEqual(reverse_words("single"), "single")
        self.assertEqual(reverse_words(None), "")

    def test_reverse_words_special_characters(self):
        """Test reverse_words with special characters and punctuation."""
        self.assertEqual(reverse_words("hello! world?"), "world? hello!")
        self.assertEqual(reverse_words("test-case example"), "example test-case")
        self.assertEqual(reverse_words("one, two, three"), "three two, one,")

    def test_reverse_words_multiple_spaces(self):
        """Test reverse_words handles multiple spaces correctly."""
        self.assertEqual(reverse_words("hello    world"), "world hello")
        self.assertEqual(reverse_words("  leading spaces"), "spaces leading")
        self.assertEqual(reverse_words("trailing spaces  "), "spaces trailing")

    def test_reverse_words_type_error(self):
        """Test reverse_words raises TypeError for invalid input."""
        with self.assertRaises(TypeError):
            reverse_words(123)
        with self.assertRaises(TypeError):
            reverse_words([])

    def test_is_palindrome_true_cases(self):
        """Test is_palindrome with palindromic strings."""
        palindromes = ["racecar", "level", "noon", "civic", "radar"]
        for text in palindromes:
            with self.subTest(text=text):
                self.assertTrue(is_palindrome(text))

    def test_is_palindrome_false_cases(self):
        """Test is_palindrome with non-palindromic strings."""
        non_palindromes = ["hello", "world", "python", "test", "example"]
        for text in non_palindromes:
            with self.subTest(text=text):
                self.assertFalse(is_palindrome(text))

    def test_is_palindrome_with_spaces_and_punctuation(self):
        """Test is_palindrome ignores spaces, punctuation, and case."""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))
        self.assertTrue(is_palindrome("Madam, I'm Adam"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))

    def test_is_palindrome_edge_cases(self):
        """Test is_palindrome edge cases."""
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("   "))
        self.assertTrue(is_palindrome(None))
        self.assertTrue(is_palindrome("!!!"))

    def test_is_palindrome_numbers(self):
        """Test is_palindrome with numbers."""
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("1001"))
        self.assertFalse(is_palindrome("12345"))

    def test_is_palindrome_type_error(self):
        """Test is_palindrome raises TypeError for invalid input."""
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome([])

    def test_count_vowels_normal_cases(self):
        """Test count_vowels with typical strings."""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("world"), 1)
        self.assertEqual(count_vowels("programming"), 3)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_count_vowels_edge_cases(self):
        """Test count_vowels edge cases."""
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels(None), 0)
        self.assertEqual(count_vowels("xyz"), 0)
        self.assertEqual(count_vowels("a"), 1)

    def test_count_vowels_mixed_case(self):
        """Test count_vowels is case-insensitive."""
        self.assertEqual(count_vowels("HeLLo WoRLd"), 3)
        self.assertEqual(count_vowels("AaEeIiOoUu"), 10)

    def test_count_vowels_with_special_characters(self):
        """Test count_vowels with special characters."""
        self.assertEqual(count_vowels("hello!@#$%"), 2)
        self.assertEqual(count_vowels("test 123"), 1)
        self.assertEqual(count_vowels("!@#$%^&*()"), 0)

    def test_count_vowels_unicode(self):
        """Test count_vowels with Unicode characters."""
        self.assertEqual(count_vowels("café"), 1)
        self.assertEqual(count_vowels("naïve"), 2)
        self.assertEqual(count_vowels("Björk"), 0)

    def test_count_vowels_type_error(self):
        """Test count_vowels raises TypeError for invalid input."""
        with self.assertRaises(TypeError):
            count_vowels(123)
        with self.assertRaises(TypeError):
            count_vowels([])

    def test_title_case_normal_cases(self):
        """Test title_case with typical strings."""
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("python programming"), "Python Programming")
        self.assertEqual(title_case("the quick brown fox"), "The Quick Brown Fox")

    def test_title_case_edge_cases(self):
        """Test title_case edge cases."""
        self.assertEqual(title_case(""), "")
        self.assertEqual(title_case(None), "")
        self.assertEqual(title_case("a"), "A")
        self.assertEqual(title_case("   "), "   ")

    def test_title_case_already_capitalized(self):
        """Test title_case with already capitalized strings."""
        self.assertEqual(title_case("Hello World"), "Hello World")
        self.assertEqual(title_case("HELLO WORLD"), "Hello World")

    def test_title_case_with_punctuation(self):
        """Test title_case with punctuation."""
        self.assertEqual(title_case("hello, world!"), "Hello, World!")
        self.assertEqual(title_case("it's a test"), "It'S A Test")

    def test_title_case_type_error(self):
        """Test title_case raises TypeError for invalid input."""
        with self.assertRaises(TypeError):
            title_case(123)
        with self.assertRaises(TypeError):
            title_case([])

    def test_snake_to_camel_normal_cases(self):
        """Test snake_to_camel with typical snake_case strings."""
        self.assertEqual(snake_to_camel("hello_world"), "helloWorld")
        self.assertEqual(snake_to_camel("user_name"), "userName")
        self.assertEqual(snake_to_camel("get_user_by_id"), "getUserById")
        self.assertEqual(snake_to_camel("calculate_total_price"), "calculateTotalPrice")

    def test_snake_to_camel_edge_cases(self):
        """Test snake_to_camel edge cases."""
        self.assertEqual(snake_to_camel(""), "")
        self.assertEqual(snake_to_camel(None), "")
        self.assertEqual(snake_to_camel("single"), "single")
        self.assertEqual(snake_to_camel("a_b"), "aB")

    def test_snake_to_camel_multiple_underscores(self):
        """Test snake_to_camel with multiple consecutive underscores."""
        self.assertEqual(snake_to_camel("hello__world"), "helloWorld")
        self.assertEqual(snake_to_camel("test___case"), "testCase")

    def test_snake_to_camel_leading_trailing_underscores(self):
        """Test snake_to_camel with leading/trailing underscores."""
        self.assertEqual(snake_to_camel("_hello_world"), "HelloWorld")
        self.assertEqual(snake_to_camel("hello_world_"), "helloWorld")
        self.assertEqual(snake_to_camel("_hello_world_"), "HelloWorld")

    def test_snake_to_camel_type_error(self):
        """Test snake_to_camel raises TypeError for invalid input."""
        with self.assertRaises(TypeError):
            snake_to_camel(123)
        with self.assertRaises(TypeError):
            snake_to_camel([])

    def test_camel_to_snake_normal_cases(self):
        """Test camel_to_snake with typical camelCase strings."""
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")
        self.assertEqual(camel_to_snake("userName"), "user_name")
        self.assertEqual(camel_to_snake("getUserById"), "get_user_by_id")
        self.assertEqual(camel_to_snake("calculateTotalPrice"), "calculate_total_price")

    def test_camel_to_snake_pascal_case(self):
        """Test camel_to_snake with PascalCase strings."""
        self.assertEqual(camel_to_snake("HelloWorld"), "hello_world")
        self.assertEqual(camel_to_snake("UserName"), "user_name")
        self.assertEqual(camel_to_snake("MyClass"), "my_class")

    def test_camel_to_snake_edge_cases(self):
        """Test camel_to_snake edge cases."""
        self.assertEqual(camel_to_snake(""), "")
        self.assertEqual(camel_to_snake(None), "")
        self.assertEqual(camel_to_snake("single"), "single")
        self.assertEqual(camel_to_snake("a"), "a")

    def test_camel_to_snake_consecutive_capitals(self):
        """Test camel_to_snake with consecutive capital letters."""
        self.assertEqual(camel_to_snake("HTTPResponse"), "h_t_t_p_response")
        self.assertEqual(camel_to_snake("XMLParser"), "x_m_l_parser")
        self.assertEqual(camel_to_snake("IOError"), "i_o_error")

    def test_camel_to_snake_single_capital(self):
        """Test camel_to_snake with single capital letter."""
        self.assertEqual(camel_to_snake("A"), "a")
        self.assertEqual(camel_to_snake("AB"), "a_b")

    def test_camel_to_snake_type_error(self):
        """Test camel_to_snake raises TypeError for invalid input."""
        with self.assertRaises(TypeError):
            camel_to_snake(123)
        with self.assertRaises(TypeError):
            camel_to_snake([])


if __name__ == '__main__':
    unittest.main()
