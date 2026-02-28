"""Utility functions for safe file operations and path manipulation."""

import csv
import io
import re
from pathlib import Path, PurePosixPath
from typing import List, Optional, Union


def get_file_extension(path: Union[str, Path]) -> str:
    """Return the file extension (including the leading dot) from a path.

    Args:
        path: A file path as a string or Path object.

    Returns:
        The extension including the leading dot (e.g. ".txt"), or an empty
        string if the file has no extension.

    Raises:
        TypeError: If path is not a str or Path.
    """
    if not isinstance(path, (str, Path)):
        raise TypeError(f"Expected str or Path, got {type(path).__name__}")
    return Path(path).suffix


def sanitize_filename(name: str, replacement: str = "_") -> str:
    """Remove or replace characters that are unsafe in filenames.

    Unsafe characters include: ``/ \\ : * ? " < > |`` and control characters
    (ASCII 0–31).  Leading/trailing dots and spaces are also stripped.

    Args:
        name: The raw filename to sanitize.
        replacement: The character used to replace unsafe characters. Defaults
            to ``"_"``.

    Returns:
        A sanitized filename string.  Returns ``"_"`` if the result would
        otherwise be empty.

    Raises:
        TypeError: If name or replacement is not a str.
        ValueError: If replacement contains unsafe characters.
    """
    if not isinstance(name, str):
        raise TypeError(f"Expected str, got {type(name).__name__}")
    if not isinstance(replacement, str):
        raise TypeError(f"replacement must be a str, got {type(replacement).__name__}")

    unsafe_pattern = re.compile(r'[/\\:*?"<>|\x00-\x1f]')
    if unsafe_pattern.search(replacement):
        raise ValueError(f"replacement contains unsafe characters: {replacement!r}")

    sanitized = unsafe_pattern.sub(replacement, name)
    sanitized = sanitized.strip(". ")
    return sanitized if sanitized else "_"


def parse_csv_line(line: str, delimiter: str = ",", quotechar: str = '"') -> List[str]:
    """Parse a single CSV-formatted line into a list of fields.

    Handles quoted fields, escaped quotes, and custom delimiters.

    Args:
        line: A single CSV line (without a trailing newline).
        delimiter: The field delimiter. Defaults to ``","``
        quotechar: The character used to quote fields. Defaults to ``'"'``.

    Returns:
        A list of string fields.

    Raises:
        TypeError: If line, delimiter, or quotechar is not a str.
        ValueError: If delimiter or quotechar is not exactly one character.
    """
    if not isinstance(line, str):
        raise TypeError(f"Expected str, got {type(line).__name__}")
    if not isinstance(delimiter, str):
        raise TypeError(f"delimiter must be a str, got {type(delimiter).__name__}")
    if not isinstance(quotechar, str):
        raise TypeError(f"quotechar must be a str, got {type(quotechar).__name__}")
    if len(delimiter) != 1:
        raise ValueError("delimiter must be exactly one character")
    if len(quotechar) != 1:
        raise ValueError("quotechar must be exactly one character")

    reader = csv.reader(io.StringIO(line), delimiter=delimiter, quotechar=quotechar)
    return next(reader, [])


def format_file_size(size_bytes: int) -> str:
    """Format a byte count into a human-readable file-size string.

    Uses binary prefixes (KiB, MiB, GiB, TiB).  Values below 1 KiB are
    reported in bytes.

    Args:
        size_bytes: A non-negative integer number of bytes.

    Returns:
        A human-readable string such as ``"1.50 KiB"`` or ``"512 B"``.

    Raises:
        TypeError: If size_bytes is not an int.
        ValueError: If size_bytes is negative.
    """
    if not isinstance(size_bytes, int) or isinstance(size_bytes, bool):
        raise TypeError(f"size_bytes must be an int, got {type(size_bytes).__name__}")
    if size_bytes < 0:
        raise ValueError("size_bytes must be non-negative")

    units = ["B", "KiB", "MiB", "GiB", "TiB"]
    value = float(size_bytes)
    for unit in units[:-1]:
        if value < 1024.0:
            if unit == "B":
                return f"{int(value)} B"
            return f"{value:.2f} {unit}"
        value /= 1024.0
    return f"{value:.2f} {units[-1]}"


def validate_path_safe(path: Union[str, Path], base: Optional[Union[str, Path]] = None) -> bool:
    """Check whether a path is free of directory-traversal sequences.

    When *base* is provided, the resolved path must be located inside *base*.
    When *base* is omitted, the check only verifies that the path contains no
    ``..`` components.

    Args:
        path: The path to validate.
        base: Optional base directory. If given, the resolved *path* must be
            within (or equal to) the resolved *base*.

    Returns:
        ``True`` if the path is considered safe, ``False`` otherwise.

    Raises:
        TypeError: If path or base is not a str or Path.
    """
    if not isinstance(path, (str, Path)):
        raise TypeError(f"Expected str or Path for path, got {type(path).__name__}")
    if base is not None and not isinstance(base, (str, Path)):
        raise TypeError(f"Expected str or Path for base, got {type(base).__name__}")

    pure = PurePosixPath(Path(path).as_posix())
    if ".." in pure.parts:
        return False

    if base is None:
        return True

    try:
        resolved_path = Path(path).resolve()
        resolved_base = Path(base).resolve()
        resolved_path.relative_to(resolved_base)
        return True
    except ValueError:
        return False


def get_relative_path(path: Union[str, Path], base: Union[str, Path]) -> Path:
    """Compute the relative path from *base* to *path*.

    Args:
        path: The target path.
        base: The reference base directory.

    Returns:
        A :class:`pathlib.Path` representing the relative path from *base* to
        *path*.

    Raises:
        TypeError: If path or base is not a str or Path.
        ValueError: If *path* is not relative to *base* (they share no common
            ancestor on the same drive on Windows).
    """
    if not isinstance(path, (str, Path)):
        raise TypeError(f"Expected str or Path for path, got {type(path).__name__}")
    if not isinstance(base, (str, Path)):
        raise TypeError(f"Expected str or Path for base, got {type(base).__name__}")

    try:
        return Path(path).relative_to(Path(base))
    except ValueError:
        raise ValueError(
            f"{path!r} is not relative to {base!r}"
        )
