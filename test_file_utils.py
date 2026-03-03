"""Tests for the file_utils module."""
import pytest
from pathlib import Path
import tempfile
import os
from file_utils import (
    get_file_extension,
    sanitize_filename,
    parse_csv_line,
    format_file_size,
    validate_path_safe,
    get_relative_path,
)


class TestGetFileExtension:
    """Tests for get_file_extension function."""

    def test_simple_extension(self):
        """Test basic file extensions."""
        assert get_file_extension("document.txt") == ".txt"
        assert get_file_extension("script.py") == ".py"
        assert get_file_extension("data.json") == ".json"

    def test_compound_extension(self):
        """Test files with compound extensions."""
        assert get_file_extension("archive.tar.gz") == ".gz"
        assert get_file_extension("backup.tar.bz2") == ".bz2"

    def test_no_extension(self):
        """Test files without extensions."""
        assert get_file_extension("README") == ""
        assert get_file_extension("Makefile") == ""
        assert get_file_extension("no_extension") == ""

    def test_hidden_file(self):
        """Test hidden files (starting with dot)."""
        assert get_file_extension(".gitignore") == ".gitignore"
        assert get_file_extension(".bashrc") == ".bashrc"

    def test_path_with_extension(self):
        """Test full paths with extensions."""
        assert get_file_extension("/path/to/file.txt") == ".txt"
        assert get_file_extension("relative/path/file.py") == ".py"

    def test_empty_and_none(self):
        """Test empty string and None input."""
        assert get_file_extension("") == ""
        assert get_file_extension(None) == ""


class TestSanitizeFilename:
    """Tests for sanitize_filename function."""

    def test_safe_filename(self):
        """Test filenames that are already safe."""
        assert sanitize_filename("normal_file.txt") == "normal_file.txt"
        assert sanitize_filename("file-name.pdf") == "file-name.pdf"
        assert sanitize_filename("MyFile123.doc") == "MyFile123.doc"

    def test_replace_spaces(self):
        """Test replacing spaces."""
        assert sanitize_filename("my file.txt") == "my_file.txt"
        assert sanitize_filename("multi word file.pdf") == "multi_word_file.pdf"

    def test_remove_unsafe_characters(self):
        """Test removal of unsafe characters."""
        assert sanitize_filename("file/with\\slashes.txt") == "file_with_slashes.txt"
        assert sanitize_filename("file:with*bad?chars.txt") == "file_with_bad_chars.txt"
        assert sanitize_filename('file"with<quotes>.txt') == "file_with_quotes_.txt"
        assert sanitize_filename("file|with|pipes.txt") == "file_with_pipes.txt"

    def test_custom_replacement(self):
        """Test custom replacement character."""
        assert sanitize_filename("my file.txt", replacement="-") == "my-file.txt"
        assert sanitize_filename("a/b/c.txt", replacement="") == "abc.txt"

    def test_trailing_dots_and_spaces(self):
        """Test trimming of trailing dots and spaces."""
        assert sanitize_filename("file.txt.") == "file.txt"
        assert sanitize_filename("file.txt ") == "file.txt"
        assert sanitize_filename("file.txt . ") == "file.txt"

    def test_empty_result(self):
        """Test handling of filenames that become empty after sanitization."""
        assert sanitize_filename("...") == "unnamed"
        assert sanitize_filename("   ") == "unnamed"

    def test_empty_and_none(self):
        """Test empty string and None input."""
        assert sanitize_filename("") == ""
        assert sanitize_filename(None) == ""


