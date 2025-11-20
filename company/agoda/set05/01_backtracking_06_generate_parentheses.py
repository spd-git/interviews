from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """Backtracking ensures valid prefix counts for parentheses."""
        result: List[str] = []

        def backtrack(current: List[str], open_left: int, close_left: int) -> None:
            if open_left == 0 and close_left == 0:
                result.append("".join(current))
                return
            if open_left > 0:
                current.append("(")
                backtrack(current, open_left - 1, close_left)
                current.pop()
            if close_left > open_left:
                current.append(")")
                backtrack(current, open_left, close_left - 1)
                current.pop()

        backtrack([], n, n)
        return result
