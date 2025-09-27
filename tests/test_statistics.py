"""
Comprehensive test suite for statistics module.

Tests all statistical functions including edge cases, error conditions,
and mathematical property validations.
"""

import pytest
import math
from src.statistics import (
    mean, median, mode, standard_deviation, variance,
    min_max, range_calc, percentile
)


class TestMean:
    """Test cases for mean function."""

    def test_mean_basic(self):
        assert mean([1, 2, 3, 4, 5]) == 3.0
        assert mean([10, 20, 30]) == 20.0

    def test_mean_single_element(self):
        assert mean([5]) == 5.0
        assert mean([42.5]) == 42.5

    def test_mean_floats(self):
        assert mean([1.5, 2.5, 3.5]) == 2.5
        assert abs(mean([0.1, 0.2, 0.3]) - 0.2) < 1e-10

    def test_mean_negative_numbers(self):
        assert mean([-1, -2, -3]) == -2.0
        assert mean([-5, 5]) == 0.0

    def test_mean_mixed_numbers(self):
        assert mean([1, 2.5, 3]) == 2.1666666666666665

    def test_mean_large_numbers(self):
        result = mean([1e10, 1e10, 1e10])
        assert result == 1e10

    def test_mean_empty_list(self):
        with pytest.raises(ValueError, match="Cannot calculate mean of empty list"):
            mean([])

    def test_mean_non_numeric(self):
        with pytest.raises(TypeError, match="All values must be numeric"):
            mean([1, 2, "3"])
        with pytest.raises(TypeError, match="All values must be numeric"):
            mean([1, None, 3])


class TestMedian:
    """Test cases for median function."""

    def test_median_odd_length(self):
        assert median([1, 2, 3]) == 2.0
        assert median([5, 1, 3, 9, 7]) == 5.0

    def test_median_even_length(self):
        assert median([1, 2, 3, 4]) == 2.5
        assert median([10, 20]) == 15.0

    def test_median_single_element(self):
        assert median([42]) == 42.0

    def test_median_unsorted_input(self):
        assert median([3, 1, 4, 1, 5]) == 3.0
        assert median([9, 2, 5, 7]) == 6.0

    def test_median_with_duplicates(self):
        assert median([1, 1, 2, 2]) == 1.5
        assert median([5, 5, 5]) == 5.0

    def test_median_negative_numbers(self):
        assert median([-3, -1, -2]) == -2.0
        assert median([-10, -20, -30, -40]) == -25.0

    def test_median_floats(self):
        assert median([1.1, 2.2, 3.3]) == 2.2

    def test_median_empty_list(self):
        with pytest.raises(ValueError, match="Cannot calculate median of empty list"):
            median([])

    def test_median_non_numeric(self):
        with pytest.raises(TypeError, match="All values must be numeric"):
            median([1, 2, "3"])


class TestMode:
    """Test cases for mode function."""

    def test_mode_single_mode(self):
        assert mode([1, 2, 2, 3]) == [2]
        assert mode([5, 5, 1, 2, 3]) == [5]

    def test_mode_multiple_modes(self):
        result = mode([1, 1, 2, 2, 3])
        assert sorted(result) == [1, 2]

    def test_mode_all_same(self):
        assert mode([5, 5, 5, 5]) == [5]

    def test_mode_all_unique(self):
        result = mode([1, 2, 3, 4])
        assert sorted(result) == [1, 2, 3, 4]

    def test_mode_single_element(self):
        assert mode([42]) == [42]

    def test_mode_with_floats(self):
        assert mode([1.5, 1.5, 2.0]) == [1.5]

    def test_mode_negative_numbers(self):
        assert mode([-1, -1, -2]) == [-1]

    def test_mode_empty_list(self):
        with pytest.raises(ValueError, match="Cannot calculate mode of empty list"):
            mode([])

    def test_mode_non_numeric(self):
        with pytest.raises(TypeError, match="All values must be numeric"):
            mode([1, 2, "3"])


