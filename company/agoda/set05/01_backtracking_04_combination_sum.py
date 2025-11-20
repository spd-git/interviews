from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Backtracking with pruning; candidates reused, order irrelevant."""
        result: List[List[int]] = []
        candidates.sort()

        def backtrack(start: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                result.append(path.copy())
                return
            for i in range(start, len(candidates)):
                val = candidates[i]
                if val > remaining:
                    break
                path.append(val)
                backtrack(i, remaining - val, path)
                path.pop()

        backtrack(0, target, [])
        return result
