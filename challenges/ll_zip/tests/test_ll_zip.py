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
    list3 = zip_lists(list1,list2)

    actual = list3.__str__()
    expected = '{1}->{5}->{3}->{9}->{2}->NULL'
    assert expected ==actual

# def test_zip_lists_one_empty_list(data):
#     list1.appened(1)
#     list1.appened(3)
#     list1.appened(2)

#     actual = zip_lists(list1,list2)
#     expected =[1,3,2]
#     assert expected == actual

# def test_zip_lists_both_empty(data):

#     actual = zip_lists(list1,list2)
#     expected = []
#     assert expected == actual