class TestStandardDeviation:
    """Test cases for standard_deviation function."""

    def test_std_dev_population(self):
        result = standard_deviation([1, 2, 3, 4, 5], sample=False)
        expected = math.sqrt(2.0)
        assert abs(result - expected) < 1e-10

    def test_std_dev_sample(self):
        result = standard_deviation([1, 2, 3, 4, 5], sample=True)
        expected = math.sqrt(2.5)
        assert abs(result - expected) < 1e-10

    def test_std_dev_identical_values(self):
        assert standard_deviation([5, 5, 5, 5]) == 0.0
        assert standard_deviation([5, 5, 5, 5], sample=True) == 0.0

    def test_std_dev_two_values(self):
        result = standard_deviation([1, 3], sample=True)
        expected = math.sqrt(2.0)
        assert abs(result - expected) < 1e-10

    def test_std_dev_negative_numbers(self):
        result = standard_deviation([-2, -1, 0, 1, 2])
        expected = math.sqrt(2.0)
        assert abs(result - expected) < 1e-10

    def test_std_dev_single_element_population(self):
        assert standard_deviation([42]) == 0.0

    def test_std_dev_single_element_sample(self):
        with pytest.raises(ValueError, match="Sample standard deviation requires at least 2 values"):
            standard_deviation([42], sample=True)

    def test_std_dev_empty_list(self):
        with pytest.raises(ValueError, match="Cannot calculate standard deviation of empty list"):
            standard_deviation([])

    def test_std_dev_non_numeric(self):
        with pytest.raises(TypeError, match="All values must be numeric"):
            standard_deviation([1, 2, "3"])


class TestVariance:
    """Test cases for variance function."""

    def test_variance_population(self):
        result = variance([1, 2, 3, 4, 5], sample=False)
        expected = 2.0
        assert abs(result - expected) < 1e-10

    def test_variance_sample(self):
        result = variance([1, 2, 3, 4, 5], sample=True)
        expected = 2.5
        assert abs(result - expected) < 1e-10

    def test_variance_identical_values(self):
        assert variance([7, 7, 7]) == 0.0
        assert variance([7, 7, 7], sample=True) == 0.0

    def test_variance_std_dev_relationship(self):
        data = [1, 4, 7, 2, 8]
        var_pop = variance(data, sample=False)
        std_pop = standard_deviation(data, sample=False)
        assert abs(var_pop - std_pop ** 2) < 1e-10

        var_sample = variance(data, sample=True)
        std_sample = standard_deviation(data, sample=True)
        assert abs(var_sample - std_sample ** 2) < 1e-10

    def test_variance_single_element_population(self):
        assert variance([42]) == 0.0

    def test_variance_single_element_sample(self):
        with pytest.raises(ValueError, match="Sample variance requires at least 2 values"):
            variance([42], sample=True)

    def test_variance_empty_list(self):
        with pytest.raises(ValueError, match="Cannot calculate variance of empty list"):
            variance([])


class TestMinMax:
    """Test cases for min_max function."""

    def test_min_max_basic(self):
        assert min_max([1, 2, 3, 4, 5]) == (1, 5)
        assert min_max([10, 5, 8, 2, 15]) == (2, 15)

    def test_min_max_single_element(self):
        assert min_max([42]) == (42, 42)

    def test_min_max_identical_values(self):
        assert min_max([7, 7, 7]) == (7, 7)

    def test_min_max_negative_numbers(self):
        assert min_max([-5, -2, -8, -1]) == (-8, -1)
        assert min_max([-10, 0, 10]) == (-10, 10)

    def test_min_max_floats(self):
        assert min_max([1.5, 2.7, 0.3, 4.1]) == (0.3, 4.1)

    def test_min_max_empty_list(self):
        with pytest.raises(ValueError, match="Cannot find min/max of empty list"):
            min_max([])

    def test_min_max_non_numeric(self):
        with pytest.raises(TypeError, match="All values must be numeric"):
            min_max([1, 2, "3"])


class TestRangeCalc:
    """Test cases for range_calc function."""

    def test_range_calc_basic(self):
        assert range_calc([1, 2, 3, 4, 5]) == 4
        assert range_calc([10, 5, 15]) == 10

    def test_range_calc_single_element(self):
        assert range_calc([42]) == 0

    def test_range_calc_identical_values(self):
        assert range_calc([5, 5, 5]) == 0

    def test_range_calc_negative_numbers(self):
        assert range_calc([-10, -5, -15]) == 10
        assert range_calc([-5, 0, 5]) == 10

    def test_range_calc_floats(self):
        result = range_calc([1.1, 2.3, 0.7])
        expected = 2.3 - 0.7
        assert abs(result - expected) < 1e-10

    def test_range_calc_empty_list(self):
        with pytest.raises(ValueError, match="Cannot calculate range of empty list"):
            range_calc([])


