"""Graph Valid Tree problem implementation."""
from typing import List


def valid_tree(n: int, edges: List[List[int]]) -> bool:
    """Union-Find to determine if edges form a valid tree."""
    if len(edges) != n - 1:
        return False

    parent = list(range(n))
    rank = [0] * n

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> bool:
        root_x, root_y = find(x), find(y)
        if root_x == root_y:
            return False
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True

    return all(union(u, v) for u, v in edges)


if __name__ == "__main__":
    assert valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
