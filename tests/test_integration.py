"""
Integration tests that demonstrate how functions work together with decorators.

This module contains end-to-end test scenarios that combine multiple functions
with various decorators to validate complex behaviors and interactions.
"""

import pytest
import time
import json
import logging
from datetime import datetime, timezone, timedelta
from io import StringIO
from typing import List, Dict, Any
from unittest.mock import patch, MagicMock

from utils import (
    reverse_string, capitalize_words, clean_whitespace,
    fibonacci, factorial, is_prime,
    flatten_list, unique_elements, filter_even
)
from decorators import (
    timing, retry, cache, validate, validate_types,
    log_calls, simple_log
)
from data_processing import (
    parse_json_string, validate_json_schema, json_to_string,
    parse_csv_string, format_as_csv, deep_merge,
    filter_keys, transform_values, format_datetime,
    parse_datetime_string
)


class TestEndToEndScenarios:
    """Test scenarios that combine multiple functions across modules."""

    def test_data_pipeline_with_decorators(self):
        """Test a complete data processing pipeline with multiple decorators."""

        @timing
        @cache(maxsize=10)
        @validate_types(data=str)
        def process_user_data(data: str) -> Dict[str, Any]:
            """Process user data through multiple transformation steps."""
            # Parse JSON
            parsed = parse_json_string(data)

            # Validate required fields
            if not validate_json_schema(parsed, ['users']):
                raise ValueError("Invalid data schema")

            # Process each user
            processed_users = []
            for user in parsed['users']:
                # Clean and capitalize names
                if 'name' in user:
                    user['name'] = capitalize_words(clean_whitespace(user['name']))

                # Add processed flag
                user['processed'] = True
                processed_users.append(user)

            return {'processed_users': processed_users, 'count': len(processed_users)}

        # Test data
        test_data = json.dumps({
            'users': [
                {'name': '  john   doe  ', 'age': 30},
                {'name': 'jane  smith', 'age': 25}
            ]
        })

        # First call - should be slow and cached
        result1 = process_user_data(test_data)

        # Second call - should be fast due to caching
        result2 = process_user_data(test_data)

        # Verify results are identical
        assert result1 == result2
        assert result1['count'] == 2
        assert result1['processed_users'][0]['name'] == 'John Doe'
        assert result1['processed_users'][1]['name'] == 'Jane Smith'
        assert all(user['processed'] for user in result1['processed_users'])

    def test_mathematical_operations_with_retry_and_validation(self):
        """Test mathematical operations with retry logic and validation."""

        # Validation functions
        def is_non_negative(x):
            return isinstance(x, int) and x >= 0

        def is_reasonable_size(x):
            return x <= 20  # Prevent huge calculations

        @retry(max_attempts=3, delay=0.1)
        @validate(is_non_negative, is_reasonable_size)
        @timing
        def calculate_fibonacci_factorial(n: int) -> Dict[str, int]:
            """Calculate both fibonacci and factorial with validation."""
            # Simulate occasional failure for retry testing
            import random
            if random.random() < 0.3:  # 30% failure rate
                raise ValueError("Simulated calculation error")

            fib = fibonacci(n)
            fact = factorial(n)

            return {
                'input': n,
                'fibonacci': fib,
                'factorial': fact,
                'is_prime': is_prime(fib) if fib > 1 else False
            }

        # Test with valid input
        with patch('random.random', return_value=0.5):  # Force success
            result = calculate_fibonacci_factorial(5)
            assert result['input'] == 5
            assert result['fibonacci'] == 5
            assert result['factorial'] == 120
            assert result['is_prime'] == True  # 5 is prime

        # Test validation failure
        with pytest.raises(ValueError, match="Argument 0 failed validation"):
            calculate_fibonacci_factorial(-1)

        with pytest.raises(ValueError, match="Argument 0 failed validation"):
            calculate_fibonacci_factorial(25)

    def test_list_processing_chain_with_logging(self):
        """Test chained list processing operations with comprehensive logging."""

        @simple_log("List Processing")
        @validate_types(data=list)
        def process_nested_numbers(data: List[Any]) -> Dict[str, Any]:
            """Process nested list through multiple transformations."""
            # Flatten nested structure
            flattened = flatten_list(data)

            # Filter to get only even numbers
            even_numbers = filter_even(flattened)

            # Get unique elements
            unique_evens = unique_elements(even_numbers)

            # Calculate some statistics
            total = sum(unique_evens) if unique_evens else 0
            count = len(unique_evens)
            average = total / count if count > 0 else 0

            return {
                'original_structure': data,
                'flattened': flattened,
                'even_numbers': even_numbers,
                'unique_evens': unique_evens,
                'statistics': {
                    'total': total,
                    'count': count,
                    'average': average
                }
            }

        # Test with nested list containing duplicates
        test_data = [1, [2, 3, 4], [4, 5, [6, 7, 8]], 2, 6]

        # Capture print output to verify logging
        with patch('builtins.print') as mock_print:
            result = process_nested_numbers(test_data)

            # Verify function was called and completed
            assert mock_print.call_count >= 2  # At least call and completion logs

            # Verify processing results
            assert result['flattened'] == [1, 2, 3, 4, 4, 5, 6, 7, 8, 2, 6]
            assert result['even_numbers'] == [2, 4, 4, 6, 8, 2, 6]
            assert result['unique_evens'] == [2, 4, 6, 8]
            assert result['statistics']['total'] == 20
            assert result['statistics']['count'] == 4
            assert result['statistics']['average'] == 5.0

    def test_csv_json_conversion_pipeline(self):
        """Test data format conversion between CSV and JSON with transformations."""

        @cache(maxsize=5)
        @timing
        def csv_to_json_processor(csv_data: str) -> str:
            """Convert CSV to JSON with data transformations."""
            # Parse CSV
            parsed_data = parse_csv_string(csv_data)

            # Transform data: capitalize names, convert ages to integers
            for row in parsed_data:
                if 'name' in row:
                    row['name'] = capitalize_words(row['name'])
                if 'age' in row:
                    try:
                        row['age'] = int(row['age'])
                    except ValueError:
                        row['age'] = 0  # Default for invalid ages

            # Group by age ranges
            age_groups = {}
            for row in parsed_data:
                age = row.get('age', 0)
                if age < 30:
                    group = 'young'
                elif age < 60:
                    group = 'middle'
                else:
                    group = 'senior'

                if group not in age_groups:
                    age_groups[group] = []
                age_groups[group].append(row)

            result = {
                'total_records': len(parsed_data),
                'age_groups': age_groups,
                'processed_at': format_datetime(datetime.now())
            }

            return json_to_string(result, indent=2)

        # Test CSV data
        csv_data = """name,age,city
john doe,25,new york
jane smith,35,san francisco
bob johnson,65,chicago
alice brown,22,boston"""

        # Process data
        result_json = csv_to_json_processor(csv_data)
        parsed_result = parse_json_string(result_json)

        # Verify structure and transformations
        assert parsed_result['total_records'] == 4
        assert len(parsed_result['age_groups']) == 3
        assert 'young' in parsed_result['age_groups']
        assert 'middle' in parsed_result['age_groups']
        assert 'senior' in parsed_result['age_groups']

        # Verify name capitalization
        young_users = parsed_result['age_groups']['young']
        assert any(user['name'] == 'John Doe' for user in young_users)
        assert any(user['name'] == 'Alice Brown' for user in young_users)

    def test_error_handling_across_modules(self):
        """Test error handling and recovery across different modules."""

        @retry(max_attempts=2, delay=0.1, exceptions=(ValueError, TypeError))
        @validate_types(input_data=str)
        def robust_data_processor(input_data: str) -> Dict[str, Any]:
            """Process data with comprehensive error handling."""
            try:
                # Try to parse as JSON first
                data = parse_json_string(input_data)
                return {'format': 'json', 'data': data, 'success': True}

            except ValueError:
                # If JSON parsing fails, try CSV
                try:
                    data = parse_csv_string(input_data)
                    return {'format': 'csv', 'data': data, 'success': True}

                except Exception:
                    # If both fail, treat as plain text and process words
                    words = input_data.split()
                    processed_words = [capitalize_words(clean_whitespace(word)) for word in words]
                    return {'format': 'text', 'data': processed_words, 'success': True}

        # Test JSON input
        json_input = '{"message": "hello world"}'
        result = robust_data_processor(json_input)
        assert result['format'] == 'json'
        assert result['data']['message'] == 'hello world'

        # Test CSV input
        csv_input = "name,value\njohn,123\njane,456"
        result = robust_data_processor(csv_input)
        assert result['format'] == 'csv'
        assert len(result['data']) == 2

        # Test plain text input
        text_input = "hello world from python"
        result = robust_data_processor(text_input)
        assert result['format'] == 'text'
        assert 'Hello' in result['data']


