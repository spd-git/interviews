from typing import List, Optional


class Node:
    def __init__(self, val: bool, isLeaf: bool, topLeft: Optional['Node'] = None, topRight: Optional['Node'] = None,
                 bottomLeft: Optional['Node'] = None, bottomRight: Optional['Node'] = None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """Build quad tree recursively by checking if region is uniform."""
        n = len(grid)

        def helper(x: int, y: int, length: int) -> Node:
            first = grid[x][y]
            uniform = True
            for i in range(x, x + length):
                for j in range(y, y + length):
                    if grid[i][j] != first:
                        uniform = False
                        break
                if not uniform:
                    break
            if uniform:
                return Node(bool(first), True)
            half = length // 2
            return Node(
                True,
                False,
                helper(x, y, half),
                helper(x, y + half, half),
                helper(x + half, y, half),
                helper(x + half, y + half, half),
            )

        return helper(0, 0, n)
