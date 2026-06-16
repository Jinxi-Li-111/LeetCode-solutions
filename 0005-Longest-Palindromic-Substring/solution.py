# LeetCode Solution
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        if n <= 1 or s == s[::-1]:
            return s

        x, max_len = 0, 1

        for i in range(1, n):

            d_odd = i - max_len
            d_even = d_odd - 1

            odd = s[d_even: i + 1]
            even = s[d_odd: i + 1]

            if d_even >= 0 and odd == odd[::-1]:
                x = d_even
                max_len += 2

            elif even == even[::-1]:
                x = d_odd
                max_len += 1

        return s[x: max_len + x]
