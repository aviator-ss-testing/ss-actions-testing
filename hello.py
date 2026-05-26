def greet(name: str = "World") -> str:
    """Return a personalized greeting string.

    Args:
        name: The name to greet (defaults to "World")

    Returns:
        A greeting string in the format "Hello, {name}!"
    """
    return f"Hello, {name}!"


def greet_multiple(names: list[str]) -> list[str]:
    """Return greetings for multiple names.

    Args:
        names: A list of names to greet

    Returns:
        A list of greeting strings, one for each name
    """
    return [greet(name) for name in names]


def format_greeting(name: str, greeting_type: str = "hello") -> str:
    """Format a greeting with different greeting types.

    Args:
        name: The name to greet
        greeting_type: Type of greeting ("hello", "hi", "hey", "goodbye")

    Returns:
        A formatted greeting string
    """
    greeting_map = {
        "hello": "Hello",
        "hi": "Hi",
        "hey": "Hey",
        "goodbye": "Goodbye"
    }

    greeting_word = greeting_map.get(greeting_type.lower(), "Hello")
    return f"{greeting_word}, {name}!"


def is_valid_name(name: str) -> bool:
    """Validate that a name is suitable for greeting.

    Args:
        name: The name to validate

    Returns:
        True if the name is valid (non-empty and reasonable length), False otherwise
    """
    if not name or not isinstance(name, str):
        return False

    stripped_name = name.strip()
    if len(stripped_name) == 0:
        return False

    if len(stripped_name) > 100:
        return False

    return True


def main() -> None:
    """Demonstrate usage of the greeting functions."""
    print(greet())
    print(greet("Aviator"))
    print()

    names = ["Alice", "Bob", "Charlie"]
    print("Multiple greetings:")
    for greeting in greet_multiple(names):
        print(f"  {greeting}")
    print()

    print("Different greeting types:")
    print(f"  {format_greeting('Aviator', 'hi')}")
    print(f"  {format_greeting('Aviator', 'hey')}")
    print(f"  {format_greeting('Aviator', 'goodbye')}")
    print()

    print("Name validation:")
    test_names = ["Valid Name", "", "   ", "A" * 150]
    for test_name in test_names:
        result = is_valid_name(test_name)
        display = test_name if len(test_name) <= 20 else test_name[:20] + "..."
        print(f"  '{display}' is valid: {result}")


if __name__ == "__main__":
    main()
