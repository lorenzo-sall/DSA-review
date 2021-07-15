class Stack:
    """
    implementation of the stack abstract data type
    using a python list where the elemtent at index 0 is
    the bottom of the stack
    access to the elemtents is by LIFO (last in first out)
    """

    def __init__(self):
        # the stack is created empty
        self.elemtents = []

    def is_empty(self):
        # returns True if the stack is empty
        return self.elemtents == []

    def push(self, elemtent):
        # push an elemtent to the top of the stack
        self.elemtents.append(elemtent)

    def pop(self):
        # pop one elemtent from the top of the stack
        return self.elemtents.pop()

    def peek(self):
        # it looks at the elemtent at the top of the stack
        return self.elemtents[len(self.elemtents) - 1]

    def size(self):
        # returns the number of elemtents in the stack
        return len(self.elemtents)

class Queue:
    """
    implementation of the queue abstract data type
    using a python list where the elemtent at index 0 is the rear of the queue
    and the elemtent at index (len(queue) -1) is the front
    with this implementation adding an elemtent will be O(n) and removing an
    elemtent will be O(1)
    access to the elemtents is by FIFO (first in first out)
    """

    def __init__(self):
        # the queue is created empty
        self.elemtents = []

    def is_empty(self):
        # returns True if the queue is empty
        return self.elemtents == []

    def enqueue(self, elemtent):
        # add an elemtent to the rear of the queue
        self.elemtents.insert(0, elemtent)

    def dequeue(self):
        # remove one elemtent from the front of the queue
        return self.elemtents.pop()

    def peek(self):
        # it looks at the elemtent at the front of the queue
        return self.elemtents[len(self.elemtents) - 1]

    def size(self):
        # returns the number of elemtents in the queue
        return len(self.elemtents)

class Deque:
    """
    implementation of the deque (double ended queue) abstract data type
    using a python list where the elemtent at index 0 is the rear of the deque
    and the elemtent at index (len(queue) -1) is the front
    """

    def __init__(self):
        # the queue is created empty
        self.elemtents = []

    def is_empty(self):
        # returns True if the queue is empty
        return self.elemtents == []

    def add_front(self, elemtent):
        # add an elemtent to the front of the deque
        self.elemtents.append(elemtent)

    def add_rear(self, elemtent):
        # add an elemtent to the rear of the deque
        self.elemtents.insert(0, elemtent)

    def remove_front(self):
        # remove one elemtent from the front of the deque
        return self.elemtents.pop()

    def remove_rear(self):
        # remove one elemtent from the rear of the deque
        return self.elemtents.pop(0)

    def peek(self):
        # looks at the elemtents at the front and rear of the deque
        return (self.elemtents[len(self.elemtents) - 1], self.elemtents[0])

    def size(self):
        # returns the number of elemtents in the deque
        return len(self.elemtents)
