"""Tests for the data_utils module."""

import pytest
from data_utils import (
    chunk_list,
    filter_none_values,
    find_duplicates,
    flatten_list,
    group_by,
    merge_dicts,
)


class TestFlattenList:
    def test_already_flat(self):
        assert flatten_list([1, 2, 3]) == [1, 2, 3]

    def test_one_level_nested(self):
        assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]

    def test_deeply_nested(self):
        assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]

    def test_mixed_nesting(self):
        assert flatten_list([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

    def test_empty_list(self):
        assert flatten_list([]) == []

    def test_nested_empty_lists(self):
        assert flatten_list([[], [], []]) == []

    def test_depth_zero(self):
        assert flatten_list([[1, 2], [3, 4]], depth=0) == [[1, 2], [3, 4]]

    def test_depth_one(self):
        assert flatten_list([1, [2, [3]]], depth=1) == [1, 2, [3]]

    def test_depth_two(self):
        assert flatten_list([1, [2, [3, [4]]]], depth=2) == [1, 2, 3, [4]]

    def test_mixed_types(self):
        assert flatten_list([1, ["a", True], [None]]) == [1, "a", True, None]

    def test_type_error(self):
        with pytest.raises(TypeError):
            flatten_list("not a list")

    def test_value_error_invalid_depth(self):
        with pytest.raises(ValueError):
            flatten_list([1, 2], depth=-2)


class TestChunkList:
    def test_even_chunks(self):
        assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_uneven_chunks(self):
        assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_chunk_size_one(self):
        assert chunk_list([1, 2, 3], 1) == [[1], [2], [3]]

    def test_chunk_size_larger_than_list(self):
        assert chunk_list([1, 2, 3], 10) == [[1, 2, 3]]

    def test_empty_list(self):
        assert chunk_list([], 3) == []

    def test_chunk_size_equals_list_length(self):
        assert chunk_list([1, 2, 3], 3) == [[1, 2, 3]]

    def test_strings(self):
        assert chunk_list(["a", "b", "c", "d"], 2) == [["a", "b"], ["c", "d"]]

    def test_type_error_not_list(self):
        with pytest.raises(TypeError):
            chunk_list("abc", 2)

    def test_type_error_size_not_int(self):
        with pytest.raises(TypeError):
            chunk_list([1, 2, 3], 1.5)

    def test_value_error_zero_size(self):
        with pytest.raises(ValueError):
            chunk_list([1, 2, 3], 0)

    def test_value_error_negative_size(self):
        with pytest.raises(ValueError):
            chunk_list([1, 2, 3], -1)


class TestMergeDicts:
    def test_no_conflicts(self):
        assert merge_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}

    def test_last_wins_by_default(self):
        assert merge_dicts({"a": 1}, {"a": 2}) == {"a": 2}

    def test_first_wins_strategy(self):
        assert merge_dicts({"a": 1}, {"a": 2}, strategy="first") == {"a": 1}

    def test_error_strategy_on_conflict(self):
        with pytest.raises(ValueError, match="Conflicting key"):
            merge_dicts({"a": 1}, {"a": 2}, strategy="error")

    def test_error_strategy_no_conflict(self):
        assert merge_dicts({"a": 1}, {"b": 2}, strategy="error") == {"a": 1, "b": 2}

    def test_three_dicts(self):
        assert merge_dicts({"a": 1}, {"b": 2}, {"c": 3}) == {"a": 1, "b": 2, "c": 3}

    def test_empty_dicts(self):
        assert merge_dicts({}, {}) == {}

    def test_one_empty(self):
        assert merge_dicts({"a": 1}, {}) == {"a": 1}

    def test_no_args(self):
        assert merge_dicts() == {}

    def test_type_error_not_dict(self):
        with pytest.raises(TypeError):
            merge_dicts({"a": 1}, [1, 2])

    def test_invalid_strategy(self):
        with pytest.raises(ValueError):
            merge_dicts({"a": 1}, strategy="unknown")

    def test_none_values_preserved(self):
        assert merge_dicts({"a": None}, {"b": 1}) == {"a": None, "b": 1}


class TestFindDuplicates:
    def test_basic_duplicates(self):
        assert find_duplicates([1, 2, 3, 2, 4, 1]) == [1, 2]

    def test_no_duplicates(self):
        assert find_duplicates([1, 2, 3]) == []

    def test_empty_list(self):
        assert find_duplicates([]) == []

    def test_all_same(self):
        assert find_duplicates([5, 5, 5]) == [5]

    def test_strings(self):
        assert find_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b"]

    def test_mixed_types(self):
        assert find_duplicates([1, "1", 1]) == [1]

    def test_preserves_first_occurrence_order(self):
        result = find_duplicates([3, 1, 2, 1, 3])
        assert result == [3, 1]

    def test_type_error(self):
        with pytest.raises(TypeError):
            find_duplicates("not a list")


class TestGroupBy:
    def test_group_by_length(self):
        result = group_by(["cat", "dog", "ox", "ant", "bee"], key=len)
        assert result == {3: ["cat", "dog", "ant", "bee"], 2: ["ox"]}

    def test_group_by_parity(self):
        result = group_by([1, 2, 3, 4, 5], key=lambda x: x % 2)
        assert result == {1: [1, 3, 5], 0: [2, 4]}

    def test_empty_list(self):
        assert group_by([], key=str) == {}

    def test_all_same_key(self):
        result = group_by([1, 2, 3], key=lambda x: "same")
        assert result == {"same": [1, 2, 3]}

    def test_all_unique_keys(self):
        result = group_by([1, 2, 3], key=lambda x: x)
        assert result == {1: [1], 2: [2], 3: [3]}

    def test_group_dicts_by_field(self):
        data = [{"type": "a", "v": 1}, {"type": "b", "v": 2}, {"type": "a", "v": 3}]
        result = group_by(data, key=lambda x: x["type"])
        assert result == {
            "a": [{"type": "a", "v": 1}, {"type": "a", "v": 3}],
            "b": [{"type": "b", "v": 2}],
        }

    def test_type_error_not_list(self):
        with pytest.raises(TypeError):
            group_by("abc", key=str)

    def test_type_error_key_not_callable(self):
        with pytest.raises(TypeError):
            group_by([1, 2, 3], key="length")


class TestFilterNoneValues:
    def test_removes_none(self):
        assert filter_none_values({"a": 1, "b": None, "c": 3}) == {"a": 1, "c": 3}

    def test_all_none(self):
        assert filter_none_values({"a": None, "b": None}) == {}

    def test_no_none(self):
        assert filter_none_values({"a": 1, "b": 2}) == {"a": 1, "b": 2}

    def test_empty_dict(self):
        assert filter_none_values({}) == {}

    def test_preserves_falsy_non_none(self):
        assert filter_none_values({"a": 0, "b": "", "c": False, "d": None}) == {
            "a": 0,
            "b": "",
            "c": False,
        }

    def test_mixed_value_types(self):
        assert filter_none_values({"x": [1, 2], "y": None, "z": {"nested": True}}) == {
            "x": [1, 2],
            "z": {"nested": True},
        }

    def test_type_error(self):
        with pytest.raises(TypeError):
            filter_none_values([("a", 1)])
