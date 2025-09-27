"""
Comprehensive tests for basic_math module.

This module tests all mathematical operations with edge cases,
error conditions, and parametrized scenarios.
"""

import math
import pytest
from src.basic_math import add, subtract, multiply, divide, power, factorial


class TestAdd:
    """Test cases for the add function."""

    @pytest.mark.parametrize("a, b, expected", [
        # Basic integer addition
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (-5, -3, -8),
        (100, 200, 300),

        # Float addition
        (1.5, 2.5, 4.0),
        (0.1, 0.2, 0.3),
        (-1.5, 1.5, 0.0),
        (3.14, 2.86, 6.0),

        # Mixed int and float
        (1, 2.5, 3.5),
        (2.5, 1, 3.5),
        (-1, 1.5, 0.5),

        # Large numbers
        (1000000, 2000000, 3000000),
        (1e10, 2e10, 3e10),

        # Very small numbers
        (1e-10, 2e-10, 3e-10),
    ])
    def test_add_valid_inputs(self, a, b, expected):
        """Test add function with valid inputs."""
        result = add(a, b)
        if isinstance(expected, float):
            assert abs(result - expected) < 1e-10
        else:
            assert result == expected

    @pytest.mark.parametrize("a, b", [
        ("1", 2),
        (1, "2"),
        ("1", "2"),
        (None, 1),
        (1, None),
        ([], 1),
        ({}, 1),
        (complex(1, 1), 2),
    ])
    def test_add_invalid_types(self, a, b):
        """Test add function with invalid input types."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            add(a, b)


class TestSubtract:
    """Test cases for the subtract function."""

    @pytest.mark.parametrize("a, b, expected", [
        # Basic integer subtraction
        (5, 3, 2),
        (0, 0, 0),
        (-1, 1, -2),
        (-5, -3, -2),
        (100, 200, -100),

        # Float subtraction
        (5.5, 2.5, 3.0),
        (0.3, 0.1, 0.2),
        (-1.5, 1.5, -3.0),
        (10.0, 3.14, 6.86),

        # Mixed int and float
        (5, 2.5, 2.5),
        (5.5, 2, 3.5),
        (-1, 1.5, -2.5),

        # Large numbers
        (3000000, 1000000, 2000000),
        (3e10, 1e10, 2e10),

        # Very small numbers
        (3e-10, 1e-10, 2e-10),
    ])
    def test_subtract_valid_inputs(self, a, b, expected):
        """Test subtract function with valid inputs."""
        result = subtract(a, b)
        if isinstance(expected, float):
            assert abs(result - expected) < 1e-10
        else:
            assert result == expected

    @pytest.mark.parametrize("a, b", [
        ("5", 2),
        (5, "2"),
        ("5", "2"),
        (None, 5),
        (5, None),
        ([], 5),
        ({}, 5),
        (complex(5, 1), 2),
    ])
    def test_subtract_invalid_types(self, a, b):
        """Test subtract function with invalid input types."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            subtract(a, b)


class TestMultiply:
    """Test cases for the multiply function."""

    @pytest.mark.parametrize("a, b, expected", [
        # Basic integer multiplication
        (3, 4, 12),
        (0, 5, 0),
        (5, 0, 0),
        (-3, 4, -12),
        (-3, -4, 12),
        (1, 100, 100),

        # Float multiplication
        (2.5, 4.0, 10.0),
        (0.5, 0.5, 0.25),
        (-2.5, 4.0, -10.0),
        (-2.5, -4.0, 10.0),
        (3.14, 2.0, 6.28),

        # Mixed int and float
        (3, 2.5, 7.5),
        (2.5, 3, 7.5),
        (-3, 2.5, -7.5),

        # Large numbers
        (1000, 2000, 2000000),
        (1e5, 2e5, 2e10),

        # Very small numbers
        (1e-5, 2e-5, 2e-10),
        (0.001, 0.001, 0.000001),
    ])
    def test_multiply_valid_inputs(self, a, b, expected):
        """Test multiply function with valid inputs."""
        result = multiply(a, b)
        if isinstance(expected, float):
            assert abs(result - expected) < 1e-10
        else:
            assert result == expected

    @pytest.mark.parametrize("a, b", [
        ("3", 4),
        (3, "4"),
        ("3", "4"),
        (None, 3),
        (3, None),
        ([], 3),
        ({}, 3),
        (complex(3, 1), 4),
    ])
    def test_multiply_invalid_types(self, a, b):
        """Test multiply function with invalid input types."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(a, b)


class TestDivide:
    """Test cases for the divide function."""

    @pytest.mark.parametrize("a, b, expected", [
        # Basic division
        (10, 2, 5.0),
        (15, 3, 5.0),
        (7, 2, 3.5),
        (-10, 2, -5.0),
        (10, -2, -5.0),
        (-10, -2, 5.0),

        # Float division
        (10.0, 2.0, 5.0),
        (7.5, 2.5, 3.0),
        (1.0, 3.0, 1/3),

        # Mixed int and float
        (10, 2.0, 5.0),
        (10.0, 2, 5.0),
        (7, 2.0, 3.5),

        # Division resulting in repeating decimals
        (1, 3, 1/3),
        (2, 3, 2/3),
        (22, 7, 22/7),

        # Large numbers
        (1000000, 1000, 1000.0),
        (1e10, 1e5, 1e5),

        # Very small numbers
        (1e-10, 1e-5, 1e-5),
        (0.001, 0.01, 0.1),
    ])
    def test_divide_valid_inputs(self, a, b, expected):
        """Test divide function with valid inputs."""
        result = divide(a, b)
        assert abs(result - expected) < 1e-10

    def test_divide_by_zero(self):
        """Test division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(10, 0)

        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(10.5, 0.0)

        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(-10, 0)

    @pytest.mark.parametrize("a, b", [
        ("10", 2),
        (10, "2"),
        ("10", "2"),
        (None, 10),
        (10, None),
        ([], 10),
        ({}, 10),
        (complex(10, 1), 2),
    ])
    def test_divide_invalid_types(self, a, b):
        """Test divide function with invalid input types."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            divide(a, b)


class TestPower:
    """Test cases for the power function."""

    @pytest.mark.parametrize("base, exponent, expected", [
        # Basic integer powers
        (2, 3, 8),
        (3, 2, 9),
        (5, 0, 1),
        (0, 5, 0),
        (1, 100, 1),
        (-2, 3, -8),
        (-2, 2, 4),

        # Negative exponents
        (2, -1, 0.5),
        (4, -2, 0.0625),
        (10, -3, 0.001),

        # Float powers
        (2.0, 3.0, 8.0),
        (4.0, 0.5, 2.0),
        (9.0, 0.5, 3.0),
        (8.0, 1/3, 2.0),

        # Mixed int and float
        (2, 3.0, 8.0),
        (2.0, 3, 8.0),
        (4, 0.5, 2.0),

        # Edge cases
        (0, 0, 1),  # By mathematical convention
        (-1, 2, 1),
        (-1, 3, -1),

        # Large numbers
        (10, 6, 1000000),
        (2, 10, 1024),
    ])
    def test_power_valid_inputs(self, base, exponent, expected):
        """Test power function with valid inputs."""
        result = power(base, exponent)
        if isinstance(expected, float):
            assert abs(result - expected) < 1e-10
        else:
            assert result == expected

    def test_power_invalid_operations(self):
        """Test power function with operations that should raise ValueError."""
        # Negative base with fractional exponent
        with pytest.raises(ValueError, match="Invalid power operation"):
            power(-2, 0.5)

        with pytest.raises(ValueError, match="Invalid power operation"):
            power(-4, 1/3)

    @pytest.mark.parametrize("base, exponent", [
        ("2", 3),
        (2, "3"),
        ("2", "3"),
        (None, 2),
        (2, None),
        ([], 2),
        ({}, 2),
        (complex(2, 1), 3),
    ])
    def test_power_invalid_types(self, base, exponent):
        """Test power function with invalid input types."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power(base, exponent)


