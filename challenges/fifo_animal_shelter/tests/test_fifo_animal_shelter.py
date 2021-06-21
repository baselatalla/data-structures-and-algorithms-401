from fifo_animal_shelter import __version__
from fifo_animal_shelter.fifo_animal_shelter import Cat, Dog, AnimalShelter


def test_version():
    assert __version__ == '0.1.0'



def test_enqueue_cat():
    shosho = Cat('shsho')
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(shosho)

    actual = animal_shelter.frontcat.name
    expected = 'shsho'
    assert actual == expected
    
def test_enqueue_dog():
    popy = Dog('popy')
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(popy)

    actual = animal_shelter.frontdog.name
    expected = 'popy'
    assert actual == expected


def test_enqueue_dog_and_cat():
    shosho = Cat('shsho')
    popy = Dog('popy')
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(popy)
    animal_shelter.enqueue(shosho)

    actual1 = animal_shelter.frontdog.name
    expected1 = 'popy'
    actual2 = animal_shelter.frontcat.name
    expected2 = 'shsho'
    assert actual1 == expected1
    assert actual2 == expected2


def test_dequeue_cat():
    shosho = Cat('shosho')
    shyshy = Cat('shyshy')
    
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(shyshy)
    animal_shelter.enqueue(shosho)
    animal_shelter.dequeue('cat')

    actual = animal_shelter.frontcat.name
    expected = 'shosho'
    assert actual == expected

def test_dequeue_dog():
    vik = Dog('vik')
    rox = Dog('rox')
    
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(rox)
    animal_shelter.enqueue(vik)
    animal_shelter.dequeue('dog')

    actual = animal_shelter.frontdog.name
    expected = 'vik'
    assert actual == expected

def test_dequeue_dog_and_cat():
    shosho = Cat('shsho')
    shyshy = Cat('shyshy')
    lolo = Cat('lolo')
    popy = Dog('popy')
    vik = Dog('vik')
    rox = Dog('rox')

    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(popy)
    animal_shelter.enqueue(shyshy)
    animal_shelter.enqueue(vik)
    animal_shelter.enqueue(rox)
    animal_shelter.enqueue(lolo)
    animal_shelter.enqueue(shosho)
    animal_shelter.dequeue('dog')
    actual4 = animal_shelter.dequeue('dog')
    animal_shelter.dequeue('cat')
    actual3 = animal_shelter.dequeue('cat')

    actual1 = animal_shelter.frontdog.name
    expected1 = 'rox'
    actual2 = animal_shelter.frontcat.name
    expected2 = 'shsho'
    expected3 = "lolo"
    expected4 = "vik"
    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3
    assert actual4 == expected4


def test_edge_case():
    
    vik = Dog('vik')
    rox = Dog('rox')
    
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(rox)
    animal_shelter.enqueue(vik)
    animal_shelter.dequeue('dog')
    animal_shelter.dequeue('dog')
    

    actual = animal_shelter.dequeue('dog')
    expected = 'null'
    assert actual == expected


def test_edge_case2():
    
    vik = Dog('vik')
    rox = Dog('rox')
    
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(rox)
    animal_shelter.enqueue(vik)
    animal_shelter.dequeue('dog')
    

    actual = animal_shelter.dequeue('lizzerd')
    expected = 'null'
    assert actual == expected