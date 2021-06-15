from ll_zip.ll_zip import zip_lists
from ll_zip.linked_list import LinkedList ,Node
from ll_zip import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_zip_list_correct_input_and_output():
    list1 = LinkedList()
    list1.insert(1)
    list1.append(3)
    list1.append(2)

    list2 = LinkedList()
    list2.insert(5)
    list2.append(9)
    list2.append(8)
    zip_lists(list1,list2)

    actual = list1.__str__()
    expected ='{1}->{5}->{3}->{9}->{2}->{8}->NULL'
    assert expected ==actual

def test_not_equal():
    list1 = LinkedList()
    test2 = LinkedList()
    list1.append(11)
    list1.append(33)
    test2.append(50)
    test2.append(90)
    test2.append(40)
    zip_lists(list1,test2)
    expected = "{11}->{50}->{33}->{90}->{40}->NULL"
    actual = list1.__str__()
    assert expected == actual

def test_not_equal2():
    list1 = LinkedList()
    test2 = LinkedList()
    list1.append(12)
    list1.append(32)
    list1.append(22)
    test2.append(52)
    test2.append(92)
    zip_lists(list1,test2)
    expected ="{12}->{52}->{32}->{92}->{22}->NULL"
    actual = list1.__str__()
    assert expected == actual

