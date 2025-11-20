from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """DP grid updated in place to count paths avoiding obstacles."""
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for c in range(1, cols):
            obstacleGrid[0][c] = 0 if obstacleGrid[0][c] == 1 else obstacleGrid[0][c - 1]
        for r in range(1, rows):
            obstacleGrid[r][0] = 0 if obstacleGrid[r][0] == 1 else obstacleGrid[r - 1][0]
        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]
        return obstacleGrid[-1][-1]
