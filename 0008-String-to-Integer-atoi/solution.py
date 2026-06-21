# LeetCode Solution
from typing import List


class Solution:
    # 状态机将当前字符分成四类：空格，正负号，数字，其他
    table = {
        'start': {'space': 'start', 'sign': 'sign', 'number': 'number', 'other': 'end'},
        'sign': {'space': 'end', 'sign': 'end', 'number': 'number', 'other': 'end'},
        'number': {'space': 'end', 'sign': 'end', 'number': 'number', 'other': 'end'},
        'end': {'space': 'end', 'sign': 'end', 'number': 'end', 'other': 'end'}
    }

    int_max = 2**31 - 1
    int_min = -2**31

    def myAtoi(self, s: str) -> int:
        status = 'start'
        sign = 1
        res = 0

        for char in s:

            cur_type = self.determine_status(char)

            status = self.table[status][cur_type]

            if status == 'number':
                res = res * 10 + int(char)
                if res > self.int_max:
                    break

            elif status == 'sign' and char == '-':
                sign = -1

            elif status == 'end':
                break

        res = sign * res
        return max(self.int_min, min(res, self.int_max))

    def determine_status(self, s: str):

        if s == ' ':
            return 'space'

        elif s in '+-':
            return 'sign'

        elif s.isdigit():
            return 'number'
        return 'other'
