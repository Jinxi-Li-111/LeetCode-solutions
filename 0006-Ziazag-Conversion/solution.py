# LeetCode Solution
from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        each_row = [''] * numRows
        curr_row = 0
        direction = -1

        for char in s:

            each_row[curr_row] += char

            if curr_row == 0 or curr_row == numRows - 1:
                direction = -direction
            curr_row += direction

        return ''.join(each_row)
