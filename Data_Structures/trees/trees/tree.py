class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None 


    def  preOrder(self):
        output =[] 
        if not self.root:
            return output

        def traversal(node):

            output.append(node.value)

            if node.left :
                traversal(node.left)
            if node.right:
                traversal(node.right)
           
        traversal(self.root)

        return output 

    def inOrder(self):
        output =[] 
        if not self.root:
            return output

        def traversal(node):


            if node.left :
                traversal(node.left)

            output.append(node.value)

            if node.right:
                traversal(node.right)
           
        traversal(self.root)
        
        return output 

    def  postOrder(self):
        output =[] 
        if not self.root:
            return output

        def traversal(node):


            if node.left :
                traversal(node.left)

            if node.right:
                traversal(node.right)
                
            output.append(node.value)
           
        traversal(self.root)
        
        return output  


class Binary_Search_Tree(Tree):
    def Add(self,value):
        if not self.root:
            self.root = Node(value)
        else:
            node = self.root
            while True :
                if node.value >= value:
                    if node.left:
                        node = node.left
                    else :
                        node.left = Node(value)
                        break
                elif node.value < value:
                    if node.right:
                        node = node.right
                    else :
                        node.right = Node(value)
                        break


    def Contains(self,value):
        if not self.root:
            return "the tree is empty"
        else:
            node = self.root
            while node.right!= None or node.left != None:
                if node.value == value :
                    return True
                elif node.value < value:
                    node= node.right
                elif node.value > value:
                    node = node.left
                if node.value == value :
                    return True
            return False
            





if __name__ == '__main__':
    bst = Binary_Search_Tree()
    bst.Add(10)
    bst.Add(8)
    bst.Add(20)
    bst.Add(10)
    bst.Add(25)
    bst.Add(88)
    bst.Add(7)
    print(bst.preOrder())