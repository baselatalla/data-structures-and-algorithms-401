class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'its a node with value :{self.value} and pointing for : {self.next}'


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        
        if not self.head:
            self.head = Node(value)
        else:
            raise Exception(f"This list already has a head! , try '.append({value})'")

    def includes(self, checkvalue):
        """
        Adds a node of a value to the head of LinkedList
        """
        if self.head != None:
            nodes_values = self.head
            while (nodes_values):
                if nodes_values.value == checkvalue:
                    return True
                nodes_values = nodes_values.next
            return False
        else:
            raise Exception("This list is empty! ,try to insert valus frist")



    def __str__(self):
        if self.head :
            
            nodes_values = self.head
            string = f''
            while (nodes_values):
                string += '{'+str(nodes_values.value)+'}->'
                nodes_values = nodes_values.next
            return string + "NULL"
        else:
            raise Exception("This list is empty! , nothing to print")



    def append(self, value):

        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)



    def insertBefore(self,value,newVal):
        """
         In this method we new node with the given value before the value node
        """
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                break
            current = current.next
        if current.next is None:
            raise Exception(f"The list hasn't include {value}, insert valide node ")
        else:
            node = Node(newVal)
            node.next = current.next
            current.next = node  



    def insertAfter(self,value,newVal):
        """
         which add a new node with the given newValue immediately after the first value node
        """
        current = self.head
        while current is not None:
            if current.value == value:
                break
            current = current.next
        if current is None:
            raise Exception(f"The list hasn't include {value}, insert valide node " )
        else:
            new_node = Node(newVal)
            new_node.next = current.next
            current.next = new_node  
    

            


if __name__ == "__main__":
    list = LinkedList()
    list.insert(46)
    list.append(55)
    list.append(66)
    list.append(10)
    print(list)
    # print(list.includes(10))
    # list.insert(55)
