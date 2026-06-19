"""Tests for the file_utils module."""
import pytest
from file_utils import (
    read_lines,
    write_lines,
    get_file_extension,
    is_valid_path,
    count_file_lines
)


@pytest.fixture
def sample_file(tmp_path):
    """Create a temporary file with sample content.

    Args:
        tmp_path: pytest fixture providing a temporary directory

    Returns:
        Path to the temporary test file
    """
    file_path = tmp_path / "test_file.txt"
    content = ["Line 1\n", "Line 2\n", "Line 3\n"]
    file_path.write_text("".join(content))
    return str(file_path)


@pytest.fixture
def empty_file(tmp_path):
    """Create an empty temporary file.

    Args:
        tmp_path: pytest fixture providing a temporary directory

    Returns:
        Path to the empty temporary file
    """
    file_path = tmp_path / "empty_file.txt"
    file_path.write_text("")
    return str(file_path)


@pytest.fixture
def multiline_file(tmp_path):
    """Create a temporary file with multiple lines of varying content.

    Args:
        tmp_path: pytest fixture providing a temporary directory

    Returns:
        Path to the temporary test file
    """
    file_path = tmp_path / "multiline_file.txt"
    content = [
        "First line\n",
        "Second line with more text\n",
        "Third line\n",
        "Fourth line\n",
        "Fifth line\n",
        "Sixth line\n",
        "Seventh line\n",
        "Eighth line\n",
        "Ninth line\n",
        "Tenth line\n"
    ]
    file_path.write_text("".join(content))
    return str(file_path)


class TestReadLines:
    """Tests for read_lines function."""

    def test_read_lines_simple_file(self, sample_file):
        """Test reading lines from a simple file."""
        lines = read_lines(sample_file)
        assert len(lines) == 3
        assert lines[0] == "Line 1\n"
        assert lines[1] == "Line 2\n"
        assert lines[2] == "Line 3\n"

    def test_read_lines_empty_file(self, empty_file):
        """Test reading lines from an empty file."""
        lines = read_lines(empty_file)
        assert lines == []

    def test_read_lines_multiline_file(self, multiline_file):
        """Test reading lines from a file with multiple lines."""
        lines = read_lines(multiline_file)
        assert len(lines) == 10
        assert lines[0] == "First line\n"
        assert lines[9] == "Tenth line\n"

    def test_read_lines_preserves_newlines(self, tmp_path):
        """Test that read_lines preserves newline characters."""
        file_path = tmp_path / "newlines.txt"
        content = "Line 1\nLine 2\nLine 3"
        file_path.write_text(content)

        lines = read_lines(str(file_path))
        assert lines[0] == "Line 1\n"
        assert lines[1] == "Line 2\n"
        assert lines[2] == "Line 3"

    def test_read_lines_with_special_characters(self, tmp_path):
        """Test reading lines with special characters."""
        file_path = tmp_path / "special.txt"
        content = ["Hello! @#$%\n", "Special chars: éàü\n", "Symbols: •™®\n"]
        file_path.write_text("".join(content))

        lines = read_lines(str(file_path))
        assert len(lines) == 3
        assert lines[0] == "Hello! @#$%\n"
        assert lines[1] == "Special chars: éàü\n"
        assert lines[2] == "Symbols: •™®\n"


