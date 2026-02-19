"""Tests for the data_ops module."""
import pytest
from data_ops import (
    find_duplicates,
    flatten_list,
    merge_dicts,
    group_by_key,
    sort_by_multiple_keys
)


class TestFindDuplicates:
    """Tests for find_duplicates function."""

    def test_find_duplicates_with_duplicates(self):
        """Test finding duplicates in a list with duplicates."""
        assert set(find_duplicates([1, 2, 3, 2, 4, 3, 5])) == {2, 3}
        assert set(find_duplicates(['a', 'b', 'c', 'a', 'd'])) == {'a'}
        assert set(find_duplicates([1, 1, 1, 1])) == {1}

    def test_find_duplicates_no_duplicates(self):
        """Test finding duplicates in a list with no duplicates."""
        assert find_duplicates([1, 2, 3, 4, 5]) == []
        assert find_duplicates(['a', 'b', 'c', 'd']) == []
        assert find_duplicates([10]) == []

    def test_find_duplicates_empty_list(self):
        """Test finding duplicates in an empty list."""
        assert find_duplicates([]) == []

    def test_find_duplicates_all_same(self):
        """Test finding duplicates when all elements are the same."""
        assert set(find_duplicates([5, 5, 5, 5, 5])) == {5}
        assert set(find_duplicates(['x', 'x', 'x'])) == {'x'}

    def test_find_duplicates_mixed_types(self):
        """Test finding duplicates with mixed data types."""
        result = find_duplicates([1, '1', 2, '2', 1, '1'])
        assert 1 in result
        assert '1' in result

    def test_find_duplicates_multiple_pairs(self):
        """Test finding multiple different duplicate values."""
        result = set(find_duplicates([1, 2, 1, 3, 2, 4, 3]))
        assert result == {1, 2, 3}


