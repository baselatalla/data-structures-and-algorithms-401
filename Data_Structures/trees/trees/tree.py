from collections import deque

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = value
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
            return temp
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


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


class Tree:
    def __init__(self):
        self.root = None

    def preOrder(self):
        output = []
        if not self.root:
            return output

        def traversal(node):

            output.append(node.value)

            if node.left:
                traversal(node.left)
            if node.right:
                traversal(node.right)

        traversal(self.root)

        return output

    def inOrder(self):
        output = []
        if not self.root:
            return output

        def traversal(node):

            if node.left:
                traversal(node.left)

            output.append(node.value)

            if node.right:
                traversal(node.right)

        traversal(self.root)

        return output

    def postOrder(self):
        output = []
        if not self.root:
            return output

        def traversal(node):

            if node.left:
                traversal(node.left)

            if node.right:
                traversal(node.right)

            output.append(node.value)

        traversal(self.root)

        return output

    def maximum_value(self):
        if self.root == None:
            return "This is empty tree"
        node = self.root
        global max_value
        max_value = node.value

        def maximum(node):
            global max_value
            if not node:
                return max_value
            if node.value > max_value:
                max_value = node.value
            maximum(node.left)
            maximum(node.right)
        maximum(self.root)

        return max_value

    def breadth_first(self):
        Queue_breadth = Queue()
        output = []
        node = self.root
        Queue_breadth.enqueue(node)

        while Queue_breadth.front:
            node_front = Queue_breadth.dequeue()
            output += [node_front.value]
            if node_front.left:
                Queue_breadth.enqueue(node_front.left)

            if node_front.right:
                Queue_breadth.enqueue(node_front.right)

        return output


class Binary_Search_Tree(Tree):
    def Add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            node = self.root
            while True:
                if node.value >= value:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(value)
                        break
                elif node.value < value:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(value)
                        break

    def Contains(self, value):
        if not self.root:
            return "the tree is empty"
        else:
            node = self.root
            while node.right != None or node.left != None:
                if node.value == value:
                    return True
                elif node.value < value:
                    node = node.right
                elif node.value > value:
                    node = node.left
                if node.value == value:
                    return True
            return False

# _________________________________________________ lab-18 _________________________


class k_ary_Node:
    def __init__(self, value):
        self.value = value
        self.child = []

class k_ary_tree:
    def __init__(self):
        self.root = None

def tree_fizz_buzz(tree):
    if tree.root == None:
        return "This is empty tree, insert a tree with data"

    new_tree = tree
    node = new_tree.root

    def fizz_buzz(value):
        if value % 3 == 0 and value % 5 == 0:
            return 'fizzbuzz'
        elif value % 3 == 0:
            return 'fizz'
        elif value % 5 == 0:
            return 'buzz'
        else:
            return str(value)

    def traversal(node):
        node.value = fizz_buzz(node.value)
        if len(node.child) > 0:
            for child in node.child :
                traversal(child)
        
    traversal(node)

    return new_tree


# ***********************************************************************************


if __name__ == '__main__':
    bst = Binary_Search_Tree()
    bst.Add(10)
    bst.Add(8)
    bst.Add(20)
    bst.Add(10)
    bst.Add(25)
    bst.Add(88)
    bst.Add(7)

   
    
    print(bst.breadth_first())
    print(bst.preOrder())
