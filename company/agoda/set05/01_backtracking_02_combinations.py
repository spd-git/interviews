from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """Generate all k-length combinations from numbers 1..n via backtracking."""
        result: List[List[int]] = []

        def backtrack(start: int, path: List[int]) -> None:
            if len(path) == k:
                result.append(path.copy())
                return
            for num in range(start, n + 1):
                # Prune when remaining numbers are insufficient to fill path
                if len(path) + (n - num + 1) < k:
                    break
                path.append(num)
                backtrack(num + 1, path)
                path.pop()

        backtrack(1, [])
        return result
