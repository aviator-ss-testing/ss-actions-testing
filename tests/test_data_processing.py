"""
Comprehensive unit tests for the data_processing module.
Tests JSON processing, CSV handling, dictionary operations, and datetime utilities.
"""

import pytest
import json
from datetime import datetime, timezone, timedelta
from data_processing import (
    parse_json_string, validate_json_schema, json_to_string, extract_json_values,
    parse_csv_string, format_as_csv, csv_column_stats,
    deep_merge, filter_keys, transform_values, flatten_dict, group_by_key,
    format_datetime, parse_datetime_string, add_business_days,
    calculate_age_in_years, get_date_range, is_weekend, get_month_boundaries,
    convert_timezone
)


class TestJSONProcessing:
    """Test JSON processing functions."""

    def test_parse_json_string_basic(self):
        json_str = '{"name": "John", "age": 30}'
        result = parse_json_string(json_str)
        assert result == {"name": "John", "age": 30}

    def test_parse_json_string_array(self):
        json_str = '[1, 2, 3, "test"]'
        result = parse_json_string(json_str)
        assert result == [1, 2, 3, "test"]

    def test_parse_json_string_nested(self):
        json_str = '{"user": {"name": "Alice", "profile": {"age": 25}}}'
        result = parse_json_string(json_str)
        expected = {"user": {"name": "Alice", "profile": {"age": 25}}}
        assert result == expected

    def test_parse_json_string_invalid(self):
        with pytest.raises(ValueError, match="Invalid JSON"):
            parse_json_string('{"invalid": json}')

        with pytest.raises(ValueError, match="Invalid JSON"):
            parse_json_string('{missing_quotes: true}')

    def test_parse_json_string_empty(self):
        with pytest.raises(ValueError):
            parse_json_string("")

    @pytest.mark.parametrize("json_str,expected", [
        ('{"a": 1}', {"a": 1}),
        ('[]', []),
        ('null', None),
        ('true', True),
        ('42', 42),
        ('"string"', "string"),
    ])
    def test_parse_json_string_parametrized(self, json_str, expected):
        assert parse_json_string(json_str) == expected

    def test_validate_json_schema_valid(self):
        data = {"name": "John", "age": 30, "email": "john@example.com"}
        required_keys = ["name", "age"]
        assert validate_json_schema(data, required_keys) is True

    def test_validate_json_schema_missing_keys(self):
        data = {"name": "John"}
        required_keys = ["name", "age", "email"]
        assert validate_json_schema(data, required_keys) is False

    def test_validate_json_schema_not_dict(self):
        assert validate_json_schema([1, 2, 3], ["name"]) is False
        assert validate_json_schema("string", ["name"]) is False
        assert validate_json_schema(None, ["name"]) is False

    def test_validate_json_schema_empty(self):
        assert validate_json_schema({}, []) is True
        assert validate_json_schema({"a": 1}, []) is True

    def test_json_to_string_basic(self):
        data = {"name": "John", "age": 30}
        result = json_to_string(data)
        assert json.loads(result) == data

    def test_json_to_string_with_indent(self):
        data = {"name": "John", "nested": {"value": 42}}
        result = json_to_string(data, indent=2)
        assert "\n" in result
        assert json.loads(result) == data

    def test_json_to_string_non_serializable(self):
        class CustomObject:
            pass

        with pytest.raises(ValueError, match="not JSON serializable"):
            json_to_string({"obj": CustomObject()})

    def test_json_to_string_unicode(self):
        data = {"message": "Hello 🌍", "chinese": "你好"}
        result = json_to_string(data)
        parsed = json.loads(result)
        assert parsed == data

    def test_extract_json_values_basic(self):
        data = {"user": {"profile": {"name": "Alice"}}}
        assert extract_json_values(data, "user.profile.name") == "Alice"
        assert extract_json_values(data, "user.profile") == {"name": "Alice"}

    def test_extract_json_values_not_found(self):
        data = {"user": {"name": "Alice"}}
        assert extract_json_values(data, "user.age") is None
        assert extract_json_values(data, "missing.path") is None

    def test_extract_json_values_array_access(self):
        data = {"items": [{"name": "first"}, {"name": "second"}]}
        assert extract_json_values(data, "items") == [{"name": "first"}, {"name": "second"}]

    def test_extract_json_values_root_level(self):
        data = {"name": "John", "age": 30}
        assert extract_json_values(data, "name") == "John"
        assert extract_json_values(data, "age") == 30

    @pytest.mark.parametrize("data,path,expected", [
        ({"a": {"b": {"c": 123}}}, "a.b.c", 123),
        ({"x": {"y": "value"}}, "x.y", "value"),
        ({"root": "value"}, "root", "value"),
        ({"a": {"b": None}}, "a.b", None),
    ])
    def test_extract_json_values_parametrized(self, data, path, expected):
        assert extract_json_values(data, path) == expected


