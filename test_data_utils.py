"""Tests for the data_utils module."""
import pytest
from data_utils import (
    flatten_list,
    chunk_list,
    merge_dicts,
    find_duplicates,
    group_by,
    filter_none_values,
)


class TestFlattenList:
    """Tests for flatten_list function."""

    def test_simple_nested_list(self):
        """Test basic nested list flattening."""
        assert flatten_list([1, [2, 3], [4, 5]]) == [1, 2, 3, 4, 5]
        assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]

    def test_deeply_nested_list(self):
        """Test deeply nested list structures."""
        assert flatten_list([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]
        assert flatten_list([[[[1]]], [[[2]]], [[[3]]]]) == [1, 2, 3]

    def test_mixed_nesting(self):
        """Test lists with mixed nesting levels."""
        assert flatten_list([1, [2, 3], [4, [5, 6]], 7]) == [1, 2, 3, 4, 5, 6, 7]
        assert flatten_list([[], [1], [[2]], [[[3]]]]) == [1, 2, 3]

    def test_already_flat_list(self):
        """Test lists that are already flat."""
        assert flatten_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        assert flatten_list(["a", "b", "c"]) == ["a", "b", "c"]

    def test_empty_lists(self):
        """Test empty and nested empty lists."""
        assert flatten_list([]) == []
        assert flatten_list([[], [], []]) == []
        assert flatten_list([1, [], 2, [], 3]) == [1, 2, 3]

    def test_none_input(self):
        """Test None input."""
        assert flatten_list(None) == []

    def test_mixed_types(self):
        """Test lists with mixed data types."""
        assert flatten_list([1, "a", [2, "b"], [3, [4, "c"]]]) == [1, "a", 2, "b", 3, 4, "c"]
        assert flatten_list([True, [False], [[None]]]) == [True, False, None]

    def test_single_element(self):
        """Test single element lists."""
        assert flatten_list([1]) == [1]
        assert flatten_list([[1]]) == [1]
        assert flatten_list([[[1]]]) == [1]


class TestChunkList:
    """Tests for chunk_list function."""

    def test_even_chunks(self):
        """Test lists that divide evenly into chunks."""
        assert chunk_list([1, 2, 3, 4, 5, 6], 2) == [[1, 2], [3, 4], [5, 6]]
        assert chunk_list([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [4, 5, 6]]

    def test_uneven_chunks(self):
        """Test lists that don't divide evenly."""
        assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
        assert chunk_list([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]

    def test_chunk_size_larger_than_list(self):
        """Test chunk size larger than list length."""
        assert chunk_list([1, 2, 3], 5) == [[1, 2, 3]]
        assert chunk_list([1], 10) == [[1]]

    def test_chunk_size_one(self):
        """Test chunk size of 1."""
        assert chunk_list([1, 2, 3], 1) == [[1], [2], [3]]
        assert chunk_list(["a", "b"], 1) == [["a"], ["b"]]

    def test_empty_list(self):
        """Test empty list."""
        assert chunk_list([], 2) == []
        assert chunk_list([], 10) == []

    def test_none_input(self):
        """Test None input."""
        assert chunk_list(None, 2) == []

    def test_invalid_chunk_size(self):
        """Test invalid chunk sizes raise errors."""
        with pytest.raises(ValueError, match="chunk_size must be at least 1"):
            chunk_list([1, 2, 3], 0)
        with pytest.raises(ValueError, match="chunk_size must be at least 1"):
            chunk_list([1, 2, 3], -1)

    def test_various_data_types(self):
        """Test chunking lists of various data types."""
        assert chunk_list(["a", "b", "c", "d", "e"], 2) == [["a", "b"], ["c", "d"], ["e"]]
        assert chunk_list([True, False, True, False], 2) == [[True, False], [True, False]]


class TestMergeDicts:
    """Tests for merge_dicts function."""

    def test_simple_merge(self):
        """Test basic dictionary merging."""
        assert merge_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}
        assert merge_dicts({"a": 1}, {"b": 2}, {"c": 3}) == {"a": 1, "b": 2, "c": 3}

    def test_overlapping_keys(self):
        """Test merging with overlapping keys."""
        assert merge_dicts({"a": 1}, {"a": 2}) == {"a": 2}
        assert merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}

    def test_multiple_dicts_with_conflicts(self):
        """Test merging multiple dicts with conflicting keys."""
        assert merge_dicts({"a": 1}, {"a": 2}, {"a": 3}) == {"a": 3}
        assert merge_dicts({"a": 1, "b": 1}, {"b": 2, "c": 2}, {"c": 3, "d": 3}) == {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 3,
        }

    def test_empty_dicts(self):
        """Test merging empty dictionaries."""
        assert merge_dicts() == {}
        assert merge_dicts({}) == {}
        assert merge_dicts({}, {}) == {}
        assert merge_dicts({"a": 1}, {}, {"b": 2}) == {"a": 1, "b": 2}

    def test_none_input(self):
        """Test None in the input dictionaries."""
        assert merge_dicts(None) == {}
        assert merge_dicts({"a": 1}, None, {"b": 2}) == {"a": 1, "b": 2}

    def test_deep_merge_disabled(self):
        """Test shallow merge (default behavior)."""
        result = merge_dicts({"a": {"x": 1}}, {"a": {"y": 2}})
        assert result == {"a": {"y": 2}}

    def test_deep_merge_enabled(self):
        """Test deep merge of nested dictionaries."""
        result = merge_dicts({"a": {"x": 1}}, {"a": {"y": 2}}, deep=True)
        assert result == {"a": {"x": 1, "y": 2}}

        result = merge_dicts(
            {"a": {"b": {"c": 1}}}, {"a": {"b": {"d": 2}}}, {"a": {"e": 3}}, deep=True
        )
        assert result == {"a": {"b": {"c": 1, "d": 2}, "e": 3}}

    def test_deep_merge_with_conflicts(self):
        """Test deep merge with conflicting nested keys."""
        result = merge_dicts({"a": {"x": 1, "y": 2}}, {"a": {"y": 3, "z": 4}}, deep=True)
        assert result == {"a": {"x": 1, "y": 3, "z": 4}}

    def test_deep_merge_mixed_types(self):
        """Test deep merge when values have different types."""
        result = merge_dicts({"a": {"x": 1}}, {"a": 2}, deep=True)
        assert result == {"a": 2}

        result = merge_dicts({"a": 1}, {"a": {"x": 2}}, deep=True)
        assert result == {"a": {"x": 2}}

    def test_various_value_types(self):
        """Test merging dicts with various value types."""
        result = merge_dicts(
            {"a": 1, "b": "string", "c": [1, 2]}, {"d": True, "e": None, "f": {"nested": 1}}
        )
        assert result == {"a": 1, "b": "string", "c": [1, 2], "d": True, "e": None, "f": {"nested": 1}}


class TestFindDuplicates:
    """Tests for find_duplicates function."""

    def test_simple_duplicates(self):
        """Test finding simple duplicates."""
        assert find_duplicates([1, 2, 3, 2, 4, 3, 5]) == [2, 3]
        assert find_duplicates([1, 1, 2, 2, 3, 3]) == [1, 2, 3]

    def test_no_duplicates(self):
        """Test lists with no duplicates."""
        assert find_duplicates([1, 2, 3, 4, 5]) == []
        assert find_duplicates(["a", "b", "c"]) == []

    def test_all_duplicates(self):
        """Test lists where all elements are duplicates."""
        assert find_duplicates([1, 1, 1, 1]) == [1]
        assert find_duplicates([5, 5]) == [5]

    def test_multiple_occurrences(self):
        """Test elements appearing more than twice."""
        assert find_duplicates([1, 2, 1, 2, 1, 2]) == [1, 2]
        assert find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3]) == [1, 2, 3]

    def test_empty_list(self):
        """Test empty list."""
        assert find_duplicates([]) == []

    def test_none_input(self):
        """Test None input."""
        assert find_duplicates(None) == []

    def test_single_element(self):
        """Test single element list."""
        assert find_duplicates([1]) == []

    def test_string_duplicates(self):
        """Test finding duplicate strings."""
        assert find_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b"]
        assert find_duplicates(["hello", "world", "hello"]) == ["hello"]

    def test_mixed_types(self):
        """Test lists with mixed data types."""
        assert find_duplicates([1, "1", 1, "1"]) == [1, "1"]
        assert find_duplicates([True, 1, True, 1]) == [True]

    def test_preserve_order(self):
        """Test that duplicates are returned in order of first duplicate occurrence."""
        assert find_duplicates([3, 1, 2, 1, 3, 4, 2]) == [1, 3, 2]
        assert find_duplicates([5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


class TestGroupBy:
    """Tests for group_by function."""

    def test_simple_grouping(self):
        """Test basic grouping by a key function."""
        result = group_by([1, 2, 3, 4, 5, 6], lambda x: x % 2)
        assert result == {1: [1, 3, 5], 0: [2, 4, 6]}

    def test_group_by_length(self):
        """Test grouping strings by length."""
        result = group_by(["a", "bb", "ccc", "dd", "e"], lambda x: len(x))
        assert result == {1: ["a", "e"], 2: ["bb", "dd"], 3: ["ccc"]}

    def test_group_by_first_character(self):
        """Test grouping by first character."""
        result = group_by(["apple", "apricot", "banana", "berry", "cherry"], lambda x: x[0])
        assert result == {"a": ["apple", "apricot"], "b": ["banana", "berry"], "c": ["cherry"]}

    def test_group_by_type(self):
        """Test grouping by type."""
        result = group_by([1, "a", 2, "b", 3, "c"], lambda x: type(x).__name__)
        assert result == {"int": [1, 2, 3], "str": ["a", "b", "c"]}

    def test_empty_list(self):
        """Test empty list."""
        assert group_by([], lambda x: x) == {}

    def test_none_input(self):
        """Test None input."""
        assert group_by(None, lambda x: x) == {}

    def test_single_group(self):
        """Test when all elements map to the same key."""
        result = group_by([1, 2, 3, 4, 5], lambda x: "same")
        assert result == {"same": [1, 2, 3, 4, 5]}

    def test_each_element_unique_group(self):
        """Test when each element maps to a unique key."""
        result = group_by([1, 2, 3], lambda x: x)
        assert result == {1: [1], 2: [2], 3: [3]}

    def test_complex_key_function(self):
        """Test with more complex key functions."""
        data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 30}]
        result = group_by(data, lambda x: x["age"])
        assert result == {
            30: [{"name": "Alice", "age": 30}, {"name": "Charlie", "age": 30}],
            25: [{"name": "Bob", "age": 25}],
        }

    def test_preserve_order(self):
        """Test that items preserve their original order within groups."""
        result = group_by([5, 4, 3, 2, 1, 6], lambda x: x % 2)
        assert result == {1: [5, 3, 1], 0: [4, 2, 6]}


