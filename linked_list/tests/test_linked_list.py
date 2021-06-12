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

def test_str():
    list3 = LinkedList()
    list3.insert(46)
    list3.append(55)
    list3.append(66)
    actual = list3.__str__()
    expected = '{46}->{55}->{66}->NULL'
    assert actual == expected

    