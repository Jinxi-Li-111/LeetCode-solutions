# LeetCode Solution
from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
            'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
            'D': 500, 'CD': 400, 'CM': 900, 'M': 1000
        }

        res, idx = 0, 0

        while idx < len(s):
            if idx + 1 < len(s) and s[idx: idx + 2] in table:
                res += table[s[idx: idx + 2]]
                idx += 2

            else:
                res += table[s[idx]]
                idx += 1

        return res
