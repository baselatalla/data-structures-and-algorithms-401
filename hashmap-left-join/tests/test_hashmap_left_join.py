from hashmap_left_join import __version__
from hashmap_left_join.left_join import *



def test_version():
    assert __version__ == '0.1.0'


def test_join_1():
    table1 = Hashtables(800)
    table1.add('fond', 'enamored')
    table1.add('wrath', 'anger')
    table1.add('diligent', 'employed')
    table1.add('outfit', 'garb')
    table1.add('guide', 'usher')
    table2 = Hashtables(800)
    table2.add('fond', 'averse')
    table2.add('wrath', 'delight')
    table2.add('diligent', 'idle')
    table2.add('guide', 'follow')
    table2.add('flow', 'jam')
    assert left_join(table1, table2)==[['outfit', 'garb', None], ['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ['guide', 'usher', 'follow'], ['diligent', 'employed', 'idle']]

def test_join_2():
    table1 = Hashtables(800)
    table1.add('a', '1')
    table1.add('b', '2')
    table2 = Hashtables(800)
    table2.add('a', '')
    table2.add('k', '8')
    assert left_join(table1, table2)==[['b', '2', None], ['a', '1', '']]

def test_join_3():
    table1 = Hashtables(800)
    table1.add('a', '1')
    table1.add('b', '2')
    table1.add('z', '1')
    table1.add('k', '2')
    table2 = Hashtables(800)
    table2.add('a', '')
    table2.add('l', '8')
    table2.add('y', '7')
    table2.add('j', '8')
    assert left_join(table1, table2)==[['k', '2', None], ['z', '1', None],['b', '2', None],['a', '1', '']]