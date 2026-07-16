class Node:
    """
    Represents a node in a Binary Search Tree.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree implementation.
    """

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):

        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        return node

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):

        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self._search(node.left, value)

        return self._search(node.right, value)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):

        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)


if __name__ == "__main__":

    bst = BinarySearchTree()

    numbers = [50, 30, 70, 20, 40, 60, 80]

    for number in numbers:
        bst.insert(number)

    print("Inorder Traversal:", bst.inorder())

    print("Search 40:", bst.search(40))
    print("Search 100:", bst.search(100))