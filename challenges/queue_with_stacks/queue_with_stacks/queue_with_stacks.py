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
            if temp.value == None :
                return "there is no data to dequeue"
            else:
                return temp.value
        else:
            return ("there is no data to dequeue")
        

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def peek(self):
        try:
            return self.top.value
        except:
            return ("there is no data to dequeue")

    def __str__(self):
        while self.top.next != None:
            pass


class PseudoQueue :
    def __init__(self):
        self.first_stack=Stack()
        self.secand_stack=Stack()
        self.front = None
        self.rear=None

    def enqueue(self , value):
        self.first_stack.push(value)
        self.rear=self.first_stack.top.value

    def dequeue(self):
        if self.first_stack.top :
            stack = self.first_stack
            while not stack.isEmpty():
                self.secand_stack.push(stack.pop())
            poped = self.secand_stack.pop()
            self.front = self.secand_stack.top
            self.first_stack = Stack()
            stack1 = self.secand_stack
            while not stack1.isEmpty():
                self.first_stack.push(stack1.pop())
                
            return poped



if __name__=="__main__" :
    queue= PseudoQueue()
    queue.enqueue(5)
    # print(queue)