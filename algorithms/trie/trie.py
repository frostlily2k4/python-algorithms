class TrieNode:
    """
    Represents a node in a Trie.
    """

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Trie (Prefix Tree) implementation.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie.
        """
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.is_end_of_word = True

    def search(self, word):
        """
        Return True if the word exists.
        """
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.is_end_of_word

    def starts_with(self, prefix):
        """
        Return True if any word starts with the prefix.
        """
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True


if __name__ == "__main__":

    trie = Trie()

    words = ["apple", "app", "apply", "bat", "ball"]

    for word in words:
        trie.insert(word)

    print("Search 'apple':", trie.search("apple"))
    print("Search 'apps':", trie.search("apps"))

    print("Starts with 'app':", trie.starts_with("app"))
    print("Starts with 'cat':", trie.starts_with("cat"))