"""LeetCode 380. Insert Delete GetRandom O(1)."""

import random
from typing import Dict, List


class RandomizedSet:
    def __init__(self) -> None:
        self.values: List[int] = []
        self.index: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        idx = self.index[val]
        last_val = self.values[-1]
        self.values[idx] = last_val
        self.index[last_val] = idx
        self.values.pop()
        del self.index[val]
        return True

    def getRandom(self) -> int:  # noqa: N802 (LeetCode signature)
        return random.choice(self.values)
