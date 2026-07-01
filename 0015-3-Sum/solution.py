# LeetCode Solution
from typing import List


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums = sorted(nums)
        res = []
        length = len(nums)

        for i in range(length - 2):

            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = length - 1

            while j < k:

                cur = nums[i] + nums[j] + nums[k]

                if cur == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

                elif cur > 0:
                    k -= 1

                else:
                    j += 1
        return res
