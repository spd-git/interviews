"""Product of Array Except Self problem implementation."""
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """Return the product of array except self without using division."""
    n = len(nums)
    output = [1] * n

    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
