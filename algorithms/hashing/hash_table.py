class HashTable:
    """
    Simple Hash Table implementation using Separate Chaining.
    """

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Generate an index for the given key.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)

        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def search(self, key):
        index = self._hash(key)

        bucket = self.table[index]

        for stored_key, stored_value in bucket:
            if stored_key == key:
                return stored_value

        return None

    def delete(self, key):
        index = self._hash(key)

        bucket = self.table[index]

        for i, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                del bucket[i]
                return True

        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")


if __name__ == "__main__":

    ht = HashTable()

    ht.insert("Alice", 92)
    ht.insert("Bob", 85)
    ht.insert("Charlie", 78)

    print("Alice:", ht.search("Alice"))
    print("Bob:", ht.search("Bob"))

    ht.delete("Bob")

    print("\nHash Table:")

    ht.display()