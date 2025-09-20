"""
Data processing module with JSON, CSV, dictionary, and datetime utilities.
Provides functions for common data processing tasks without external dependencies.
"""

import json
import csv
from io import StringIO
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Any, Union, Optional, Callable


def parse_json_string(json_str: str) -> Any:
    """Parse a JSON string and return the parsed object.

    Args:
        json_str: JSON string to parse

    Returns:
        Parsed JSON object

    Raises:
        ValueError: If JSON string is invalid
    """
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON string: {e}")


def validate_json_schema(data: Any, required_keys: List[str]) -> bool:
    """Validate that a data structure contains all required keys.

    Args:
        data: Data structure to validate (typically a dict)
        required_keys: List of required keys

    Returns:
        True if all required keys are present, False otherwise
    """
    if not isinstance(data, dict):
        return False

    return all(key in data for key in required_keys)


def json_to_string(data: Any, indent: Optional[int] = None) -> str:
    """Convert a Python object to a JSON string.

    Args:
        data: Object to convert to JSON
        indent: Optional indentation for pretty printing

    Returns:
        JSON string representation
    """
    try:
        return json.dumps(data, indent=indent, ensure_ascii=False)
    except TypeError as e:
        raise ValueError(f"Object is not JSON serializable: {e}")


def extract_json_values(data: Dict[str, Any], path: str) -> Any:
    """Extract values from nested JSON using dot notation path.

    Args:
        data: Dictionary to extract from
        path: Dot-separated path (e.g., 'user.profile.name')

    Returns:
        Value at the specified path or None if not found
    """
    keys = path.split('.')
    current = data

    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None

    return current


def parse_csv_string(csv_string: str, delimiter: str = ',', header: bool = True) -> List[Dict[str, str]]:
    """Parse a CSV string into a list of dictionaries.

    Args:
        csv_string: CSV data as string
        delimiter: Field delimiter (default: comma)
        header: Whether first row contains headers

    Returns:
        List of dictionaries representing CSV rows
    """
    reader = csv.DictReader(StringIO(csv_string), delimiter=delimiter)

    if not header:
        fieldnames = [f'col_{i}' for i in range(len(csv_string.split('\n')[0].split(delimiter)))]
        reader.fieldnames = fieldnames

    return list(reader)


def format_as_csv(data: List[Dict[str, Any]], delimiter: str = ',') -> str:
    """Format a list of dictionaries as CSV string.

    Args:
        data: List of dictionaries to format
        delimiter: Field delimiter (default: comma)

    Returns:
        CSV formatted string
    """
    if not data:
        return ""

    output = StringIO()
    fieldnames = list(data[0].keys())
    writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=delimiter)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

    return output.getvalue()


def csv_column_stats(csv_string: str, column_name: str, delimiter: str = ',') -> Dict[str, Union[int, float]]:
    """Calculate basic statistics for a numeric column in CSV data.

    Args:
        csv_string: CSV data as string
        column_name: Name of column to analyze
        delimiter: Field delimiter

    Returns:
        Dictionary with count, sum, mean, min, max statistics
    """
    data = parse_csv_string(csv_string, delimiter)
    values = []

    for row in data:
        if column_name in row:
            try:
                values.append(float(row[column_name]))
            except (ValueError, TypeError):
                continue

    if not values:
        return {'count': 0, 'sum': 0, 'mean': 0, 'min': 0, 'max': 0}

    return {
        'count': len(values),
        'sum': sum(values),
        'mean': sum(values) / len(values),
        'min': min(values),
        'max': max(values)
    }


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries.

    Args:
        dict1: First dictionary
        dict2: Second dictionary (takes precedence)

    Returns:
        Merged dictionary
    """
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value

    return result


def filter_keys(data: Dict[str, Any], predicate: Callable[[str], bool]) -> Dict[str, Any]:
    """Filter dictionary keys based on a predicate function.

    Args:
        data: Dictionary to filter
        predicate: Function that returns True for keys to keep

    Returns:
        New dictionary with filtered keys
    """
    return {k: v for k, v in data.items() if predicate(k)}


def transform_values(data: Dict[str, Any], transformer: Callable[[Any], Any]) -> Dict[str, Any]:
    """Transform all values in a dictionary using a function.

    Args:
        data: Dictionary to transform
        transformer: Function to apply to each value

    Returns:
        New dictionary with transformed values
    """
    return {k: transformer(v) for k, v in data.items()}


def flatten_dict(data: Dict[str, Any], separator: str = '.') -> Dict[str, Any]:
    """Flatten a nested dictionary using separator notation.

    Args:
        data: Dictionary to flatten
        separator: Separator for nested keys

    Returns:
        Flattened dictionary
    """
    def _flatten(obj: Any, parent_key: str = '') -> Dict[str, Any]:
        items = []
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_key = f"{parent_key}{separator}{key}" if parent_key else key
                items.extend(_flatten(value, new_key).items())
        else:
            return {parent_key: obj}
        return dict(items)

    return _flatten(data)


def group_by_key(data: List[Dict[str, Any]], key: str) -> Dict[str, List[Dict[str, Any]]]:
    """Group a list of dictionaries by a specific key.

    Args:
        data: List of dictionaries to group
        key: Key to group by

    Returns:
        Dictionary with grouped results
    """
    groups = {}
    for item in data:
        if key in item:
            group_key = str(item[key])
            if group_key not in groups:
                groups[group_key] = []
            groups[group_key].append(item)
    return groups


def format_datetime(dt: datetime, format_string: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format a datetime object as a string.

    Args:
        dt: Datetime object to format
        format_string: Format string (default: ISO-like format)

    Returns:
        Formatted datetime string
    """
    return dt.strftime(format_string)


