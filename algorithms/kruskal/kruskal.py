class DisjointSet:
    def __init__(self, vertices):
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def kruskal(self):

        self.edges.sort()

        dsu = DisjointSet(self.vertices)

        mst = []
        total_weight = 0

        for weight, u, v in self.edges:

            if dsu.union(u, v):
                mst.append((u, v, weight))
                total_weight += weight

        return mst, total_weight


if __name__ == "__main__":

    graph = Graph(4)

    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 4)

    mst, total = graph.kruskal()

    print("Minimum Spanning Tree:")

    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")

    print(f"\nTotal Weight = {total}")