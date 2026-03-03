"""Tests for datetime_utils module."""

import pytest
from datetime import datetime, date, timedelta, timezone
from datetime_utils import (
    is_business_day,
    add_business_days,
    format_duration,
    parse_iso_date,
    get_week_range,
    days_between,
)


class TestIsBusinessDay:
    """Tests for is_business_day function."""

    def test_monday_is_business_day(self):
        """Monday should be a business day."""
        monday = date(2024, 1, 1)  # Jan 1, 2024 is a Monday
        assert is_business_day(monday) is True

    def test_friday_is_business_day(self):
        """Friday should be a business day."""
        friday = date(2024, 1, 5)  # Jan 5, 2024 is a Friday
        assert is_business_day(friday) is True

    def test_saturday_is_not_business_day(self):
        """Saturday should not be a business day."""
        saturday = date(2024, 1, 6)  # Jan 6, 2024 is a Saturday
        assert is_business_day(saturday) is False

    def test_sunday_is_not_business_day(self):
        """Sunday should not be a business day."""
        sunday = date(2024, 1, 7)  # Jan 7, 2024 is a Sunday
        assert is_business_day(sunday) is False

    def test_leap_year_business_day(self):
        """Test business day check on leap year date."""
        leap_day = date(2024, 2, 29)  # Feb 29, 2024 is a Thursday
        assert is_business_day(leap_day) is True


class TestAddBusinessDays:
    """Tests for add_business_days function."""

    def test_add_zero_business_days(self):
        """Adding zero business days should return the same date."""
        start = date(2024, 1, 1)  # Monday
        result = add_business_days(start, 0)
        assert result == start

    def test_add_one_business_day_from_monday(self):
        """Adding 1 business day from Monday should give Tuesday."""
        monday = date(2024, 1, 1)
        result = add_business_days(monday, 1)
        assert result == date(2024, 1, 2)

    def test_add_business_days_skips_weekend(self):
        """Adding business days should skip weekends."""
        friday = date(2024, 1, 5)
        result = add_business_days(friday, 1)
        assert result == date(2024, 1, 8)  # Next Monday

    def test_add_multiple_business_days_over_weekend(self):
        """Adding multiple business days should skip weekends."""
        thursday = date(2024, 1, 4)
        result = add_business_days(thursday, 3)
        assert result == date(2024, 1, 9)  # Tuesday of next week

    def test_subtract_business_days(self):
        """Subtracting business days should work correctly."""
        wednesday = date(2024, 1, 10)
        result = add_business_days(wednesday, -3)
        assert result == date(2024, 1, 5)  # Previous Friday

    def test_subtract_business_days_over_weekend(self):
        """Subtracting business days should skip weekends backwards."""
        monday = date(2024, 1, 8)
        result = add_business_days(monday, -1)
        assert result == date(2024, 1, 5)  # Previous Friday

    def test_add_business_days_across_month_boundary(self):
        """Adding business days should work across month boundaries."""
        jan_31 = date(2024, 1, 31)  # Wednesday
        result = add_business_days(jan_31, 2)
        assert result == date(2024, 2, 2)  # Friday, Feb 2


class TestFormatDuration:
    """Tests for format_duration function."""

    def test_zero_seconds(self):
        """Zero seconds should format as '0s'."""
        assert format_duration(0) == "0s"

    def test_only_seconds(self):
        """Duration with only seconds."""
        assert format_duration(45) == "45s"

    def test_fractional_seconds(self):
        """Duration with fractional seconds."""
        assert format_duration(3.14) == "3.14s"

    def test_minutes_and_seconds(self):
        """Duration with minutes and seconds."""
        assert format_duration(125) == "2m 5s"

    def test_hours_minutes_seconds(self):
        """Duration with hours, minutes, and seconds."""
        assert format_duration(3661) == "1h 1m 1s"

    def test_days_hours_minutes_seconds(self):
        """Duration with days, hours, minutes, and seconds."""
        assert format_duration(90061) == "1d 1h 1m 1s"

    def test_only_days(self):
        """Duration with only complete days."""
        assert format_duration(172800) == "2d"

    def test_negative_duration(self):
        """Negative duration should be formatted with minus sign."""
        assert format_duration(-125) == "-2m 5s"

    def test_large_duration(self):
        """Large duration should be formatted correctly."""
        result = format_duration(259200)  # 3 days
        assert result == "3d"