class TestCSVProcessing:
    """Test CSV processing functions."""

    def test_parse_csv_string_basic(self):
        csv_str = "name,age,city\nJohn,30,NYC\nAlice,25,LA"
        result = parse_csv_string(csv_str)
        expected = [
            {"name": "John", "age": "30", "city": "NYC"},
            {"name": "Alice", "age": "25", "city": "LA"}
        ]
        assert result == expected

    def test_parse_csv_string_no_header(self):
        csv_str = "John,30,NYC\nAlice,25,LA"
        result = parse_csv_string(csv_str, header=False)
        expected = [
            {"col_0": "John", "col_1": "30", "col_2": "NYC"},
            {"col_0": "Alice", "col_1": "25", "col_2": "LA"}
        ]
        assert result == expected

    def test_parse_csv_string_custom_delimiter(self):
        csv_str = "name;age;city\nJohn;30;NYC\nAlice;25;LA"
        result = parse_csv_string(csv_str, delimiter=";")
        expected = [
            {"name": "John", "age": "30", "city": "NYC"},
            {"name": "Alice", "age": "25", "city": "LA"}
        ]
        assert result == expected

    def test_parse_csv_string_empty(self):
        result = parse_csv_string("")
        assert result == []

    def test_parse_csv_string_single_row(self):
        csv_str = "name,age\nJohn,30"
        result = parse_csv_string(csv_str)
        assert result == [{"name": "John", "age": "30"}]

    def test_format_as_csv_basic(self):
        data = [
            {"name": "John", "age": "30"},
            {"name": "Alice", "age": "25"}
        ]
        result = format_as_csv(data)
        lines = result.strip().split('\n')
        assert lines[0] == "name,age"
        assert "John,30" in lines
        assert "Alice,25" in lines

    def test_format_as_csv_empty(self):
        assert format_as_csv([]) == ""

    def test_format_as_csv_custom_delimiter(self):
        data = [{"name": "John", "city": "NYC"}]
        result = format_as_csv(data, delimiter="|")
        lines = result.strip().split('\n')
        assert lines[0] == "name|city"
        assert "John|NYC" in lines

    def test_format_as_csv_mixed_types(self):
        data = [{"name": "John", "age": 30, "active": True}]
        result = format_as_csv(data)
        assert "John" in result
        assert "30" in result
        assert "True" in result

    def test_csv_column_stats_basic(self):
        csv_str = "name,score\nJohn,85\nAlice,92\nBob,78"
        result = csv_column_stats(csv_str, "score")
        expected = {
            'count': 3,
            'sum': 255.0,
            'mean': 85.0,
            'min': 78.0,
            'max': 92.0
        }
        assert result == expected

    def test_csv_column_stats_non_numeric(self):
        csv_str = "name,score\nJohn,A\nAlice,92\nBob,invalid"
        result = csv_column_stats(csv_str, "score")
        expected = {
            'count': 1,
            'sum': 92.0,
            'mean': 92.0,
            'min': 92.0,
            'max': 92.0
        }
        assert result == expected

    def test_csv_column_stats_missing_column(self):
        csv_str = "name,age\nJohn,30\nAlice,25"
        result = csv_column_stats(csv_str, "score")
        expected = {'count': 0, 'sum': 0, 'mean': 0, 'min': 0, 'max': 0}
        assert result == expected

    def test_csv_column_stats_negative_numbers(self):
        csv_str = "value\n-10\n5\n-3"
        result = csv_column_stats(csv_str, "value")
        assert result['sum'] == -8.0
        assert result['min'] == -10.0
        assert result['max'] == 5.0

    @pytest.mark.parametrize("csv_data,column,expected_count", [
        ("val\n1\n2\n3", "val", 3),
        ("val\n1.5\n2.5", "val", 2),
        ("val\n1\ninvalid\n3", "val", 2),
        ("val\n", "val", 0),
    ])
    def test_csv_column_stats_parametrized(self, csv_data, column, expected_count):
        result = csv_column_stats(csv_data, column)
        assert result['count'] == expected_count


