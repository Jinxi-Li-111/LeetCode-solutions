# LeetCode Solution
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n, min_diff, best = len(nums), float('inf'), 0

        for i in range(n - 2):
            if i and nums[i] == nums[i-1]:
                continue
            x = nums[i]

            # Bound 1: Smallest possible sum is already too large
            if (s_min := x + nums[i+1] + nums[i+2]) >= target:
                return s_min if s_min - target < min_diff else best

            # Bound 2: Largest possible sum is too small
            if (s_max := x + nums[-2] + nums[-1]) <= target:
                if target - s_max < min_diff:
                    min_diff, best = target - s_max, s_max
                continue  # Skip the inner loop, we maxed out this 'i'

            # two-pointer scan for what's left
            j, k, newt = i+1, n-1, target-x
            while min_diff and j < k:
                if (diff := abs(newt - (c_sum := nums[j] + nums[k]))) < min_diff:
                    min_diff, best = diff, x + c_sum
                if c_sum > newt:
                    k -= 1
                else:
                    j += 1

        return best
