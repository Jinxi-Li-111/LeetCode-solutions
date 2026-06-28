# LeetCode Solution
from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:

        value_to_symbol = {
            1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
            6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
            10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L',
            60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C',
            200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
            600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
            2000: 'MM', 3000: 'MMM', 0: ''
        }

        res = ''
        divisor = 1000

        while divisor:
            quotient = num // divisor
            value = quotient * divisor
            res += value_to_symbol[value]
            divisor //= 10
            num -= value

        return res
