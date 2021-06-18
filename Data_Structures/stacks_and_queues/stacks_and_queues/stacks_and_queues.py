

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None


    def push(self, value):
        node = Node(value)
        if self.top == None:
            self.top = node 
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if not self.isEmpty():
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        else:
            return ("This stak are empty, try to fill it first !")
        

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def peek(self):
        try:
            return self.top.value
        except:
            return "This is Empty stack"

    def __str__(self):
        while self.top.next != None:
            pass




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


if __name__ == "__main__":
    # stack = Stack()
    # stack.push(5)
    # stack.push(10)
    # stack.push(15)
    # stack.push(20)
    # print(stack.pop())
    # stack.push(25)
    # print(stack.top.value)

    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    print(queue.dequeue())
    print(queue.front.value)
    print(queue.front.next.next.value)


    

