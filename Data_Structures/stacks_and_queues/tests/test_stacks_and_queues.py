from stacks_and_queues import __version__
from stacks_and_queues.stacks_and_queues import Node, Queue, Stack


def test_version():
    assert __version__ == '0.1.0'


def test_Can_successfully_push_onto_a_stack():
    stack=Stack()
    stack.push(22)
    excepted=stack.top.value
    assert excepted == 22

def test_Can_successfully_push_multiple_values_onto_a_stack():
    stack=Stack()
    stack.push(22)
    stack.push(1)
    excepted=stack.top.value
    assert excepted == 1




def test_Can_successfully_pop_off_the_stack():
    stack = Stack()
    stack.push(5)
    stack.push(10)
    actual = stack.pop()
    expected = 10
    assert actual == expected


def test_Can_successfully_empty_a_stack_after_multiple_pops():
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push(20)
    stack.push(300)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.top
    expected = None
    assert actual == expected

def test_Can_successfully_peek_the_next_item_on_the_stack():
    stack=Stack()
    stack.push(33)
    stack.push(22)
    expected = 22
    actual=stack.peek() 
    assert actual == expected

def test_Can_successfully_instantiate_an_empty_stack():
    stack=Stack()
    expected=None
    assert expected==stack.top

def test_Calling_pop_or_peek_on_empty_stack_raises_exception():
   stack=Stack()
   expected="This is Empty stack"
   assert expected==stack.peek()


def test_Can_successfully_enqueue_into_a_queue():
    queue =Queue()
    queue.enqueue(5)
    actual = queue.front.value
    expected = 5
    assert expected == actual


def test_Can_successfully_enqueue_multiple_values_into_a_queue():
    queue =Queue()
    queue.enqueue(5)
    queue.enqueue(10)
    actual = queue.front.next.value
    expected = 10
    assert expected == actual

def test_Can_successfully_dequeue_out_of_a_queue_the_expected_value():
    queue =Queue()
    queue.enqueue(5)
    queue.enqueue(10)
    queue.dequeue()
    actual = queue.front.value
    expected = 10
    assert expected == actual

def test_Can_successfully_peek_into_a_queue_seeing_the_expected_value():
    queue=Queue()
    expected=None
    assert expected==queue.front

def test_Can_successfully_empty_a_queue_after_multiple_dequeues():
    queue=Queue()
    queue.enqueue(80)
    queue.enqueue(66)
    expected = 80
    actual=queue.peek() 
    assert actual == expected

def test_Can_successfully_instantiate_an_empty_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(82)
    queue.enqueue(99)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual =  queue.front
    expected = None
    assert actual == expected

def test_Calling_dequeue_or_peek_on_empty_queue_raises_exception():
    queue= Queue()
    expected="This is Empty Queue"
    assert expected==queue.peek()