class TestPercentile:
    """Test cases for percentile function."""

    def test_percentile_basic(self):
        data = [1, 2, 3, 4, 5]
        assert percentile(data, 0) == 1.0
        assert percentile(data, 100) == 5.0
        assert percentile(data, 50) == 3.0

    def test_percentile_25th_75th(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert percentile(data, 25) == 3.25
        assert percentile(data, 75) == 7.75

    def test_percentile_single_element(self):
        assert percentile([42], 50) == 42.0
        assert percentile([42], 0) == 42.0
        assert percentile([42], 100) == 42.0

    def test_percentile_interpolation(self):
        data = [1, 2, 3, 4]
        result = percentile(data, 33.33)
        # Should interpolate between values
        assert 1.0 < result < 4.0

    def test_percentile_unsorted_data(self):
        data = [5, 1, 9, 3, 7]
        assert percentile(data, 50) == 5.0

    def test_percentile_with_duplicates(self):
        data = [1, 2, 2, 3, 4]
        result = percentile(data, 50)
        assert result == 2.0

    def test_percentile_edge_cases(self):
        data = [1, 2, 3, 4, 5]
        assert percentile(data, 0.0) == 1.0
        assert percentile(data, 100.0) == 5.0

    def test_percentile_invalid_range(self):
        data = [1, 2, 3]
        with pytest.raises(ValueError, match="Percentile must be between 0 and 100"):
            percentile(data, -1)
        with pytest.raises(ValueError, match="Percentile must be between 0 and 100"):
            percentile(data, 101)

    def test_percentile_empty_list(self):
        with pytest.raises(ValueError, match="Cannot calculate percentile of empty list"):
            percentile([], 50)

    def test_percentile_non_numeric_data(self):
        with pytest.raises(TypeError, match="All values must be numeric"):
            percentile([1, 2, "3"], 50)

    def test_percentile_non_numeric_percentile(self):
        with pytest.raises(TypeError, match="Percentile must be numeric"):
            percentile([1, 2, 3], "50")


class TestMathematicalProperties:
    """Test mathematical relationships and properties between functions."""

    def test_mean_median_mode_relationships(self):
        # For a perfectly symmetric distribution
        symmetric_data = [1, 2, 3, 4, 5]
        mean_val = mean(symmetric_data)
        median_val = median(symmetric_data)
        assert abs(mean_val - median_val) < 1e-10

    def test_variance_std_dev_relationship(self):
        data = [10, 12, 23, 23, 16, 23, 21, 16]
        var = variance(data)
        std = standard_deviation(data)
        assert abs(var - std ** 2) < 1e-10

    def test_range_min_max_relationship(self):
        data = [5, 2, 8, 1, 9, 3]
        min_val, max_val = min_max(data)
        range_val = range_calc(data)
        assert range_val == max_val - min_val

    def test_percentile_min_max_relationship(self):
        data = [1, 5, 3, 9, 2, 7, 4]
        min_val, max_val = min_max(data)
        assert percentile(data, 0) == min_val
        assert percentile(data, 100) == max_val

    def test_median_50th_percentile_relationship(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        median_val = median(data)
        percentile_50 = percentile(data, 50)
        assert median_val == percentile_50

    def test_sample_vs_population_variance(self):
        data = [1, 2, 3, 4, 5]
        pop_var = variance(data, sample=False)
        sample_var = variance(data, sample=True)
        # Sample variance should be larger than population variance
        assert sample_var > pop_var

        # Mathematical relationship: sample_var = pop_var * n / (n-1)
        n = len(data)
        expected_sample_var = pop_var * n / (n - 1)
        assert abs(sample_var - expected_sample_var) < 1e-10


@pytest.mark.parametrize("data,expected_mean", [
    ([1], 1.0),
    ([1, 2], 1.5),
    ([1, 2, 3], 2.0),
    ([0, 0, 0], 0.0),
    ([-1, 0, 1], 0.0),
    ([10.5, 20.5], 15.5),
])
def test_mean_parametrized(data, expected_mean):
    """Parametrized tests for mean function."""
    assert mean(data) == expected_mean


@pytest.mark.parametrize("data,expected_median", [
    ([1], 1.0),
    ([1, 2], 1.5),
    ([1, 2, 3], 2.0),
    ([1, 3, 2], 2.0),
    ([4, 1, 3, 2], 2.5),
])
def test_median_parametrized(data, expected_median):
    """Parametrized tests for median function."""
    assert median(data) == expected_median


@pytest.mark.parametrize("data,expected_range", [
    ([1], 0),
    ([1, 5], 4),
    ([1, 2, 3, 4, 5], 4),
    ([-5, 0, 5], 10),
    ([100, 200, 50], 150),
])
def test_range_calc_parametrized(data, expected_range):
    """Parametrized tests for range_calc function."""
    assert range_calc(data) == expected_range