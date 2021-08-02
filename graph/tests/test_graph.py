from graph import __version__
from graph.graph import *
import pytest
def test_version():
    assert __version__ == '0.1.0'


def test_add_node():
    graph = Graphs()
    assert graph.add_node('a').value == 'a'

def test_add_node2():

    graph = Graphs()

    expected = 'spam'  # a vertex's value that comes back

    actual = graph.add_node('spam').value

    assert actual == expected

def test_add_edge():
    graph = Graphs()

    node1 = graph.add_node('a')

    node2 = graph.add_node('b')

    graph.add_edge(node1,node2)

    assert  graph.adjacency_list[node1][0].node == node2



def test_size_empty():

    graph = Graphs()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graphs()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected



def test_get_nodes():
    graph = Graphs()
    graph.add_node('a')
    graph.add_node('b')
    expected = 2
    actual = len(graph.get_nodes())

    assert actual == expected


def test_get_neighbors():

    graph = Graphs()

    a = graph.add_node('a')

    b = graph.add_node('b')

    graph.add_edge(a, b, 90)

    neighbors = graph.get_neighbors(a)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.node.value == 'b'

    assert neighbor_edge.weight == 90

def test_get_Null():
    graph = Graphs()
    
    assert graph.get_nodes() == "NULL"

def test_breadth_first1():
    g=Graphs()
    a=g.add_node('a')
    b=g.add_node('b')
    c=g.add_node('c')
    d=g.add_node('d')

    g.add_edge(a,b,5)
    g.add_edge(a,c,4)   
    g.add_edge(c,d,3)
    g.add_edge(b,d,3)

    actual = g.breadth_first(a)
    expected = ['a', 'b', 'c', 'd']

    assert actual == expected 

def test_breadth_frist2():
    g=Graphs()
    a=g.add_node('a')
    b=g.add_node('b')
    c=g.add_node('c')
    d=g.add_node('d')
    e=g.add_node('e')
    f=g.add_node('f')

    g.add_edge(a,b,5)
    g.add_edge(a,c,4)   
    g.add_edge(c,d,3)
    g.add_edge(b,d,3)
    g.add_edge(d,e,3)
    g.add_edge(d,f,3)

    actual = g.breadth_first(a)
    expected = ['a', 'b', 'c', 'd', 'e', 'f']

    assert actual == expected 

def test_breadth_frist3():
    g=Graphs()
    a=g.add_node('Pandora')
    b=g.add_node('Arendelle')
    c=g.add_node('Metroville')
    d=g.add_node('Monstroplolis')
    e=g.add_node('Narnia')
    f=g.add_node('Naboo')

    g.add_edge(a,b,5)
    g.add_edge(b,c,4)   
    g.add_edge(b,d,3)
    g.add_edge(c,b,3)
    g.add_edge(c,d,3)
    g.add_edge(c,f,3)
    g.add_edge(c,e,3)
    g.add_edge(d,b,3)
    g.add_edge(d,b,3)
    g.add_edge(d,b,3)

    actual = g.breadth_first(a)
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']

    assert actual == expected 

