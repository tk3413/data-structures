import sort
import pytest
import unittest

@pytest.fixture
def unordered_list():
    return [3, 5, 1, 7, 15, 42, 0, -9, 3]

def test_merge_sort(unordered_list):
    s = sort.Sort()
    assert s.merge_sort(unordered_list) == [-9, 0, 1, 3, 3, 5, 7, 15,42]

def test_builtin_sort(unordered_list):
    s = sort.Sort()
    assert s.builtin_sort(unordered_list) == [-9, 0, 1, 3, 3, 5, 7, 15,42]

def test_divide_list(unordered_list):
    s = sort.Sort()
    assert s.divide_list(unordered_list) == ([3, 5, 1, 7], [15, 42,
                                                                0,-9,
                                                                3])

def test_get_mid(unordered_list):
    s = sort.Sort()
    assert s.get_middle(unordered_list) == 4
    unordered_list.pop()
    assert s.get_middle(unordered_list) == 4