class TestParseCsvLine:
    """Tests for parse_csv_line function."""

    def test_simple_csv(self):
        """Test basic CSV parsing."""
        assert parse_csv_line("a,b,c") == ["a", "b", "c"]
        assert parse_csv_line("name,age,city") == ["name", "age", "city"]
        assert parse_csv_line("1,2,3") == ["1", "2", "3"]

    def test_empty_fields(self):
        """Test CSV with empty fields."""
        assert parse_csv_line("a,,c") == ["a", "", "c"]
        assert parse_csv_line(",b,") == ["", "b", ""]
        assert parse_csv_line(",,") == ["", "", ""]

    def test_quoted_fields(self):
        """Test CSV with quoted fields."""
        assert parse_csv_line('"quoted field",normal,field') == ["quoted field", "normal", "field"]
        assert parse_csv_line('"a,b,c",d,e') == ["a,b,c", "d", "e"]
        assert parse_csv_line('"first","second","third"') == ["first", "second", "third"]

    def test_quoted_field_with_delimiter(self):
        """Test quoted fields containing delimiters."""
        assert parse_csv_line('"field,with,commas",other') == ["field,with,commas", "other"]
        assert parse_csv_line('a,"b,c,d",e') == ["a", "b,c,d", "e"]

    def test_escaped_quotes(self):
        """Test fields with escaped quotes."""
        assert parse_csv_line('"field with ""quotes"""') == ['field with "quotes"']
        assert parse_csv_line('"a ""quoted"" word",b') == ['a "quoted" word', "b"]

    def test_custom_delimiter(self):
        """Test CSV with custom delimiter."""
        assert parse_csv_line("a;b;c", delimiter=";") == ["a", "b", "c"]
        assert parse_csv_line("a|b|c", delimiter="|") == ["a", "b", "c"]
        assert parse_csv_line("a\tb\tc", delimiter="\t") == ["a", "b", "c"]

    def test_single_field(self):
        """Test CSV with single field."""
        assert parse_csv_line("single") == ["single"]
        assert parse_csv_line('"single quoted"') == ["single quoted"]

    def test_empty_and_none(self):
        """Test empty string and None input."""
        assert parse_csv_line("") == [""]
        assert parse_csv_line(None) == []


class TestFormatFileSize:
    """Tests for format_file_size function."""

    def test_bytes(self):
        """Test formatting of byte sizes."""
        assert format_file_size(0) == "0.00 B"
        assert format_file_size(500) == "500.00 B"
        assert format_file_size(1023) == "1023.00 B"

    def test_kilobytes(self):
        """Test formatting of kilobyte sizes."""
        assert format_file_size(1024) == "1.00 KB"
        assert format_file_size(1536) == "1.50 KB"
        assert format_file_size(2048) == "2.00 KB"

    def test_megabytes(self):
        """Test formatting of megabyte sizes."""
        assert format_file_size(1048576) == "1.00 MB"
        assert format_file_size(1572864) == "1.50 MB"
        assert format_file_size(5242880) == "5.00 MB"

    def test_gigabytes(self):
        """Test formatting of gigabyte sizes."""
        assert format_file_size(1073741824) == "1.00 GB"
        assert format_file_size(2147483648) == "2.00 GB"
        assert format_file_size(5368709120) == "5.00 GB"

    def test_terabytes(self):
        """Test formatting of terabyte sizes."""
        assert format_file_size(1099511627776) == "1.00 TB"
        assert format_file_size(2199023255552) == "2.00 TB"

    def test_custom_decimal_places(self):
        """Test custom decimal places."""
        assert format_file_size(1536, decimal_places=0) == "2 KB"
        assert format_file_size(1536, decimal_places=1) == "1.5 KB"
        assert format_file_size(1536, decimal_places=3) == "1.500 KB"

    def test_large_sizes(self):
        """Test very large file sizes."""
        assert format_file_size(1125899906842624) == "1.00 PB"

    def test_negative_size(self):
        """Test that negative sizes raise ValueError."""
        with pytest.raises(ValueError, match="size_bytes must be non-negative"):
            format_file_size(-1)

    def test_negative_decimal_places(self):
        """Test that negative decimal places raise ValueError."""
        with pytest.raises(ValueError, match="decimal_places must be non-negative"):
            format_file_size(1024, decimal_places=-1)


class TestValidatePathSafe:
    """Tests for validate_path_safe function."""

    def test_safe_relative_paths(self):
        """Test safe relative paths."""
        assert validate_path_safe("documents/file.txt") is True
        assert validate_path_safe("folder/subfolder/file.txt") is True
        assert validate_path_safe("file.txt") is True
        assert validate_path_safe("a/b/c/d.txt") is True

    def test_path_traversal_attempts(self):
        """Test detection of path traversal attempts."""
        assert validate_path_safe("../etc/passwd") is False
        assert validate_path_safe("folder/../../etc/passwd") is False
        assert validate_path_safe("../../file.txt") is False
        assert validate_path_safe("a/../b") is False

    def test_absolute_paths(self):
        """Test rejection of absolute paths."""
        assert validate_path_safe("/etc/passwd") is False
        assert validate_path_safe("/home/user/file.txt") is False
        assert validate_path_safe("/absolute/path") is False

    def test_home_directory_expansion(self):
        """Test rejection of home directory expansion."""
        assert validate_path_safe("~/file.txt") is False
        assert validate_path_safe("~user/file.txt") is False

    def test_current_directory_reference(self):
        """Test that current directory references are allowed."""
        assert validate_path_safe("./file.txt") is True
        assert validate_path_safe("./folder/file.txt") is True

    def test_empty_and_none(self):
        """Test empty string and None input."""
        assert validate_path_safe("") is False
        assert validate_path_safe(None) is False


