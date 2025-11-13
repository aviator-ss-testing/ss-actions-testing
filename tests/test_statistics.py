import unittest
from math_utils.statistics import mean, median, mode, variance, standard_deviation


class TestMean(unittest.TestCase):
    """Test cases for mean calculation."""

    def test_mean_positive_numbers(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(mean([10, 20, 30]), 20.0)

    def test_mean_negative_numbers(self):
        self.assertEqual(mean([-1, -2, -3]), -2.0)
        self.assertEqual(mean([-10, -20, -30, -40]), -25.0)

    def test_mean_mixed_numbers(self):
        self.assertEqual(mean([-5, 0, 5]), 0.0)
        self.assertEqual(mean([-10, 10, -5, 5]), 0.0)

    def test_mean_single_value(self):
        self.assertEqual(mean([42]), 42.0)
        self.assertEqual(mean([0]), 0.0)

    def test_mean_floats(self):
        self.assertEqual(mean([1.5, 2.5, 3.5]), 2.5)
        self.assertAlmostEqual(mean([1.1, 2.2, 3.3]), 2.2)

    def test_mean_large_list(self):
        values = list(range(1, 101))
        self.assertEqual(mean(values), 50.5)

    def test_mean_empty_list_raises_error(self):
        with self.assertRaises(ValueError) as context:
            mean([])
        self.assertEqual(str(context.exception), "Cannot calculate mean of an empty list")


class TestMedian(unittest.TestCase):
    """Test cases for median calculation."""

    def test_median_odd_length(self):
        self.assertEqual(median([1, 2, 3]), 2)
        self.assertEqual(median([5, 1, 3, 2, 4]), 3)

    def test_median_even_length(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([10, 20, 30, 40]), 25.0)

    def test_median_single_value(self):
        self.assertEqual(median([42]), 42)

    def test_median_two_values(self):
        self.assertEqual(median([10, 20]), 15.0)
        self.assertEqual(median([5, 15]), 10.0)

    def test_median_negative_numbers(self):
        self.assertEqual(median([-5, -1, -3]), -3)
        self.assertEqual(median([-10, -20, -30, -40]), -25.0)

    def test_median_unsorted_list(self):
        self.assertEqual(median([5, 2, 8, 1, 9]), 5)
        self.assertEqual(median([100, 1, 50, 25]), 37.5)

    def test_median_with_duplicates(self):
        self.assertEqual(median([1, 2, 2, 3]), 2.0)
        self.assertEqual(median([5, 5, 5]), 5)

    def test_median_empty_list_raises_error(self):
        with self.assertRaises(ValueError) as context:
            median([])
        self.assertEqual(str(context.exception), "Cannot calculate median of an empty list")


class TestMode(unittest.TestCase):
    """Test cases for mode calculation."""

    def test_mode_single_mode(self):
        self.assertEqual(mode([1, 2, 2, 3]), 2)
        self.assertEqual(mode([5, 5, 5, 1, 2, 3]), 5)

    def test_mode_all_unique(self):
        result = mode([1, 2, 3, 4, 5])
        self.assertIn(result, [1, 2, 3, 4, 5])

    def test_mode_multiple_modes(self):
        result = mode([1, 1, 2, 2, 3])
        self.assertIn(result, [1, 2])

    def test_mode_single_value(self):
        self.assertEqual(mode([42]), 42)

    def test_mode_all_same(self):
        self.assertEqual(mode([7, 7, 7, 7]), 7)

    def test_mode_negative_numbers(self):
        self.assertEqual(mode([-5, -5, -3, -1]), -5)

    def test_mode_floats(self):
        self.assertEqual(mode([1.5, 2.5, 1.5, 3.5]), 1.5)

    def test_mode_empty_list_raises_error(self):
        with self.assertRaises(ValueError) as context:
            mode([])
        self.assertEqual(str(context.exception), "Cannot calculate mode of an empty list")


class TestVariance(unittest.TestCase):
    """Test cases for variance calculation."""

    def test_variance_simple_values(self):
        self.assertEqual(variance((1, 2, 3, 4, 5)), 2.0)

    def test_variance_all_same(self):
        self.assertEqual(variance((5, 5, 5, 5)), 0.0)

    def test_variance_two_values(self):
        self.assertEqual(variance((10, 20)), 25.0)

    def test_variance_negative_numbers(self):
        self.assertEqual(variance((-2, -1, 0, 1, 2)), 2.0)

    def test_variance_single_value(self):
        self.assertEqual(variance((42,)), 0.0)

    def test_variance_floats(self):
        result = variance((1.5, 2.5, 3.5))
        self.assertAlmostEqual(result, 0.6666666666666666)

    def test_variance_empty_tuple_raises_error(self):
        with self.assertRaises(ValueError) as context:
            variance(())
        self.assertEqual(str(context.exception), "Cannot calculate variance of an empty list")


class TestStandardDeviation(unittest.TestCase):
    """Test cases for standard deviation calculation."""

    def test_standard_deviation_simple_values(self):
        result = standard_deviation((1, 2, 3, 4, 5))
        self.assertAlmostEqual(result, 1.4142135623730951)

    def test_standard_deviation_all_same(self):
        self.assertEqual(standard_deviation((5, 5, 5, 5)), 0.0)

    def test_standard_deviation_two_values(self):
        self.assertEqual(standard_deviation((10, 20)), 5.0)

    def test_standard_deviation_negative_numbers(self):
        result = standard_deviation((-2, -1, 0, 1, 2))
        self.assertAlmostEqual(result, 1.4142135623730951)

    def test_standard_deviation_single_value(self):
        self.assertEqual(standard_deviation((42,)), 0.0)

    def test_standard_deviation_relationship_to_variance(self):
        values = (1, 2, 3, 4, 5)
        var = variance(values)
        std_dev = standard_deviation(values)
        self.assertAlmostEqual(std_dev, var ** 0.5)

    def test_standard_deviation_empty_tuple_raises_error(self):
        with self.assertRaises(ValueError) as context:
            standard_deviation(())
        self.assertEqual(str(context.exception), "Cannot calculate standard deviation of an empty list")


class TestMemoization(unittest.TestCase):
    """Test cases for memoization in statistics functions."""

    def test_variance_uses_memoization(self):
        values = (1, 2, 3, 4, 5)

        variance(values)
        cache_size_after_first = len(variance.cache)
        self.assertGreater(cache_size_after_first, 0)

        variance(values)
        cache_size_after_second = len(variance.cache)
        self.assertEqual(cache_size_after_first, cache_size_after_second)

        variance((10, 20, 30))
        cache_size_after_different = len(variance.cache)
        self.assertGreater(cache_size_after_different, cache_size_after_first)

    def test_standard_deviation_uses_memoization(self):
        values = (1, 2, 3, 4, 5)

        result1 = standard_deviation(values)
        cache_size_after_first = len(standard_deviation.cache)
        self.assertGreater(cache_size_after_first, 0)

        result2 = standard_deviation(values)
        self.assertEqual(result1, result2)
        cache_size_after_second = len(standard_deviation.cache)
        self.assertEqual(cache_size_after_first, cache_size_after_second)

    def test_memoization_effectiveness(self):
        values1 = (1, 2, 3, 4, 5)
        values2 = (10, 20, 30, 40, 50)

        variance(values1)
        variance(values2)
        variance(values1)
        variance(values2)

        self.assertEqual(len(variance.cache), 2)


if __name__ == '__main__':
    unittest.main()
