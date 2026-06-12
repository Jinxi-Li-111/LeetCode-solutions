from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up
        to target
        """
        dct = {}
        for i in range(len(nums)):
            if target - nums[i] in dct:
                return [i, dct[target - nums[i]]]
            dct[nums[i]] = i
