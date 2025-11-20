from __future__ import annotations

from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coordinates(square: int) -> (int, int):
            quot, rem = divmod(square - 1, n)
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return row, col

        visited = set([1])
        queue = deque([(1, 0)])
        while queue:
            square, moves = queue.popleft()
            if square == n * n:
                return moves
            for step in range(1, 7):
                next_square = square + step
                if next_square > n * n:
                    break
                r, c = get_coordinates(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        return -1
