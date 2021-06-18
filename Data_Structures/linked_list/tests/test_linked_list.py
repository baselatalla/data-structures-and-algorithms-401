from linked_list import linked_list
import pytest 
from linked_list import __version__
from linked_list.linked_list import Node ,LinkedList


def test_version():
    assert __version__ == '0.1.0'


def test_instantiate():
    list0 = LinkedList()
    actual = list0.head
    expected = None
    assert actual == expected


def test_insert():
    list1 = LinkedList()
    list1.insert(5)
    actual = list1.__str__()
    expected = '{5}->NULL'
    assert actual == expected

def test_head_pointing():
    List2 = LinkedList()
    List2.insert(99)
    actual = List2.head.value
    expected = 99
    assert actual == expected

def test_insert_multiple_nodes():
    list3 = LinkedList()
    list3.insert(46)
    list3.append(55)
    list3.append(66)
    actual_head = list3.head.value
    expected_head = 46
    actual_second = list3.head.next.value
    expected_second = 55
    actual_third = list3.head.next.next.value
    expected_third = 66

    assert actual_head == expected_head
    assert actual_second == expected_second
    assert actual_third == expected_third

def  test_includes_if_true():
    list4 = LinkedList()
    list4.insert(46)
    list4.append(55)
    list4.append(66)
    actual = list4.includes(55)
    expected = True
    assert actual == expected

def  test_includes_if_fulse():
    list5 = LinkedList()
    list5.insert(46)
    list5.append(55)
    list5.append(66)
    actual = list5.includes(85)
    expected = False
    assert actual == expected

def test_str_and_append():
    list6 = LinkedList()
    list6.insert(46)
    list6.append(55)
    list6.append(66)
    actual = list6.__str__()
    expected = '{46}->{55}->{66}->NULL'
    assert actual == expected

def test_inseartBefor():
    list8 = LinkedList()
    list8.insert(46)
    list8.append(55)
    list8.append(66)
    list8.insertBefore(55,99)
    list8.insertBefore(46,99)
    actual = list8.__str__()
    expected = '{99}->{46}->{99}->{55}->{66}->NULL'
    assert actual == expected


def test_insertAfter():
    list7 = LinkedList()
    list7.insert(46)
    list7.append(55)
    list7.append(66)
    list7.insertAfter(55,99)
    list7.insertAfter(66,99)
    actual = list7.__str__()
    expected = '{46}->{55}->{99}->{66}->{99}->NULL'
    assert actual == expected

def test_kthFromEnd():
    list88 = LinkedList()
    list88.insert(5)
    list88.append(10)
    list88.append(15)
    list88.append(20)
    list88.append(25)
    list88.append(30)
    
    actual1 = list88.kthFromEnd(0)
    actual2 = list88.kthFromEnd(1)
    actual3 = list88.kthFromEnd(2)
    actual4 = list88.kthFromEnd(3)
    actual5 = list88.kthFromEnd(4)
    actual6 = list88.kthFromEnd(5)

    expected1 = 30
    expected2 = 25
    expected3 = 20
    expected4 = 15
    expected5 = 10
    expected6 = 5

    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3
    assert actual4 == expected4
    assert actual5 == expected5
    assert actual6 == expected6