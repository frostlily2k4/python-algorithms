INF = float("inf")


def floyd_warshall(graph):
    """
    Compute shortest paths between all pairs of vertices
    using the Floyd-Warshall Algorithm.
    """

    vertices = len(graph)

    distance = [row[:] for row in graph]

    for k in range(vertices):

        for i in range(vertices):

            for j in range(vertices):

                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance


if __name__ == "__main__":

    graph = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0],
    ]

    shortest = floyd_warshall(graph)

    print("Shortest Distance Matrix:\n")

    for row in shortest:
        print(row)