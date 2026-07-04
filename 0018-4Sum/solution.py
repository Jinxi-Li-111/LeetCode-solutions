# LeetCode Solution
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        return self.kSum(nums, 0, target, 4)

    def kSum(self, nums, start, target, k):
        res = []
        n = len(nums)

        if k == 2:
            return self.twoSum(nums, start, target)

        for i in range(start, n):
            if i > start and nums[i] == nums[i - 1]:
                continue

            if nums[i] * k > target:
                break

            if nums[i] + (k - 1) * nums[n - 1] < target:
                continue
            for subset in self.kSum(nums, i + 1, target - nums[i], k - 1):
                res.append([nums[i]] + subset)

        return res

    def twoSum(self, nums, start, target):
        left, right = start, len(nums) - 1
        res = []
        while left < right:
            total = nums[left] + nums[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        return res