class TestParseIsoDate:
    """Tests for parse_iso_date function."""

    def test_parse_date_only(self):
        """Parse ISO date without time."""
        result = parse_iso_date("2024-01-15")
        assert result == datetime(2024, 1, 15)

    def test_parse_datetime_with_time(self):
        """Parse ISO datetime with time."""
        result = parse_iso_date("2024-01-15T14:30:00")
        assert result == datetime(2024, 1, 15, 14, 30, 0)

    def test_parse_datetime_with_timezone(self):
        """Parse ISO datetime with timezone."""
        result = parse_iso_date("2024-01-15T14:30:00+00:00")
        expected = datetime(2024, 1, 15, 14, 30, 0, tzinfo=timezone.utc)
        assert result == expected

    def test_parse_datetime_with_microseconds(self):
        """Parse ISO datetime with microseconds."""
        result = parse_iso_date("2024-01-15T14:30:00.123456")
        assert result == datetime(2024, 1, 15, 14, 30, 0, 123456)

    def test_parse_leap_year_date(self):
        """Parse leap year date."""
        result = parse_iso_date("2024-02-29")
        assert result == datetime(2024, 2, 29)

    def test_parse_invalid_date_raises_error(self):
        """Invalid date string should raise ValueError."""
        with pytest.raises(ValueError, match="Invalid ISO date format"):
            parse_iso_date("not-a-date")

    def test_parse_invalid_month_raises_error(self):
        """Invalid month should raise ValueError."""
        with pytest.raises(ValueError, match="Invalid ISO date format"):
            parse_iso_date("2024-13-01")


class TestGetWeekRange:
    """Tests for get_week_range function."""

    def test_monday_gives_same_week(self):
        """Monday should return week starting from itself."""
        monday = date(2024, 1, 1)
        start, end = get_week_range(monday)
        assert start == date(2024, 1, 1)
        assert end == date(2024, 1, 7)

    def test_friday_gives_week_starting_monday(self):
        """Friday should return week starting from previous Monday."""
        friday = date(2024, 1, 5)
        start, end = get_week_range(friday)
        assert start == date(2024, 1, 1)
        assert end == date(2024, 1, 7)

    def test_sunday_gives_week_starting_monday(self):
        """Sunday should return week starting from previous Monday."""
        sunday = date(2024, 1, 7)
        start, end = get_week_range(sunday)
        assert start == date(2024, 1, 1)
        assert end == date(2024, 1, 7)

    def test_week_range_across_month_boundary(self):
        """Week range should work across month boundaries."""
        jan_31 = date(2024, 1, 31)  # Wednesday
        start, end = get_week_range(jan_31)
        assert start == date(2024, 1, 29)  # Previous Monday
        assert end == date(2024, 2, 4)  # Next Sunday

    def test_week_range_across_year_boundary(self):
        """Week range should work across year boundaries."""
        jan_1 = date(2024, 1, 1)  # Monday
        start, end = get_week_range(jan_1)
        assert start == date(2024, 1, 1)
        assert end == date(2024, 1, 7)


class TestDaysBetween:
    """Tests for days_between function."""

    def test_same_date_returns_zero(self):
        """Same start and end date should return 0."""
        dt = date(2024, 1, 1)
        assert days_between(dt, dt) == 0

    def test_consecutive_days(self):
        """Consecutive days should return 1."""
        start = date(2024, 1, 1)
        end = date(2024, 1, 2)
        assert days_between(start, end) == 1

    def test_one_week_apart(self):
        """Dates one week apart should return 7."""
        start = date(2024, 1, 1)
        end = date(2024, 1, 8)
        assert days_between(start, end) == 7

    def test_negative_days_when_end_before_start(self):
        """Should return negative days when end is before start."""
        start = date(2024, 1, 8)
        end = date(2024, 1, 1)
        assert days_between(start, end) == -7

    def test_include_end_date_positive(self):
        """Including end date should add 1 to positive result."""
        start = date(2024, 1, 1)
        end = date(2024, 1, 5)
        assert days_between(start, end, include_end=True) == 5

    def test_include_end_date_negative(self):
        """Including end date should subtract 1 from negative result."""
        start = date(2024, 1, 5)
        end = date(2024, 1, 1)
        assert days_between(start, end, include_end=True) == -5

    def test_same_date_include_end(self):
        """Same date with include_end should return 1."""
        dt = date(2024, 1, 1)
        assert days_between(dt, dt, include_end=True) == 1

    def test_across_month_boundary(self):
        """Days between should work across month boundaries."""
        start = date(2024, 1, 25)
        end = date(2024, 2, 5)
        assert days_between(start, end) == 11

    def test_across_year_boundary(self):
        """Days between should work across year boundaries."""
        start = date(2023, 12, 25)
        end = date(2024, 1, 5)
        assert days_between(start, end) == 11

    def test_leap_year_february(self):
        """Days between should handle leap year February correctly."""
        start = date(2024, 2, 28)
        end = date(2024, 3, 1)
        assert days_between(start, end) == 2  # Feb 28 -> Feb 29 -> Mar 1
