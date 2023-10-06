# The functions associated with stack are:

# empty() – Returns whether the stack is empty – Time Complexity: O(1)
# size() – Returns the size of the stack – Time Complexity: O(1)
# top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
# push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
# pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

from typing import Union
from collections import deque


# Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the put() function and get() takes data out from the Queue.
# There are various functions available in this module:

# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If the queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
# qsize() – Return the number of items in the queue.
from queue import LifoQueue


# Implementation using a singly linked list:
# The linked list has two methods addHead(item) and removeHead() that run in constant time. These two methods are suitable to implement a stack.

# getSize()– Get the number of items in the stack.
# isEmpty() – Return True if the stack is empty, False otherwise.
# peek() – Return the top item in the stack. If the stack is empty, raise an exception.
# push(value) – Push a value into the head of the stack.
# pop() – Remove and return a value in the head of the stack. If the stack is empty, raise an exception.


class StackList:
    """Python's built-in data structure list can be used as a stack.
    Instead of push(), append() is used to add elements to the top of the stack while pop() removes the element in LIFO order.
    Unfortunately, the list has a few shortcomings. The biggest issue is that it can run into speed issues as it grows.
    The items in the list are stored next to each other in memory, if the stack grows bigger than the block of memory that
    currently holds it, then Python needs to do some memory allocations. This can lead to some append() calls taking much longer than other ones.
    """

    def __init__(self) -> None:
        self.stack: list[int, float, str, bool] = list()

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def get_size(self) -> int:
        return len(self.stack)

    def top(self) -> Union[int, float, str, bool]:
        return self.stack[-1]

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop_element(self) -> Union[int, float, str, bool]:
        return self.stack.pop()

    def print_stack(self) -> None:
        print(self.stack)


class StackDeque:
    '''Python stack can be implemented using the deque class from the collections module.
    Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container,
    as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
    '''

    def __init__(self) -> None:
        self.stack: deque = deque()

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def get_size(self) -> int:
        return len(self.stack)

    def top(self) -> Union[int, float, str, bool]:
        return self.stack[-1]

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop_element(self) -> Union[int, float, str, bool]:
        return self.stack.pop()

    def print_stack(self) -> None:
        print(self.stack)


if __name__ == "__main__":
    # stack = StackList()
    stack = StackDeque()
    # stack = LifoQueue(maxsize=10)

    print(stack.is_empty())

    stack.push(value=1)
    stack.push(value=2)
    stack.push(value=3)

    print(stack.is_empty())
    print(stack.top())

    stack.push(value=4)
    stack.push(value=5)
    stack.push(value=6)
    stack.push(value=7)

    stack.print_stack()

    print(stack.pop_element())
    print(stack.pop_element())
    print(stack.pop_element())

    print(stack.get_size())
    stack.print_stack()