class TestFilterNoneValues:
    """Tests for filter_none_values function."""

    def test_filter_some_none(self):
        """Test filtering dictionaries with some None values."""
        assert filter_none_values({"a": 1, "b": None, "c": 3}) == {"a": 1, "c": 3}
        assert filter_none_values({"x": "hello", "y": None, "z": "world"}) == {"x": "hello", "z": "world"}

    def test_filter_all_none(self):
        """Test filtering dictionaries with all None values."""
        assert filter_none_values({"a": None, "b": None, "c": None}) == {}

    def test_filter_no_none(self):
        """Test filtering dictionaries with no None values."""
        assert filter_none_values({"a": 1, "b": 2, "c": 3}) == {"a": 1, "b": 2, "c": 3}

    def test_empty_dict(self):
        """Test empty dictionary."""
        assert filter_none_values({}) == {}

    def test_none_input(self):
        """Test None input."""
        assert filter_none_values(None) == {}

    def test_preserve_falsy_values(self):
        """Test that other falsy values are preserved."""
        result = filter_none_values({"a": 0, "b": "", "c": False, "d": None, "e": []})
        assert result == {"a": 0, "b": "", "c": False, "e": []}

    def test_various_value_types(self):
        """Test filtering with various value types."""
        result = filter_none_values({
            "int": 42,
            "str": "hello",
            "list": [1, 2, 3],
            "dict": {"nested": "value"},
            "none1": None,
            "bool": True,
            "none2": None,
        })
        assert result == {
            "int": 42,
            "str": "hello",
            "list": [1, 2, 3],
            "dict": {"nested": "value"},
            "bool": True,
        }

    def test_preserve_key_order(self):
        """Test that key order is preserved (Python 3.7+)."""
        result = filter_none_values({"z": 1, "y": None, "x": 2, "w": None, "v": 3})
        assert list(result.keys()) == ["z", "x", "v"]
        assert result == {"z": 1, "x": 2, "v": 3}
