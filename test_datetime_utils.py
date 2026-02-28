"""Tests for the datetime_utils module."""

from datetime import date, datetime, timedelta, timezone

import pytest
from datetime_utils import (
    add_business_days,
    days_between,
    format_duration,
    get_week_range,
    is_business_day,
    parse_iso_date,
)


class TestIsBusinessDay:
    def test_monday(self):
        assert is_business_day(date(2024, 1, 1)) is True  # Monday

    def test_tuesday(self):
        assert is_business_day(date(2024, 1, 2)) is True

    def test_wednesday(self):
        assert is_business_day(date(2024, 1, 3)) is True

    def test_thursday(self):
        assert is_business_day(date(2024, 1, 4)) is True

    def test_friday(self):
        assert is_business_day(date(2024, 1, 5)) is True

    def test_saturday(self):
        assert is_business_day(date(2024, 1, 6)) is False

    def test_sunday(self):
        assert is_business_day(date(2024, 1, 7)) is False

    def test_datetime_weekday(self):
        assert is_business_day(datetime(2024, 1, 1, 9, 0)) is True  # Monday

    def test_datetime_weekend(self):
        assert is_business_day(datetime(2024, 1, 6, 12, 0)) is False  # Saturday

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_business_day("2024-01-01")

    def test_type_error_int(self):
        with pytest.raises(TypeError):
            is_business_day(20240101)


class TestAddBusinessDays:
    def test_add_zero_days(self):
        d = date(2024, 1, 1)  # Monday
        assert add_business_days(d, 0) == d

    def test_add_one_day_weekday(self):
        assert add_business_days(date(2024, 1, 1), 1) == date(2024, 1, 2)  # Mon -> Tue

    def test_add_five_days_within_week(self):
        assert add_business_days(date(2024, 1, 1), 5) == date(2024, 1, 8)  # Mon -> next Mon

    def test_skips_weekend_forward(self):
        assert add_business_days(date(2024, 1, 5), 1) == date(2024, 1, 8)  # Fri -> Mon

    def test_skips_weekend_two_days(self):
        assert add_business_days(date(2024, 1, 5), 2) == date(2024, 1, 9)  # Fri -> Tue

    def test_subtract_business_days(self):
        assert add_business_days(date(2024, 1, 8), -1) == date(2024, 1, 5)  # Mon -> Fri

    def test_subtract_skips_weekend(self):
        assert add_business_days(date(2024, 1, 8), -3) == date(2024, 1, 3)  # Mon -> Wed

    def test_start_on_saturday_forward(self):
        assert add_business_days(date(2024, 1, 6), 1) == date(2024, 1, 8)  # Sat -> Mon

    def test_add_large_number(self):
        result = add_business_days(date(2024, 1, 1), 10)
        assert result == date(2024, 1, 15)

    def test_returns_datetime_when_given_datetime(self):
        dt = datetime(2024, 1, 1, 9, 30)
        result = add_business_days(dt, 1)
        assert isinstance(result, datetime)
        assert result.date() == date(2024, 1, 2)

    def test_type_error_date(self):
        with pytest.raises(TypeError):
            add_business_days("2024-01-01", 1)

    def test_type_error_days_float(self):
        with pytest.raises(TypeError):
            add_business_days(date(2024, 1, 1), 1.5)

    def test_type_error_days_bool(self):
        with pytest.raises(TypeError):
            add_business_days(date(2024, 1, 1), True)

    def test_month_boundary(self):
        assert add_business_days(date(2024, 1, 31), 1) == date(2024, 2, 1)

    def test_year_boundary(self):
        assert add_business_days(date(2023, 12, 29), 1) == date(2024, 1, 1)

    def test_leap_year_boundary(self):
        assert add_business_days(date(2024, 2, 28), 1) == date(2024, 2, 29)


