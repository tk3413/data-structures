import tree
import pytest
import unittest


# test tree:
#           2
#      1          4
#              3     5

@pytest.fixture
def node_1():
    return tree.Node(val=1, left=None, right=None)

@pytest.fixture
def node_3():
    return tree.Node(val=3, left=None, right=None)

@pytest.fixture
def node_5():
    return tree.Node(val=5, left=None, right=None)

@pytest.fixture
def node_4(node_3, node_5):
    return tree.Node(val=4, left=node_3, right=node_5)

@pytest.fixture
def node_2(node_1, node_4):
    return tree.Node(val=2, left=node_1, right=node_4)


def test_nodes(node_1, node_2, node_3, node_4, node_5):
    assert node_1.val == 1
    assert node_1.right == None and node_1.left == None
    assert node_2.val == 2
    assert node_2.left == node_1
    assert node_2.right == node_4
    assert node_3.val == 3
    assert node_3.left == None and node_3.right == None
    assert node_4.val == 4
    assert node_4.left == node_3 and node_4.right == node_5
    assert node_5.val == 5
    assert node_5.left == None and node_5.right == None

def test_dfs_recurs_preorder(node_1, node_2, node_3, node_4, node_5):
    t = tree.Tree()
    t.dfs_recurs_preord(node=node_2)
    print(t.visits)
    assert[v for v in t.visits if v is not None] == [2, 1, 4, 3, 5]


def test_dfs_recurs_inorder(node_1, node_2, node_3, node_4, node_5):
    t = tree.Tree()
    t.dfs_recurs_inord(node=node_2)
    print(t.visits)
    assert [v for v in t.visits if v is not None] == [1, 2, 3, 4, 5]

def test_dfs_recurs_postorder(node_1, node_2, node_3, node_4, node_5):
    t = tree.Tree()
    t.dfs_recurs_postord(node=node_2)
    assert [v for v in t.visits if v is not None] == [1, 3, 5, 4, 2]

def test_dfs_iterative(node_1, node_2, node_3, node_4, node_5):
    t = tree.Tree()
    t.dfs_iterative_preord(node=node_2)
    assert [v for v in t.visits if v is not None] == [2, 1, 4, 3, 5]

def test_bfs(node_1, node_2, node_3, node_4, node_5):
    t = tree.Tree()
    t.bfs(node_2)
    assert [v for v in t.visits if v is not None] == [2, 1, 4, 3, 5]