class TestDictionaryOperations:
    """Test dictionary manipulation functions."""

    def test_deep_merge_basic(self):
        dict1 = {"a": 1, "b": {"c": 2}}
        dict2 = {"b": {"d": 3}, "e": 4}
        result = deep_merge(dict1, dict2)
        expected = {"a": 1, "b": {"c": 2, "d": 3}, "e": 4}
        assert result == expected

    def test_deep_merge_overwrite(self):
        dict1 = {"a": 1, "b": {"c": 2}}
        dict2 = {"a": 10, "b": {"c": 20}}
        result = deep_merge(dict1, dict2)
        expected = {"a": 10, "b": {"c": 20}}
        assert result == expected

    def test_deep_merge_nested(self):
        dict1 = {"level1": {"level2": {"level3": "old"}}}
        dict2 = {"level1": {"level2": {"level3": "new", "other": "value"}}}
        result = deep_merge(dict1, dict2)
        expected = {"level1": {"level2": {"level3": "new", "other": "value"}}}
        assert result == expected

    def test_deep_merge_empty(self):
        assert deep_merge({}, {"a": 1}) == {"a": 1}
        assert deep_merge({"a": 1}, {}) == {"a": 1}
        assert deep_merge({}, {}) == {}

    def test_deep_merge_non_dict_values(self):
        dict1 = {"a": {"b": [1, 2]}}
        dict2 = {"a": {"b": [3, 4]}}
        result = deep_merge(dict1, dict2)
        assert result == {"a": {"b": [3, 4]}}

    def test_filter_keys_basic(self):
        data = {"apple": 1, "banana": 2, "apricot": 3, "orange": 4}
        result = filter_keys(data, lambda k: k.startswith("a"))
        assert result == {"apple": 1, "apricot": 3}

    def test_filter_keys_no_matches(self):
        data = {"x": 1, "y": 2}
        result = filter_keys(data, lambda k: k.startswith("z"))
        assert result == {}

    def test_filter_keys_all_match(self):
        data = {"a1": 1, "a2": 2, "a3": 3}
        result = filter_keys(data, lambda k: k.startswith("a"))
        assert result == data

    def test_filter_keys_length_filter(self):
        data = {"a": 1, "bb": 2, "ccc": 3, "dddd": 4}
        result = filter_keys(data, lambda k: len(k) <= 2)
        assert result == {"a": 1, "bb": 2}

    def test_transform_values_basic(self):
        data = {"a": 1, "b": 2, "c": 3}
        result = transform_values(data, lambda x: x * 2)
        assert result == {"a": 2, "b": 4, "c": 6}

    def test_transform_values_string_upper(self):
        data = {"name": "john", "city": "nyc"}
        result = transform_values(data, str.upper)
        assert result == {"name": "JOHN", "city": "NYC"}

    def test_transform_values_mixed_types(self):
        data = {"str": "hello", "num": 42, "list": [1, 2]}
        result = transform_values(data, str)
        assert result == {"str": "hello", "num": "42", "list": "[1, 2]"}

    def test_transform_values_empty(self):
        result = transform_values({}, lambda x: x)
        assert result == {}

    def test_flatten_dict_basic(self):
        data = {"a": {"b": {"c": 1}}}
        result = flatten_dict(data)
        assert result == {"a.b.c": 1}

    def test_flatten_dict_multiple_nested(self):
        data = {"user": {"name": "John", "profile": {"age": 30, "city": "NYC"}}}
        result = flatten_dict(data)
        expected = {
            "user.name": "John",
            "user.profile.age": 30,
            "user.profile.city": "NYC"
        }
        assert result == expected

    def test_flatten_dict_custom_separator(self):
        data = {"a": {"b": {"c": 1}}}
        result = flatten_dict(data, separator="_")
        assert result == {"a_b_c": 1}

    def test_flatten_dict_mixed_types(self):
        data = {"a": 1, "b": {"c": 2}, "d": [1, 2]}
        result = flatten_dict(data)
        assert result == {"a": 1, "b.c": 2, "d": [1, 2]}

    def test_flatten_dict_empty(self):
        assert flatten_dict({}) == {}
        assert flatten_dict({"a": {}}) == {}

    def test_group_by_key_basic(self):
        data = [
            {"type": "fruit", "name": "apple"},
            {"type": "vegetable", "name": "carrot"},
            {"type": "fruit", "name": "banana"}
        ]
        result = group_by_key(data, "type")
        assert len(result["fruit"]) == 2
        assert len(result["vegetable"]) == 1
        assert result["fruit"][0]["name"] == "apple"

    def test_group_by_key_missing_key(self):
        data = [
            {"name": "item1"},
            {"type": "A", "name": "item2"},
            {"type": "A", "name": "item3"}
        ]
        result = group_by_key(data, "type")
        assert "A" in result
        assert len(result["A"]) == 2

    def test_group_by_key_empty(self):
        assert group_by_key([], "type") == {}

    def test_group_by_key_numeric_values(self):
        data = [
            {"score": 85, "name": "John"},
            {"score": 85, "name": "Alice"},
            {"score": 90, "name": "Bob"}
        ]
        result = group_by_key(data, "score")
        assert "85" in result
        assert "90" in result
        assert len(result["85"]) == 2

    @pytest.mark.parametrize("separator,expected_key", [
        (".", "a.b.c"), ("_", "a_b_c"), ("-", "a-b-c"), ("/", "a/b/c")
    ])
    def test_flatten_dict_separators(self, separator, expected_key):
        data = {"a": {"b": {"c": 1}}}
        result = flatten_dict(data, separator=separator)
        assert result == {expected_key: 1}


