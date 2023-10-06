# Operations associated with queue are:

# Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
# Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
# Front: Get the front item from queue – Time Complexity : O(1)
# Rear: Get the last item from queue – Time Complexity : O(1)

from typing import Union
from collections import deque
import random

# Implementation using queue.Queue
# Queue is built-in module of Python which is used to implement a queue. queue.Queue(maxsize) initializes a variable to a maximum size of maxsize. A maxsize of zero ‘0’ means a infinite queue. This Queue follows FIFO rule.
# There are various functions available in this module:

# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
# qsize() – Return the number of items in the queue.

from queue import Queue


class QueueList:
    """Implementation using list
    List is a Python's built-in data structure that can be used as a queue.
    Instead of enqueue() and dequeue(), append() and pop() function is used.
    However, lists are quite slow for this purpose because inserting or deleting an element at the
    beginning requires shifting all of the other elements by one, requiring O(n) time.
    """

    def __init__(self) -> None:
        self.queue: list[int, float, str, bool] = list()

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def get_size(self) -> int:
        return len(self.queue)

    def front(self) -> Union[int, float, str, bool]:
        return self.queue[0]

    def rear(self) -> Union[int, float, str, bool]:
        return self.queue[-1]

    def enqueue_element(self, value: int) -> None:
        self.queue.append(value)

    def dequeue_element(self) -> Union[int, float, str, bool]:
        return self.queue.pop(0)

    def print_queue(self) -> None:
        print(self.queue)


class QueueDeque:
    '''Implementation using collections.deque
    Queue in Python can be implemented using deque class from the collections module.
    Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container,
    as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
    Instead of enqueue and deque, append() and popleft() functions are used.
    '''

    def __init__(self) -> None:
        self.queue: deque = deque()

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def get_size(self) -> int:
        return len(self.queue)

    def front(self) -> Union[int, float, str, bool]:
        return self.queue[0]

    def rear(self) -> Union[int, float, str, bool]:
        return self.queue[-1]

    def enqueue_element(self, value: int) -> None:
        self.queue.append(value)

    def dequeue_element(self) -> Union[int, float, str, bool]:
        return self.queue.popleft()

    def print_queue(self) -> None:
        print(self.queue)


if __name__ == "__main__":
    q = QueueList()

    print(q.is_empty())

    q.enqueue_element(value=random.randint(0, 100))
    q.enqueue_element(value=random.randint(0, 100))
    q.enqueue_element(value=random.randint(0, 100))

    print(q.is_empty())
    print(q.front())
    print(q.rear())

    q.enqueue_element(value=random.randint(0, 100))
    q.enqueue_element(value=random.randint(0, 100))
    q.enqueue_element(value=random.randint(0, 100))
    q.enqueue_element(value=random.randint(0, 100))

    q.print_queue()

    print(q.dequeue_element())
    print(q.dequeue_element())
    print(q.dequeue_element())

    print(q.get_size())
    q.print_queue()
