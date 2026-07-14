import heapq


def dijkstra(graph, start):
    """
    Find the shortest distance from the start node
    to every other node using Dijkstra's Algorithm.

    Args:
        graph (dict): Weighted graph represented as an adjacency list.
        start (str): Starting node.

    Returns:
        dict: Shortest distance from the start node.
    """

    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":

    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2, "F": 6},
        "E": {"C": 10, "D": 2, "F": 3},
        "F": {"D": 6, "E": 3},
    }

    shortest_paths = dijkstra(graph, "A")

    print("Shortest distances from node A:\n")

    for node, distance in shortest_paths.items():
        print(f"{node}: {distance}")