class TestFormatDuration:
    def test_zero_seconds(self):
        assert format_duration(0) == "0 seconds"

    def test_one_second(self):
        assert format_duration(1) == "1 second"

    def test_two_seconds(self):
        assert format_duration(2) == "2 seconds"

    def test_one_minute(self):
        assert format_duration(60) == "1 minute"

    def test_one_hour(self):
        assert format_duration(3600) == "1 hour"

    def test_one_day(self):
        assert format_duration(86400) == "1 day"

    def test_combined(self):
        assert format_duration(90061) == "1 day, 1 hour, 1 minute, 1 second"

    def test_combined_plural(self):
        assert format_duration(2 * 86400 + 2 * 3600 + 2 * 60 + 2) == "2 days, 2 hours, 2 minutes, 2 seconds"

    def test_timedelta_input(self):
        assert format_duration(timedelta(hours=2, minutes=30)) == "2 hours, 30 minutes"

    def test_timedelta_zero(self):
        assert format_duration(timedelta(0)) == "0 seconds"

    def test_float_input(self):
        assert format_duration(61.9) == "1 minute, 1 second"

    def test_only_minutes_and_seconds(self):
        assert format_duration(125) == "2 minutes, 5 seconds"

    def test_value_error_negative(self):
        with pytest.raises(ValueError):
            format_duration(-1)

    def test_value_error_negative_timedelta(self):
        with pytest.raises(ValueError):
            format_duration(timedelta(seconds=-1))

    def test_type_error(self):
        with pytest.raises(TypeError):
            format_duration("1 hour")

    def test_type_error_bool(self):
        with pytest.raises(TypeError):
            format_duration(True)


class TestParseIsoDate:
    def test_date_only(self):
        result = parse_iso_date("2024-03-15")
        assert result == date(2024, 3, 15)
        assert type(result) is date

    def test_naive_datetime(self):
        result = parse_iso_date("2024-03-15T10:30:00")
        assert result == datetime(2024, 3, 15, 10, 30, 0)
        assert result.tzinfo is None

    def test_aware_datetime_utc_offset(self):
        result = parse_iso_date("2024-03-15T10:30:00+00:00")
        assert isinstance(result, datetime)
        assert result.tzinfo is not None

    def test_aware_datetime_positive_offset(self):
        result = parse_iso_date("2024-03-15T10:30:00+05:30")
        assert isinstance(result, datetime)
        assert result.utcoffset() == timedelta(hours=5, minutes=30)

    def test_aware_datetime_negative_offset(self):
        result = parse_iso_date("2024-03-15T10:30:00-08:00")
        assert isinstance(result, datetime)
        assert result.utcoffset() == timedelta(hours=-8)

    def test_z_suffix(self):
        result = parse_iso_date("2024-03-15T10:30:00Z")
        assert isinstance(result, datetime)
        assert result.utcoffset() == timedelta(0)

    def test_leading_trailing_whitespace(self):
        result = parse_iso_date("  2024-01-01  ")
        assert result == date(2024, 1, 1)

    def test_leap_year_date(self):
        assert parse_iso_date("2024-02-29") == date(2024, 2, 29)

    def test_value_error_invalid_date(self):
        with pytest.raises(ValueError):
            parse_iso_date("2023-02-29")  # Not a leap year

    def test_value_error_invalid_format(self):
        with pytest.raises(ValueError):
            parse_iso_date("15/03/2024")

    def test_value_error_empty_string(self):
        with pytest.raises(ValueError):
            parse_iso_date("")

    def test_type_error(self):
        with pytest.raises(TypeError):
            parse_iso_date(20240315)

    def test_year_only_invalid(self):
        with pytest.raises(ValueError):
            parse_iso_date("2024")


