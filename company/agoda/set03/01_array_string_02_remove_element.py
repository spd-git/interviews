"""LeetCode 27. Remove Element."""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k

def all_partition_sums(s: str):
    """
    Returns all possible partitions of adjacent integers and their sums.
    Example: '123' -> [(['1', '2', '3'], 6), (['12', '3'], 15), (['1', '23'], 24), (['123'], 123)]
    """
    n = len(s)
    results = []
    # There are (n-1) places to cut, so 2**(n-1) combinations
    for mask in range(1 << (n - 1)):
        partition = []
        last = 0
        for i in range(n - 1):
            if mask & (1 << i):
                partition.append(s[last:i+1])
                last = i + 1
        partition.append(s[last:])
        partition_sum = sum(int(x) for x in partition)
        results.append((partition, partition_sum))
    return results

def findSmallerNumGap(nums):
    result = [0] * len(nums)
    stack = []  # stores indices
    for i, num in enumerate(nums):
        while stack and nums[i] < nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result

# Example usage
nums = [73, 74, 75, 71, 69, 72, 76, 73]
print(findSmallerNumGap(nums))  # Output: [3, 2, 1, 1, 0, 0, 1, 0]
