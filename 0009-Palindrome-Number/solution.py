# LeetCode Solution
from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 边界条件：
        # 1. 负数绝对不是回文数
        # 2. 如果数字最后一位是 0，为了是回文数，第一位也必须是 0，只有 0 本身符合
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        # 当数字长度为奇数时，我们可以通过 reverted_number // 10 去掉中间的数字。
        # 例如，当输入为 12321 时，在 while 循环结束时 x = 12，reverted_number = 123，
        # 因为中间的数字不影响回文（它总是等于自身），所以我们可以简单地将其去掉。
        return x == reverted_number or x == reverted_number // 10
