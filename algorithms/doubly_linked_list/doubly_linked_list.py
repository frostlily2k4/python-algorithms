class Node:
    """
    Represents a node in a doubly linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Doubly Linked List implementation.
    """

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return True
            current = current.next

        return False

    def delete(self, key):
        current = self.head

        while current:
            if current.data == key:

                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev

                return

            current = current.next

    def display_forward(self):
        current = self.head

        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next

        print()

    def display_backward(self):

        if self.head is None:
            return

        current = self.head

        while current.next:
            current = current.next

        while current:
            print(current.data, end=" <-> " if current.prev else "")
            current = current.prev

        print()


if __name__ == "__main__":

    dll = DoublyLinkedList()

    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)

    dll.insert_at_beginning(5)

    print("Forward Traversal:")
    dll.display_forward()

    print("\nBackward Traversal:")
    dll.display_backward()

    print("\nSearch 20:", dll.search(20))
    print("Search 100:", dll.search(100))

    dll.delete(20)

    print("\nAfter deleting 20:")
    dll.display_forward()