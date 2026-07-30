class Graph:
    """
    Graph implementation for Bellman-Ford Algorithm.
    """

    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, source, destination, weight):
        """
        Add a directed weighted edge.
        """
        self.edges.append((source, destination, weight))

    def bellman_ford(self, source):
        """
        Compute shortest paths from the source vertex.
        Detect negative weight cycles.
        """

        distance = [float("inf")] * self.vertices
        distance[source] = 0

        # Relax all edges V-1 times
        for _ in range(self.vertices - 1):
            updated = False

            for u, v, weight in self.edges:

                if (
                    distance[u] != float("inf")
                    and distance[u] + weight < distance[v]
                ):
                    distance[v] = distance[u] + weight
                    updated = True

            if not updated:
                break

        # Check for negative weight cycles
        for u, v, weight in self.edges:

            if (
                distance[u] != float("inf")
                and distance[u] + weight < distance[v]
            ):
                print("Graph contains a negative weight cycle.")
                return None

        return distance


if __name__ == "__main__":

    graph = Graph(5)

    graph.add_edge(0, 1, -1)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 2)
    graph.add_edge(3, 2, 5)
    graph.add_edge(3, 1, 1)
    graph.add_edge(4, 3, -3)

    source = 0

    distances = graph.bellman_ford(source)

    if distances is not None:
        print(f"Shortest distances from vertex {source}:")

        for vertex, distance in enumerate(distances):
            print(f"{source} → {vertex} = {distance}")