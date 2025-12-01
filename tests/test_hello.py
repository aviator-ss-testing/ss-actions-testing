import pytest
from hello import greet, greet_multiple, format_greeting, is_valid_name


class TestGreet:
    def test_greet_default(self):
        result = greet()
        assert result == "Hello, World!"

    def test_greet_with_name(self):
        result = greet("Aviator")
        assert result == "Hello, Aviator!"

    def test_greet_empty_string(self):
        result = greet("")
        assert result == "Hello, !"


class TestGreetMultiple:
    def test_greet_multiple_names(self):
        names = ["Alice", "Bob", "Charlie"]
        result = greet_multiple(names)
        assert result == ["Hello, Alice!", "Hello, Bob!", "Hello, Charlie!"]

    def test_greet_empty_list(self):
        result = greet_multiple([])
        assert result == []

    def test_greet_single_name(self):
        result = greet_multiple(["Dave"])
        assert result == ["Hello, Dave!"]


class TestFormatGreeting:
    def test_format_hello(self):
        result = format_greeting("Aviator", "hello")
        assert result == "Hello, Aviator!"

    def test_format_hi(self):
        result = format_greeting("Aviator", "hi")
        assert result == "Hi, Aviator!"

    def test_format_goodbye(self):
        result = format_greeting("Aviator", "goodbye")
        assert result == "Goodbye, Aviator!"

    def test_format_invalid_type(self):
        result = format_greeting("Aviator", "invalid")
        assert result == "Hello, Aviator!"

    def test_format_case_insensitive(self):
        result = format_greeting("Aviator", "HeLLo")
        assert result == "Hello, Aviator!"

    def test_format_default_type(self):
        result = format_greeting("Aviator")
        assert result == "Hello, Aviator!"


class TestIsValidName:
    def test_valid_names(self):
        valid_names = ["Alice", "Bob Smith", "O'Connor", "José", "Anne-Marie"]
        for name in valid_names:
            assert is_valid_name(name) is True

    def test_invalid_names(self):
        assert is_valid_name("") is False
        assert is_valid_name(None) is False

    def test_empty_string(self):
        assert is_valid_name("") is False

    def test_very_long_name(self):
        long_name = "A" * 150
        assert is_valid_name(long_name) is False

    def test_whitespace_only(self):
        assert is_valid_name("   ") is False
        assert is_valid_name("\t\n") is False

    def test_valid_length_boundary(self):
        exactly_100 = "A" * 100
        assert is_valid_name(exactly_100) is True

        one_over_100 = "A" * 101
        assert is_valid_name(one_over_100) is False

    def test_name_with_whitespace_around(self):
        assert is_valid_name("  Valid Name  ") is True
