"""Tests for the file_utils module."""

import tempfile
from pathlib import Path

import pytest
from file_utils import (
    format_file_size,
    get_file_extension,
    get_relative_path,
    parse_csv_line,
    sanitize_filename,
    validate_path_safe,
)


class TestGetFileExtension:
    def test_simple_extension(self):
        assert get_file_extension("report.pdf") == ".pdf"

    def test_txt_extension(self):
        assert get_file_extension("notes.txt") == ".txt"

    def test_no_extension(self):
        assert get_file_extension("Makefile") == ""

    def test_hidden_file_no_extension(self):
        assert get_file_extension(".gitignore") == ""

    def test_hidden_file_with_extension(self):
        assert get_file_extension(".env.local") == ".local"

    def test_multiple_dots(self):
        assert get_file_extension("archive.tar.gz") == ".gz"

    def test_path_with_directory(self):
        assert get_file_extension("/home/user/file.py") == ".py"

    def test_path_object(self):
        assert get_file_extension(Path("/tmp/data.csv")) == ".csv"

    def test_empty_string(self):
        assert get_file_extension("") == ""

    def test_type_error(self):
        with pytest.raises(TypeError):
            get_file_extension(123)


class TestSanitizeFilename:
    def test_clean_name_unchanged(self):
        assert sanitize_filename("hello_world.txt") == "hello_world.txt"

    def test_replaces_slash(self):
        assert sanitize_filename("path/to/file") == "path_to_file"

    def test_replaces_backslash(self):
        assert sanitize_filename("path\\file") == "path_file"

    def test_replaces_colon(self):
        assert sanitize_filename("C:file") == "C_file"

    def test_replaces_asterisk(self):
        assert sanitize_filename("file*.txt") == "file_.txt"

    def test_replaces_question_mark(self):
        assert sanitize_filename("what?.txt") == "what_.txt"

    def test_replaces_angle_brackets(self):
        assert sanitize_filename("<tag>") == "_tag_"

    def test_replaces_pipe(self):
        assert sanitize_filename("a|b") == "a_b"

    def test_strips_leading_trailing_dots(self):
        assert sanitize_filename(".hidden.") == "hidden"

    def test_strips_leading_trailing_spaces(self):
        assert sanitize_filename("  file  ") == "file"

    def test_fallback_for_empty_result(self):
        assert sanitize_filename("...") == "_"

    def test_custom_replacement(self):
        assert sanitize_filename("a/b/c", replacement="-") == "a-b-c"

    def test_empty_replacement(self):
        assert sanitize_filename("a/b", replacement="") == "ab"

    def test_type_error_name(self):
        with pytest.raises(TypeError):
            sanitize_filename(123)

    def test_type_error_replacement(self):
        with pytest.raises(TypeError):
            sanitize_filename("file.txt", replacement=0)

    def test_value_error_unsafe_replacement(self):
        with pytest.raises(ValueError):
            sanitize_filename("file.txt", replacement="/")


class TestParseCsvLine:
    def test_simple_line(self):
        assert parse_csv_line("a,b,c") == ["a", "b", "c"]

    def test_quoted_field(self):
        assert parse_csv_line('"hello world",foo') == ["hello world", "foo"]

    def test_quoted_field_with_comma(self):
        assert parse_csv_line('"a,b",c') == ["a,b", "c"]

    def test_quoted_field_with_escaped_quote(self):
        assert parse_csv_line('"say ""hi""",next') == ['say "hi"', "next"]

    def test_custom_delimiter(self):
        assert parse_csv_line("a;b;c", delimiter=";") == ["a", "b", "c"]

    def test_single_field(self):
        assert parse_csv_line("only") == ["only"]

    def test_empty_fields(self):
        assert parse_csv_line("a,,c") == ["a", "", "c"]

    def test_all_empty(self):
        assert parse_csv_line(",") == ["", ""]

    def test_empty_string(self):
        assert parse_csv_line("") == []

    def test_numeric_strings(self):
        assert parse_csv_line("1,2,3") == ["1", "2", "3"]

    def test_type_error_line(self):
        with pytest.raises(TypeError):
            parse_csv_line(123)

    def test_type_error_delimiter(self):
        with pytest.raises(TypeError):
            parse_csv_line("a,b", delimiter=0)

    def test_value_error_multi_char_delimiter(self):
        with pytest.raises(ValueError):
            parse_csv_line("a,,b", delimiter=",,")

    def test_value_error_multi_char_quotechar(self):
        with pytest.raises(ValueError):
            parse_csv_line("a,b", quotechar="''")


