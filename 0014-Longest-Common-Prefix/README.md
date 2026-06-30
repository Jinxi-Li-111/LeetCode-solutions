# 0014. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

---
## 思路
因为是求解列表中共同的最长前缀，只要列表中任何一个单词不满足，该前缀就无法生效。所以取列表第一个单词作为最开始的前缀，依次与后面单词进行比对，并实时更新。当某次遍历中前缀为空时，因为当前已不存在任何前缀，无需与后面比对，剪枝早退。

## Method
Since we are finding the longest common prefix in the list, if any word in the list does not satisfy the condition, the prefix is invalid. Therefore, we take the first word in the list as the initial prefix, compare it with subsequent words one by one, and update the result in real time. If the prefix is empty during an iteration—meaning there is no valid prefix at that point—there is no need to compare it with subsequent words, so we prune the search and exit early.


## Time Complexity
$O(n)$

## Space Complexity
$O(1)$
