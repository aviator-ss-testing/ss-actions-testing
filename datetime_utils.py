"""Utility functions for common datetime and temporal operations."""

from datetime import date, datetime, timedelta, timezone
from typing import Optional, Tuple, Union


def is_business_day(d: Union[date, datetime]) -> bool:
    """Return True if the given date falls on a weekday (Monday–Friday).

    Args:
        d: A :class:`datetime.date` or :class:`datetime.datetime` instance.

    Returns:
        True if *d* is Monday through Friday, False for Saturday or Sunday.

    Raises:
        TypeError: If *d* is not a :class:`datetime.date` or
            :class:`datetime.datetime`.
    """
    if not isinstance(d, date):
        raise TypeError(f"Expected date or datetime, got {type(d).__name__}")
    return d.weekday() < 5


def add_business_days(d: Union[date, datetime], days: int) -> Union[date, datetime]:
    """Add a number of business days (Mon–Fri) to a date.

    Negative values move the date backwards.

    Args:
        d: The starting :class:`datetime.date` or :class:`datetime.datetime`.
        days: Number of business days to add (may be negative).

    Returns:
        A new :class:`datetime.date` (or :class:`datetime.datetime` if a
        datetime was passed) offset by *days* business days.

    Raises:
        TypeError: If *d* is not a date/datetime or *days* is not an int.
    """
    if not isinstance(d, date):
        raise TypeError(f"Expected date or datetime, got {type(d).__name__}")
    if not isinstance(days, int) or isinstance(days, bool):
        raise TypeError(f"days must be an int, got {type(days).__name__}")

    step = 1 if days >= 0 else -1
    remaining = abs(days)
    current = d
    while remaining > 0:
        current = current + timedelta(days=step)
        if current.weekday() < 5:
            remaining -= 1
    return current


def format_duration(duration: Union[timedelta, int, float]) -> str:
    """Format a duration into a human-readable string.

    Accepts a :class:`datetime.timedelta`, or a numeric value representing
    total seconds.  The result is expressed in the largest applicable units
    down to seconds (days, hours, minutes, seconds).  Fractional seconds are
    truncated.

    Examples::

        format_duration(timedelta(seconds=3661))  # "1 hour, 1 minute, 1 second"
        format_duration(90061)                     # "1 day, 1 hour, 1 minute, 1 second"

    Args:
        duration: A :class:`datetime.timedelta` or numeric total seconds.

    Returns:
        A human-readable string such as ``"2 days, 3 hours, 4 minutes, 5 seconds"``,
        or ``"0 seconds"`` for a zero-length duration.

    Raises:
        TypeError: If *duration* is not a timedelta, int, or float.
        ValueError: If *duration* represents a negative number of total seconds.
    """
    if isinstance(duration, bool):
        raise TypeError(f"Expected timedelta or numeric, got {type(duration).__name__}")
    if isinstance(duration, timedelta):
        total_seconds = int(duration.total_seconds())
    elif isinstance(duration, (int, float)):
        total_seconds = int(duration)
    else:
        raise TypeError(f"Expected timedelta or numeric, got {type(duration).__name__}")

    if total_seconds < 0:
        raise ValueError("duration must be non-negative")

    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    parts = []
    if days:
        parts.append(f"{days} day" if days == 1 else f"{days} days")
    if hours:
        parts.append(f"{hours} hour" if hours == 1 else f"{hours} hours")
    if minutes:
        parts.append(f"{minutes} minute" if minutes == 1 else f"{minutes} minutes")
    if seconds or not parts:
        parts.append(f"{seconds} second" if seconds == 1 else f"{seconds} seconds")

    return ", ".join(parts)


def parse_iso_date(date_str: str) -> Union[date, datetime]:
    """Parse an ISO 8601 date or datetime string.

    Supported formats:

    * ``YYYY-MM-DD`` → returns a :class:`datetime.date`
    * ``YYYY-MM-DDTHH:MM:SS`` → returns a naive :class:`datetime.datetime`
    * ``YYYY-MM-DDTHH:MM:SS+HH:MM`` / ``...Z`` → returns a timezone-aware
      :class:`datetime.datetime`

    Args:
        date_str: An ISO 8601 formatted date or datetime string.

    Returns:
        A :class:`datetime.date` for date-only strings, or a
        :class:`datetime.datetime` (naive or aware) for datetime strings.

    Raises:
        TypeError: If *date_str* is not a str.
        ValueError: If *date_str* cannot be parsed as an ISO 8601 date or
            datetime.
    """
    if not isinstance(date_str, str):
        raise TypeError(f"Expected str, got {type(date_str).__name__}")

    date_str = date_str.strip()

    if "T" not in date_str and " " not in date_str:
        try:
            return date.fromisoformat(date_str)
        except ValueError:
            raise ValueError(f"Invalid ISO date string: {date_str!r}")

    normalized = date_str
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"

    try:
        return datetime.fromisoformat(normalized)
    except ValueError:
        raise ValueError(f"Invalid ISO datetime string: {date_str!r}")


def get_week_range(d: Union[date, datetime]) -> Tuple[date, date]:
    """Return the Monday and Sunday bounding the ISO week that contains *d*.

    Args:
        d: A :class:`datetime.date` or :class:`datetime.datetime`.

    Returns:
        A tuple ``(monday, sunday)`` of :class:`datetime.date` objects
        representing the first and last day of *d*'s ISO week.

    Raises:
        TypeError: If *d* is not a date or datetime.
    """
    if not isinstance(d, date):
        raise TypeError(f"Expected date or datetime, got {type(d).__name__}")

    day = d.date() if isinstance(d, datetime) else d
    monday = day - timedelta(days=day.weekday())
    sunday = monday + timedelta(days=6)
    return monday, sunday


def days_between(
    d1: Union[date, datetime],
    d2: Union[date, datetime],
    absolute: bool = True,
) -> int:
    """Return the number of days between two dates.

    When both arguments are timezone-aware :class:`datetime.datetime` objects,
    the comparison accounts for timezone offsets.  A naive datetime and a
    timezone-aware datetime cannot be compared directly; pass *date* objects or
    ensure both datetimes share the same awareness.

    Args:
        d1: The first date or datetime.
        d2: The second date or datetime.
        absolute: If True (default), return the absolute difference so the
            argument order does not matter.  If False, return ``d2 - d1``,
            which may be negative.

    Returns:
        The number of whole days between *d1* and *d2*.

    Raises:
        TypeError: If *d1* or *d2* is not a date or datetime, or if one is
            timezone-aware and the other is not.
        ValueError: If a timezone-aware and timezone-naive datetime are mixed.
    """
    if not isinstance(d1, date):
        raise TypeError(f"Expected date or datetime for d1, got {type(d1).__name__}")
    if not isinstance(d2, date):
        raise TypeError(f"Expected date or datetime for d2, got {type(d2).__name__}")

    both_datetime = isinstance(d1, datetime) and isinstance(d2, datetime)

    if both_datetime:
        aware1 = d1.tzinfo is not None and d1.tzinfo.utcoffset(d1) is not None
        aware2 = d2.tzinfo is not None and d2.tzinfo.utcoffset(d2) is not None
        if aware1 != aware2:
            raise ValueError(
                "Cannot mix timezone-aware and timezone-naive datetimes"
            )
        delta = d2 - d1
    else:
        date1 = d1.date() if isinstance(d1, datetime) else d1
        date2 = d2.date() if isinstance(d2, datetime) else d2
        delta = date2 - date1

    diff = int(delta.total_seconds() // 86400)
    return abs(diff) if absolute else diff
