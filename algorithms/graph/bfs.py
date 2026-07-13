from collections import deque


def bfs(graph, start):
    """
    Perform Breadth-First Search (BFS) on a graph.

    Args:
        graph (dict): Graph represented as an adjacency list.
        start: Starting node.

    Returns:
        list: Nodes visited in BFS order.
    """

    visited = set()
    queue = deque([start])
    traversal = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            traversal.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal


if __name__ == "__main__":

    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }

    result = bfs(graph, "A")

    print("BFS Traversal:", " -> ".join(result))