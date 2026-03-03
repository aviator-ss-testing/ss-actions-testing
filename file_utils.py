"""File and path utility functions for safe file operations."""

from typing import Optional, List, Tuple
from pathlib import Path
import re


def get_file_extension(filepath: Optional[str]) -> str:
    """
    Extract the file extension from a filepath.

    Returns the extension including the dot (e.g., '.txt', '.py').
    Returns empty string if no extension is present or for None input.
    For hidden files (starting with dot), returns the entire filename if no other extension.

    Args:
        filepath: The file path to extract extension from

    Returns:
        The file extension including the dot, or empty string

    Examples:
        >>> get_file_extension("document.txt")
        '.txt'
        >>> get_file_extension("/path/to/file.tar.gz")
        '.gz'
        >>> get_file_extension("no_extension")
        ''
        >>> get_file_extension(".gitignore")
        '.gitignore'
    """
    if filepath is None or filepath == "":
        return ""

    path = Path(filepath)
    name = path.name

    if name.startswith('.') and '.' not in name[1:]:
        return name

    return path.suffix


def sanitize_filename(filename: Optional[str], replacement: str = "_") -> str:
    """
    Sanitize a filename by removing or replacing unsafe characters.

    Removes or replaces characters that are problematic in filenames
    across different operating systems (Windows, Linux, macOS).
    Preserves file extensions.

    Args:
        filename: The filename to sanitize
        replacement: Character to use for replacing unsafe characters (default: "_")

    Returns:
        Sanitized filename safe for use across platforms, empty string for None input

    Examples:
        >>> sanitize_filename("my file.txt")
        'my_file.txt'
        >>> sanitize_filename("file/with\\bad:chars*.txt")
        'file_with_bad_chars_.txt'
        >>> sanitize_filename("normal_file.txt")
        'normal_file.txt'
    """
    if filename is None or filename == "":
        return ""

    unsafe_chars = r'[<>:"/\\|?*\x00-\x1f ]'
    sanitized = re.sub(unsafe_chars, replacement, filename)

    sanitized = sanitized.strip(f'. {replacement}')

    if not sanitized:
        return "unnamed"

    return sanitized


def parse_csv_line(line: Optional[str], delimiter: str = ",") -> List[str]:
    """
    Parse a CSV line into a list of fields.

    Handles quoted fields containing delimiters and preserves empty fields.
    This is a basic parser; for complex CSV needs, use the csv module.

    Args:
        line: The CSV line to parse
        delimiter: The field delimiter (default: ",")

    Returns:
        List of fields from the CSV line, empty list for None input

    Examples:
        >>> parse_csv_line("a,b,c")
        ['a', 'b', 'c']
        >>> parse_csv_line("name,age,city")
        ['name', 'age', 'city']
        >>> parse_csv_line("a,,c")
        ['a', '', 'c']
        >>> parse_csv_line('"quoted,field",normal,field')
        ['quoted,field', 'normal', 'field']
    """
    if line is None:
        return []

    if line == "":
        return [""]

    fields = []
    current_field = ""
    in_quotes = False

    i = 0
    while i < len(line):
        char = line[i]

        if char == '"':
            if in_quotes and i + 1 < len(line) and line[i + 1] == '"':
                current_field += '"'
                i += 1
            else:
                in_quotes = not in_quotes
        elif char == delimiter and not in_quotes:
            fields.append(current_field)
            current_field = ""
        else:
            current_field += char

        i += 1

    fields.append(current_field)

    return fields


def format_file_size(size_bytes: int, decimal_places: int = 2) -> str:
    """
    Format a file size in bytes to a human-readable string.

    Converts bytes to appropriate unit (B, KB, MB, GB, TB).

    Args:
        size_bytes: The size in bytes
        decimal_places: Number of decimal places to display (default: 2)

    Returns:
        Human-readable file size string

    Raises:
        ValueError: If size_bytes is negative or decimal_places is negative

    Examples:
        >>> format_file_size(1024)
        '1.00 KB'
        >>> format_file_size(1536)
        '1.50 KB'
        >>> format_file_size(1048576)
        '1.00 MB'
        >>> format_file_size(500)
        '500.00 B'
    """
    if size_bytes < 0:
        raise ValueError(f"size_bytes must be non-negative, got {size_bytes}")

    if decimal_places < 0:
        raise ValueError(f"decimal_places must be non-negative, got {decimal_places}")

    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    unit_index = 0
    size = float(size_bytes)

    while size >= 1024.0 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1

    return f"{size:.{decimal_places}f} {units[unit_index]}"


def validate_path_safe(path: Optional[str]) -> bool:
    """
    Validate that a path is safe to use (doesn't contain path traversal attempts).

    Checks for common path traversal patterns like '..', absolute paths,
    and other potentially dangerous constructs.

    Args:
        path: The path to validate

    Returns:
        True if the path appears safe, False otherwise or for None input

    Examples:
        >>> validate_path_safe("documents/file.txt")
        True
        >>> validate_path_safe("../etc/passwd")
        False
        >>> validate_path_safe("/absolute/path")
        False
        >>> validate_path_safe("normal/path/to/file.txt")
        True
    """
    if path is None or path == "":
        return False

    path_obj = Path(path)

    if path_obj.is_absolute():
        return False

    parts = path_obj.parts
    for part in parts:
        if part == '..':
            return False
        if part == '.':
            continue
        if part.startswith('~'):
            return False

    return True


def get_relative_path(from_path: Optional[str], to_path: Optional[str]) -> str:
    """
    Get the relative path from one path to another.

    Computes the relative path needed to go from from_path to to_path.

    Args:
        from_path: The starting path
        to_path: The destination path

    Returns:
        The relative path from from_path to to_path, empty string if either input is None

    Raises:
        ValueError: If paths cannot be made relative (e.g., on different drives on Windows)

    Examples:
        >>> get_relative_path("/home/user/docs", "/home/user/pictures")
        '../pictures'
        >>> get_relative_path("/a/b/c", "/a/b/c/d")
        'd'
        >>> get_relative_path("/a/b/c/d", "/a/b")
        '../..'
    """
    if from_path is None or to_path is None:
        return ""

    if from_path == "" or to_path == "":
        return ""

    try:
        from_path_obj = Path(from_path)
        to_path_obj = Path(to_path)

        relative = to_path_obj.relative_to(from_path_obj)
        return str(relative)
    except ValueError:
        try:
            from_path_obj = Path(from_path).resolve()
            to_path_obj = Path(to_path).resolve()

            relative = to_path_obj.relative_to(from_path_obj)
            return str(relative)
        except ValueError:
            common = Path(*[p for p in from_path_obj.parts
                          if p in to_path_obj.parts[:len(from_path_obj.parts)]])

            from_rel = from_path_obj.relative_to(common) if common.parts else from_path_obj
            to_rel = to_path_obj.relative_to(common) if common.parts else to_path_obj

            up_levels = len(from_rel.parts)
            up_path = Path(*(['..'] * up_levels))

            if up_levels > 0:
                result = up_path / to_rel
            else:
                result = to_rel

            return str(result)
