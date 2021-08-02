class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.front == None:
            self.front = node  
            self.rear = node
        else:

            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.isEmpty():
           temp = self.front 
           self.front = temp.next
           temp.next = None
           return temp.value
        else:
            return ("This Queue are empty, try to fill it first !")


    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False

    def peek(self):
        try:
            return self.front.value
        except:
            return "This is Empty Queue"
