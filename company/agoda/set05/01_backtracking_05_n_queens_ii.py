from typing import Set


class Solution:
    def totalNQueens(self, n: int) -> int:
        """Count solutions using backtracking and diagonals tracking."""
        cols: Set[int] = set()
        diag1: Set[int] = set()  # row - col
        diag2: Set[int] = set()  # row + col
        count = 0

        def backtrack(row: int) -> None:
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                backtrack(row + 1)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return count
