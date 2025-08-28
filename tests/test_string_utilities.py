"""
Comprehensive test suite for string utility functions.

Tests cover normal cases, edge cases, error conditions, Unicode handling,
and performance scenarios for all string manipulation functions.
"""

import unittest
import time
from utils.string_utilities import (
    reverse_string, is_palindrome, remove_duplicates, capitalize_words,
    count_vowels, count_consonants, extract_numbers, is_valid_email,
    is_valid_phone, count_word_frequency, longest_common_substring,
    sanitize_string
)


class TestStringUtilities(unittest.TestCase):
    """Test suite for string utility functions."""

    def test_reverse_string_normal_cases(self):
        """Test reverse_string with normal string inputs."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_reverse_string_edge_cases(self):
        """Test reverse_string with edge cases."""
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string(None), "")
        self.assertEqual(reverse_string(" "), " ")
        self.assertEqual(reverse_string("  "), "  ")

    def test_reverse_string_special_characters(self):
        """Test reverse_string with special characters."""
        self.assertEqual(reverse_string("!@#$%"), "%$#@!")
        self.assertEqual(reverse_string("hello world!"), "!dlrow olleh")
        self.assertEqual(reverse_string("a!b@c#"), "#c@b!a")

    def test_reverse_string_unicode(self):
        """Test reverse_string with Unicode characters."""
        self.assertEqual(reverse_string("café"), "éfac")
        self.assertEqual(reverse_string("🙂😊"), "😊🙂")
        self.assertEqual(reverse_string("Здравствуй"), "йувтсвардЗ")
        self.assertEqual(reverse_string("こんにちは"), "はちにんこ")

    def test_is_palindrome_normal_cases(self):
        """Test is_palindrome with normal palindromes."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("noon"))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_case_insensitive(self):
        """Test is_palindrome with mixed case."""
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("MadAm"))
        self.assertTrue(is_palindrome("A"))
        self.assertTrue(is_palindrome("AbA"))

    def test_is_palindrome_with_punctuation(self):
        """Test is_palindrome ignores punctuation and spaces."""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("race a car"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))

    def test_is_palindrome_non_palindromes(self):
        """Test is_palindrome with non-palindromes."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("test"))
        self.assertFalse(is_palindrome("abc"))

    def test_is_palindrome_edge_cases(self):
        """Test is_palindrome with edge cases."""
        self.assertFalse(is_palindrome(None))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome(" "))
        self.assertTrue(is_palindrome("!@#"))

    def test_is_palindrome_unicode(self):
        """Test is_palindrome with Unicode characters."""
        self.assertTrue(is_palindrome("아바"))
        self.assertTrue(is_palindrome("上中上"))
        self.assertFalse(is_palindrome("café"))

    def test_remove_duplicates_normal_cases(self):
        """Test remove_duplicates with normal strings."""
        self.assertEqual(remove_duplicates("hello"), "helo")
        self.assertEqual(remove_duplicates("aabbcc"), "abc")
        self.assertEqual(remove_duplicates("programming"), "progamin")
        self.assertEqual(remove_duplicates("abcdef"), "abcdef")

    def test_remove_duplicates_edge_cases(self):
        """Test remove_duplicates with edge cases."""
        self.assertEqual(remove_duplicates(""), "")
        self.assertEqual(remove_duplicates(None), "")
        self.assertEqual(remove_duplicates("a"), "a")
        self.assertEqual(remove_duplicates("aa"), "a")
        self.assertEqual(remove_duplicates("aaaa"), "a")

    def test_remove_duplicates_special_characters(self):
        """Test remove_duplicates with special characters."""
        self.assertEqual(remove_duplicates("!!@@##"), "!@#")
        self.assertEqual(remove_duplicates("hello world!!!"), "helo wrd!")
        self.assertEqual(remove_duplicates("   "), " ")

    def test_remove_duplicates_unicode(self):
        """Test remove_duplicates with Unicode characters."""
        self.assertEqual(remove_duplicates("ááéé"), "áé")
        self.assertEqual(remove_duplicates("🙂🙂😊😊"), "🙂😊")
        self.assertEqual(remove_duplicates("こんにちはは"), "こんにちは")

    def test_capitalize_words_normal_cases(self):
        """Test capitalize_words with normal strings."""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python programming"), "Python Programming")
        self.assertEqual(capitalize_words("the quick brown fox"), "The Quick Brown Fox")
        self.assertEqual(capitalize_words("hello"), "Hello")

    def test_capitalize_words_edge_cases(self):
        """Test capitalize_words with edge cases."""
        self.assertEqual(capitalize_words(""), "")
        self.assertEqual(capitalize_words(None), "")
        self.assertEqual(capitalize_words(" "), "")
        self.assertEqual(capitalize_words("   "), "")

    def test_capitalize_words_mixed_cases(self):
        """Test capitalize_words with mixed cases."""
        self.assertEqual(capitalize_words("hELLo WoRLd"), "Hello World")
        self.assertEqual(capitalize_words("PYTHON programming"), "Python Programming")
        self.assertEqual(capitalize_words("tHe QuIcK bRoWn FoX"), "The Quick Brown Fox")

    def test_capitalize_words_special_characters(self):
        """Test capitalize_words with special characters."""
        self.assertEqual(capitalize_words("hello-world"), "Hello-World")
        self.assertEqual(capitalize_words("test@example.com"), "Test@Example.Com")
        self.assertEqual(capitalize_words("multiple   spaces"), "Multiple Spaces")

    def test_capitalize_words_unicode(self):
        """Test capitalize_words with Unicode characters."""
        self.assertEqual(capitalize_words("café restaurant"), "Café Restaurant")
        self.assertEqual(capitalize_words("москва россия"), "Москва Россия")

    def test_count_vowels_normal_cases(self):
        """Test count_vowels with normal strings."""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("python"), 1)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("programming"), 3)

    def test_count_vowels_edge_cases(self):
        """Test count_vowels with edge cases."""
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels(None), 0)
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(count_vowels("AAAAAA"), 6)

    def test_count_vowels_special_characters(self):
        """Test count_vowels with special characters."""
        self.assertEqual(count_vowels("hello world!"), 3)
        self.assertEqual(count_vowels("123456789"), 0)
        self.assertEqual(count_vowels("!@#$%^&*()"), 0)
        self.assertEqual(count_vowels("a1e2i3o4u5"), 5)

    def test_count_vowels_unicode(self):
        """Test count_vowels with Unicode characters."""
        self.assertEqual(count_vowels("café"), 2)
        self.assertEqual(count_vowels("naïve"), 3)
        self.assertEqual(count_vowels("résumé"), 4)

    def test_count_consonants_normal_cases(self):
        """Test count_consonants with normal strings."""
        self.assertEqual(count_consonants("hello"), 3)
        self.assertEqual(count_consonants("python"), 4)
        self.assertEqual(count_consonants("bcdfg"), 5)
        self.assertEqual(count_consonants("Programming"), 8)

    def test_count_consonants_edge_cases(self):
        """Test count_consonants with edge cases."""
        self.assertEqual(count_consonants(""), 0)
        self.assertEqual(count_consonants(None), 0)
        self.assertEqual(count_consonants("aeiou"), 0)
        self.assertEqual(count_consonants("AEIOU"), 0)
        self.assertEqual(count_consonants("b"), 1)

    def test_count_consonants_special_characters(self):
        """Test count_consonants with special characters."""
        self.assertEqual(count_consonants("hello world!"), 7)
        self.assertEqual(count_consonants("123456789"), 0)
        self.assertEqual(count_consonants("!@#$%^&*()"), 0)
        self.assertEqual(count_consonants("b1c2d3f4g5"), 5)

    def test_count_consonants_unicode(self):
        """Test count_consonants with Unicode characters."""
        self.assertEqual(count_consonants("café"), 2)
        self.assertEqual(count_consonants("москва"), 4)

    def test_extract_numbers_normal_cases(self):
        """Test extract_numbers with normal strings."""
        self.assertEqual(extract_numbers("hello123world"), [123.0])
        self.assertEqual(extract_numbers("price is $19.99"), [19.99])
        self.assertEqual(extract_numbers("numbers: 1, 2, 3.5, -4"), [1.0, 2.0, 3.5, -4.0])
        self.assertEqual(extract_numbers("test 42 and 3.14159"), [42.0, 3.14159])

    def test_extract_numbers_edge_cases(self):
        """Test extract_numbers with edge cases."""
        self.assertEqual(extract_numbers(""), [])
        self.assertEqual(extract_numbers(None), [])
        self.assertEqual(extract_numbers("no numbers here"), [])
        self.assertEqual(extract_numbers("just letters abc"), [])

    def test_extract_numbers_special_cases(self):
        """Test extract_numbers with special number formats."""
        self.assertEqual(extract_numbers("0.5"), [0.5])
        self.assertEqual(extract_numbers("-123.456"), [-123.456])
        self.assertEqual(extract_numbers("100."), [100.0])
        self.assertEqual(extract_numbers(".5"), [0.5])
        self.assertEqual(extract_numbers("1000000"), [1000000.0])

    def test_extract_numbers_mixed_content(self):
        """Test extract_numbers with mixed content."""
        self.assertEqual(extract_numbers("Temperature: -15.5°C"), [-15.5])
        self.assertEqual(extract_numbers("Call 555-123-4567 now!"), [555.0, 123.0, 4567.0])
        self.assertEqual(extract_numbers("Version 3.14.159"), [3.0, 14.0, 159.0])

    def test_is_valid_email_valid_emails(self):
        """Test is_valid_email with valid email addresses."""
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertTrue(is_valid_email("user.name@domain.org"))
        self.assertTrue(is_valid_email("user+tag@example.co.uk"))
        self.assertTrue(is_valid_email("simple@test.io"))
        self.assertTrue(is_valid_email("user123@domain123.com"))

    def test_is_valid_email_invalid_emails(self):
        """Test is_valid_email with invalid email addresses."""
        self.assertFalse(is_valid_email("invalid"))
        self.assertFalse(is_valid_email("@example.com"))
        self.assertFalse(is_valid_email("user@"))
        self.assertFalse(is_valid_email("user@.com"))
        self.assertFalse(is_valid_email("user..name@example.com"))
        self.assertFalse(is_valid_email("user@example"))

    def test_is_valid_email_edge_cases(self):
        """Test is_valid_email with edge cases."""
        self.assertFalse(is_valid_email(""))
        self.assertFalse(is_valid_email(None))
        self.assertFalse(is_valid_email(" "))
        self.assertFalse(is_valid_email(123))

    def test_is_valid_email_whitespace(self):
        """Test is_valid_email handles whitespace properly."""
        self.assertTrue(is_valid_email("  test@example.com  "))
        self.assertFalse(is_valid_email("test @example.com"))
        self.assertFalse(is_valid_email("test@ example.com"))

    def test_is_valid_phone_valid_phones(self):
        """Test is_valid_phone with valid phone numbers."""
        self.assertTrue(is_valid_phone("(123) 456-7890"))
        self.assertTrue(is_valid_phone("123-456-7890"))
        self.assertTrue(is_valid_phone("1234567890"))
        self.assertTrue(is_valid_phone("+1-123-456-7890"))
        self.assertTrue(is_valid_phone("123.456.7890"))
        self.assertTrue(is_valid_phone("123 456 7890"))

    def test_is_valid_phone_invalid_phones(self):
        """Test is_valid_phone with invalid phone numbers."""
        self.assertFalse(is_valid_phone("123"))
        self.assertFalse(is_valid_phone("12345"))
        self.assertFalse(is_valid_phone("123456789012"))
        self.assertFalse(is_valid_phone("abc-def-ghij"))
        self.assertFalse(is_valid_phone("(123 456-7890"))
        self.assertFalse(is_valid_phone("123) 456-7890"))

    def test_is_valid_phone_edge_cases(self):
        """Test is_valid_phone with edge cases."""
        self.assertFalse(is_valid_phone(""))
        self.assertFalse(is_valid_phone(None))
        self.assertFalse(is_valid_phone(" "))
        self.assertFalse(is_valid_phone(1234567890))

    def test_is_valid_phone_whitespace(self):
        """Test is_valid_phone handles whitespace properly."""
        self.assertTrue(is_valid_phone("  (123) 456-7890  "))
        self.assertTrue(is_valid_phone("  123-456-7890  "))

    def test_count_word_frequency_normal_cases(self):
        """Test count_word_frequency with normal text."""
        result = count_word_frequency("hello world hello")
        expected = {"hello": 2, "world": 1}
        self.assertEqual(result, expected)

        result = count_word_frequency("the quick brown fox jumps over the lazy dog")
        expected = {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1,
                   "over": 1, "lazy": 1, "dog": 1}
        self.assertEqual(result, expected)

    def test_count_word_frequency_edge_cases(self):
        """Test count_word_frequency with edge cases."""
        self.assertEqual(count_word_frequency(""), {})
        self.assertEqual(count_word_frequency(None), {})
        self.assertEqual(count_word_frequency(" "), {})
        self.assertEqual(count_word_frequency("   "), {})

    def test_count_word_frequency_case_insensitive(self):
        """Test count_word_frequency is case insensitive."""
        result = count_word_frequency("Hello HELLO hello")
        expected = {"hello": 3}
        self.assertEqual(result, expected)

    def test_count_word_frequency_punctuation(self):
        """Test count_word_frequency ignores punctuation."""
        result = count_word_frequency("Hello, world! Hello world.")
        expected = {"hello": 2, "world": 2}
        self.assertEqual(result, expected)

        result = count_word_frequency("It's a test. Test's over!")
        expected = {"it": 1, "s": 2, "a": 1, "test": 2, "over": 1}
        self.assertEqual(result, expected)

    def test_count_word_frequency_numbers_symbols(self):
        """Test count_word_frequency with numbers and symbols."""
        result = count_word_frequency("test123 @#$% test")
        expected = {"test": 1}
        self.assertEqual(result, expected)

    def test_longest_common_substring_normal_cases(self):
        """Test longest_common_substring with normal strings."""
        self.assertEqual(longest_common_substring("hello", "world"), "l")
        self.assertEqual(longest_common_substring("python", "typhoon"), "thon")
        self.assertEqual(longest_common_substring("programming", "program"), "program")
        self.assertEqual(longest_common_substring("abcdef", "cdefgh"), "cdef")

    def test_longest_common_substring_edge_cases(self):
        """Test longest_common_substring with edge cases."""
        self.assertEqual(longest_common_substring("", ""), "")
        self.assertEqual(longest_common_substring("", "hello"), "")
        self.assertEqual(longest_common_substring("hello", ""), "")
        self.assertEqual(longest_common_substring(None, "hello"), "")
        self.assertEqual(longest_common_substring("hello", None), "")
        self.assertEqual(longest_common_substring(None, None), "")

    def test_longest_common_substring_no_common(self):
        """Test longest_common_substring with no common substrings."""
        self.assertEqual(longest_common_substring("abc", "def"), "")
        self.assertEqual(longest_common_substring("xyz", "123"), "")

    def test_longest_common_substring_identical(self):
        """Test longest_common_substring with identical strings."""
        self.assertEqual(longest_common_substring("hello", "hello"), "hello")
        self.assertEqual(longest_common_substring("test", "test"), "test")

    def test_longest_common_substring_case_sensitive(self):
        """Test longest_common_substring is case sensitive."""
        self.assertEqual(longest_common_substring("Hello", "hello"), "ello")
        self.assertEqual(longest_common_substring("ABC", "abc"), "")

    def test_longest_common_substring_unicode(self):
        """Test longest_common_substring with Unicode characters."""
        self.assertEqual(longest_common_substring("café", "cafeteria"), "café")
        self.assertEqual(longest_common_substring("🙂😊", "😊🙂"), "😊")

    def test_sanitize_string_normal_cases(self):
        """Test sanitize_string with normal strings."""
        self.assertEqual(sanitize_string("  hello world  "), "hello world")
        self.assertEqual(sanitize_string("multiple   spaces"), "multiple spaces")
        self.assertEqual(sanitize_string("test\n\nstring"), "test string")
        self.assertEqual(sanitize_string("hello\tworld"), "hello world")

    def test_sanitize_string_edge_cases(self):
        """Test sanitize_string with edge cases."""
        self.assertEqual(sanitize_string(""), "")
        self.assertEqual(sanitize_string(None), "")
        self.assertEqual(sanitize_string("   "), "")
        self.assertEqual(sanitize_string("\n\t"), "")

    def test_sanitize_string_non_printable(self):
        """Test sanitize_string removes non-printable characters."""
        # Test with control characters
        test_string = "hello\x00\x01\x02world"
        self.assertEqual(sanitize_string(test_string), "helloworld")
        
        # Test preserving newlines and tabs
        test_string = "hello\nworld\ttab"
        self.assertEqual(sanitize_string(test_string), "hello world tab")

    def test_sanitize_string_non_string_input(self):
        """Test sanitize_string with non-string input."""
        self.assertEqual(sanitize_string(123), "123")
        self.assertEqual(sanitize_string([1, 2, 3]), "[1, 2, 3]")
        self.assertEqual(sanitize_string({"key": "value"}), "{'key': 'value'}")

    def test_sanitize_string_unicode(self):
        """Test sanitize_string with Unicode characters."""
        self.assertEqual(sanitize_string("  café  "), "café")
        self.assertEqual(sanitize_string("🙂  😊"), "🙂 😊")

    def test_performance_large_strings(self):
        """Test functions with large strings for performance."""
        large_string = "a" * 10000
        large_palindrome = "a" * 5000 + "b" + "a" * 5000
        
        # Test reverse_string performance
        start_time = time.time()
        result = reverse_string(large_string)
        duration = time.time() - start_time
        self.assertLess(duration, 1.0)  # Should complete within 1 second
        self.assertEqual(len(result), 10000)
        
        # Test is_palindrome performance
        start_time = time.time()
        is_palindrome(large_palindrome)
        duration = time.time() - start_time
        self.assertLess(duration, 1.0)  # Should complete within 1 second
        
        # Test remove_duplicates performance
        large_string_with_dups = ("abc" * 3000) + ("def" * 3000)
        start_time = time.time()
        result = remove_duplicates(large_string_with_dups)
        duration = time.time() - start_time
        self.assertLess(duration, 1.0)  # Should complete within 1 second
        self.assertEqual(result, "abcdef")

    def test_performance_longest_common_substring(self):
        """Test longest_common_substring performance with large strings."""
        # Create large strings with common substring
        str1 = "x" * 1000 + "common" + "y" * 1000
        str2 = "z" * 1000 + "common" + "w" * 1000
        
        start_time = time.time()
        result = longest_common_substring(str1, str2)
        duration = time.time() - start_time
        
        self.assertLess(duration, 2.0)  # Should complete within 2 seconds
        self.assertEqual(result, "common")

    def test_performance_word_frequency_large_text(self):
        """Test count_word_frequency performance with large text."""
        # Create large text with repeated words
        words = ["hello", "world", "python", "test", "performance"]
        large_text = " ".join(words * 2000)
        
        start_time = time.time()
        result = count_word_frequency(large_text)
        duration = time.time() - start_time
        
        self.assertLess(duration, 1.0)  # Should complete within 1 second
        self.assertEqual(len(result), 5)
        for word in words:
            self.assertEqual(result[word], 2000)

    def test_unicode_edge_cases_comprehensive(self):
        """Comprehensive Unicode edge case testing."""
        # Test with various Unicode categories
        unicode_strings = [
            "café résumé naïve",  # Latin with diacritics
            "Москва Россия",      # Cyrillic
            "こんにちは世界",        # Japanese
            "你好世界",             # Chinese
            "مرحبا بالعالم",        # Arabic
            "🙂😊🎉🚀",           # Emojis
            "½¼¾⅓⅔",            # Fractions
            "αβγδε",             # Greek
        ]
        
        for unicode_str in unicode_strings:
            # Test basic string operations don't crash with Unicode
            self.assertIsInstance(reverse_string(unicode_str), str)
            self.assertIsInstance(remove_duplicates(unicode_str), str)
            self.assertIsInstance(capitalize_words(unicode_str), str)
            self.assertIsInstance(count_vowels(unicode_str), int)
            self.assertIsInstance(count_consonants(unicode_str), int)
            self.assertIsInstance(sanitize_string(unicode_str), str)
            
            # Test palindrome detection
            self.assertIsInstance(is_palindrome(unicode_str), bool)
            
            # Test word frequency
            self.assertIsInstance(count_word_frequency(unicode_str), dict)


if __name__ == '__main__':
    unittest.main()