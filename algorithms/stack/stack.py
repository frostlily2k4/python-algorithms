class Stack:
    """
    Stack implementation using a Python list.
    Follows the Last In, First Out (LIFO) principle.
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Add an element to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top element.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        """
        Return the top element without removing it.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def is_empty(self):
        """
        Check whether the stack is empty.
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of elements in the stack.
        """
        return len(self.items)


if __name__ == "__main__":

    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top Element:", stack.peek())
    print("Stack Size:", stack.size())

    print("Popped:", stack.pop())

    print("Top Element After Pop:", stack.peek())
    print("Is Empty:", stack.is_empty())