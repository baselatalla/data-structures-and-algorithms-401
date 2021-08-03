from graph_business_trip import __version__
from graph_business_trip.business_trip import * 

def test_version():
    assert __version__ == '0.1.0'
    
def ready_graph():
    g=Graphs()
    a=g.add_node('Pandora')
    b=g.add_node('Arendelle')
    c=g.add_node('Metroville')
    d=g.add_node('Monstropolis')
    e=g.add_node('Naboo')
    f=g.add_node('Narnia')

    g.add_edge(a,b,150)
    g.add_edge(b,a,150)
    g.add_edge(a,c,82)   
    g.add_edge(c,a,82)   
    g.add_edge(b,c,99)
    g.add_edge(c,b,99)
    g.add_edge(b,d,42)
    g.add_edge(d,b,42)
    g.add_edge(c,d,105)
    g.add_edge(d,c,105)
    g.add_edge(c,e,26)
    g.add_edge(e,c,26)
    g.add_edge(c,f,37)
    g.add_edge(f,c,37)
    g.add_edge(d,e,73)
    g.add_edge(e,d,73)
    g.add_edge(e,f,250)
    g.add_edge(f,e,250)
    return g


def test_graph_business_trip_1():
    graph = ready_graph()
    path1 = ['Metroville', 'Pandora',]
    actual = graph_business_trip(graph,path1)
    expected = f'{True} , $82'
    assert actual == expected


def test_graph_business_trip_2():
    graph = ready_graph()
    path2 = ['Arendelle', 'Monstropolis', 'Naboo']
    actual = graph_business_trip(graph,path2)
    expected = f'{True} , $115'
    assert actual == expected
    

def test_graph_business_trip_3():
    graph = ready_graph()
    path3 = ['Naboo', 'Pandora']
    actual = graph_business_trip(graph,path3)
    expected = f'{False} , $0'
    assert actual == expected


def test_graph_business_trip_4():
    graph = ready_graph()
    path4 = ['Narnia', 'Arendelle', 'Naboo']
    actual = graph_business_trip(graph,path4)
    expected = f'{False} , $0'
    assert actual == expected


def test_graph_business_trip_5():
    graph = ready_graph()
    path5 = ['Pandora', 'Arendelle', 'Monstropolis','Naboo','Narnia']
    actual = graph_business_trip(graph,path5)
    expected = f'{True} , $515'
    assert actual == expected
