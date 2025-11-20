"""3 Sum problem implementation."""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result

    def threeSum02(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(1, n - 2):
            left = 0
            right = n - 1
            while left < i < right:
                total = nums[left] + nums[i] + nums[right]
                if total == 0:
                    result.append([nums[left], nums[i], nums[right]])
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        print(result)
        return result

if __name__ == "__main__":
    assert sorted(Solution().threeSum02([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
