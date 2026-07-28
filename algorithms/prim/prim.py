import heapq


class Graph:
    """
    Graph implementation for Prim's Algorithm.
    """

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((weight, v))
        self.graph[v].append((weight, u))

    def prim(self):

        visited = [False] * self.vertices
        min_heap = [(0, 0, -1)]  # (weight, current_vertex, parent)

        mst = []
        total_weight = 0

        while min_heap:

            weight, current, parent = heapq.heappop(min_heap)

            if visited[current]:
                continue

            visited[current] = True
            total_weight += weight

            if parent != -1:
                mst.append((parent, current, weight))

            for edge_weight, neighbor in self.graph[current]:

                if not visited[neighbor]:
                    heapq.heappush(
                        min_heap,
                        (edge_weight, neighbor, current)
                    )

        return mst, total_weight


if __name__ == "__main__":

    graph = Graph(5)

    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 6)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, 5)
    graph.add_edge(2, 4, 7)
    graph.add_edge(3, 4, 9)

    mst, total = graph.prim()

    print("Minimum Spanning Tree:")

    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")

    print(f"\nTotal Weight = {total}")