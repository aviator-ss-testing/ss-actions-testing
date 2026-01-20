"""Comprehensive test suite for string_utils module with normal, edge, Unicode, and error cases."""
import unittest
from string_utils import reverse_words, is_palindrome, count_vowels, title_case, snake_to_camel, camel_to_snake

class TestStringUtils(unittest.TestCase):
    """Test cases for string processing and manipulation utility functions."""

    def test_reverse_words_normal_cases(self):
        """Test reverse_words with typical strings."""
        self.assertEqual(reverse_words("hello world"), "world hello")
        self.assertEqual(reverse_words("one two three"), "three two one")
        self.assertEqual(reverse_words("Python is awesome"), "awesome is Python")
        self.assertEqual(reverse_words("single"), "single")

    def test_reverse_words_edge_cases(self):
        """Test reverse_words with boundary conditions."""
        self.assertEqual(reverse_words(""), "")
        self.assertEqual(reverse_words("   "), "")
        self.assertEqual(reverse_words("word"), "word")
        self.assertEqual(reverse_words("  multiple   spaces  between  "), "between spaces multiple")

    def test_reverse_words_special_characters(self):
        """Test reverse_words with punctuation and special characters."""
        self.assertEqual(reverse_words("hello, world!"), "world! hello,")
        self.assertEqual(reverse_words("one-two three"), "three one-two")
        self.assertEqual(reverse_words("test@example.com foo"), "foo test@example.com")

    def test_reverse_words_none_input(self):
        """Test reverse_words returns empty string for None."""
        self.assertEqual(reverse_words(None), "")

    def test_reverse_words_type_error(self):
        """Test reverse_words raises TypeError for non-string inputs."""
        with self.assertRaises(TypeError):
            reverse_words(123)
        with self.assertRaises(TypeError):
            reverse_words(['hello', 'world'])

    def test_is_palindrome_normal_cases(self):
        """Test is_palindrome with typical palindromes and non-palindromes."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

    def test_is_palindrome_edge_cases(self):
        """Test is_palindrome with boundary conditions."""
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("  "))
        self.assertTrue(is_palindrome(None))

    def test_is_palindrome_special_characters(self):
        """Test is_palindrome ignores punctuation and spaces."""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("race-car"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))

    def test_is_palindrome_numbers(self):
        """Test is_palindrome with numeric characters."""
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("1a2b2a1"))
        self.assertFalse(is_palindrome("12345"))

    def test_is_palindrome_type_error(self):
        """Test is_palindrome raises TypeError for non-string inputs."""
        with self.assertRaises(TypeError):
            is_palindrome(12321)
        with self.assertRaises(TypeError):
            is_palindrome(['a', 'b', 'a'])

    def test_count_vowels_normal_cases(self):
        """Test count_vowels with typical strings."""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("world"), 1)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_count_vowels_edge_cases(self):
        """Test count_vowels with boundary conditions."""
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(count_vowels(None), 0)

    def test_count_vowels_mixed_case(self):
        """Test count_vowels is case-insensitive."""
        self.assertEqual(count_vowels("AaEeIiOoUu"), 10)
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("UPPERCASE"), 4)

    def test_count_vowels_special_characters(self):
        """Test count_vowels with numbers and punctuation."""
        self.assertEqual(count_vowels("hello123"), 2)
        self.assertEqual(count_vowels("test@example.com"), 5)
        self.assertEqual(count_vowels("one, two, three!"), 5)

    def test_count_vowels_unicode(self):
        """Test count_vowels with Unicode characters (ASCII vowels only)."""
        self.assertEqual(count_vowels("café"), 1)
        self.assertEqual(count_vowels("naïve"), 2)
        self.assertEqual(count_vowels("Zürich"), 1)

    def test_count_vowels_type_error(self):
        """Test count_vowels raises TypeError for non-string inputs."""
        with self.assertRaises(TypeError):
            count_vowels(123)
        with self.assertRaises(TypeError):
            count_vowels(['a', 'e', 'i'])

    def test_title_case_normal_cases(self):
        """Test title_case with typical strings."""
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("python programming"), "Python Programming")
        self.assertEqual(title_case("the quick brown fox"), "The Quick Brown Fox")

    def test_title_case_edge_cases(self):
        """Test title_case with boundary conditions."""
        self.assertEqual(title_case(""), "")
        self.assertEqual(title_case("a"), "A")
        self.assertEqual(title_case("ALREADY UPPERCASE"), "Already Uppercase")
        self.assertEqual(title_case(None), "")

    def test_title_case_special_characters(self):
        """Test title_case with punctuation and numbers."""
        self.assertEqual(title_case("hello-world"), "Hello-World")
        self.assertEqual(title_case("test123case"), "Test123Case")
        self.assertEqual(title_case("one's book"), "One'S Book")

    def test_title_case_type_error(self):
        """Test title_case raises TypeError for non-string inputs."""
        with self.assertRaises(TypeError):
            title_case(123)
        with self.assertRaises(TypeError):
            title_case(['hello', 'world'])

    def test_snake_to_camel_normal_cases(self):
        """Test snake_to_camel with typical snake_case strings."""
        self.assertEqual(snake_to_camel("hello_world"), "helloWorld")
        self.assertEqual(snake_to_camel("user_name"), "userName")
        self.assertEqual(snake_to_camel("get_user_by_id"), "getUserById")
        self.assertEqual(snake_to_camel("single"), "single")

    def test_snake_to_camel_edge_cases(self):
        """Test snake_to_camel with boundary conditions."""
        self.assertEqual(snake_to_camel(""), "")
        self.assertEqual(snake_to_camel("a"), "a")
        self.assertEqual(snake_to_camel("_leading_underscore"), "LeadingUnderscore")
        self.assertEqual(snake_to_camel("trailing_underscore_"), "trailingUnderscore")
        self.assertEqual(snake_to_camel(None), "")

    def test_snake_to_camel_multiple_underscores(self):
        """Test snake_to_camel with consecutive underscores."""
        test_cases = [
            ("double__underscore", "doubleUnderscore"),
            ("triple___underscore", "tripleUnderscore"),
            ("_multiple___gaps_", "MultipleGaps"),
        ]
        for input_str, expected in test_cases:
            with self.subTest(input=input_str):
                self.assertEqual(snake_to_camel(input_str), expected)

    def test_snake_to_camel_type_error(self):
        """Test snake_to_camel raises TypeError for non-string inputs."""
        with self.assertRaises(TypeError):
            snake_to_camel(123)
        with self.assertRaises(TypeError):
            snake_to_camel(['hello', 'world'])

    def test_camel_to_snake_normal_cases(self):
        """Test camel_to_snake with typical camelCase strings."""
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")
        self.assertEqual(camel_to_snake("userName"), "user_name")
        self.assertEqual(camel_to_snake("getUserById"), "get_user_by_id")
        self.assertEqual(camel_to_snake("single"), "single")

    def test_camel_to_snake_pascal_case(self):
        """Test camel_to_snake with PascalCase strings."""
        self.assertEqual(camel_to_snake("HelloWorld"), "hello_world")
        self.assertEqual(camel_to_snake("UserName"), "user_name")
        self.assertEqual(camel_to_snake("MyClassName"), "my_class_name")

    def test_camel_to_snake_edge_cases(self):
        """Test camel_to_snake with boundary conditions."""
        self.assertEqual(camel_to_snake(""), "")
        self.assertEqual(camel_to_snake("a"), "a")
        self.assertEqual(camel_to_snake("A"), "a")
        self.assertEqual(camel_to_snake(None), "")

    def test_camel_to_snake_consecutive_capitals(self):
        """Test camel_to_snake with consecutive capital letters."""
        test_cases = [
            ("HTTPResponse", "http_response"),
            ("XMLParser", "xml_parser"),
            ("URLPath", "url_path"),
            ("IOError", "io_error"),
        ]
        for input_str, expected in test_cases:
            with self.subTest(input=input_str):
                self.assertEqual(camel_to_snake(input_str), expected)

    def test_camel_to_snake_numbers(self):
        """Test camel_to_snake with numbers in the string."""
        self.assertEqual(camel_to_snake("test123Value"), "test123_value")
        self.assertEqual(camel_to_snake("value2Name"), "value2_name")
        self.assertEqual(camel_to_snake("get2Users"), "get2_users")

    def test_camel_to_snake_type_error(self):
        """Test camel_to_snake raises TypeError for non-string inputs."""
        with self.assertRaises(TypeError):
            camel_to_snake(123)
        with self.assertRaises(TypeError):
            camel_to_snake(['hello', 'world'])

if __name__ == '__main__':
    unittest.main()
