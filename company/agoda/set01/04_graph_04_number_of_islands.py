"""Number of Islands problem implementation."""
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """DFS flood fill to count islands in the grid."""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count


if __name__ == "__main__":
    sample = [list("11110"), list("11010"), list("11000"), list("00000")]
    assert num_islands(sample) == 1
