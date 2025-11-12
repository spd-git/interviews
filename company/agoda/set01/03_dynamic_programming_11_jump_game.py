"""Jump Game problem implementation."""
from typing import List


def can_jump(nums: List[int]) -> bool:
    """Greedy solution to determine reachability of last index."""
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4]) is True
