"""Missing Number problem implementation."""
from typing import List


def missing_number(nums: List[int]) -> int:
    """Find missing number using XOR trick."""
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing


if __name__ == "__main__":
    assert missing_number([3, 0, 1]) == 2