class TestFlattenList:
    """Tests for flatten_list function."""

    def test_flatten_simple_nested_list(self):
        """Test flattening a simple nested list."""
        assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
        assert flatten_list([['a', 'b'], ['c', 'd']]) == ['a', 'b', 'c', 'd']

    def test_flatten_deeply_nested_list(self):
        """Test flattening a deeply nested list."""
        assert flatten_list([1, [2, [3, [4, 5]]]]) == [1, 2, 3, 4, 5]
        assert flatten_list([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) == [1, 2, 3, 4, 5, 6, 7, 8]

    def test_flatten_with_empty_sublists(self):
        """Test flattening with empty sublists."""
        assert flatten_list([1, [], 2, [3, []], 4]) == [1, 2, 3, 4]
        assert flatten_list([[], [], []]) == []

    def test_flatten_already_flat_list(self):
        """Test flattening an already flat list."""
        assert flatten_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        assert flatten_list(['a', 'b', 'c']) == ['a', 'b', 'c']

    def test_flatten_empty_list(self):
        """Test flattening an empty list."""
        assert flatten_list([]) == []

    def test_flatten_mixed_nesting_levels(self):
        """Test flattening with various nesting levels."""
        assert flatten_list([1, [2, 3], 4, [5, [6, 7]], 8]) == [1, 2, 3, 4, 5, 6, 7, 8]

    def test_flatten_single_element_nested(self):
        """Test flattening a single element in nested lists."""
        assert flatten_list([[[[[1]]]]]) == [1]


class TestMergeDicts:
    """Tests for merge_dicts function."""

    def test_merge_dicts_no_overlap(self):
        """Test merging dictionaries with no overlapping keys."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        assert merge_dicts(dict1, dict2) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    def test_merge_dicts_with_overlap(self):
        """Test merging dictionaries with overlapping keys."""
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        dict2 = {'b': 20, 'c': 30, 'd': 4}
        result = merge_dicts(dict1, dict2)
        assert result == {'a': 1, 'b': 20, 'c': 30, 'd': 4}

    def test_merge_dicts_empty_first(self):
        """Test merging with first dictionary empty."""
        dict1 = {}
        dict2 = {'a': 1, 'b': 2}
        assert merge_dicts(dict1, dict2) == {'a': 1, 'b': 2}

    def test_merge_dicts_empty_second(self):
        """Test merging with second dictionary empty."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        assert merge_dicts(dict1, dict2) == {'a': 1, 'b': 2}

    def test_merge_dicts_both_empty(self):
        """Test merging two empty dictionaries."""
        assert merge_dicts({}, {}) == {}

    def test_merge_dicts_nested_structures(self):
        """Test merging dictionaries with nested structures."""
        dict1 = {'a': 1, 'b': {'x': 10, 'y': 20}}
        dict2 = {'c': 3, 'd': {'z': 30}}
        result = merge_dicts(dict1, dict2)
        assert result == {'a': 1, 'b': {'x': 10, 'y': 20}, 'c': 3, 'd': {'z': 30}}

    def test_merge_dicts_nested_overlap(self):
        """Test merging with overlapping keys containing nested structures."""
        dict1 = {'a': 1, 'nested': {'x': 10}}
        dict2 = {'a': 2, 'nested': {'y': 20}}
        result = merge_dicts(dict1, dict2)
        assert result['a'] == 2
        assert result['nested'] == {'y': 20}

    def test_merge_dicts_does_not_modify_originals(self):
        """Test that merging does not modify original dictionaries."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 20, 'c': 3}
        merge_dicts(dict1, dict2)
        assert dict1 == {'a': 1, 'b': 2}
        assert dict2 == {'b': 20, 'c': 3}


class TestGroupByKey:
    """Tests for group_by_key function."""

    def test_group_by_key_simple(self):
        """Test grouping by a simple key."""
        items = [
            {'name': 'Alice', 'age': 30},
            {'name': 'Bob', 'age': 25},
            {'name': 'Charlie', 'age': 30}
        ]
        result = group_by_key(items, 'age')
        assert result[30] == [{'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 30}]
        assert result[25] == [{'name': 'Bob', 'age': 25}]

    def test_group_by_key_string_values(self):
        """Test grouping by string key values."""
        items = [
            {'name': 'Alice', 'department': 'Engineering'},
            {'name': 'Bob', 'department': 'Sales'},
            {'name': 'Charlie', 'department': 'Engineering'}
        ]
        result = group_by_key(items, 'department')
        assert len(result['Engineering']) == 2
        assert len(result['Sales']) == 1

    def test_group_by_key_missing_key_in_some_items(self):
        """Test grouping when some items don't have the key."""
        items = [
            {'name': 'Alice', 'age': 30},
            {'name': 'Bob'},
            {'name': 'Charlie', 'age': 30}
        ]
        result = group_by_key(items, 'age')
        assert 30 in result
        assert len(result[30]) == 2
        assert len(result) == 1

    def test_group_by_key_empty_list(self):
        """Test grouping an empty list."""
        assert group_by_key([], 'key') == {}

    def test_group_by_key_all_unique_values(self):
        """Test grouping where all items have unique key values."""
        items = [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'},
            {'id': 3, 'name': 'Charlie'}
        ]
        result = group_by_key(items, 'id')
        assert len(result) == 3
        assert len(result[1]) == 1
        assert len(result[2]) == 1
        assert len(result[3]) == 1

    def test_group_by_key_all_same_value(self):
        """Test grouping where all items have the same key value."""
        items = [
            {'name': 'Alice', 'status': 'active'},
            {'name': 'Bob', 'status': 'active'},
            {'name': 'Charlie', 'status': 'active'}
        ]
        result = group_by_key(items, 'status')
        assert len(result) == 1
        assert len(result['active']) == 3

    def test_group_by_key_nonexistent_key(self):
        """Test grouping by a key that doesn't exist in any items."""
        items = [
            {'name': 'Alice', 'age': 30},
            {'name': 'Bob', 'age': 25}
        ]
        result = group_by_key(items, 'department')
        assert result == {}


class TestSortByMultipleKeys:
    """Tests for sort_by_multiple_keys function."""

    def test_sort_by_single_key(self):
        """Test sorting by a single key."""
        items = [
            {'name': 'Charlie', 'age': 30},
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 35}
        ]
        result = sort_by_multiple_keys(items, ['name'])
        assert result[0]['name'] == 'Alice'
        assert result[1]['name'] == 'Bob'
        assert result[2]['name'] == 'Charlie'

    def test_sort_by_multiple_keys_in_order(self):
        """Test sorting by multiple keys with priority order."""
        items = [
            {'name': 'Bob', 'age': 30, 'score': 85},
            {'name': 'Alice', 'age': 25, 'score': 90},
            {'name': 'Bob', 'age': 25, 'score': 80},
            {'name': 'Alice', 'age': 30, 'score': 95}
        ]
        result = sort_by_multiple_keys(items, ['name', 'age'])
        assert result[0] == {'name': 'Alice', 'age': 25, 'score': 90}
        assert result[1] == {'name': 'Alice', 'age': 30, 'score': 95}
        assert result[2] == {'name': 'Bob', 'age': 25, 'score': 80}
        assert result[3] == {'name': 'Bob', 'age': 30, 'score': 85}

    def test_sort_by_numeric_values(self):
        """Test sorting by numeric key values."""
        items = [
            {'id': 3, 'value': 100},
            {'id': 1, 'value': 200},
            {'id': 2, 'value': 150}
        ]
        result = sort_by_multiple_keys(items, ['id'])
        assert result[0]['id'] == 1
        assert result[1]['id'] == 2
        assert result[2]['id'] == 3

    def test_sort_by_mixed_data_types(self):
        """Test sorting with mixed data types."""
        items = [
            {'name': 'Bob', 'age': 30},
            {'name': 'Alice', 'age': 25},
            {'name': 'Charlie', 'age': 30}
        ]
        result = sort_by_multiple_keys(items, ['age', 'name'])
        assert result[0] == {'name': 'Alice', 'age': 25}
        assert result[1] == {'name': 'Bob', 'age': 30}
        assert result[2] == {'name': 'Charlie', 'age': 30}

    def test_sort_empty_list(self):
        """Test sorting an empty list."""
        assert sort_by_multiple_keys([], ['key']) == []

    def test_sort_single_item(self):
        """Test sorting a list with a single item."""
        items = [{'name': 'Alice', 'age': 30}]
        result = sort_by_multiple_keys(items, ['name'])
        assert result == items

    def test_sort_with_missing_keys(self):
        """Test sorting when some items don't have all keys."""
        items = [
            {'name': 'Charlie', 'age': 30},
            {'name': 'Alice'},
            {'name': 'Bob', 'age': 25}
        ]
        result = sort_by_multiple_keys(items, ['age', 'name'])
        assert result[0]['name'] == 'Alice'
        assert result[1]['name'] == 'Bob'
        assert result[2]['name'] == 'Charlie'

    def test_sort_does_not_modify_original(self):
        """Test that sorting does not modify the original list."""
        items = [
            {'name': 'Charlie', 'age': 30},
            {'name': 'Alice', 'age': 25}
        ]
        original_order = [item['name'] for item in items]
        sort_by_multiple_keys(items, ['name'])
        assert [item['name'] for item in items] == original_order

    def test_sort_three_keys(self):
        """Test sorting by three keys in priority order."""
        items = [
            {'dept': 'Sales', 'level': 'Senior', 'name': 'Bob'},
            {'dept': 'Engineering', 'level': 'Junior', 'name': 'Alice'},
            {'dept': 'Sales', 'level': 'Junior', 'name': 'Charlie'},
            {'dept': 'Engineering', 'level': 'Senior', 'name': 'Dave'}
        ]
        result = sort_by_multiple_keys(items, ['dept', 'level', 'name'])
        assert result[0]['name'] == 'Alice'
        assert result[1]['name'] == 'Dave'
        assert result[2]['name'] == 'Charlie'
        assert result[3]['name'] == 'Bob'