class TestGetWeekRange:
    def test_monday_is_start(self):
        monday = date(2024, 1, 1)
        start, end = get_week_range(monday)
        assert start == date(2024, 1, 1)
        assert end == date(2024, 1, 7)

    def test_sunday_is_end(self):
        sunday = date(2024, 1, 7)
        start, end = get_week_range(sunday)
        assert start == date(2024, 1, 1)
        assert end == date(2024, 1, 7)

    def test_midweek(self):
        wednesday = date(2024, 1, 3)
        start, end = get_week_range(wednesday)
        assert start == date(2024, 1, 1)
        assert end == date(2024, 1, 7)

    def test_range_spans_month_boundary(self):
        saturday = date(2024, 2, 3)
        start, end = get_week_range(saturday)
        assert start == date(2024, 1, 29)
        assert end == date(2024, 2, 4)

    def test_range_spans_year_boundary(self):
        d = date(2024, 1, 3)  # Wednesday
        start, end = get_week_range(d)
        assert start == date(2024, 1, 1)
        assert end == date(2024, 1, 7)

    def test_week_range_around_new_year(self):
        d = date(2024, 12, 31)  # Tuesday
        start, end = get_week_range(d)
        assert start == date(2024, 12, 30)
        assert end == date(2025, 1, 5)

    def test_result_is_always_monday_to_sunday(self):
        for day_offset in range(7):
            d = date(2024, 3, 4) + timedelta(days=day_offset)
            start, end = get_week_range(d)
            assert start.weekday() == 0  # Monday
            assert end.weekday() == 6    # Sunday
            assert (end - start).days == 6

    def test_leap_year_week(self):
        d = date(2024, 2, 29)  # Thursday
        start, end = get_week_range(d)
        assert start == date(2024, 2, 26)
        assert end == date(2024, 3, 3)

    def test_datetime_input(self):
        dt = datetime(2024, 1, 3, 15, 30)  # Wednesday
        start, end = get_week_range(dt)
        assert start == date(2024, 1, 1)
        assert end == date(2024, 1, 7)

    def test_returns_date_objects(self):
        start, end = get_week_range(date(2024, 1, 1))
        assert type(start) is date
        assert type(end) is date

    def test_type_error(self):
        with pytest.raises(TypeError):
            get_week_range("2024-01-01")


class TestDaysBetween:
    def test_same_date(self):
        d = date(2024, 1, 15)
        assert days_between(d, d) == 0

    def test_one_day_apart(self):
        assert days_between(date(2024, 1, 1), date(2024, 1, 2)) == 1

    def test_absolute_order_independent(self):
        d1 = date(2024, 1, 1)
        d2 = date(2024, 1, 10)
        assert days_between(d1, d2) == days_between(d2, d1)

    def test_signed_positive(self):
        assert days_between(date(2024, 1, 1), date(2024, 1, 10), absolute=False) == 9

    def test_signed_negative(self):
        assert days_between(date(2024, 1, 10), date(2024, 1, 1), absolute=False) == -9

    def test_across_month_boundary(self):
        assert days_between(date(2024, 1, 31), date(2024, 2, 1)) == 1

    def test_across_year_boundary(self):
        assert days_between(date(2023, 12, 31), date(2024, 1, 1)) == 1

    def test_leap_year(self):
        assert days_between(date(2024, 2, 28), date(2024, 3, 1)) == 2

    def test_non_leap_year(self):
        assert days_between(date(2023, 2, 28), date(2023, 3, 1)) == 1

    def test_full_year(self):
        assert days_between(date(2024, 1, 1), date(2025, 1, 1)) == 366  # 2024 is leap

    def test_naive_datetimes(self):
        dt1 = datetime(2024, 1, 1, 6, 0)
        dt2 = datetime(2024, 1, 3, 18, 0)
        assert days_between(dt1, dt2) == 2

    def test_aware_datetimes(self):
        utc = timezone.utc
        dt1 = datetime(2024, 1, 1, 0, 0, tzinfo=utc)
        dt2 = datetime(2024, 1, 5, 0, 0, tzinfo=utc)
        assert days_between(dt1, dt2) == 4

    def test_mixed_date_and_datetime(self):
        assert days_between(date(2024, 1, 1), datetime(2024, 1, 4, 12, 0)) == 3

    def test_mixed_aware_naive_raises(self):
        utc = timezone.utc
        aware = datetime(2024, 1, 1, tzinfo=utc)
        naive = datetime(2024, 1, 5)
        with pytest.raises(ValueError):
            days_between(aware, naive)

    def test_type_error_d1(self):
        with pytest.raises(TypeError):
            days_between("2024-01-01", date(2024, 1, 5))

    def test_type_error_d2(self):
        with pytest.raises(TypeError):
            days_between(date(2024, 1, 1), "2024-01-05")
