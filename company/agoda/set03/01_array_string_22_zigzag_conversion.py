"""LeetCode 6. Zigzag Conversion."""


class Solution:
    def convert(self, s: str, numRows: int) -> str:  # noqa: N802 (LeetCode signature)
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ["" for _ in range(numRows)]
        index, step = 0, 1

        for ch in s:
            rows[index] += ch
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return "".join(rows)
