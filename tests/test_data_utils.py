"""Tests for data utilities module."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from utils.data_utils import flatten_list, remove_duplicates, group_by_key, filter_none


class TestFlattenList:
    """Tests for flatten_list function."""

    @pytest.mark.parametrize(
        "input_list,expected",
        [
            ([1, 2, 3], [1, 2, 3]),
            ([1, [2, 3], 4], [1, 2, 3, 4]),
            ([[1, 2], [3, 4]], [1, 2, 3, 4]),
            ([1, [2, [3, 4]], 5], [1, 2, 3, 4, 5]),
            ([1, [2, [3, [4, [5]]]]], [1, 2, 3, 4, 5]),
            ([], []),
            ([[]], []),
            ([[], []], []),
            ([[1], [2], [3]], [1, 2, 3]),
            ([1, [], 2, [], 3], [1, 2, 3]),
            ([[1, 2, 3]], [1, 2, 3]),
            ([[[1]]], [1]),
            ([[[[1]]]], [1]),
            ([1, [2, 3], [4, [5, 6]], 7], [1, 2, 3, 4, 5, 6, 7]),
            ([[], [[]], [[[]]]], []),
        ],
    )
    def test_flatten_list(self, input_list, expected):
        """Test flatten_list with various nested list structures."""
        assert flatten_list(input_list) == expected

    def test_flatten_list_empty(self):
        """Test flatten_list with empty lists."""
        assert flatten_list([]) == []
        assert flatten_list([[]]) == []
        assert flatten_list([[], [], []]) == []

    def test_flatten_list_single_level(self):
        """Test flatten_list with already flat lists."""
        assert flatten_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        assert flatten_list(["a", "b", "c"]) == ["a", "b", "c"]
        assert flatten_list([1]) == [1]

    def test_flatten_list_varying_depths(self):
        """Test flatten_list with lists of varying depths."""
        assert flatten_list([1, [2], [[3]], [[[4]]]]) == [1, 2, 3, 4]
        assert flatten_list([[1, [2]], 3, [4, [5, [6]]]]) == [1, 2, 3, 4, 5, 6]

    def test_flatten_list_mixed_types(self):
        """Test flatten_list with mixed data types."""
        assert flatten_list([1, [2.5, "hello"], [None, True]]) == [1, 2.5, "hello", None, True]
        assert flatten_list(["a", [1, [True, [None]]]]) == ["a", 1, True, None]

    def test_flatten_list_deep_nesting(self):
        """Test flatten_list with deeply nested structures."""
        deep_list = [1, [2, [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert flatten_list(deep_list) == expected


class TestRemoveDuplicates:
    """Tests for remove_duplicates function."""

    @pytest.mark.parametrize(
        "input_list,expected",
        [
            ([1, 2, 2, 3, 1, 4], [1, 2, 3, 4]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([1, 1, 1, 1], [1]),
            ([1], [1]),
            ([], []),
            ([1, 2, 1, 2, 1, 2], [1, 2]),
            (["a", "b", "a", "c", "b"], ["a", "b", "c"]),
            ([1, "1", 1, "1"], [1, "1"]),
            ([None, 1, None, 2, None], [None, 1, 2]),
            ([True, False, True, False], [True, False]),
            ([1.0, 1, 2.0, 2, 3.0, 3], [1.0, 2.0, 3.0]),
        ],
    )
    def test_remove_duplicates(self, input_list, expected):
        """Test remove_duplicates with various inputs."""
        assert remove_duplicates(input_list) == expected

    def test_remove_duplicates_no_duplicates(self):
        """Test remove_duplicates with lists containing no duplicates."""
        assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
        assert remove_duplicates(["a", "b", "c"]) == ["a", "b", "c"]
        assert remove_duplicates([1]) == [1]

    def test_remove_duplicates_empty_list(self):
        """Test remove_duplicates with empty list."""
        assert remove_duplicates([]) == []

    def test_remove_duplicates_all_duplicates(self):
        """Test remove_duplicates with all duplicate elements."""
        assert remove_duplicates([1, 1, 1, 1, 1]) == [1]
        assert remove_duplicates(["a", "a", "a"]) == ["a"]

    def test_remove_duplicates_preserves_order(self):
        """Test that remove_duplicates preserves order of first occurrence."""
        assert remove_duplicates([3, 1, 2, 1, 3, 2]) == [3, 1, 2]
        assert remove_duplicates([5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]

    def test_remove_duplicates_mixed_types(self):
        """Test remove_duplicates with mixed types.

        Note: In Python, False == 0 and True == 1, so they are treated as duplicates.
        """
        assert remove_duplicates([1, "1", 2, "2", 1, "1"]) == [1, "1", 2, "2"]
        assert remove_duplicates([None, 0, False, ""]) == [None, 0, ""]
        assert remove_duplicates([True, 1, False, 0]) == [True, False]


class TestGroupByKey:
    """Tests for group_by_key function."""

    @pytest.mark.parametrize(
        "input_list,key,expected",
        [
            (
                [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 25}],
                "age",
                {30: [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 30}], 25: [{"name": "Charlie", "age": 25}]},
            ),
            (
                [{"type": "fruit", "name": "apple"}, {"type": "vegetable", "name": "carrot"}, {"type": "fruit", "name": "banana"}],
                "type",
                {"fruit": [{"type": "fruit", "name": "apple"}, {"type": "fruit", "name": "banana"}], "vegetable": [{"type": "vegetable", "name": "carrot"}]},
            ),
            ([], "key", {}),
            ([{"name": "Alice", "age": 30}], "age", {30: [{"name": "Alice", "age": 30}]}),
            (
                [{"id": 1, "value": "a"}, {"id": 2, "value": "b"}, {"id": 1, "value": "c"}],
                "id",
                {1: [{"id": 1, "value": "a"}, {"id": 1, "value": "c"}], 2: [{"id": 2, "value": "b"}]},
            ),
        ],
    )
    def test_group_by_key(self, input_list, key, expected):
        """Test group_by_key with valid dictionaries."""
        assert group_by_key(input_list, key) == expected

    def test_group_by_key_empty_list(self):
        """Test group_by_key with empty list."""
        assert group_by_key([], "any_key") == {}
        assert group_by_key([], "age") == {}

    def test_group_by_key_missing_keys(self):
        """Test group_by_key when some dictionaries are missing the key."""
        items = [
            {"name": "Alice", "age": 30},
            {"name": "Bob"},
            {"name": "Charlie", "age": 30},
        ]
        result = group_by_key(items, "age")
        expected = {30: [{"name": "Alice", "age": 30}, {"name": "Charlie", "age": 30}]}
        assert result == expected

    def test_group_by_key_all_missing_keys(self):
        """Test group_by_key when all dictionaries are missing the key."""
        items = [
            {"name": "Alice"},
            {"name": "Bob"},
            {"name": "Charlie"},
        ]
        assert group_by_key(items, "age") == {}

    def test_group_by_key_single_group(self):
        """Test group_by_key when all items belong to the same group."""
        items = [
            {"name": "Alice", "type": "user"},
            {"name": "Bob", "type": "user"},
            {"name": "Charlie", "type": "user"},
        ]
        result = group_by_key(items, "type")
        expected = {
            "user": [
                {"name": "Alice", "type": "user"},
                {"name": "Bob", "type": "user"},
                {"name": "Charlie", "type": "user"},
            ]
        }
        assert result == expected

    def test_group_by_key_various_types(self):
        """Test group_by_key with various key value types.

        Note: In Python, True == 1 and False == 0, so they are treated as the same dictionary key.
        """
        items = [
            {"id": 1, "name": "one"},
            {"id": "1", "name": "one-str"},
            {"id": True, "name": "true"},
            {"id": None, "name": "none"},
            {"id": 1, "name": "one-again"},
        ]
        result = group_by_key(items, "id")
        expected = {
            1: [{"id": 1, "name": "one"}, {"id": True, "name": "true"}, {"id": 1, "name": "one-again"}],
            "1": [{"id": "1", "name": "one-str"}],
            None: [{"id": None, "name": "none"}],
        }
        assert result == expected

    def test_group_by_key_multiple_groups(self):
        """Test group_by_key with multiple distinct groups."""
        items = [
            {"category": "A", "value": 1},
            {"category": "B", "value": 2},
            {"category": "C", "value": 3},
            {"category": "A", "value": 4},
            {"category": "B", "value": 5},
        ]
        result = group_by_key(items, "category")
        expected = {
            "A": [{"category": "A", "value": 1}, {"category": "A", "value": 4}],
            "B": [{"category": "B", "value": 2}, {"category": "B", "value": 5}],
            "C": [{"category": "C", "value": 3}],
        }
        assert result == expected


class TestFilterNone:
    """Tests for filter_none function."""

    @pytest.mark.parametrize(
        "input_list,expected",
        [
            ([1, None, 2, None, 3], [1, 2, 3]),
            ([1, 2, 3], [1, 2, 3]),
            ([None, None, None], []),
            ([], []),
            ([None], []),
            ([1], [1]),
            ([0, None, False, "", None], [0, False, ""]),
            (["a", None, "b", None, "c"], ["a", "b", "c"]),
            ([None, 0, None, 1, None, 2], [0, 1, 2]),
            ([[], None, {}, None, ()], [[], {}, ()]),
            ([True, False, None, True, None, False], [True, False, True, False]),
        ],
    )
    def test_filter_none(self, input_list, expected):
        """Test filter_none with various inputs."""
        assert filter_none(input_list) == expected

    def test_filter_none_no_none_values(self):
        """Test filter_none with lists containing no None values."""
        assert filter_none([1, 2, 3]) == [1, 2, 3]
        assert filter_none(["a", "b", "c"]) == ["a", "b", "c"]
        assert filter_none([0, False, "", []]) == [0, False, "", []]

    def test_filter_none_empty_list(self):
        """Test filter_none with empty list."""
        assert filter_none([]) == []

    def test_filter_none_all_none(self):
        """Test filter_none with all None values."""
        assert filter_none([None]) == []
        assert filter_none([None, None]) == []
        assert filter_none([None, None, None, None]) == []

    def test_filter_none_mixed_types(self):
        """Test filter_none with mixed data types."""
        assert filter_none([1, 2.5, "hello", None, True, None, [], {}]) == [1, 2.5, "hello", True, [], {}]
        assert filter_none([None, "string", 123, None, [1, 2, 3]]) == ["string", 123, [1, 2, 3]]

    def test_filter_none_preserves_order(self):
        """Test that filter_none preserves order of elements."""
        assert filter_none([5, None, 4, None, 3, None, 2, None, 1]) == [5, 4, 3, 2, 1]
        assert filter_none([None, "z", None, "y", None, "x"]) == ["z", "y", "x"]

    def test_filter_none_falsy_values(self):
        """Test that filter_none preserves falsy values that aren't None."""
        assert filter_none([0, None, False, None, "", None, []]) == [0, False, "", []]
        assert filter_none([None, 0, None, False, None, ""]) == [0, False, ""]
