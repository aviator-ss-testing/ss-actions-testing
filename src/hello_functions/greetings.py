def say_hello(name: str) -> str:
    """Return a hello greeting for the given name.

    Args:
        name: The name to greet

    Returns:
        A greeting string
    """
    return f"Hello, {name}!"


def say_goodbye(name: str) -> str:
    """Return a goodbye message for the given name.

    Args:
        name: The name to say goodbye to

    Returns:
        A goodbye string
    """
    return f"Goodbye, {name}!"


def greet_multiple(names: list[str]) -> list[str]:
    """Return hello greetings for multiple names.

    Args:
        names: A list of names to greet

    Returns:
        A list of greeting strings
    """
    return [say_hello(name) for name in names]
