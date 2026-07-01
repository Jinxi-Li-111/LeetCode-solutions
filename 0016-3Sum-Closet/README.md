# 0016. 3Sum Closet

Given an integer array `nums` of length `n` and an integer `target`, find three integers at **distinct indices** in `nums` such that the sum is closest to `target`.

Return *the sum of the three integers*.

You may assume that each input would have exactly one solution.

---
## 思路
对数组先排序，遍历数组，用当前索引`i`看作第一个值，剩下两个值在索引`i`后面取，并使用变量`min_diff`和`best`分别记录当前与`target`的最小距离和其自身数值。

此外，因为数组有序，可以使用两个剪枝去除大量不必要的循环比较:
1. 对于当前索引`i`，所能组成的最小值为`i`，`i+1`，`i+2`三处之和，若之和大于等于`target`，则说明对于索引i与后面所有的总和可能都大于等于`target`，即后面不存在比当前距离`target`更近的答案。所以比较当前距离`s_min - target`与历史最小距离`min_diff`，小的距离就是答案。

2. 对于当前索引`i`，所能组成的最大值为`i`，数组倒数第一个，数组倒数第二个的三处之和，若之和小于等于`target`，则说明对于索引`i`，任何一个组合都不可能大于该组合，既然最大的组合仍小于等于`target`，则比较其他组合不会对结果产生影响。所以比较当前距离`s_max - target`与历史最小距离`min_diff`，更新`min_diff`并跳过索引`i`。


## Method

First, sort the array. Then, iterate through the array, treating the current index `i` as the first value, and taking the remaining two values from the indices following `i`. Use the variables `min_diff` and `best` to record the minimum distance to `target` and the value itself, respectively.

Additionally, since the array is sorted, two pruning techniques can be used to eliminate a large number of unnecessary iterative comparisons:
1. For the current index `i`, the minimum possible value is the sum of `i`, `i+1`, and `i+2`. If this sum is greater than or equal to `target`, it means that the sum of `i` and all subsequent indices is likely greater than or equal to `target`—that is, there is no solution closer to `target` than the current distance. Therefore, compare the current distance `s_min - target` with the historical minimum distance `min_diff`; the smaller of the two is the answer.

2. For the current index `i`, the maximum possible value is the sum of `i`, the second-to-last element of the array, and the third-to-last element of the array. If this sum is less than or equal to `target`, it means that for index `i`, no other combination can be greater than this one. Since the largest combination is still less than or equal to `target`, comparing other combinations will not affect the result. Therefore, compare the current distance `s_max - target` with the historical minimum distance `min_diff`, update `min_diff`, and skip index `i`.


## Time Complexity
$O(n^2)$
## Space Complexity
$O(n)$

