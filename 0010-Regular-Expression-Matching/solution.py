# LeetCode Solution
from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        lens, lenp = len(s), len(p)

        # 剪枝
        if lens < lenp - 2 * p.count('*'):
            return False

        dp = [0] * (lenp + 1)
        dp[0] = 1  # dp[p]

        for j in range(2, lenp + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 2]

        for i in range(1, lens + 1):

            s_char = s[i - 1]

            # 每个dp[j]的左上角
            prev = dp[0]
            dp[0] = 0

            for j in range(1, lenp + 1):
                p_char = p[j - 1]

                # 更新前的dp[j]的值
                temp = dp[j]

                # 处理当前p为*
                if p_char == '*':

                    # 尝试匹配0次或多次
                    dp[j] = dp[j - 2] or (temp and (p[j - 2]
                                          == s_char or p[j - 2] == '.'))

                # 处理当前p为字母或.
                elif p_char == s_char or p_char == '.':
                    dp[j] = prev
                else:
                    dp[j] = 0

                # 将更新前的值赋给左上角，负责作为下一次循环的左上角
                prev = temp

            # 剪枝，如果当前s所指的字符，p没有任何一种方法去匹配，那整体就一定无法匹配成功
            if not any(dp):
                return False

        return bool(dp[-1])
