"""Tests for data_utils module."""

import pytest

from data_utils import (
    chunk_list,
    filter_none_values,
    find_duplicates,
    flatten_list,
    group_by,
    merge_dicts,
)


# ---------------------------------------------------------------------------
# flatten_list
# ---------------------------------------------------------------------------


class TestFlattenList:
    def test_already_flat(self):
        assert flatten_list([1, 2, 3]) == [1, 2, 3]

    def test_one_level_nesting(self):
        assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]

    def test_deep_nesting(self):
        assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]

    def test_mixed_types(self):
        assert flatten_list([1, "a", [2, "b"], [3, [None]]]) == [1, "a", 2, "b", 3, None]

    def test_empty_list(self):
        assert flatten_list([]) == []

    def test_nested_empty_lists(self):
        assert flatten_list([[], [[]], [1]]) == [1]

    def test_type_error(self):
        with pytest.raises(TypeError):
            flatten_list("not a list")  # type: ignore

    def test_type_error_integer(self):
        with pytest.raises(TypeError):
            flatten_list(42)  # type: ignore


# ---------------------------------------------------------------------------
# chunk_list
# ---------------------------------------------------------------------------


class TestChunkList:
    def test_even_division(self):
        assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_uneven_division(self):
        assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_chunk_larger_than_list(self):
        assert chunk_list([1, 2], 10) == [[1, 2]]

    def test_chunk_size_one(self):
        assert chunk_list([1, 2, 3], 1) == [[1], [2], [3]]

    def test_empty_list(self):
        assert chunk_list([], 3) == []

    def test_preserves_types(self):
        result = chunk_list(["a", "b", "c"], 2)
        assert result == [["a", "b"], ["c"]]

    def test_invalid_size_zero(self):
        with pytest.raises(ValueError):
            chunk_list([1, 2], 0)

    def test_invalid_size_negative(self):
        with pytest.raises(ValueError):
            chunk_list([1, 2], -1)

    def test_invalid_size_float(self):
        with pytest.raises(ValueError):
            chunk_list([1, 2], 1.5)  # type: ignore

    def test_type_error_not_list(self):
        with pytest.raises(TypeError):
            chunk_list("abc", 2)  # type: ignore


# ---------------------------------------------------------------------------
# merge_dicts
# ---------------------------------------------------------------------------


class TestMergeDicts:
    def test_no_conflicts(self):
        assert merge_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}

    def test_overwrite_true(self):
        result = merge_dicts({"a": 1}, {"a": 2}, overwrite=True)
        assert result == {"a": 2}

    def test_overwrite_false(self):
        result = merge_dicts({"a": 1}, {"a": 2}, overwrite=False)
        assert result == {"a": 1}

    def test_three_dicts(self):
        result = merge_dicts({"a": 1}, {"b": 2}, {"c": 3})
        assert result == {"a": 1, "b": 2, "c": 3}

    def test_empty_dicts(self):
        assert merge_dicts({}, {}) == {}

    def test_single_dict(self):
        assert merge_dicts({"x": 10}) == {"x": 10}

    def test_no_dicts(self):
        assert merge_dicts() == {}

    def test_type_error(self):
        with pytest.raises(TypeError):
            merge_dicts({"a": 1}, [1, 2])  # type: ignore

    def test_does_not_mutate_inputs(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        merge_dicts(d1, d2)
        assert d1 == {"a": 1}
        assert d2 == {"b": 2}

    def test_mixed_value_types(self):
        result = merge_dicts({"a": [1, 2]}, {"b": {"nested": True}})
        assert result == {"a": [1, 2], "b": {"nested": True}}


# ---------------------------------------------------------------------------
# find_duplicates
# ---------------------------------------------------------------------------


class TestFindDuplicates:
    def test_no_duplicates(self):
        assert find_duplicates([1, 2, 3]) == []

    def test_single_duplicate(self):
        assert find_duplicates([1, 2, 1]) == [1]

    def test_multiple_duplicates(self):
        result = find_duplicates([1, 2, 1, 3, 2, 4])
        assert result == [1, 2]

    def test_each_duplicate_once(self):
        result = find_duplicates([1, 1, 1, 1])
        assert result == [1]

    def test_empty_list(self):
        assert find_duplicates([]) == []

    def test_strings(self):
        assert find_duplicates(["a", "b", "a"]) == ["a"]

    def test_mixed_types(self):
        result = find_duplicates([1, "1", 1])
        assert 1 in result

    def test_type_error(self):
        with pytest.raises(TypeError):
            find_duplicates("not a list")  # type: ignore

    def test_preserves_first_occurrence_order(self):
        result = find_duplicates([3, 1, 2, 1, 3])
        assert result == [3, 1]


# ---------------------------------------------------------------------------
# group_by
# ---------------------------------------------------------------------------


class TestGroupBy:
    def test_group_by_length(self):
        result = group_by(["cat", "bat", "elephant"], key=len)
        assert result == {3: ["cat", "bat"], 8: ["elephant"]}

    def test_group_by_first_char(self):
        result = group_by(["apple", "avocado", "banana"], key=lambda s: s[0])
        assert result == {"a": ["apple", "avocado"], "b": ["banana"]}

    def test_empty_list(self):
        assert group_by([], key=lambda x: x) == {}

    def test_all_same_key(self):
        result = group_by([1, 2, 3], key=lambda x: "all")
        assert result == {"all": [1, 2, 3]}

    def test_group_by_modulo(self):
        result = group_by([1, 2, 3, 4, 5, 6], key=lambda x: x % 2)
        assert result == {1: [1, 3, 5], 0: [2, 4, 6]}

    def test_type_error_not_list(self):
        with pytest.raises(TypeError):
            group_by("abc", key=lambda x: x)  # type: ignore

    def test_type_error_not_callable(self):
        with pytest.raises(TypeError):
            group_by([1, 2], key="not_callable")  # type: ignore

    def test_group_dicts_by_field(self):
        items = [{"type": "a", "val": 1}, {"type": "b", "val": 2}, {"type": "a", "val": 3}]
        result = group_by(items, key=lambda d: d["type"])
        assert len(result["a"]) == 2
        assert len(result["b"]) == 1


# ---------------------------------------------------------------------------
# filter_none_values
# ---------------------------------------------------------------------------


class TestFilterNoneValues:
    def test_removes_none(self):
        assert filter_none_values({"a": 1, "b": None, "c": 3}) == {"a": 1, "c": 3}

    def test_all_none(self):
        assert filter_none_values({"a": None, "b": None}) == {}

    def test_no_none(self):
        assert filter_none_values({"a": 1, "b": 2}) == {"a": 1, "b": 2}

    def test_empty_dict(self):
        assert filter_none_values({}) == {}

    def test_falsy_values_kept(self):
        result = filter_none_values({"a": 0, "b": "", "c": False, "d": None})
        assert result == {"a": 0, "b": "", "c": False}

    def test_does_not_mutate_input(self):
        d = {"a": 1, "b": None}
        filter_none_values(d)
        assert d == {"a": 1, "b": None}

    def test_type_error(self):
        with pytest.raises(TypeError):
            filter_none_values([1, None, 2])  # type: ignore

    def test_nested_dict_values_untouched(self):
        inner = {"x": None}
        result = filter_none_values({"a": inner, "b": None})
        assert result == {"a": inner}
