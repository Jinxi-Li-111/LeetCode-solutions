# LeetCode Solution
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return self.get(nums1, 0, nums2, 0, total // 2 + 1)
        else:
            left = self.get(nums1, 0, nums2, 0, total // 2)
            right = self.get(nums1, 0, nums2, 0, total // 2 + 1)
            return (left + right) / 2

    def get(self, nums1, n1, nums2, n2, k):
        remain1, remain2 = len(nums1) - n1, len(nums2) - n2

        if remain1 > remain2:
            return self.get(nums2, n2, nums1, n1, k)
        if remain1 <= 0:
            return nums2[n2 + k - 1]
        if k == 1:
            return min(nums1[n1], nums2[n2])

        step_A = min(remain1, k // 2)
        step_B = min(remain2, k // 2)

        if nums1[n1 + step_A - 1] <= nums2[n2 + step_B - 1]:
            return self.get(nums1, n1 + step_A, nums2, n2, k - step_A)

        else:
            return self.get(nums1, n1, nums2, n2 + step_B, k - step_B)