class TestDateTimeUtilities:
    """Test datetime utility functions."""

    def test_format_datetime_default(self):
        dt = datetime(2023, 12, 25, 15, 30, 45)
        result = format_datetime(dt)
        assert result == "2023-12-25 15:30:45"

    def test_format_datetime_custom_format(self):
        dt = datetime(2023, 12, 25, 15, 30, 45)
        result = format_datetime(dt, "%Y/%m/%d %H:%M")
        assert result == "2023/12/25 15:30"

    def test_format_datetime_date_only(self):
        dt = datetime(2023, 12, 25)
        result = format_datetime(dt, "%Y-%m-%d")
        assert result == "2023-12-25"

    def test_parse_datetime_string_default(self):
        date_string = "2023-12-25 15:30:45"
        result = parse_datetime_string(date_string)
        expected = datetime(2023, 12, 25, 15, 30, 45)
        assert result == expected

    def test_parse_datetime_string_custom_format(self):
        date_string = "25/12/2023 15:30"
        format_string = "%d/%m/%Y %H:%M"
        result = parse_datetime_string(date_string, format_string)
        expected = datetime(2023, 12, 25, 15, 30)
        assert result == expected

    def test_parse_datetime_string_invalid(self):
        with pytest.raises(ValueError, match="Invalid datetime format"):
            parse_datetime_string("invalid date")

        with pytest.raises(ValueError, match="Invalid datetime format"):
            parse_datetime_string("2023-12-25", "%Y/%m/%d")

    def test_add_business_days_basic(self):
        start_date = datetime(2023, 12, 22)  # Friday
        result = add_business_days(start_date, 1)
        expected = datetime(2023, 12, 25)  # Monday
        assert result == expected

    def test_add_business_days_multiple(self):
        start_date = datetime(2023, 12, 20)  # Wednesday
        result = add_business_days(start_date, 5)
        expected = datetime(2023, 12, 27)  # Wednesday (next week)
        assert result == expected

    def test_add_business_days_zero(self):
        start_date = datetime(2023, 12, 20)
        result = add_business_days(start_date, 0)
        assert result == start_date

    def test_add_business_days_weekend_start(self):
        start_date = datetime(2023, 12, 23)  # Saturday
        result = add_business_days(start_date, 1)
        expected = datetime(2023, 12, 25)  # Monday
        assert result == expected

    def test_calculate_age_in_years_basic(self):
        birth_date = datetime(1990, 6, 15)
        reference_date = datetime(2023, 6, 15)
        assert calculate_age_in_years(birth_date, reference_date) == 33

    def test_calculate_age_in_years_before_birthday(self):
        birth_date = datetime(1990, 6, 15)
        reference_date = datetime(2023, 6, 10)
        assert calculate_age_in_years(birth_date, reference_date) == 32

    def test_calculate_age_in_years_after_birthday(self):
        birth_date = datetime(1990, 6, 15)
        reference_date = datetime(2023, 6, 20)
        assert calculate_age_in_years(birth_date, reference_date) == 33

    def test_calculate_age_in_years_same_day(self):
        birth_date = datetime(2000, 1, 1)
        reference_date = datetime(2020, 1, 1)
        assert calculate_age_in_years(birth_date, reference_date) == 20

    def test_get_date_range_basic(self):
        start = datetime(2023, 1, 1)
        end = datetime(2023, 1, 5)
        result = get_date_range(start, end)
        assert len(result) == 5
        assert result[0] == start
        assert result[-1] == end

    def test_get_date_range_custom_step(self):
        start = datetime(2023, 1, 1)
        end = datetime(2023, 1, 10)
        result = get_date_range(start, end, step_days=3)
        expected_dates = [
            datetime(2023, 1, 1),
            datetime(2023, 1, 4),
            datetime(2023, 1, 7),
            datetime(2023, 1, 10)
        ]
        assert result == expected_dates

    def test_get_date_range_single_day(self):
        start = datetime(2023, 1, 1)
        end = datetime(2023, 1, 1)
        result = get_date_range(start, end)
        assert result == [start]

    def test_is_weekend_saturday(self):
        saturday = datetime(2023, 12, 23)  # Saturday
        assert is_weekend(saturday) is True

    def test_is_weekend_sunday(self):
        sunday = datetime(2023, 12, 24)  # Sunday
        assert is_weekend(sunday) is True

    def test_is_weekend_weekday(self):
        monday = datetime(2023, 12, 25)  # Monday
        assert is_weekend(monday) is False

        friday = datetime(2023, 12, 22)  # Friday
        assert is_weekend(friday) is False

    @pytest.mark.parametrize("date,expected", [
        (datetime(2023, 12, 23), True),   # Saturday
        (datetime(2023, 12, 24), True),   # Sunday
        (datetime(2023, 12, 25), False),  # Monday
        (datetime(2023, 12, 26), False),  # Tuesday
        (datetime(2023, 12, 29), False),  # Friday
    ])
    def test_is_weekend_parametrized(self, date, expected):
        assert is_weekend(date) == expected

    def test_get_month_boundaries_basic(self):
        date = datetime(2023, 6, 15, 12, 30, 45)
        first_day, last_day = get_month_boundaries(date)

        assert first_day == datetime(2023, 6, 1, 0, 0, 0, 0)
        assert last_day.year == 2023
        assert last_day.month == 6
        assert last_day.day == 30
        assert last_day.hour == 23
        assert last_day.minute == 59

    def test_get_month_boundaries_december(self):
        date = datetime(2023, 12, 15)
        first_day, last_day = get_month_boundaries(date)

        assert first_day == datetime(2023, 12, 1, 0, 0, 0, 0)
        assert last_day.year == 2023
        assert last_day.month == 12
        assert last_day.day == 31

    def test_get_month_boundaries_february(self):
        date = datetime(2024, 2, 15)  # Leap year
        first_day, last_day = get_month_boundaries(date)

        assert first_day == datetime(2024, 2, 1, 0, 0, 0, 0)
        assert last_day.day == 29  # Leap year February

    def test_convert_timezone_basic(self):
        dt = datetime(2023, 6, 15, 12, 0, 0)
        utc = timezone.utc
        eastern = timezone(timedelta(hours=-5))

        result = convert_timezone(dt, utc, eastern)
        assert result.hour == 7  # 12 UTC - 5 hours = 7 EST

    def test_convert_timezone_with_existing_timezone(self):
        utc = timezone.utc
        eastern = timezone(timedelta(hours=-5))
        dt = datetime(2023, 6, 15, 12, 0, 0, tzinfo=utc)

        result = convert_timezone(dt, utc, eastern)
        assert result.hour == 7


