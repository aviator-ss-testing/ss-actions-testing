"""
Pytest configuration and common fixtures for testing.
"""

import pytest
import tempfile
import os
from datetime import datetime
from typing import Dict, List, Any


@pytest.fixture
def sample_strings():
    """Fixture providing sample strings for testing string functions."""
    return [
        "hello",
        "Hello World",
        "  whitespace test  ",
        "",
        "123",
        "MixedCase",
        "   multiple   spaces   ",
    ]


@pytest.fixture
def sample_numbers():
    """Fixture providing sample numbers for testing numeric functions."""
    return [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 100, 1000]


@pytest.fixture
def sample_lists():
    """Fixture providing sample lists for testing list processing functions."""
    return [
        [],
        [1, 2, 3],
        [1, 2, 2, 3, 3, 3],
        [[1, 2], [3, 4], [5]],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        ["a", "b", "c"],
        [1, "mixed", 3.14, True],
    ]


@pytest.fixture
def sample_json_data():
    """Fixture providing sample JSON data for testing JSON functions."""
    return {
        "valid_json": '{"name": "test", "value": 42}',
        "invalid_json": '{"name": "test", "value":}',
        "nested_json": '{"user": {"name": "Alice", "settings": {"theme": "dark"}}}',
        "array_json": '[1, 2, 3, "test"]',
        "empty_json": "{}",
    }


@pytest.fixture
def sample_csv_data():
    """Fixture providing sample CSV data for testing CSV functions."""
    return {
        "simple": "name,age,city\nAlice,30,NYC\nBob,25,LA",
        "with_quotes": 'name,description\nAlice,"Software Engineer, Python"\nBob,"Data Scientist"',
        "empty": "",
        "headers_only": "name,age,city",
        "single_row": "name,age,city\nAlice,30,NYC",
    }


@pytest.fixture
def sample_dictionaries():
    """Fixture providing sample dictionaries for testing dict functions."""
    return {
        "dict1": {"a": 1, "b": 2, "nested": {"x": 10}},
        "dict2": {"b": 3, "c": 4, "nested": {"y": 20}},
        "empty": {},
        "complex": {
            "users": [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}],
            "settings": {"theme": "dark", "language": "en"},
            "metadata": {"version": "1.0", "created": "2023-01-01"},
        },
    }


@pytest.fixture
def temp_file():
    """Fixture providing a temporary file for testing file operations."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
        yield f.name
    os.unlink(f.name)


@pytest.fixture
def mock_datetime():
    """Fixture providing a mock datetime for consistent testing."""
    return datetime(2023, 1, 15, 12, 30, 45)


@pytest.fixture
def test_data_dir(tmp_path):
    """Fixture providing a temporary directory for test data."""
    test_dir = tmp_path / "test_data"
    test_dir.mkdir()
    return test_dir


@pytest.fixture(autouse=True)
def reset_logging():
    """Fixture to reset logging configuration between tests."""
    import logging
    yield
    # Clear any handlers that might have been added during tests
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)


@pytest.fixture
def capture_function_calls():
    """Fixture to capture and track function calls for decorator testing."""
    calls = []

    def record_call(func_name, args, kwargs, result=None, error=None):
        calls.append({
            'function': func_name,
            'args': args,
            'kwargs': kwargs,
            'result': result,
            'error': error,
            'timestamp': datetime.now()
        })

    return calls, record_call


# Test configuration helpers
class TestConfig:
    """Configuration class for test settings."""

    TIMEOUT_SECONDS = 5
    MAX_RETRIES = 3
    TEST_DATA_SIZE = 1000


@pytest.fixture
def test_config():
    """Fixture providing test configuration."""
    return TestConfig()