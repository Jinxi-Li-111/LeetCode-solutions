# 0017. Letter Combinations of a Phone Number

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

---
## 思路
采用DFS回溯的思路，通过建立的dict查找当前数字对应的可能字母，并遍历到下一层，通过回溯来实现上一级的信息保存。

## Method
Using the DFS backtracking approach, we look up the possible letters corresponding to the current number in the dictionary we’ve created, then proceed to the next level, using backtracking to preserve information from the previous level.

## Time Complexity
$O(4^nn)$
## Space Complexity
$O(n)$
