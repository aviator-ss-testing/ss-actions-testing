"""Tests for the hello module."""
from hello import greet, farewell


def test_greet():
    """Test greeting function."""
    assert greet("World") == "Hello, World!"
    assert greet("Alice") == "Hello, Alice!"
    assert greet("") == "Hello, !"


def test_farewell():
    """Test farewell function."""
    assert farewell("World") == "Goodbye, World!"
    assert farewell("Bob") == "Goodbye, Bob!"
    assert farewell("") == "Goodbye, !"
