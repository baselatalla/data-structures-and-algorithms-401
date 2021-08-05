from .queue_stack import Queue, Stack


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Edge():
    def __init__(self, node, weight=None):
        self.node = node
        self.weight = weight


class Graphs():
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self, node1, node2, weghit=None):
        if node1 and node2 in self.adjacency_list:
            if weghit != None:
                self.adjacency_list[node1].append(Edge(node2, weghit))
            else:
                self.adjacency_list[node1].append(Edge(node2))

    def get_nodes(self):
        if self.adjacency_list.keys():
            return self.adjacency_list.keys()
        else:
            return "NULL"

    def get_neighbors(self, node):
        return self.adjacency_list[node]

    def size(self):
        return len(self.adjacency_list)

    def breadth_first(self, vertex):
        breadth = Queue()
        nodes = []
        visited = []

        breadth.enqueue(vertex)
        visited.append(vertex)

        while breadth.front:
            front = breadth.dequeue()
            nodes.append(front.value)

            for child in self.adjacency_list[front]:
                if child.node not in visited:
                    visited.append(child.node)
                    breadth.enqueue(child.node)

        return nodes

    def depth_first(self, node):
        depth = Stack()
        visited = []
        nodes = []
        depth.push(node)
        while depth.top != None:
            top = depth.pop()
            childern = self.adjacency_list[top]
            child_nodes = []
            for child in childern:
                child_nodes.append(child.node)   
            if all(n in visited for n in child_nodes):
                visited.append(top)
                nodes.append(top.value)
                depth.pop()
            else:
                for child in child_nodes:
                    if child not in visited:
                        depth.push(child)

                visited.append(top)
                nodes.append(top.value)
               
        return nodes



g=Graphs()
a=g.add_node('Pandora')
b=g.add_node('Arendelle')
c=g.add_node('Metroville')
d=g.add_node('Monstroplolis')
e=g.add_node('Naboo')
f=g.add_node('Narnia')

g.add_edge(a,b,5)
g.add_edge(b,c,4)   
g.add_edge(b,d,3)
g.add_edge(c,b,3)
g.add_edge(c,d,3)
g.add_edge(c,f,3)
g.add_edge(c,e,3)
g.add_edge(d,b,3)
g.add_edge(d,c,3)
g.add_edge(d,f,3)
g.add_edge(f,c,3)
g.add_edge(f,d,3)
g.add_edge(f,e,3)
g.add_edge(e,c,3)
g.add_edge(e,f,3)


print(g.breadth_first(a))
print(g.depth_first(a))