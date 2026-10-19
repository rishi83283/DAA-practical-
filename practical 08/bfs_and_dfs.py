"""
Breadth First Search (BFS) and Depth First Search (DFS) for Graph Traversal

Time Complexity: O(V + E) for both BFS and DFS

Space Complexity: O(V) for both BFS and DFS
"""

from collections import deque, defaultdict


def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    traversal = []

    while queue:
        node = queue.popleft()
        traversal.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal


def dfs(graph, start, visited=None, traversal=None):
    if visited is None:
        visited = set()
    if traversal is None:
        traversal = []

    visited.add(start)
    traversal.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal)

    return traversal


def main():
    print("Name: Rishi")
    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))

    graph = defaultdict(list)
    print("Enter edges (u v):")
    for _ in range(edges):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    start_node = int(input("\nEnter starting vertex: "))

    print("\nBFS Traversal:", bfs(graph, start_node))
    print("DFS Traversal:", dfs(graph, start_node))


if __name__ == "__main__":
    main()
