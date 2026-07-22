class Node:
    """
    Represents a node in a singly linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    Singly Linked List implementation.
    """

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a node at the beginning."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def search(self, key):
        """Search for a value in the linked list."""
        current = self.head

        while current:
            if current.data == key:
                return True
            current = current.next

        return False

    def delete(self, key):
        """Delete the first occurrence of a value."""

        if self.head is None:
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        current = self.head

        while current.next and current.next.data != key:
            current = current.next

        if current.next:
            current.next = current.next.next

    def display(self):
        """Display the linked list."""

        elements = []

        current = self.head

        while current:
            elements.append(str(current.data))
            current = current.next

        print(" -> ".join(elements))


if __name__ == "__main__":

    linked_list = SinglyLinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)

    linked_list.insert_at_beginning(5)

    print("Linked List:")
    linked_list.display()

    print("\nSearch 20:", linked_list.search(20))
    print("Search 100:", linked_list.search(100))

    linked_list.delete(20)

    print("\nAfter deleting 20:")
    linked_list.display()