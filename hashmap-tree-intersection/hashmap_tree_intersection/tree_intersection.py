from .trees import Tree

def hashmap_tree_intersection(tree1 , tree2):
    tree1_list = tree1.breadth_first()
    tree2_list = tree2.breadth_first()

    output = list(set(tree1_list) & set(tree2_list))
    return output



if __name__ == '__main__':
    bst1 = Tree()
    bst1.Add(22)
    bst1.Add(8)
    bst1.Add(90)
    bst1.Add(10)
    bst1.Add(55)
    bst1.Add(38)
    bst1.Add(27)

    bst2 = Tree()
    bst2.Add(10)
    bst2.Add(8)
    bst2.Add(90)
    bst2.Add(10)
    bst2.Add(25)
    bst2.Add(88)
    bst2.Add(71)

    print(hashmap_tree_intersection(bst1,bst2))