class TestErrorHandling:
    """Test error handling and edge cases."""

    def test_csv_functions_with_invalid_data(self):
        with pytest.raises((AttributeError, TypeError)):
            parse_csv_string(None)

        with pytest.raises(TypeError):
            format_as_csv("not a list")

    def test_datetime_functions_with_invalid_data(self):
        with pytest.raises(AttributeError):
            format_datetime(None)

        with pytest.raises(AttributeError):
            is_weekend("not a date")

    def test_dict_functions_with_invalid_data(self):
        with pytest.raises(AttributeError):
            deep_merge("not a dict", {})

        with pytest.raises(TypeError):
            filter_keys("not a dict", lambda x: True)

    def test_json_extract_with_invalid_path(self):
        data = {"a": 1}
        assert extract_json_values(data, "") is None
        assert extract_json_values(data, "...") is None


class TestPerformance:
    """Test performance characteristics with larger inputs."""

    def test_large_json_processing(self):
        large_data = {"items": [{"id": i, "value": f"item_{i}"} for i in range(1000)]}
        json_str = json_to_string(large_data)
        parsed = parse_json_string(json_str)
        assert len(parsed["items"]) == 1000

    def test_large_csv_processing(self):
        data = [{"id": i, "value": i * 2} for i in range(100)]
        csv_str = format_as_csv(data)
        parsed = parse_csv_string(csv_str)
        assert len(parsed) == 100

    def test_deep_dict_nesting(self):
        data = {"level": 1}
        current = data
        for i in range(2, 10):
            current["nested"] = {"level": i}
            current = current["nested"]

        flattened = flatten_dict(data)
        assert "nested.nested.nested.nested.nested.nested.nested.nested.level" in flattened

    def test_large_date_range(self):
        start = datetime(2020, 1, 1)
        end = datetime(2020, 12, 31)
        dates = get_date_range(start, end)
        assert len(dates) == 366  # 2020 is a leap year