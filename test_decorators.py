import time
import pytest
from io import StringIO
import sys
from decorators import timer, memoize, repeat


class TestTimerDecorator:
    def test_timer_prints_timing_info(self, capsys):
        @timer
        def sample_function():
            time.sleep(0.1)
            return "result"

        result = sample_function()
        captured = capsys.readouterr()

        assert result == "result"
        assert "Function 'sample_function' took" in captured.out
        assert "seconds" in captured.out

    def test_timer_with_arguments(self, capsys):
        @timer
        def add_numbers(a, b):
            return a + b

        result = add_numbers(3, 5)
        captured = capsys.readouterr()

        assert result == 8
        assert "Function 'add_numbers' took" in captured.out

    def test_timer_with_keyword_arguments(self, capsys):
        @timer
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}"

        result = greet("Alice", greeting="Hi")
        captured = capsys.readouterr()

        assert result == "Hi, Alice"
        assert "Function 'greet' took" in captured.out

    def test_timer_preserves_function_name(self):
        @timer
        def my_function():
            pass

        assert my_function.__name__ == "my_function"

    def test_timer_with_different_return_types(self, capsys):
        @timer
        def return_list():
            return [1, 2, 3]

        @timer
        def return_dict():
            return {"key": "value"}

        @timer
        def return_none():
            pass

        assert return_list() == [1, 2, 3]
        assert return_dict() == {"key": "value"}
        assert return_none() is None

        captured = capsys.readouterr()
        assert captured.out.count("took") == 3


class TestMemoizeDecorator:
    def test_memoize_caches_results(self):
        call_count = {"count": 0}

        @memoize
        def expensive_function(n):
            call_count["count"] += 1
            return n * 2

        result1 = expensive_function(5)
        result2 = expensive_function(5)
        result3 = expensive_function(5)

        assert result1 == 10
        assert result2 == 10
        assert result3 == 10
        assert call_count["count"] == 1

    def test_memoize_different_arguments(self):
        call_count = {"count": 0}

        @memoize
        def compute(x):
            call_count["count"] += 1
            return x ** 2

        result1 = compute(3)
        result2 = compute(4)
        result3 = compute(3)
        result4 = compute(4)

        assert result1 == 9
        assert result2 == 16
        assert result3 == 9
        assert result4 == 16
        assert call_count["count"] == 2

    def test_memoize_with_multiple_arguments(self):
        call_count = {"count": 0}

        @memoize
        def multiply(a, b):
            call_count["count"] += 1
            return a * b

        result1 = multiply(3, 4)
        result2 = multiply(3, 4)
        result3 = multiply(4, 3)

        assert result1 == 12
        assert result2 == 12
        assert result3 == 12
        assert call_count["count"] == 2

    def test_memoize_with_keyword_arguments(self):
        call_count = {"count": 0}

        @memoize
        def concat(a, b="default"):
            call_count["count"] += 1
            return f"{a}-{b}"

        result1 = concat("test", b="value")
        result2 = concat("test", b="value")
        result3 = concat("test", b="other")

        assert result1 == "test-value"
        assert result2 == "test-value"
        assert result3 == "test-other"
        assert call_count["count"] == 2

    def test_memoize_preserves_function_name(self):
        @memoize
        def my_function():
            pass

        assert my_function.__name__ == "my_function"

    def test_memoize_with_different_return_types(self):
        call_count = {"count": 0}

        @memoize
        def get_data(key):
            call_count["count"] += 1
            if key == "list":
                return [1, 2, 3]
            elif key == "dict":
                return {"a": 1}
            else:
                return None

        assert get_data("list") == [1, 2, 3]
        assert get_data("list") == [1, 2, 3]
        assert get_data("dict") == {"a": 1}
        assert get_data("dict") == {"a": 1}
        assert get_data("other") is None
        assert get_data("other") is None

        assert call_count["count"] == 3


class TestRepeatDecorator:
    def test_repeat_zero_times(self):
        @repeat(0)
        def get_value():
            return 42

        result = get_value()
        assert result == []

    def test_repeat_once(self):
        @repeat(1)
        def get_value():
            return 42

        result = get_value()
        assert result == [42]

    def test_repeat_multiple_times(self):
        @repeat(5)
        def get_value():
            return "test"

        result = get_value()
        assert result == ["test", "test", "test", "test", "test"]
        assert len(result) == 5

    def test_repeat_with_arguments(self):
        @repeat(3)
        def add(a, b):
            return a + b

        result = add(2, 3)
        assert result == [5, 5, 5]

    def test_repeat_with_keyword_arguments(self):
        @repeat(2)
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}"

        result = greet("Alice", greeting="Hi")
        assert result == ["Hi, Alice", "Hi, Alice"]

    def test_repeat_execution_count(self):
        call_count = {"count": 0}

        @repeat(4)
        def increment():
            call_count["count"] += 1
            return call_count["count"]

        result = increment()
        assert result == [1, 2, 3, 4]
        assert call_count["count"] == 4

    def test_repeat_preserves_function_name(self):
        @repeat(3)
        def my_function():
            pass

        assert my_function.__name__ == "my_function"

    def test_repeat_with_different_return_types(self):
        @repeat(2)
        def return_list():
            return [1, 2]

        @repeat(2)
        def return_dict():
            return {"key": "value"}

        @repeat(2)
        def return_none():
            pass

        assert return_list() == [[1, 2], [1, 2]]
        assert return_dict() == [{"key": "value"}, {"key": "value"}]
        assert return_none() == [None, None]

    def test_repeat_with_varying_results(self):
        counter = {"value": 0}

        @repeat(3)
        def increment_and_return():
            counter["value"] += 1
            return counter["value"]

        result = increment_and_return()
        assert result == [1, 2, 3]


class TestDecoratorCombinations:
    def test_timer_with_memoize(self, capsys):
        @timer
        @memoize
        def compute(x):
            time.sleep(0.05)
            return x * 2

        result1 = compute(5)
        captured1 = capsys.readouterr()

        result2 = compute(5)
        captured2 = capsys.readouterr()

        assert result1 == 10
        assert result2 == 10
        assert "Function 'compute' took" in captured1.out
        assert "Function 'compute' took" in captured2.out

    def test_repeat_with_timer(self, capsys):
        @repeat(2)
        @timer
        def simple_function():
            return "value"

        result = simple_function()
        captured = capsys.readouterr()

        assert result == ["value", "value"]
        assert captured.out.count("took") == 2
