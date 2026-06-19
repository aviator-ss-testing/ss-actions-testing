"""File and path manipulation utilities for I/O operations."""

import os


def read_lines(filepath: str) -> list[str]:
    """Read file lines into a list.

    Args:
        filepath: Path to the file to read

    Returns:
        A list of strings, one for each line in the file (including newline chars)
    """
    with open(filepath, 'r') as f:
        return f.readlines()


def write_lines(filepath: str, lines: list[str]) -> None:
    """Write lines to a file.

    Args:
        filepath: Path to the file to write
        lines: List of strings to write to the file
    """
    with open(filepath, 'w') as f:
        f.writelines(lines)


def get_file_extension(filepath: str) -> str:
    """Extract the file extension from a filepath.

    Args:
        filepath: Path to extract extension from

    Returns:
        The file extension including the dot (e.g., '.txt'), or empty string if no extension
    """
    return os.path.splitext(filepath)[1]


def is_valid_path(filepath: str) -> bool:
    """Check if a path format is valid.

    Args:
        filepath: Path string to validate

    Returns:
        True if the path format is valid, False otherwise
    """
    if not filepath or not isinstance(filepath, str):
        return False

    invalid_chars = '<>"|?*'
    if any(char in filepath for char in invalid_chars):
        return False

    if filepath.strip() != filepath:
        return False

    if '..' in filepath.replace('...', ''):
        parts = filepath.split(os.sep)
        if '..' in parts:
            return False

    return True


def count_file_lines(filepath: str) -> int:
    """Count the number of lines in a file.

    Args:
        filepath: Path to the file to count lines in

    Returns:
        The number of lines in the file
    """
    with open(filepath, 'r') as f:
        return sum(1 for _ in f)
