from hashmap_tree_intersection.trees import Tree
from hashmap_tree_intersection.tree_intersection import hashmap_tree_intersection
from hashmap_tree_intersection import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_tree_intersection():
    bst1 = Tree()
    bst1.Add(22)
    bst1.Add(8)
    bst1.Add(90)
    bst1.Add(10)
    bst1.Add(55)
    bst1.Add(38)
    bst1.Add(27)

    bst2 = Tree()
    bst2.Add(10)
    bst2.Add(8)
    bst2.Add(90)
    bst2.Add(10)
    bst2.Add(25)
    bst2.Add(88)
    bst2.Add(71)

    actual = hashmap_tree_intersection(bst1,bst2)
    print(actual)
    expected = [8, 10, 90]

    assert actual == expected

def test_intersection2():
    bst1 = Tree()
    bst2 = Tree()
    bst1.Add(1)
    bst1.Add(2)
    bst1.Add(3)
    bst2.Add(3)
    bst2.Add(12)
    bst2.Add(5)
    actual = hashmap_tree_intersection(bst1,bst2)
    expected = [3]
    assert actual == expected

def test_intersection3():
    bst1 = Tree()
    bst2 = Tree()
    bst1.Add(5)
    bst1.Add(20)
    bst1.Add(3)
    bst1.Add(30)
    bst2.Add(3)
    bst2.Add(20)
    bst2.Add(5)
    bst2.Add(17)
    actual = hashmap_tree_intersection(bst1,bst2)
    expected = [3,20,5]
    assert actual == expected