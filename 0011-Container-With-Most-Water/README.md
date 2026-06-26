# 0011. Container With Most Water

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the i<sup>th</sup> line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Notice** that you may not slant the container.

---
## 思路

采用贪心思想，从数组的两端向中间遍历，每次更新最大值，因为最大矩形是受限于更小的那端，所以之后要比较两端的大小，小的那端向中间靠拢

终止条件为两端指针相遇

## Method
Using a greedy approach, traverse the array from both ends toward the middle, updating the maximum value each time. Since the size of the largest rectangle is constrained by the smaller end, you must then compare the sizes at both ends, with the smaller end moving toward the middle.

The termination condition is when the two pointers meet.


## Time Complexity
$O(n)$
## Space Complexity
$O(1)$

