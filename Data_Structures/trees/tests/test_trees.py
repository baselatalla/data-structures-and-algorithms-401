from trees import __version__
from trees.tree import Binary_Search_Tree, Tree, Node ,k_ary_tree, k_ary_Node, tree_fizz_buzz, preorderTraversal
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

def test_maxvalue():
    bst = Binary_Search_Tree()
    bst.Add(10)
    bst.Add(8)
    bst.Add(20)
    bst.Add(40)

    assert bst.maximum_value() == 40

def test_maximum_value():
    bst = Binary_Search_Tree()
    bst.Add(10)
    bst.Add(12)
    bst.Add(21)
    bst.Add(50)
    bst.Add(1000)
    bst.Add(700)
    assert bst.maximum_value()== 1000
    
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

def test_breadth_first():
    bst = Binary_Search_Tree()
    bst.Add(10)
    bst.Add(8)
    bst.Add(20)
    bst.Add(10)
    bst.Add(25)
    bst.Add(88)
    bst.Add(7)

    assert bst.breadth_first() == [10, 8, 20, 7, 10, 25, 88]

def test_breadth_first1():
    bst = Binary_Search_Tree()
    bst.Add(10)
    bst.Add(12)
    bst.Add(21)
    bst.Add(50)
    bst.Add(1000)
    bst.Add(700)
    
    assert bst.breadth_first() == [10, 12, 21, 50, 1000, 700]

def test_k_ary_tree():
    k_tree = k_ary_tree()
    k_tree.root = k_ary_Node(1)
    k_tree.root.child.append(k_ary_Node(2))
    k_tree.root.child.append(k_ary_Node(3))
    k_tree.root.child.append(k_ary_Node(4)) 
    k_tree.root.child[0].child.append(k_ary_Node(5)) 
    k_tree.root.child[0].child[0].child.append(k_ary_Node(10)) 
    k_tree.root.child[0].child.append(k_ary_Node(6)) 
    k_tree.root.child[0].child[1].child.append(k_ary_Node(11))
    k_tree.root.child[0].child[1].child.append(k_ary_Node(12))
    k_tree.root.child[0].child[1].child.append(k_ary_Node(13)) 
    k_tree.root.child[2].child.append(k_ary_Node(15))
    k_tree.root.child[2].child.append(k_ary_Node(8))
    k_tree.root.child[2].child.append(k_ary_Node(9))

    new_tree = tree_fizz_buzz(k_tree)          
    assert new_tree.root.child[0].value == '2'
    assert new_tree.root.child[1].value == 'fizz'
    assert new_tree.root.child[2].value == '4'
    assert new_tree.root.child[0].child[0].value == 'buzz' 
    assert new_tree.root.child[0].child[0].child[0].value == 'buzz'
    assert new_tree.root.child[0].child[1].value == 'fizz'
    assert new_tree.root.child[0].child[1].child[0].value == '11'
    assert new_tree.root.child[0].child[1].child[1].value == 'fizz'
    assert new_tree.root.child[0].child[1].child[2].value == '13'
    assert k_tree.root.child[2].child[0].value == 'fizzbuzz'
    assert k_tree.root.child[2].child[1].value == '8'
    assert k_tree.root.child[2].child[2].value == 'fizz'

    


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

