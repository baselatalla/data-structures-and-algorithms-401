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
    actual = list8.__str__()
    expected = '{46}->{99}->{55}->{66}->NULL'
    assert actual == expected


def test_insertAfter():
    list7 = LinkedList()
    list7.insert(46)
    list7.append(55)
    list7.append(66)
    list7.insertAfter(55,99)
    actual = list7.__str__()
    expected = '{46}->{55}->{99}->{66}->NULL'
    assert actual == expected

    