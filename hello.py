def greet() -> str:
    """
    Return a standard greeting message.

    Returns:
        str: The greeting message "Hello, Aviator!"
    """
    return "Hello, Aviator!"


def greet_user(name: str) -> str:
    """
    Return a personalized greeting message for a specific user.

    Args:
        name: The name of the user to greet

    Returns:
        str: A personalized greeting message in the format "Hello, {name}!"
    """
    return f"Hello, {name}!"
