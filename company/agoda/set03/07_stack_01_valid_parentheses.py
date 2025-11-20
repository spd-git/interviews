"""LeetCode 20. Valid Parentheses."""


class Solution:
    def isValid(self, s: str) -> bool:  # noqa: N802
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False
        return not stack
