from trees import __version__
from trees.tree import Binary_Search_Tree, Tree, Node
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_Can_successfully_return_a_collection_from_a_preorder_traversal(prepared_tree):
    assert prepared_tree.preOrder() == ['A', 'B', 'D', 'E', 'C', 'F']


def test_Can_successfully_return_a_collection_from_an_inorder_traversal(prepared_tree):
    assert prepared_tree.inOrder() == ['D', 'B', 'E', 'A', 'F', 'C']


def test_Can_successfully_return_a_collection_from_a_postorder_traversal(prepared_tree):
    assert prepared_tree.postOrder() == ['D', 'E', 'B', 'F', 'C', 'A']

def test_Can_successfully_instantiate_an_empty_tree():
    tree = Tree()
    actual = tree.root 
    expected = None
    
    assert actual == expected
   
def test_Can_successfully_instantiate_a_tree_with_a_single_root_node():
    tree = Tree()
    tree.root = Node('hi i am the root')
    actual = tree.root.value
    expected = 'hi i am the root'
    
    assert actual == expected

def test_Can_successfully_add_a_left_child_and_right_child_to_a_single_root_node():
    tree = Tree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    actual = tree.root.left.value
    actual1 = tree.root.right.value
    expected = 'B'
    expected1 = 'C'
    assert actual == expected
    assert actual1 == expected1


def test_pre_order_empty_tree():
    tree = Tree()
    assert tree.preOrder() == []


def test_BinarySearchTree():
    bst = Binary_Search_Tree()
    bst.Add(10)
    bst.Add(8)
    bst.Add(20)
    bst.Add(40)

    assert bst.preOrder() == [10, 8, 20, 40]
    assert bst.root.value == 10
    assert bst.root.left.value == 8
    assert bst.root.right.value == 20
    assert bst.root.right.right.value == 40


def test_BinarySearchTree1():
    tree = Binary_Search_Tree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    tree.Add('H')
    assert tree.preOrder() == ['A', 'B', 'D', 'E', 'C', 'F','H']



    
def test_BinarySearchTree_contains():
    bst = Binary_Search_Tree()
    bst.Add(10)
    bst.Add(8)
    bst.Add(20)
    bst.Add(10)
    bst.Add(25)
    bst.Add(88)
    bst.Add(7)

    assert bst.Contains(5) == False
    assert bst.Contains(88) == True
    assert bst.Contains(10) == True
    assert bst.Contains(7) == True
    assert bst.Contains(100) == False

@pytest.fixture
def prepared_tree():
    tree = Tree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    return tree

