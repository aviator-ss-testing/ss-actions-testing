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
        """Test reverse_words with normal strings."""
        self.assertEqual(reverse_words("hello world"), "world hello")
        self.assertEqual(reverse_words("one two three"), "three two one")
        self.assertEqual(reverse_words("Python is great"), "great is Python")
        self.assertEqual(reverse_words("single"), "single")

    def test_reverse_words_edge_cases(self):
        """Test reverse_words with edge cases."""
        self.assertEqual(reverse_words(""), "")
        self.assertEqual(reverse_words("   "), "")
        self.assertEqual(reverse_words("  multiple   spaces  "), "spaces multiple")
        self.assertEqual(reverse_words("word"), "word")

    def test_reverse_words_special_characters(self):
        """Test reverse_words with special characters and punctuation."""
        self.assertEqual(reverse_words("hello, world!"), "world! hello,")
        self.assertEqual(reverse_words("one-two three"), "three one-two")
        self.assertEqual(reverse_words("test@example.com test2"), "test2 test@example.com")

    def test_reverse_words_unicode(self):
        """Test reverse_words with Unicode characters."""
        self.assertEqual(reverse_words("café résumé"), "résumé café")
        self.assertEqual(reverse_words("日本語 テスト"), "テスト 日本語")
        self.assertEqual(reverse_words("emoji 😀 test"), "test 😀 emoji")

    def test_reverse_words_none_input(self):
        """Test reverse_words with None input."""
        self.assertEqual(reverse_words(None), "")

    def test_reverse_words_invalid_type(self):
        """Test reverse_words raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            reverse_words(123)
        with self.assertRaises(TypeError):
            reverse_words(['hello', 'world'])
        with self.assertRaises(TypeError):
            reverse_words({'key': 'value'})

    def test_is_palindrome_normal_cases(self):
        """Test is_palindrome with normal palindromic strings."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("noon"))

    def test_is_palindrome_non_palindrome(self):
        """Test is_palindrome correctly identifies non-palindromes."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("test"))

    def test_is_palindrome_case_insensitive(self):
        """Test is_palindrome is case-insensitive."""
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("MADAM"))
        self.assertTrue(is_palindrome("Level"))

    def test_is_palindrome_with_spaces_and_punctuation(self):
        """Test is_palindrome ignores spaces and punctuation."""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("race car"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))

    def test_is_palindrome_edge_cases(self):
        """Test is_palindrome with edge cases."""
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("   "))
        self.assertTrue(is_palindrome("!!!"))

    def test_is_palindrome_unicode(self):
        """Test is_palindrome with Unicode characters."""
        for test_case, expected in [
            ("測測", True),
            ("aba", True),
        ]:
            with self.subTest(test_case=test_case):
                self.assertEqual(is_palindrome(test_case), expected)

    def test_is_palindrome_none_input(self):
        """Test is_palindrome with None input."""
        self.assertTrue(is_palindrome(None))

    def test_is_palindrome_invalid_type(self):
        """Test is_palindrome raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome(['test'])
        with self.assertRaises(TypeError):
            is_palindrome({'key': 'value'})

    def test_count_vowels_normal_cases(self):
        """Test count_vowels with normal strings."""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("world"), 1)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("Python"), 1)

    def test_count_vowels_case_insensitive(self):
        """Test count_vowels is case-insensitive."""
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)
        self.assertEqual(count_vowels("HeLLo WoRLd"), 3)
        self.assertEqual(count_vowels("TESTING"), 2)

    def test_count_vowels_edge_cases(self):
        """Test count_vowels with edge cases."""
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("   "), 0)
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(count_vowels("xyz"), 0)

    def test_count_vowels_special_characters(self):
        """Test count_vowels with special characters and punctuation."""
        self.assertEqual(count_vowels("hello, world!"), 3)
        self.assertEqual(count_vowels("test@example.com"), 5)
        self.assertEqual(count_vowels("one-two-three"), 5)
        self.assertEqual(count_vowels("123!@#"), 0)

    def test_count_vowels_unicode(self):
        """Test count_vowels with Unicode characters."""
        for test_case, expected in [
            ("café", 1),
            ("résumé", 1),
            ("日本語", 0),
            ("emoji test", 4),
        ]:
            with self.subTest(test_case=test_case):
                self.assertEqual(count_vowels(test_case), expected)

    def test_count_vowels_none_input(self):
        """Test count_vowels with None input."""
        self.assertEqual(count_vowels(None), 0)

    def test_count_vowels_invalid_type(self):
        """Test count_vowels raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            count_vowels(123)
        with self.assertRaises(TypeError):
            count_vowels(['test'])
        with self.assertRaises(TypeError):
            count_vowels({'key': 'value'})

    def test_title_case_normal_cases(self):
        """Test title_case with normal strings."""
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("python programming"), "Python Programming")
        self.assertEqual(title_case("test string"), "Test String")
        self.assertEqual(title_case("one two three"), "One Two Three")

    def test_title_case_edge_cases(self):
        """Test title_case with edge cases."""
        self.assertEqual(title_case(""), "")
        self.assertEqual(title_case("a"), "A")
        self.assertEqual(title_case("   "), "   ")
        self.assertEqual(title_case("word"), "Word")

    def test_title_case_special_characters(self):
        """Test title_case with special characters and punctuation."""
        self.assertEqual(title_case("hello, world!"), "Hello, World!")
        self.assertEqual(title_case("one-two-three"), "One-Two-Three")
        self.assertEqual(title_case("test@example.com"), "Test@Example.Com")
        self.assertEqual(title_case("it's a test"), "It'S A Test")

    def test_title_case_already_title_case(self):
        """Test title_case with already formatted strings."""
        self.assertEqual(title_case("Hello World"), "Hello World")
        self.assertEqual(title_case("Python Programming"), "Python Programming")

    def test_title_case_unicode(self):
        """Test title_case with Unicode characters."""
        for test_case, expected in [
            ("café résumé", "Café Résumé"),
            ("日本語 test", "日本語 Test"),
        ]:
            with self.subTest(test_case=test_case):
                self.assertEqual(title_case(test_case), expected)

    def test_title_case_none_input(self):
        """Test title_case with None input."""
        self.assertEqual(title_case(None), "")

    def test_title_case_invalid_type(self):
        """Test title_case raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            title_case(123)
        with self.assertRaises(TypeError):
            title_case(['test'])
        with self.assertRaises(TypeError):
            title_case({'key': 'value'})

    def test_snake_to_camel_normal_cases(self):
        """Test snake_to_camel with normal snake_case strings."""
        self.assertEqual(snake_to_camel("hello_world"), "helloWorld")
        self.assertEqual(snake_to_camel("test_string"), "testString")
        self.assertEqual(snake_to_camel("one_two_three"), "oneTwoThree")
        self.assertEqual(snake_to_camel("user_profile_name"), "userProfileName")

    def test_snake_to_camel_edge_cases(self):
        """Test snake_to_camel with edge cases."""
        self.assertEqual(snake_to_camel(""), "")
        self.assertEqual(snake_to_camel("word"), "word")
        self.assertEqual(snake_to_camel("a_b"), "aB")
        self.assertEqual(snake_to_camel("single"), "single")

    def test_snake_to_camel_multiple_underscores(self):
        """Test snake_to_camel with multiple consecutive underscores."""
        self.assertEqual(snake_to_camel("hello__world"), "helloWorld")
        self.assertEqual(snake_to_camel("test___string"), "testString")
        self.assertEqual(snake_to_camel("_leading"), "Leading")
        self.assertEqual(snake_to_camel("trailing_"), "trailing")

    def test_snake_to_camel_special_cases(self):
        """Test snake_to_camel with special cases."""
        for test_case, expected in [
            ("uppercase_snake", "uppercaseSnake"),
            ("mixed_case_test", "mixedCaseTest"),
            ("test_123_value", "test123Value"),
        ]:
            with self.subTest(test_case=test_case):
                self.assertEqual(snake_to_camel(test_case), expected)

    def test_snake_to_camel_none_input(self):
        """Test snake_to_camel with None input."""
        self.assertEqual(snake_to_camel(None), "")

    def test_snake_to_camel_invalid_type(self):
        """Test snake_to_camel raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            snake_to_camel(123)
        with self.assertRaises(TypeError):
            snake_to_camel(['test'])
        with self.assertRaises(TypeError):
            snake_to_camel({'key': 'value'})

    def test_camel_to_snake_normal_cases(self):
        """Test camel_to_snake with normal camelCase strings."""
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")
        self.assertEqual(camel_to_snake("testString"), "test_string")
        self.assertEqual(camel_to_snake("oneTwoThree"), "one_two_three")
        self.assertEqual(camel_to_snake("userProfileName"), "user_profile_name")

    def test_camel_to_snake_pascal_case(self):
        """Test camel_to_snake with PascalCase strings."""
        self.assertEqual(camel_to_snake("HelloWorld"), "hello_world")
        self.assertEqual(camel_to_snake("TestString"), "test_string")
        self.assertEqual(camel_to_snake("UserProfile"), "user_profile")
        self.assertEqual(camel_to_snake("OneTwoThree"), "one_two_three")

    def test_camel_to_snake_edge_cases(self):
        """Test camel_to_snake with edge cases."""
        self.assertEqual(camel_to_snake(""), "")
        self.assertEqual(camel_to_snake("word"), "word")
        self.assertEqual(camel_to_snake("aB"), "a_b")
        self.assertEqual(camel_to_snake("single"), "single")

    def test_camel_to_snake_consecutive_capitals(self):
        """Test camel_to_snake with consecutive capital letters."""
        self.assertEqual(camel_to_snake("HTTPResponse"), "h_t_t_p_response")
        self.assertEqual(camel_to_snake("XMLParser"), "x_m_l_parser")
        self.assertEqual(camel_to_snake("URLPath"), "u_r_l_path")

    def test_camel_to_snake_with_numbers(self):
        """Test camel_to_snake with numbers."""
        for test_case, expected in [
            ("test123Value", "test123_value"),
            ("value1Test2", "value1_test2"),
            ("testABC123", "test_a_b_c123"),
        ]:
            with self.subTest(test_case=test_case):
                self.assertEqual(camel_to_snake(test_case), expected)

    def test_camel_to_snake_none_input(self):
        """Test camel_to_snake with None input."""
        self.assertEqual(camel_to_snake(None), "")

    def test_camel_to_snake_invalid_type(self):
        """Test camel_to_snake raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            camel_to_snake(123)
        with self.assertRaises(TypeError):
            camel_to_snake(['test'])
        with self.assertRaises(TypeError):
            camel_to_snake({'key': 'value'})


if __name__ == '__main__':
    unittest.main()
