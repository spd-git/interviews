"""LeetCode 155. Min Stack."""


class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:  # noqa: N802
        return self.min_stack[-1]
