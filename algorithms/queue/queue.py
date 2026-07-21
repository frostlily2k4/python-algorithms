from collections import deque


class Queue:
    """
    Queue implementation using collections.deque.
    Follows the First In, First Out (FIFO) principle.
    """

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """
        Add an element to the rear of the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front element.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.popleft()

    def front(self):
        """
        Return the front element without removing it.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self):
        """
        Check whether the queue is empty.
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of elements in the queue.
        """
        return len(self.items)


if __name__ == "__main__":

    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Front Element:", queue.front())
    print("Queue Size:", queue.size())

    print("Dequeued:", queue.dequeue())

    print("Front Element After Dequeue:", queue.front())
    print("Is Empty:", queue.is_empty())