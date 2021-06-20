from queue_with_stacks import __version__
from queue_with_stacks.queue_with_stacks import PseudoQueue


def test_version():
    assert __version__ == '0.1.0'


def test_enqueue_singl():
    Pseudoqueue = PseudoQueue()
    Pseudoqueue.enqueue(81)
    actual = Pseudoqueue.rear
    expected = 81
    assert expected == actual


def test_enqueue_multiple():
    Pseudoqueue = PseudoQueue()
    Pseudoqueue.enqueue(55)
    Pseudoqueue.enqueue(66)
    Pseudoqueue.enqueue(77)
    actual = Pseudoqueue.rear
    expected = 77
    assert expected == actual


def test_Can_successfully_dequeue0():
    queue = PseudoQueue()
    queue.enqueue(5)
    queue.enqueue(10)
    queue.dequeue()
    actual = queue.front.value
    expected = 10
    assert expected == actual


def test_Can_successfully_dequeue1():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(82)
    queue.enqueue(99)

    actual = queue.dequeue()
    expected = 1
    assert actual == expected

def test_dequeue():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    actual = queue.dequeue()
    expected = None
    assert expected == actual