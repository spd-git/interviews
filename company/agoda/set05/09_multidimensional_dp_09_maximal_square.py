from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """DP where dp[r][c] is side length of largest square ending at cell."""
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if matrix[r - 1][c - 1] == '1':
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                    max_side = max(max_side, dp[r][c])
        return max_side * max_side
