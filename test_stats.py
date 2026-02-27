"""Tests for the stats module."""

import math
import pytest
from stats import mean, median, mode, stdev


# mean

def test_mean_basic():
    assert mean([1, 2, 3, 4, 5]) == 3.0


def test_mean_floats():
    assert math.isclose(mean([1.5, 2.5, 3.0]), 7.0 / 3)


def test_mean_single():
    assert mean([42.0]) == 42.0


def test_mean_negative():
    assert mean([-1, -2, -3]) == -2.0


def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])


# median

def test_median_odd():
    assert median([3, 1, 2]) == 2.0


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


def test_median_single():
    assert median([7.0]) == 7.0


def test_median_already_sorted():
    assert median([10, 20, 30]) == 20.0


def test_median_empty():
    with pytest.raises(ValueError):
        median([])


# mode

def test_mode_basic():
    assert mode([1, 2, 2, 3]) == 2.0


def test_mode_tie_returns_smallest():
    assert mode([1, 1, 2, 2]) == 1.0


def test_mode_single():
    assert mode([5.0]) == 5.0


def test_mode_all_unique_returns_smallest():
    assert mode([3, 1, 2]) == 1.0


def test_mode_empty():
    with pytest.raises(ValueError):
        mode([])


# stdev

def test_stdev_basic():
    assert math.isclose(stdev([2, 4, 4, 4, 5, 5, 7, 9]), 2.1380899352993946)


def test_stdev_two_values():
    assert math.isclose(stdev([0, 2]), math.sqrt(2))


def test_stdev_identical_values():
    assert stdev([5, 5, 5]) == 0.0


def test_stdev_single_value():
    with pytest.raises(ValueError):
        stdev([1.0])


def test_stdev_empty():
    with pytest.raises(ValueError):
        stdev([])