class TestFactorial:
    """Test cases for the factorial function."""

    @pytest.mark.parametrize("n, expected", [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (10, 3628800),
        (12, 479001600),
    ])
    def test_factorial_valid_inputs(self, n, expected):
        """Test factorial function with valid inputs."""
        assert factorial(n) == expected

    def test_factorial_large_numbers(self):
        """Test factorial with larger numbers."""
        # Test that it matches Python's math.factorial
        for n in [15, 20, 25, 30]:
            assert factorial(n) == math.factorial(n)

    def test_factorial_negative_input(self):
        """Test factorial with negative input raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-1)

        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-5)

        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-100)

    @pytest.mark.parametrize("n", [
        3.5,
        2.0,
        "5",
        None,
        [],
        {},
        complex(5, 0),
    ])
    def test_factorial_invalid_types(self, n):
        """Test factorial function with invalid input types."""
        with pytest.raises(TypeError, match="Factorial input must be an integer"):
            factorial(n)


class TestEdgeCasesAndIntegration:
    """Test edge cases and integration scenarios."""

    def test_floating_point_precision(self):
        """Test that floating point operations handle precision correctly."""
        # Test known precision issues
        result = add(0.1, 0.2)
        assert abs(result - 0.3) < 1e-10

        result = subtract(1.0, 0.9)
        assert abs(result - 0.1) < 1e-10

        result = multiply(0.1, 3)
        assert abs(result - 0.3) < 1e-10

    def test_very_large_numbers(self):
        """Test operations with very large numbers."""
        large_num = 10**100

        assert add(large_num, 1) == large_num + 1
        assert subtract(large_num, 1) == large_num - 1
        assert multiply(large_num, 2) == large_num * 2
        assert divide(large_num, 2) == large_num / 2

    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        small_num = 10**-100

        result = add(small_num, small_num)
        assert result == 2 * small_num

        result = multiply(small_num, 2)
        assert result == 2 * small_num

    def test_mixed_operation_chains(self):
        """Test chaining different operations together."""
        # (2 + 3) * 4 / 2 - 1 = 9
        result = subtract(divide(multiply(add(2, 3), 4), 2), 1)
        assert result == 9.0

        # 2^3 + 3! - 5 = 8 + 6 - 5 = 9
        result = subtract(add(power(2, 3), factorial(3)), 5)
        assert result == 9

    def test_type_preservation(self):
        """Test that return types are preserved correctly."""
        # Integer operations should return integers when appropriate
        assert isinstance(add(1, 2), int)
        assert isinstance(subtract(5, 3), int)
        assert isinstance(multiply(2, 3), int)
        assert isinstance(power(2, 3), int)
        assert isinstance(factorial(5), int)

        # Float operations should return floats
        assert isinstance(add(1.0, 2.0), float)
        assert isinstance(subtract(5.0, 3.0), float)
        assert isinstance(multiply(2.0, 3.0), float)
        assert isinstance(divide(6, 2), float)  # divide always returns float
        assert isinstance(power(2.0, 3.0), float)

        # Mixed operations should return appropriate type
        assert isinstance(add(1, 2.0), float)
        assert isinstance(subtract(5, 3.0), float)
        assert isinstance(multiply(2, 3.0), float)