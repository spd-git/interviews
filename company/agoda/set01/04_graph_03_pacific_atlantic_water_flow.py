"""Pacific Atlantic Water Flow problem implementation."""
from collections import deque
from typing import List, Set, Tuple


Directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs(starts: List[Tuple[int, int]], heights: List[List[int]]) -> Set[Tuple[int, int]]:
    rows, cols = len(heights), len(heights[0])
    visited: Set[Tuple[int, int]] = set(starts)
    queue = deque(starts)
    while queue:
        r, c = queue.popleft()
        for dr, dc in Directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                visited.add((nr, nc))
                queue.append((nr, nc))
    return visited


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    """Return coordinates that can flow to both oceans."""
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])
    pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
    atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

    pacific_reachable = bfs(pacific_starts, heights)
    atlantic_reachable = bfs(atlantic_starts, heights)
    return [list(coord) for coord in sorted(pacific_reachable & atlantic_reachable)]


if __name__ == "__main__":
    sample = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    assert [0, 4] in pacific_atlantic(sample)
