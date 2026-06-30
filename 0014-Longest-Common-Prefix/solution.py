# LeetCode Solution
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        gen = iter(strs)

        prefix = next(gen)

        for word in gen:

            end = min(len(prefix), len(word))

            for i in range(end):
                if prefix[i] != word[i]:
                    end = i
                    break

            prefix = prefix[:end]

            if not prefix:
                return ''

        return prefix
