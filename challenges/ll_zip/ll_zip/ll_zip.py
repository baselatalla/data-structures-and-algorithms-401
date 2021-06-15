from ll_zip.linked_list import Node ,LinkedList

def zip_lists(list1, list2):
    """
    this function , is takes two linked list
    and returned a new linked list-withc is merged of the two before
    """
    current1 = list1.head
    current2 = list2.head
    if not current1:
        list1.head = list2.head
        return list1.head
    if not current2:
        return list1.head
    pointer = current2.next
    while current1.next and current2.next:
        current2.next = current1.next
        current1.next= current2
        current1 = current2.next
        current2 = pointer
        pointer = pointer.next
    if not current1.next:
        current1.next = current2
        return list1.head
    if not current2.next:
        current2.next = current1.next
        current1.next = current2
        return list1.head

    