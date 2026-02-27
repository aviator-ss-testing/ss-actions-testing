"""Tests for the stats module."""

import math
import pytest
from stats import mean, median, mode, stdev


# --- mean ---

def test_mean_basic():
    assert mean([1.0, 2.0, 3.0]) == 2.0


def test_mean_single():
    assert mean([5.0]) == 5.0


def test_mean_negatives():
    assert mean([-1.0, 1.0]) == 0.0


def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])


# --- median ---

def test_median_odd_length():
    assert median([3.0, 1.0, 2.0]) == 2.0


def test_median_even_length():
    assert median([1.0, 2.0, 3.0, 4.0]) == 2.5


def test_median_single():
    assert median([7.0]) == 7.0


def test_median_already_sorted():
    assert median([1.0, 2.0, 3.0]) == 2.0


def test_median_empty():
    with pytest.raises(ValueError):
        median([])


# --- mode ---

def test_mode_single_mode():
    assert mode([1.0, 2.0, 2.0, 3.0]) == 2.0


def test_mode_tie_returns_smallest():
    assert mode([1.0, 1.0, 2.0, 2.0]) == 1.0


def test_mode_all_unique():
    assert mode([3.0, 1.0, 2.0]) == 1.0


def test_mode_single():
    assert mode([4.0]) == 4.0


def test_mode_empty():
    with pytest.raises(ValueError):
        mode([])


# --- stdev ---

def test_stdev_basic():
    result = stdev([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0])
    assert math.isclose(result, 2.138089935299395, rel_tol=1e-9)


def test_stdev_two_values():
    result = stdev([1.0, 3.0])
    assert math.isclose(result, math.sqrt(2.0), rel_tol=1e-9)


def test_stdev_identical_values():
    assert stdev([5.0, 5.0, 5.0]) == 0.0


def test_stdev_single_value():
    with pytest.raises(ValueError):
        stdev([1.0])


def test_stdev_empty():
    with pytest.raises(ValueError):
        stdev([])
