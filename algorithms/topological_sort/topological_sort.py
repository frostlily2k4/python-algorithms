from collections import deque


class Graph:
    """
    Graph implementation for Kahn's Topological Sort Algorithm.
    """

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        """
        Add a directed edge u -> v.
        """
        self.graph[u].append(v)

    def topological_sort(self):
        """
        Perform Topological Sort using Kahn's Algorithm.
        """

        in_degree = [0] * self.vertices

        # Calculate in-degree of each vertex
        for u in range(self.vertices):
            for v in self.graph[u]:
                in_degree[v] += 1

        queue = deque()

        # Add all vertices with in-degree 0
        for vertex in range(self.vertices):
            if in_degree[vertex] == 0:
                queue.append(vertex)

        order = []

        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in self.graph[current]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Detect cycle
        if len(order) != self.vertices:
            return None

        return order


if __name__ == "__main__":

    graph = Graph(6)

    graph.add_edge(5, 2)
    graph.add_edge(5, 0)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)

    result = graph.topological_sort()

    if result is None:
        print("Graph contains a cycle.")
    else:
        print("Topological Order:")
        print(result)