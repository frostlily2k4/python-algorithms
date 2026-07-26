class DisjointSet:
    """
    Disjoint Set Union (Union-Find) implementation
    using Path Compression and Union by Rank.
    """

    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        """
        Find the representative (root) of the set.
        Uses path compression.
        """
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, x, y):
        """
        Merge the sets containing x and y.
        Uses union by rank.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y

        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x

        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    def connected(self, x, y):
        """
        Check if two nodes belong to the same set.
        """
        return self.find(x) == self.find(y)


if __name__ == "__main__":

    dsu = DisjointSet(7)

    dsu.union(0, 1)
    dsu.union(1, 2)
    dsu.union(3, 4)
    dsu.union(5, 6)

    print("0 and 2 connected:", dsu.connected(0, 2))
    print("0 and 4 connected:", dsu.connected(0, 4))

    dsu.union(2, 4)

    print("0 and 4 connected after union:", dsu.connected(0, 4))