from hashtable.hashtable import Hashtables
from hashtable import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_Adding_a_key_value_to_your_hashtable_results_in_the_value_being_in_the_data_structure():
    hashtable = Hashtables(10)
    hashtable.add('niv', 88)
    for index, item in enumerate(hashtable.map):
        if item:
            actual = (index, item.__str__()).__str__()
    expected = '(7, "{(\'niv\', 88)}->NULL")'
    assert actual == expected

def test_Retrieving_based_on_a_key_returns_the_value_stored():
    hashtable = Hashtables(1024)
    hashtable.add('niv', 88)
    hashtable.add('yook', 55)
    actual = hashtable.find('niv')
    expected = 88
    assert actual == expected

def test_Successfully_returns_null_for_a_key_that_does_not_exist_in_the_hashtable():
    hashtable = Hashtables(1024)
    hashtable.add('good', True)
    hashtable.add('doog', False)
    actual = hashtable.find('vin')
    expected = None
    assert actual == expected

def test_Successfully_handle_a_collision_within_the_hashtable():
    hashtable = Hashtables(1024)
    hashtable.add('good', True)
    hashtable.add('doog', False)
    actual = hashtable.map[623].__str__()
    expected = "{('good', True)}->{('doog', False)}->NULL"
    assert actual == expected


def test_Successfully_retrieve_a_value_from_a_bucket_within_the_hashtable_that_has_a_collision():
    hashtable = Hashtables(1024)
    hashtable.add('niv', 88)
    hashtable.add('vin', 55)
    actual = hashtable.find('vin')
    expected = 55
    assert actual == expected
    

def test_Successfully_hash_a_key_to_an_in_range_value():
    hashtable = Hashtables(1024)
    hashtable.add('ramy', 29)
    hashtable.add('roaa', 20)
    hashtable.add('yous', 25)
    hashtable.add('nuha', 50)
    hashtable.add('amany', 30)

    actual1 = hashtable.get_hash('ramy')
    actual2 = hashtable.get_hash('roaa')
    actual3 = hashtable.get_hash('yous')
    actual4 = hashtable.get_hash('nuha')
    actual5 = hashtable.get_hash('amany')

    expected1 = 991
    expected2 = 101
    expected3 = 432
    expected4 = 372
    expected5 = 378

    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3
    assert actual4 == expected4
    assert actual5 == expected5





