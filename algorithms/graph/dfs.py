def dfs(graph, start, visited=None):
    """
    Perform Depth-First Search (DFS) on a graph.

    Args:
        graph (dict): Graph represented as an adjacency list.
        start: Starting node.
        visited (set): Set of visited nodes.

    Returns:
        list: Nodes visited in DFS order.
    """

    if visited is None:
        visited = set()

    visited.add(start)
    traversal = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            traversal.extend(dfs(graph, neighbor, visited))

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

    result = dfs(graph, "A")

    print("DFS Traversal:", " -> ".join(result))