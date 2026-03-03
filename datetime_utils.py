"""Datetime utility functions for common temporal operations."""

from datetime import datetime, timedelta, date, timezone
from typing import Optional, Tuple


def is_business_day(dt: date) -> bool:
    """
    Check if a given date is a business day (Monday-Friday).

    Args:
        dt: The date to check

    Returns:
        True if the date is a business day (Mon-Fri), False otherwise
    """
    return dt.weekday() < 5


def add_business_days(start_date: date, days: int) -> date:
    """
    Add business days to a date, skipping weekends.

    Args:
        start_date: The starting date
        days: Number of business days to add (can be negative)

    Returns:
        The resulting date after adding business days
    """
    current = start_date
    remaining = abs(days)
    direction = 1 if days >= 0 else -1

    while remaining > 0:
        current += timedelta(days=direction)
        if is_business_day(current):
            remaining -= 1

    return current


def format_duration(seconds: float) -> str:
    """
    Format a duration in seconds to a human-readable string.

    Args:
        seconds: Duration in seconds

    Returns:
        Formatted string like "2d 3h 45m 30s"
    """
    if seconds < 0:
        return f"-{format_duration(-seconds)}"

    if seconds == 0:
        return "0s"

    parts = []

    days = int(seconds // 86400)
    if days > 0:
        parts.append(f"{days}d")
        seconds %= 86400

    hours = int(seconds // 3600)
    if hours > 0:
        parts.append(f"{hours}h")
        seconds %= 3600

    minutes = int(seconds // 60)
    if minutes > 0:
        parts.append(f"{minutes}m")
        seconds %= 60

    if seconds > 0:
        if seconds == int(seconds):
            parts.append(f"{int(seconds)}s")
        else:
            parts.append(f"{seconds:.2f}s")

    return " ".join(parts)


def parse_iso_date(date_string: str) -> datetime:
    """
    Parse an ISO 8601 formatted date string.

    Args:
        date_string: ISO 8601 formatted date string

    Returns:
        datetime object

    Raises:
        ValueError: If the date string is invalid
    """
    try:
        return datetime.fromisoformat(date_string)
    except ValueError as e:
        raise ValueError(f"Invalid ISO date format: {date_string}") from e


def get_week_range(dt: date) -> Tuple[date, date]:
    """
    Get the start (Monday) and end (Sunday) dates of the week containing the given date.

    Args:
        dt: The date to get the week range for

    Returns:
        Tuple of (week_start, week_end) as date objects
    """
    start = dt - timedelta(days=dt.weekday())
    end = start + timedelta(days=6)
    return (start, end)


def days_between(start: date, end: date, include_end: bool = False) -> int:
    """
    Calculate the number of days between two dates.

    Args:
        start: The start date
        end: The end date
        include_end: If True, include the end date in the count

    Returns:
        Number of days between the dates (can be negative if end < start)
    """
    delta = (end - start).days
    if include_end and delta >= 0:
        delta += 1
    elif include_end and delta < 0:
        delta -= 1
    return delta
