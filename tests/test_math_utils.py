"""Tests for mathematical utilities module."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from utils.math_utils import fibonacci, is_prime, factorial, gcd


class TestFibonacci:
    """Tests for fibonacci function."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (6, 8),
            (7, 13),
            (8, 21),
            (9, 34),
            (10, 55),
            (15, 610),
            (20, 6765),
            (25, 75025),
        ],
    )
    def test_fibonacci_valid_numbers(self, n, expected):
        """Test fibonacci with valid non-negative numbers."""
        assert fibonacci(n) == expected

    def test_fibonacci_zero(self):
        """Test fibonacci with zero returns 0."""
        assert fibonacci(0) == 0

    def test_fibonacci_one(self):
        """Test fibonacci with 1 returns 1."""
        assert fibonacci(1) == 1

    def test_fibonacci_larger_numbers(self):
        """Test fibonacci with larger numbers."""
        assert fibonacci(30) == 832040
        assert fibonacci(35) == 9227465

    @pytest.mark.parametrize(
        "n",
        [-1, -5, -10, -100],
    )
    def test_fibonacci_negative_raises_error(self, n):
        """Test fibonacci with negative numbers raises ValueError."""
        with pytest.raises(ValueError, match="n must be a non-negative integer"):
            fibonacci(n)


class TestIsPrime:
    """Tests for is_prime function."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (2, True),
            (3, True),
            (5, True),
            (7, True),
            (11, True),
            (13, True),
            (17, True),
            (19, True),
            (23, True),
            (29, True),
            (31, True),
            (37, True),
            (41, True),
            (43, True),
            (47, True),
            (97, True),
            (101, True),
        ],
    )
    def test_is_prime_with_primes(self, n, expected):
        """Test is_prime with actual prime numbers."""
        assert is_prime(n) == expected

    @pytest.mark.parametrize(
        "n,expected",
        [
            (4, False),
            (6, False),
            (8, False),
            (9, False),
            (10, False),
            (12, False),
            (15, False),
            (16, False),
            (20, False),
            (25, False),
            (27, False),
            (100, False),
            (121, False),
        ],
    )
    def test_is_prime_with_non_primes(self, n, expected):
        """Test is_prime with composite numbers."""
        assert is_prime(n) == expected

    def test_is_prime_zero(self):
        """Test is_prime with 0 returns False."""
        assert is_prime(0) is False

    def test_is_prime_one(self):
        """Test is_prime with 1 returns False."""
        assert is_prime(1) is False

    def test_is_prime_two(self):
        """Test is_prime with 2 returns True (smallest prime)."""
        assert is_prime(2) is True

    @pytest.mark.parametrize(
        "n",
        [-1, -2, -5, -10, -100],
    )
    def test_is_prime_negative_numbers(self, n):
        """Test is_prime with negative numbers returns False."""
        assert is_prime(n) is False

    def test_is_prime_large_primes(self):
        """Test is_prime with large prime numbers."""
        assert is_prime(997) is True
        assert is_prime(1009) is True
        assert is_prime(7919) is True

    def test_is_prime_large_composites(self):
        """Test is_prime with large composite numbers."""
        assert is_prime(1000) is False
        assert is_prime(9999) is False
        assert is_prime(10000) is False


class TestFactorial:
    """Tests for factorial function."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 1),
            (1, 1),
            (2, 2),
            (3, 6),
            (4, 24),
            (5, 120),
            (6, 720),
            (7, 5040),
            (8, 40320),
            (9, 362880),
            (10, 3628800),
        ],
    )
    def test_factorial_valid_numbers(self, n, expected):
        """Test factorial with valid non-negative numbers."""
        assert factorial(n) == expected

    def test_factorial_zero(self):
        """Test factorial of 0 returns 1 (mathematical convention)."""
        assert factorial(0) == 1

    def test_factorial_one(self):
        """Test factorial of 1 returns 1."""
        assert factorial(1) == 1

    def test_factorial_small_numbers(self):
        """Test factorial with small numbers."""
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24

    def test_factorial_larger_numbers(self):
        """Test factorial with larger numbers."""
        assert factorial(12) == 479001600
        assert factorial(15) == 1307674368000

    @pytest.mark.parametrize(
        "n",
        [-1, -2, -5, -10, -100],
    )
    def test_factorial_negative_raises_error(self, n):
        """Test factorial with negative numbers raises ValueError."""
        with pytest.raises(ValueError, match="n must be a non-negative integer"):
            factorial(n)


class TestGcd:
    """Tests for gcd function."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (48, 18, 6),
            (18, 48, 6),
            (100, 50, 50),
            (50, 100, 50),
            (17, 19, 1),
            (21, 14, 7),
            (14, 21, 7),
            (270, 192, 6),
            (1071, 462, 21),
            (15, 25, 5),
            (35, 49, 7),
            (12, 8, 4),
            (81, 57, 3),
        ],
    )
    def test_gcd_various_pairs(self, a, b, expected):
        """Test gcd with various number pairs."""
        assert gcd(a, b) == expected

    def test_gcd_with_zero(self):
        """Test gcd when one number is zero."""
        assert gcd(0, 5) == 5
        assert gcd(5, 0) == 5
        assert gcd(0, 0) == 0

    def test_gcd_same_numbers(self):
        """Test gcd with identical numbers."""
        assert gcd(7, 7) == 7
        assert gcd(100, 100) == 100
        assert gcd(1, 1) == 1

    def test_gcd_one_is_one(self):
        """Test gcd where one number is 1."""
        assert gcd(1, 5) == 1
        assert gcd(100, 1) == 1
        assert gcd(1, 999) == 1

    def test_gcd_coprime_numbers(self):
        """Test gcd with coprime numbers (gcd = 1)."""
        assert gcd(13, 17) == 1
        assert gcd(25, 36) == 1
        assert gcd(101, 103) == 1

    def test_gcd_with_negative_numbers(self):
        """Test gcd with negative numbers (should use absolute values)."""
        assert gcd(-48, 18) == 6
        assert gcd(48, -18) == 6
        assert gcd(-48, -18) == 6
        assert gcd(-100, 50) == 50
        assert gcd(-12, -8) == 4

    def test_gcd_large_numbers(self):
        """Test gcd with large numbers."""
        assert gcd(123456, 789012) == 12
        assert gcd(999999, 111111) == 111111
        assert gcd(1000000, 500000) == 500000

    def test_gcd_prime_numbers(self):
        """Test gcd with two prime numbers (should be 1)."""
        assert gcd(11, 13) == 1
        assert gcd(29, 31) == 1
        assert gcd(97, 101) == 1
