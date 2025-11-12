"""Number of Connected Components in an Undirected Graph implementation."""
from typing import List


def count_components(n: int, edges: List[List[int]]) -> int:
    """Union-Find approach to count connected components."""
    parent = list(range(n))
    rank = [0] * n
    components = n

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        nonlocal components
        root_x, root_y = find(x), find(y)
        if root_x == root_y:
            return
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        components -= 1

    for u, v in edges:
        union(u, v)
    return components


if __name__ == "__main__":
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2