class TestFormatFileSize:
    def test_zero_bytes(self):
        assert format_file_size(0) == "0 B"

    def test_single_byte(self):
        assert format_file_size(1) == "1 B"

    def test_1023_bytes(self):
        assert format_file_size(1023) == "1023 B"

    def test_exactly_one_kib(self):
        assert format_file_size(1024) == "1.00 KiB"

    def test_one_and_half_kib(self):
        assert format_file_size(1536) == "1.50 KiB"

    def test_exactly_one_mib(self):
        assert format_file_size(1024 ** 2) == "1.00 MiB"

    def test_exactly_one_gib(self):
        assert format_file_size(1024 ** 3) == "1.00 GiB"

    def test_exactly_one_tib(self):
        assert format_file_size(1024 ** 4) == "1.00 TiB"

    def test_large_value(self):
        result = format_file_size(1024 ** 4 * 2)
        assert result == "2.00 TiB"

    def test_type_error(self):
        with pytest.raises(TypeError):
            format_file_size("1024")

    def test_type_error_float(self):
        with pytest.raises(TypeError):
            format_file_size(1.5)

    def test_type_error_bool(self):
        with pytest.raises(TypeError):
            format_file_size(True)

    def test_value_error_negative(self):
        with pytest.raises(ValueError):
            format_file_size(-1)


class TestValidatePathSafe:
    def test_simple_relative_path(self):
        assert validate_path_safe("subdir/file.txt") is True

    def test_absolute_path_no_traversal(self):
        assert validate_path_safe("/home/user/docs/file.txt") is True

    def test_traversal_dotdot(self):
        assert validate_path_safe("../secret") is False

    def test_traversal_in_middle(self):
        assert validate_path_safe("a/b/../c") is False

    def test_just_dotdot(self):
        assert validate_path_safe("..") is False

    def test_path_within_base(self):
        with tempfile.TemporaryDirectory() as base:
            target = Path(base) / "subdir" / "file.txt"
            assert validate_path_safe(target, base) is True

    def test_path_outside_base(self):
        with tempfile.TemporaryDirectory() as base:
            outside = Path(base).parent / "other.txt"
            assert validate_path_safe(outside, base) is False

    def test_path_equals_base(self):
        with tempfile.TemporaryDirectory() as base:
            assert validate_path_safe(base, base) is True

    def test_path_object_input(self):
        assert validate_path_safe(Path("subdir/file.txt")) is True

    def test_type_error_path(self):
        with pytest.raises(TypeError):
            validate_path_safe(123)

    def test_type_error_base(self):
        with pytest.raises(TypeError):
            validate_path_safe("/tmp/file", base=123)


class TestGetRelativePath:
    def test_simple_relative(self):
        assert get_relative_path("/home/user/docs/file.txt", "/home/user") == Path("docs/file.txt")

    def test_same_path(self):
        assert get_relative_path("/home/user", "/home/user") == Path(".")

    def test_immediate_child(self):
        assert get_relative_path("/tmp/file.txt", "/tmp") == Path("file.txt")

    def test_deep_nesting(self):
        result = get_relative_path("/a/b/c/d/e.py", "/a/b")
        assert result == Path("c/d/e.py")

    def test_path_objects(self):
        result = get_relative_path(Path("/a/b/c"), Path("/a"))
        assert result == Path("b/c")

    def test_value_error_not_relative(self):
        with pytest.raises(ValueError):
            get_relative_path("/other/path/file.txt", "/home/user")

    def test_type_error_path(self):
        with pytest.raises(TypeError):
            get_relative_path(123, "/home")

    def test_type_error_base(self):
        with pytest.raises(TypeError):
            get_relative_path("/home/user/file.txt", 123)
