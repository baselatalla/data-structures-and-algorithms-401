from ll_zip.linked_list import Node ,LinkedList

def zip_lists(list1, llist2):
        fst1_list = list1.head
        sec2_list = llist2.head
        the_pointer = None

        if not fst1_list:
            return sec2_list
        if not sec2_list:
            return fst1_list
        if fst1_list and sec2_list:
            the_pointer = fst1_list
            fst1_list = the_pointer.next
            new_head = the_pointer
        while fst1_list and sec2_list:
            the_pointer.next = sec2_list
            the_pointer = sec2_list
            sec2_list = the_pointer.next
            the_pointer.next = fst1_list
            the_pointer = fst1_list
            fst1_list = the_pointer.next

        if not fst1_list:
            the_pointer.next = sec2_list
        if not sec2_list:
            the_pointer.next = fst1_list
            
        return new_head