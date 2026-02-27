"""Tests for the stats module."""

import math
import pytest
from stats import mean, median, mode, stdev


def test_mean_basic():
    assert mean([1, 2, 3, 4, 5]) == 3.0


def test_mean_single():
    assert mean([7.0]) == 7.0


def test_mean_floats():
    assert mean([1.5, 2.5]) == 2.0


def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])


def test_median_odd():
    assert median([3, 1, 2]) == 2.0


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


def test_median_single():
    assert median([42.0]) == 42.0


def test_median_already_sorted():
    assert median([1, 3, 5]) == 3.0


def test_median_empty():
    with pytest.raises(ValueError):
        median([])


def test_mode_basic():
    assert mode([1, 2, 2, 3]) == 2.0


def test_mode_tie_returns_smallest():
    assert mode([1, 1, 2, 2, 3]) == 1.0


def test_mode_single():
    assert mode([5.0]) == 5.0


def test_mode_all_unique():
    assert mode([3, 1, 2]) == 1.0


def test_mode_empty():
    with pytest.raises(ValueError):
        mode([])


def test_stdev_basic():
    result = stdev([2, 4, 4, 4, 5, 5, 7, 9])
    assert math.isclose(result, 2.138089935299395, rel_tol=1e-9)


def test_stdev_two_values():
    result = stdev([1.0, 3.0])
    assert math.isclose(result, math.sqrt(2), rel_tol=1e-9)


def test_stdev_single():
    with pytest.raises(ValueError):
        stdev([1.0])


def test_stdev_empty():
    with pytest.raises(ValueError):
        stdev([])