class TestDecoratorComposition:
    """Test decorator composition and chaining behaviors."""

    def test_multiple_decorator_stacking(self):
        """Test function with multiple stacked decorators."""

        def is_string(x):
            return isinstance(x, str)

        def not_empty(x):
            return len(x) > 0

        @simple_log("String Processing")
        @timing
        @cache(maxsize=3)
        @validate(is_string, not_empty)
        @validate_types(text=str)
        def complex_string_processor(text: str) -> Dict[str, str]:
            """Apply multiple string transformations with full decorator stack."""
            # Simulate some processing time
            time.sleep(0.01)

            return {
                'original': text,
                'reversed': reverse_string(text),
                'capitalized': capitalize_words(text),
                'cleaned': clean_whitespace(text),
                'length': len(text)
            }

        # Test with valid input
        with patch('builtins.print'):  # Suppress log output
            result = complex_string_processor("  hello   world  ")

            assert result['original'] == "  hello   world  "
            assert result['reversed'] == "  dlrow   olleh  "
            assert result['capitalized'] == "Hello World"
            assert result['cleaned'] == "hello world"
            assert result['length'] == 15

        # Test validation failure
        with pytest.raises(TypeError):
            complex_string_processor(123)  # Wrong type

        with pytest.raises(ValueError):
            complex_string_processor("")  # Empty string

    def test_decorator_order_dependency(self):
        """Test that decorator order affects behavior correctly."""

        call_log = []

        def logging_decorator(name):
            def decorator(func):
                def wrapper(*args, **kwargs):
                    call_log.append(f"Before {name}")
                    result = func(*args, **kwargs)
                    call_log.append(f"After {name}")
                    return result
                return wrapper
            return decorator

        @logging_decorator("Outer")
        @logging_decorator("Middle")
        @logging_decorator("Inner")
        def test_function(x):
            call_log.append(f"Executing with {x}")
            return x * 2

        # Clear log and execute
        call_log.clear()
        result = test_function(5)

        # Verify execution order
        expected_order = [
            "Before Outer",
            "Before Middle",
            "Before Inner",
            "Executing with 5",
            "After Inner",
            "After Middle",
            "After Outer"
        ]

        assert call_log == expected_order
        assert result == 10

    def test_cache_with_timing_composition(self):
        """Test cache and timing decorators working together."""

        @timing
        @cache(maxsize=2)
        def expensive_computation(n: int) -> int:
            """Simulate expensive computation that should be cached."""
            time.sleep(0.05)  # Simulate work
            return fibonacci(n) + factorial(min(n, 10))  # Prevent huge factorials

        # Capture timing output
        with patch('builtins.print') as mock_print:
            # First call - should be slow
            result1 = expensive_computation(8)

            # Second call - should be fast (cached)
            result2 = expensive_computation(8)

            # Third call with different input - should be slow
            result3 = expensive_computation(7)

            # Fourth call - should reuse cache
            result4 = expensive_computation(7)

            # Verify results are correct
            assert result1 == result2 == fibonacci(8) + factorial(8)
            assert result3 == result4 == fibonacci(7) + factorial(7)

            # Verify timing decorator was called for each execution
            assert mock_print.call_count >= 4  # At least 4 timing prints


