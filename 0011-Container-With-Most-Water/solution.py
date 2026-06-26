# LeetCode Solution
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        front = 0
        back = len(height) - 1
        while front != back:
            cur = (back - front) * min(height[front], height[back])

            max_area = max(cur, max_area)

            if height[front] < height[back]:
                front += 1
            else:
                back -= 1
        return max_area
