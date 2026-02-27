"""Tests for the collections_utils module."""

import pytest
from collections_utils import flatten, chunk, group_by, dedupe_stable


# --- flatten ---

def test_flatten_empty():
    assert flatten([]) == []


def test_flatten_already_flat():
    assert flatten([1, 2, 3]) == [1, 2, 3]


def test_flatten_single_element():
    assert flatten([42]) == [42]


def test_flatten_one_level():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_flatten_deeply_nested():
    assert flatten([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]


def test_flatten_mixed_depth():
    assert flatten([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]


def test_flatten_nested_empty_lists():
    assert flatten([[], [1], [[], 2]]) == [1, 2]


def test_flatten_strings_not_expanded():
    assert flatten(["ab", ["cd", "ef"]]) == ["ab", "cd", "ef"]


# --- chunk ---

def test_chunk_empty():
    assert chunk([], 3) == []


def test_chunk_exact_division():
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_chunk_last_chunk_shorter():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunk_size_one():
    assert chunk([1, 2, 3], 1) == [[1], [2], [3]]


def test_chunk_size_larger_than_list():
    assert chunk([1, 2], 10) == [[1, 2]]


def test_chunk_single_element():
    assert chunk([99], 3) == [[99]]


def test_chunk_invalid_size_zero():
    with pytest.raises(ValueError):
        chunk([1, 2, 3], 0)


def test_chunk_invalid_size_negative():
    with pytest.raises(ValueError):
        chunk([1, 2, 3], -1)


# --- group_by ---

def test_group_by_empty():
    assert group_by([], lambda x: x) == {}


def test_group_by_single_element():
    assert group_by([1], lambda x: x) == {1: [1]}


def test_group_by_even_odd():
    result = group_by([1, 2, 3, 4, 5], lambda x: x % 2)
    assert result[1] == [1, 3, 5]
    assert result[0] == [2, 4]


def test_group_by_preserves_insertion_order():
    result = group_by(["banana", "apple", "avocado", "blueberry"], lambda s: s[0])
    assert list(result["b"]) == ["banana", "blueberry"]
    assert list(result["a"]) == ["apple", "avocado"]


def test_group_by_all_same_key():
    assert group_by([1, 2, 3], lambda x: "all") == {"all": [1, 2, 3]}


def test_group_by_all_unique_keys():
    result = group_by([1, 2, 3], lambda x: x)
    assert result == {1: [1], 2: [2], 3: [3]}


def test_group_by_dicts():
    items = [{"type": "a", "val": 1}, {"type": "b", "val": 2}, {"type": "a", "val": 3}]
    result = group_by(items, lambda x: x["type"])
    assert len(result["a"]) == 2
    assert result["b"][0]["val"] == 2


# --- dedupe_stable ---

def test_dedupe_stable_empty():
    assert dedupe_stable([]) == []


def test_dedupe_stable_no_duplicates():
    assert dedupe_stable([1, 2, 3]) == [1, 2, 3]


def test_dedupe_stable_single_element():
    assert dedupe_stable([7]) == [7]


def test_dedupe_stable_preserves_order():
    assert dedupe_stable([3, 1, 2, 1, 3]) == [3, 1, 2]


def test_dedupe_stable_all_same():
    assert dedupe_stable([5, 5, 5, 5]) == [5]


def test_dedupe_stable_strings():
    assert dedupe_stable(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]


def test_dedupe_stable_mixed_types():
    assert dedupe_stable([1, "1", 1, "1"]) == [1, "1"]