class TestGetRelativePath:
    """Tests for get_relative_path function."""

    def test_direct_subdirectory(self):
        """Test relative path to a direct subdirectory."""
        assert get_relative_path("/a/b", "/a/b/c") == "c"
        assert get_relative_path("/home/user", "/home/user/documents") == "documents"

    def test_nested_subdirectory(self):
        """Test relative path to a nested subdirectory."""
        assert get_relative_path("/a/b", "/a/b/c/d") == "c/d"
        assert get_relative_path("/a/b", "/a/b/c/d/e") == "c/d/e"

    def test_parent_directory(self):
        """Test relative path to a parent directory."""
        result = get_relative_path("/a/b/c", "/a/b")
        assert result == "../.." or result == "..\\.."

    def test_sibling_directory(self):
        """Test relative path to a sibling directory."""
        result = get_relative_path("/a/b/c", "/a/b/d")
        assert "../d" in result or "..\\d" in result

    def test_cousin_paths(self):
        """Test relative paths between cousin directories."""
        result = get_relative_path("/a/b/c", "/a/d/e")
        assert ".." in result and ("d" in result or "e" in result)

    def test_same_path(self):
        """Test relative path when paths are the same."""
        assert get_relative_path("/a/b/c", "/a/b/c") == "."

    def test_relative_input_paths(self):
        """Test with relative input paths."""
        assert get_relative_path("a/b", "a/b/c") == "c"
        result = get_relative_path("a/b/c", "a/b")
        assert ".." in result

    def test_empty_and_none(self):
        """Test empty string and None input."""
        assert get_relative_path("", "/a/b") == ""
        assert get_relative_path("/a/b", "") == ""
        assert get_relative_path(None, "/a/b") == ""
        assert get_relative_path("/a/b", None) == ""
        assert get_relative_path(None, None) == ""


class TestFileUtilsIntegration:
    """Integration tests using temporary files."""

    def test_sanitize_and_validate_workflow(self):
        """Test combining sanitize and validate for safe file creation."""
        unsafe_name = "../../etc/passwd.txt"
        safe_name = sanitize_filename(unsafe_name)

        assert validate_path_safe(safe_name) is True
        assert ".." not in safe_name

    def test_parse_and_create_files(self):
        """Test parsing CSV and using sanitized filenames."""
        csv_line = "file1.txt,file2.txt,../../bad/file.txt"
        fields = parse_csv_line(csv_line)

        for field in fields:
            safe_name = sanitize_filename(field)
            assert validate_path_safe(safe_name) is True

    def test_file_size_formatting_realistic(self):
        """Test file size formatting with realistic file sizes."""
        small_doc = 15360
        assert "15.00 KB" == format_file_size(small_doc)

        image = 2097152
        assert "2.00 MB" == format_file_size(image)

        video = 1073741824
        assert "1.00 GB" == format_file_size(video)

    def test_extension_and_sanitize_workflow(self):
        """Test workflow of getting extension and sanitizing."""
        filename = "my document?.txt"
        ext = get_file_extension(filename)
        safe = sanitize_filename(filename)

        assert ext == ".txt"
        assert "?" not in safe
        assert get_file_extension(safe) == ".txt"

    def test_relative_path_real_directories(self, tmp_path):
        """Test relative path calculation with real temporary directories."""
        dir1 = tmp_path / "dir1"
        dir2 = tmp_path / "dir2"
        dir1.mkdir()
        dir2.mkdir()

        result = get_relative_path(str(dir1), str(dir2))
        assert "dir2" in result or result == "../dir2" or result == "..\\dir2"
