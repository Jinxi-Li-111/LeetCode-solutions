# 1. Two Sum

给定一个数组 nums 和目标值 target。

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

## 思路
## Method

使用哈希表记录已经出现过的数字。

Use a hash table to keep track of numbers that have already appeared.

遍历数组：

Iterating through an array:

- 查看 target - nums[i] 是否存在

- Check whether target - nums[i] exists

- 如果存在直接返回

- If there is a direct return

- 不存在则加入哈希表

- If it doesn't exist, add it to the hash table


## Time Complexity

O(n)

## Space Complexity

O(n)