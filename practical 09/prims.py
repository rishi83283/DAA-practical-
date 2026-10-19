"""
Prim's Algorithm for Minimum Spanning Tree (MST)

Time Complexity: O((V + E) log V)

Space Complexity: O(V + E)
"""

import heapq
from collections import defaultdict


def prims(vertices, graph, start_node):
    mst_cost = 0
    visited = set()
    min_heap = [(0, start_node)]

    while min_heap and len(visited) < vertices:
        weight, u = heapq.heappop(min_heap)

        if u in visited:
            continue

        visited.add(u)
        mst_cost += weight

        for neighbor, w in graph[u]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor))

    return mst_cost


def main():
    print("Name: Rishi")
    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))

    graph = defaultdict(list)
    print("Enter edges (u v weight):")
    for _ in range(edges):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    start_node = int(input("\nEnter starting vertex: "))

    print("\nMinimum Spanning Tree Cost =", prims(vertices, graph, start_node))


if __name__ == "__main__":
    main()
