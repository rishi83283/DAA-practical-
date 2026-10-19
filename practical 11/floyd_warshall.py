"""
Floyd-Warshall Algorithm for All-Pairs Shortest Path

Time Complexity: O(V^3)

Space Complexity: O(V^2)
"""

INF = float("inf")


def floyd_warshall(graph, v):
    dist = [[graph[i][j] for j in range(v)] for i in range(v)]

    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def main():
    print("Name: Rishi")
    v = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    graph = [[INF if i != j else 0 for j in range(v)] for i in range(v)]

    print("Enter edges (u v weight):")
    for _ in range(e):
        u, val, w = map(int, input().split())
        graph[u][val] = w

    dist = floyd_warshall(graph, v)

    print("\nShortest distance matrix:")
    for row in dist:
        print([x if x != INF else "INF" for x in row])


if __name__ == "__main__":
    main()