class TestWriteLines:
    """Tests for write_lines function."""

    def test_write_lines_simple(self, tmp_path):
        """Test writing simple lines to a file."""
        file_path = tmp_path / "output.txt"
        lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

        write_lines(str(file_path), lines)

        content = file_path.read_text()
        assert content == "Line 1\nLine 2\nLine 3\n"

    def test_write_lines_empty_list(self, tmp_path):
        """Test writing an empty list to a file."""
        file_path = tmp_path / "empty_output.txt"

        write_lines(str(file_path), [])

        content = file_path.read_text()
        assert content == ""

    def test_write_lines_without_newlines(self, tmp_path):
        """Test writing lines without explicit newline characters."""
        file_path = tmp_path / "no_newlines.txt"
        lines = ["Line 1", "Line 2", "Line 3"]

        write_lines(str(file_path), lines)

        content = file_path.read_text()
        assert content == "Line 1Line 2Line 3"

    def test_write_lines_overwrites_existing(self, sample_file, tmp_path):
        """Test that write_lines overwrites existing file content."""
        new_lines = ["New Line 1\n", "New Line 2\n"]

        write_lines(sample_file, new_lines)

        content = read_lines(sample_file)
        assert len(content) == 2
        assert content[0] == "New Line 1\n"
        assert content[1] == "New Line 2\n"

    def test_write_lines_with_special_characters(self, tmp_path):
        """Test writing lines with special characters."""
        file_path = tmp_path / "special_output.txt"
        lines = ["Hello! @#$%\n", "Special: éàü\n", "Symbols: •™®\n"]

        write_lines(str(file_path), lines)

        content = file_path.read_text()
        assert content == "Hello! @#$%\nSpecial: éàü\nSymbols: •™®\n"

    def test_write_then_read_roundtrip(self, tmp_path):
        """Test writing lines and reading them back."""
        file_path = tmp_path / "roundtrip.txt"
        original_lines = ["First\n", "Second\n", "Third\n"]

        write_lines(str(file_path), original_lines)
        read_back = read_lines(str(file_path))

        assert read_back == original_lines


class TestGetFileExtension:
    """Tests for get_file_extension function."""

    def test_get_extension_simple(self):
        """Test extracting simple file extensions."""
        assert get_file_extension("file.txt") == ".txt"
        assert get_file_extension("document.pdf") == ".pdf"
        assert get_file_extension("image.jpg") == ".jpg"

    def test_get_extension_with_path(self):
        """Test extracting extensions from full paths."""
        assert get_file_extension("/home/user/file.txt") == ".txt"
        assert get_file_extension("C:\\Users\\user\\document.pdf") == ".pdf"
        assert get_file_extension("../relative/path/file.py") == ".py"

    def test_get_extension_multiple_dots(self):
        """Test extracting extensions from files with multiple dots."""
        assert get_file_extension("file.tar.gz") == ".gz"
        assert get_file_extension("backup.2024.01.01.zip") == ".zip"
        assert get_file_extension("test.config.json") == ".json"

    def test_get_extension_no_extension(self):
        """Test files without extensions."""
        assert get_file_extension("filename") == ""
        assert get_file_extension("/path/to/file") == ""
        assert get_file_extension("README") == ""

    def test_get_extension_hidden_files(self):
        """Test extracting extensions from hidden files."""
        assert get_file_extension(".gitignore") == ".gitignore"
        assert get_file_extension(".hidden.txt") == ".txt"
        assert get_file_extension("/path/.config") == ".config"

    def test_get_extension_uppercase(self):
        """Test extracting uppercase extensions."""
        assert get_file_extension("FILE.TXT") == ".TXT"
        assert get_file_extension("IMAGE.JPG") == ".JPG"

    def test_get_extension_edge_cases(self):
        """Test edge cases for file extensions."""
        assert get_file_extension("file.") == "."
        assert get_file_extension(".") == ""
        assert get_file_extension("..") == ""