class TestPerformanceBenchmarking:
    """Performance benchmarking tests using the timing decorator."""

    def test_string_operations_performance(self):
        """Benchmark string operations with different input sizes."""

        @timing
        def string_benchmark(text: str, operations: int = 100) -> Dict[str, Any]:
            """Perform multiple string operations for benchmarking."""
            results = []

            for _ in range(operations):
                # Chain multiple string operations
                processed = clean_whitespace(text)
                processed = capitalize_words(processed)
                processed = reverse_string(processed)
                results.append(processed)

            return {
                'operations_count': operations,
                'final_length': len(results[-1]),
                'unique_results': len(set(results))
            }

        # Test with different input sizes
        small_text = "hello world"
        large_text = " ".join(["word"] * 100)

        with patch('builtins.print'):  # Suppress timing output
            small_result = string_benchmark(small_text, 50)
            large_result = string_benchmark(large_text, 50)

            assert small_result['operations_count'] == 50
            assert large_result['operations_count'] == 50
            assert large_result['final_length'] > small_result['final_length']

    def test_mathematical_operations_scaling(self):
        """Test mathematical operations performance scaling."""

        @timing
        @cache(maxsize=20)
        def math_benchmark(max_n: int) -> Dict[str, Any]:
            """Benchmark mathematical operations up to max_n."""
            fibonacci_results = []
            factorial_results = []
            prime_count = 0

            for i in range(max_n):
                fib = fibonacci(i)
                fibonacci_results.append(fib)

                if i <= 10:  # Prevent huge factorials
                    fact = factorial(i)
                    factorial_results.append(fact)

                if is_prime(i):
                    prime_count += 1

            return {
                'max_n': max_n,
                'fibonacci_sum': sum(fibonacci_results),
                'factorial_sum': sum(factorial_results),
                'prime_count': prime_count
            }

        with patch('builtins.print'):  # Suppress timing output
            # Test with different scales
            small_result = math_benchmark(15)
            medium_result = math_benchmark(25)

            assert small_result['max_n'] == 15
            assert medium_result['max_n'] == 25
            assert medium_result['fibonacci_sum'] > small_result['fibonacci_sum']
            assert medium_result['prime_count'] >= small_result['prime_count']

    def test_data_processing_throughput(self):
        """Test data processing throughput with various data sizes."""

        @timing
        def data_throughput_test(record_count: int) -> Dict[str, Any]:
            """Test data processing throughput."""
            # Generate test data
            test_records = []
            for i in range(record_count):
                test_records.append({
                    'id': i,
                    'name': f'user {i}',
                    'data': [j for j in range(i % 10)],
                    'metadata': {'created': str(datetime.now())}
                })

            # Process data through multiple transformations
            processed = []
            for record in test_records:
                # Transform the record
                transformed = {
                    'id': record['id'],
                    'name': capitalize_words(record['name']),
                    'data_length': len(flatten_list([record['data']])),
                    'has_metadata': 'metadata' in record
                }
                processed.append(transformed)

            # Group results
            groups = {}
            for item in processed:
                key = 'small' if item['data_length'] < 5 else 'large'
                if key not in groups:
                    groups[key] = []
                groups[key].append(item)

            return {
                'total_records': record_count,
                'processed_count': len(processed),
                'groups': {k: len(v) for k, v in groups.items()}
            }

        with patch('builtins.print'):  # Suppress timing output
            # Test different throughput levels
            result_100 = data_throughput_test(100)
            result_500 = data_throughput_test(500)

            assert result_100['total_records'] == 100
            assert result_500['total_records'] == 500
            assert result_100['processed_count'] == result_100['total_records']
            assert result_500['processed_count'] == result_500['total_records']

    def test_decorator_overhead_measurement(self):
        """Measure the overhead introduced by different decorators."""

        def baseline_function(n: int) -> int:
            """Baseline function without decorators."""
            return sum(range(n))

        @timing
        def timing_only_function(n: int) -> int:
            """Function with only timing decorator."""
            return sum(range(n))

        @timing
        @cache(maxsize=10)
        def cached_function(n: int) -> int:
            """Function with timing and cache decorators."""
            return sum(range(n))

        @timing
        @validate_types(n=int)
        @cache(maxsize=10)
        def fully_decorated_function(n: int) -> int:
            """Function with multiple decorators."""
            return sum(range(n))

        test_input = 1000

        with patch('builtins.print'):  # Suppress timing output
            # Test each version
            baseline_result = baseline_function(test_input)
            timing_result = timing_only_function(test_input)
            cached_result = cached_function(test_input)
            decorated_result = fully_decorated_function(test_input)

            # All should produce same mathematical result
            expected = sum(range(test_input))
            assert baseline_result == expected
            assert timing_result == expected
            assert cached_result == expected
            assert decorated_result == expected

            # Test cache effectiveness on second call
            cached_result2 = cached_function(test_input)
            decorated_result2 = fully_decorated_function(test_input)

            assert cached_result2 == expected
            assert decorated_result2 == expected


