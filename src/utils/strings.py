def greet(name: str) -> str:
    """Return a personalized greeting for the given name."""
    return f"Hello, {name}!"


def reverse_string(text: str) -> str:
    """Reverse the input string."""
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Check if the input string is a palindrome (case-sensitive)."""
    return text == text[::-1]
