"""Combination Sum IV problem implementation."""
from typing import List


def combination_sum4(nums: List[int], target: int) -> int:
    """Count number of combinations that add up to target (order matters)."""
    dp = [0] * (target + 1)
    dp[0] = 1
    for total in range(1, target + 1):
        for num in nums:
            if num <= total:
                dp[total] += dp[total - num]
    return dp[target]


if __name__ == "__main__":
    assert combination_sum4([1, 2, 3], 4) == 7