class TestComplexIntegrationScenarios:
    """Complex integration scenarios combining all modules."""

    def test_full_application_simulation(self):
        """Simulate a complete application workflow."""

        # Configuration processing
        @validate_types(config_json=str)
        @cache(maxsize=1)
        def load_config(config_json: str) -> Dict[str, Any]:
            """Load and validate application configuration."""
            config = parse_json_string(config_json)

            # Validate required configuration keys
            required_keys = ['database', 'api', 'features']
            if not validate_json_schema(config, required_keys):
                raise ValueError("Invalid configuration schema")

            return config

        # User data processing
        @retry(max_attempts=2)
        @timing
        @log_calls(level=logging.INFO)
        def process_user_batch(users_csv: str, config: Dict[str, Any]) -> Dict[str, Any]:
            """Process a batch of users according to configuration."""
            # Parse user data
            users = parse_csv_string(users_csv)

            # Process each user based on config
            processed_users = []
            for user in users:
                processed_user = {
                    'id': user.get('id', ''),
                    'name': capitalize_words(clean_whitespace(user.get('name', ''))),
                    'email': user.get('email', '').lower().strip(),
                    'active': user.get('active', 'true').lower() == 'true'
                }

                # Apply feature flags from config
                if config['features'].get('add_timestamps', False):
                    processed_user['processed_at'] = format_datetime(datetime.now())

                if config['features'].get('calculate_name_stats', False):
                    name = processed_user['name']
                    processed_user['name_stats'] = {
                        'length': len(name),
                        'word_count': len(name.split()),
                        'reversed': reverse_string(name)
                    }

                processed_users.append(processed_user)

            return {
                'total_processed': len(processed_users),
                'users': processed_users,
                'config_version': config.get('version', '1.0')
            }

        # Test the complete workflow
        config_json = json.dumps({
            'version': '2.0',
            'database': {'host': 'localhost', 'port': 5432},
            'api': {'timeout': 30, 'retries': 3},
            'features': {
                'add_timestamps': True,
                'calculate_name_stats': True
            }
        })

        users_csv = """id,name,email,active
1,  john doe  ,John.Doe@Example.Com,true
2,jane   smith,jane@test.org,false
3,bob johnson,bob@work.net,true"""

        # Setup logging to capture log_calls output
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        with patch('builtins.print'):  # Suppress timing output
            # Load configuration
            config = load_config(config_json)
            assert config['version'] == '2.0'

            # Process users
            result = process_user_batch(users_csv, config)

            # Verify processing results
            assert result['total_processed'] == 3
            assert result['config_version'] == '2.0'

            # Check user processing
            users = result['users']

            # Verify name cleaning and capitalization
            assert users[0]['name'] == 'John Doe'
            assert users[1]['name'] == 'Jane Smith'
            assert users[2]['name'] == 'Bob Johnson'

            # Verify email processing
            assert users[0]['email'] == 'john.doe@example.com'

            # Verify feature flags were applied
            assert 'processed_at' in users[0]
            assert 'name_stats' in users[0]
            assert users[0]['name_stats']['length'] == 8  # "John Doe"
            assert users[0]['name_stats']['word_count'] == 2
            assert users[0]['name_stats']['reversed'] == 'eoD nhoJ'

    def test_data_pipeline_error_recovery(self):
        """Test comprehensive error recovery in data processing pipeline."""

        # Simulate unreliable external service
        call_count = 0

        @retry(max_attempts=3, delay=0.1, exceptions=(ValueError, ConnectionError))
        @timing
        def unreliable_external_service(data: str) -> Dict[str, Any]:
            """Simulate an external service that sometimes fails."""
            nonlocal call_count
            call_count += 1

            # Fail on first two attempts, succeed on third
            if call_count < 3:
                raise ConnectionError(f"Service unavailable (attempt {call_count})")

            # Process the data when service is "available"
            parsed = parse_json_string(data)

            # Transform data
            if 'items' in parsed:
                for item in parsed['items']:
                    if 'values' in item:
                        item['values'] = unique_elements(item['values'])
                        item['even_values'] = filter_even(item['values'])
                        item['stats'] = {
                            'count': len(item['values']),
                            'even_count': len(item['even_values']),
                            'total': sum(item['values']) if item['values'] else 0
                        }

            return parsed

        # Main processing function with error handling
        @simple_log("Data Pipeline")
        def robust_data_pipeline(json_data: str) -> Dict[str, Any]:
            """Process data through unreliable external service with recovery."""
            try:
                # Reset call count for test
                nonlocal call_count
                call_count = 0

                # Try processing through external service
                processed_data = unreliable_external_service(json_data)

                return {
                    'status': 'success',
                    'data': processed_data,
                    'service_calls': call_count,
                    'fallback_used': False
                }

            except (ValueError, ConnectionError) as e:
                # Fallback to local processing
                try:
                    fallback_data = parse_json_string(json_data)

                    # Simple local processing
                    if 'items' in fallback_data:
                        for item in fallback_data['items']:
                            item['processed_locally'] = True
                            if 'name' in item:
                                item['name'] = capitalize_words(item['name'])

                    return {
                        'status': 'success_with_fallback',
                        'data': fallback_data,
                        'service_calls': call_count,
                        'fallback_used': True,
                        'error': str(e)
                    }

                except Exception as fallback_error:
                    return {
                        'status': 'error',
                        'service_calls': call_count,
                        'fallback_used': True,
                        'error': str(fallback_error)
                    }

        # Test data
        test_data = json.dumps({
            'items': [
                {
                    'name': 'item one',
                    'values': [1, 2, 3, 2, 4, 5, 4, 6]
                },
                {
                    'name': 'item two',
                    'values': [7, 8, 9, 8, 10, 11]
                }
            ]
        })

        with patch('builtins.print'):  # Suppress log output
            result = robust_data_pipeline(test_data)

            # Should eventually succeed after retries
            assert result['status'] == 'success'
            assert result['service_calls'] == 3  # Failed twice, succeeded on third
            assert result['fallback_used'] == False

            # Verify data processing
            items = result['data']['items']
            assert len(items) == 2

            # Check first item processing
            item1 = items[0]
            assert item1['values'] == [1, 2, 3, 4, 5, 6]  # unique elements
            assert item1['even_values'] == [2, 4, 6]
            assert item1['stats']['count'] == 6
            assert item1['stats']['even_count'] == 3
            assert item1['stats']['total'] == 21