class TestIsValidPath:
    """Tests for is_valid_path function."""

    def test_valid_simple_paths(self):
        """Test simple valid paths."""
        assert is_valid_path("file.txt") is True
        assert is_valid_path("folder/file.txt") is True
        assert is_valid_path("/absolute/path/file.txt") is True

    def test_valid_complex_paths(self):
        """Test more complex valid paths."""
        assert is_valid_path("C:\\Users\\user\\file.txt") is True
        assert is_valid_path("/home/user/documents/file.txt") is True
        assert is_valid_path("relative/path/to/file.txt") is True

    def test_valid_path_with_spaces(self):
        """Test valid paths with spaces in directory/file names."""
        assert is_valid_path("my folder/my file.txt") is True
        assert is_valid_path("/path/with spaces/file.txt") is True

    def test_invalid_empty_path(self):
        """Test invalid empty or None paths."""
        assert is_valid_path("") is False
        assert is_valid_path(None) is False

    def test_invalid_characters(self):
        """Test paths with invalid characters."""
        assert is_valid_path("file<name>.txt") is False
        assert is_valid_path("file>name.txt") is False
        assert is_valid_path('file"name.txt') is False
        assert is_valid_path("file|name.txt") is False
        assert is_valid_path("file?name.txt") is False
        assert is_valid_path("file*name.txt") is False

    def test_invalid_leading_trailing_whitespace(self):
        """Test paths with leading or trailing whitespace."""
        assert is_valid_path(" file.txt") is False
        assert is_valid_path("file.txt ") is False
        assert is_valid_path(" file.txt ") is False
        assert is_valid_path("\tfile.txt") is False

    def test_invalid_parent_directory_traversal(self):
        """Test paths with parent directory traversal."""
        assert is_valid_path("../file.txt") is False
        assert is_valid_path("folder/../file.txt") is False
        assert is_valid_path("/path/../file.txt") is False

    def test_valid_ellipsis(self):
        """Test that ellipsis (...) in filenames is valid."""
        assert is_valid_path("file...txt") is True
        assert is_valid_path("...config") is True

    def test_valid_single_dot(self):
        """Test paths with single dots in filenames."""
        assert is_valid_path("./file.txt") is True
        assert is_valid_path("file.name.txt") is True

    def test_invalid_non_string(self):
        """Test non-string inputs."""
        assert is_valid_path(123) is False
        assert is_valid_path([]) is False
        assert is_valid_path({}) is False


class TestCountFileLines:
    """Tests for count_file_lines function."""

    def test_count_lines_simple_file(self, sample_file):
        """Test counting lines in a simple file."""
        count = count_file_lines(sample_file)
        assert count == 3

    def test_count_lines_empty_file(self, empty_file):
        """Test counting lines in an empty file."""
        count = count_file_lines(empty_file)
        assert count == 0

    def test_count_lines_multiline_file(self, multiline_file):
        """Test counting lines in a file with multiple lines."""
        count = count_file_lines(multiline_file)
        assert count == 10

    def test_count_lines_single_line(self, tmp_path):
        """Test counting lines in a single-line file."""
        file_path = tmp_path / "single_line.txt"
        file_path.write_text("Single line without newline")

        count = count_file_lines(str(file_path))
        assert count == 1

    def test_count_lines_with_trailing_newline(self, tmp_path):
        """Test counting lines with trailing newline."""
        file_path = tmp_path / "trailing_newline.txt"
        file_path.write_text("Line 1\nLine 2\nLine 3\n")

        count = count_file_lines(str(file_path))
        assert count == 3

    def test_count_lines_without_trailing_newline(self, tmp_path):
        """Test counting lines without trailing newline."""
        file_path = tmp_path / "no_trailing_newline.txt"
        file_path.write_text("Line 1\nLine 2\nLine 3")

        count = count_file_lines(str(file_path))
        assert count == 3

    def test_count_lines_large_file(self, tmp_path):
        """Test counting lines in a larger file."""
        file_path = tmp_path / "large_file.txt"
        lines = [f"Line {i}\n" for i in range(1, 101)]
        file_path.write_text("".join(lines))

        count = count_file_lines(str(file_path))
        assert count == 100

    def test_count_lines_only_newlines(self, tmp_path):
        """Test counting lines in a file with only newlines."""
        file_path = tmp_path / "only_newlines.txt"
        file_path.write_text("\n\n\n\n")

        count = count_file_lines(str(file_path))
        assert count == 4

    def test_count_lines_empty_lines(self, tmp_path):
        """Test counting lines in a file with empty lines."""
        file_path = tmp_path / "empty_lines.txt"
        file_path.write_text("Line 1\n\nLine 3\n\nLine 5\n")

        count = count_file_lines(str(file_path))
        assert count == 5
