"""Tests for list_utils module."""

import pytest
from list_utils import flatten, chunk, group_by, most_common


class TestFlatten:
    """Tests for flatten function."""

    def test_flatten_nested_lists(self):
        """Test flattening a list with nested sublists."""
        assert flatten([1, [2, 3], [4, 5]]) == [1, 2, 3, 4, 5]
        assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]

    def test_flatten_edge_cases(self):
        """Test flatten with edge cases."""
        assert flatten([]) == []
        assert flatten([1]) == [1]
        assert flatten([[1]]) == [1]
        assert flatten([1, 2, 3]) == [1, 2, 3]


class TestChunk:
    """Tests for chunk function."""

    def test_chunk_normal_cases(self):
        """Test chunking lists into equal-sized chunks."""
        assert chunk([1, 2, 3, 4, 5, 6], 2) == [[1, 2], [3, 4], [5, 6]]
        assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
        assert chunk([1, 2, 3, 4], 3) == [[1, 2, 3], [4]]

    def test_chunk_edge_cases(self):
        """Test chunk with edge cases."""
        assert chunk([], 3) == []
        assert chunk([1], 1) == [[1]]
        assert chunk([1, 2, 3], 5) == [[1, 2, 3]]

    def test_chunk_invalid_size(self):
        """Test chunk with invalid size."""
        with pytest.raises(ValueError):
            chunk([1, 2, 3], 0)
        with pytest.raises(ValueError):
            chunk([1, 2, 3], -1)


class TestGroupBy:
    """Tests for group_by function."""

    def test_group_by_normal_cases(self):
        """Test grouping by various key functions."""
        # Group by length
        words = ["a", "bb", "ccc", "dd", "e"]
        result = group_by(words, len)
        assert result == {1: ["a", "e"], 2: ["bb", "dd"], 3: ["ccc"]}

        # Group by modulo
        numbers = [1, 2, 3, 4, 5, 6]
        result = group_by(numbers, lambda x: x % 2)
        assert result == {1: [1, 3, 5], 0: [2, 4, 6]}

    def test_group_by_edge_cases(self):
        """Test group_by with edge cases."""
        assert group_by([], len) == {}
        assert group_by([1], lambda x: x) == {1: [1]}


class TestMostCommon:
    """Tests for most_common function."""

    def test_most_common_normal_cases(self):
        """Test finding most common element."""
        assert most_common([1, 2, 2, 3, 3, 3]) == 3
        assert most_common(["a", "b", "a", "c", "a"]) == "a"
        assert most_common([1, 1, 2, 2, 3]) in [1, 2]

    def test_most_common_edge_cases(self):
        """Test most_common with edge cases."""
        assert most_common([]) is None
        assert most_common([1]) == 1
        assert most_common([1, 1]) == 1