def parse_datetime_string(date_string: str, format_string: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """Parse a datetime string into a datetime object.

    Args:
        date_string: String to parse
        format_string: Expected format of the string

    Returns:
        Parsed datetime object

    Raises:
        ValueError: If string doesn't match format
    """
    try:
        return datetime.strptime(date_string, format_string)
    except ValueError as e:
        raise ValueError(f"Invalid datetime format: {e}")


def add_business_days(start_date: datetime, days: int) -> datetime:
    """Add business days (Monday-Friday) to a date.

    Args:
        start_date: Starting date
        days: Number of business days to add

    Returns:
        New datetime with business days added
    """
    current_date = start_date
    days_added = 0

    while days_added < days:
        current_date += timedelta(days=1)
        if current_date.weekday() < 5:  # Monday = 0, Friday = 4
            days_added += 1

    return current_date


def calculate_age_in_years(birth_date: datetime, reference_date: Optional[datetime] = None) -> int:
    """Calculate age in years from birth date.

    Args:
        birth_date: Date of birth
        reference_date: Date to calculate age from (default: current date)

    Returns:
        Age in years
    """
    if reference_date is None:
        reference_date = datetime.now()

    age = reference_date.year - birth_date.year

    # Adjust if birthday hasn't occurred yet this year
    if (reference_date.month, reference_date.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


def get_date_range(start_date: datetime, end_date: datetime, step_days: int = 1) -> List[datetime]:
    """Generate a list of dates between start and end dates.

    Args:
        start_date: Starting date
        end_date: Ending date
        step_days: Number of days between each date

    Returns:
        List of datetime objects
    """
    dates = []
    current_date = start_date

    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=step_days)

    return dates


def is_weekend(date: datetime) -> bool:
    """Check if a date falls on a weekend.

    Args:
        date: Date to check

    Returns:
        True if Saturday or Sunday, False otherwise
    """
    return date.weekday() >= 5  # Saturday = 5, Sunday = 6


def get_month_boundaries(date: datetime) -> tuple[datetime, datetime]:
    """Get the first and last day of the month for a given date.

    Args:
        date: Date to get month boundaries for

    Returns:
        Tuple of (first_day, last_day) of the month
    """
    first_day = date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    # Get first day of next month, then subtract one day
    if date.month == 12:
        next_month = date.replace(year=date.year + 1, month=1, day=1)
    else:
        next_month = date.replace(month=date.month + 1, day=1)

    last_day = next_month - timedelta(days=1)
    last_day = last_day.replace(hour=23, minute=59, second=59, microsecond=999999)

    return first_day, last_day


def convert_timezone(dt: datetime, from_tz: timezone, to_tz: timezone) -> datetime:
    """Convert datetime from one timezone to another.

    Args:
        dt: Datetime to convert (assumed to be in from_tz if naive)
        from_tz: Source timezone
        to_tz: Target timezone

    Returns:
        Datetime converted to target timezone
    """
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=from_tz)

    return dt.astimezone(to_tz)