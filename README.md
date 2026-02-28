# ss-actions-testing

A Python utility library with modules covering common operations across strings, data structures, files, and dates.

## Available Modules

### `calculator.py`
Basic arithmetic operations: addition, subtraction, multiplication, and division.

### `string_utils.py`
Common string manipulation utilities:
- `is_palindrome()` — check if a string reads the same forwards and backwards
- `reverse_words()` — reverse the order of words in a string
- `camel_to_snake()` — convert camelCase to snake_case
- `snake_to_camel()` — convert snake_case to camelCase
- `count_vowels()` — count the number of vowels in a string
- `truncate_string()` — truncate a string to a maximum length with an optional suffix

### `data_utils.py`
Utilities for working with lists, dictionaries, and collections:
- `flatten_list()` — recursively flatten a nested list
- `chunk_list()` — split a list into fixed-size chunks
- `merge_dicts()` — merge multiple dictionaries, with later values taking precedence
- `find_duplicates()` — return a list of values that appear more than once
- `group_by()` — group list items by a key function
- `filter_none_values()` — remove keys with None values from a dictionary

### `file_utils.py`
Safe file operation and path manipulation utilities:
- `get_file_extension()` — extract the file extension from a path
- `sanitize_filename()` — remove unsafe characters from a filename
- `parse_csv_line()` — parse a single CSV line into a list of fields
- `format_file_size()` — format a byte count as a human-readable string
- `validate_path_safe()` — check that a path does not escape a given base directory
- `get_relative_path()` — compute the relative path from one location to another

### `datetime_utils.py`
Date and time helper functions for common temporal operations:
- `is_business_day()` — check whether a date falls on a weekday
- `add_business_days()` — advance a date by a number of business days
- `format_duration()` — format a number of seconds as a human-readable duration string
- `parse_iso_date()` — parse an ISO 8601 date string into a `date` object
- `get_week_range()` — return the Monday and Sunday bounding a given date's week
- `days_between()` — compute the number of days between two dates

## Running Tests

Install pytest if you haven't already:

```bash
pip install pytest
```

Run all tests:

```bash
pytest -v
```

Run tests for a specific module:

```bash
pytest test_string_utils.py -v
pytest test_data_utils.py -v
pytest test_file_utils.py -v
pytest test_datetime_utils.py -v
pytest test_calculator.py -v
```
