"""
Kruskal's Algorithm for Minimum Spanning Tree (MST)

Time Complexity: O(E log E) or O(E log V)

Space Complexity: O(V + E)
"""


class DisjointSet:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False


def kruskal(vertices, edges):
    edges.sort(key=lambda item: item[2])
    ds = DisjointSet(vertices)
    mst_cost = 0
    edges_count = 0

    for u, v, w in edges:
        if ds.union(u, v):
            mst_cost += w
            edges_count += 1
            if edges_count == vertices - 1:
                break

    return mst_cost


def main():
    print("Name: Rishi")
    vertices = int(input("Enter number of vertices: "))
    edges_count = int(input("Enter number of edges: "))

    edges = []
    print("Enter edges (u v weight):")
    for _ in range(edges_count):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    print("\nMinimum Spanning Tree Cost =", kruskal(vertices, edges))


if __name__ == "__main__":
    main()
