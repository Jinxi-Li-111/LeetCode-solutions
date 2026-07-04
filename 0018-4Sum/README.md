# 0018. 4Sum

Given an array `nums` of `n` integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

1. `0 <= a, b, c, d < n`

2. `a`, `b`, `c`, and `d` are **distinct**.

3. `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in **any order**.

## 思路

对于4Sum，我们引入函数K-Sum，对初始数组排序，并赋值4来解决。

对于K-Sum，主要用递归思路解决。基础事例为2Sum，分别用左右指针指向数组两端，并计算当前值，因为数组有序，我们可以通过当前值来移动左右指针，直到找到目标值。

而递归事例为，若k>2，则寻找可能组成目标值的第一个，并将起始点，目标值的通过递归传递给下一层。

另外高效的剪枝可以避免重复答案和节省时间：若k个当前值大于目标值，因为当前值是最小的，代表后续组合没有答案，可以直接结束。

## Method

For the 4Sum problem, we introduce the K-Sum function, sort the initial array, and set the value to 4 to solve it.

For the K-Sum problem, we primarily use a recursive approach. The base case is the 2Sum problem: we use left and right pointers to point to the ends of the array and calculate the current value. Since the array is sorted, we can move the left and right pointers based on the current value until we find the target value.

The recursive case is as follows: if k > 2, we find the first value that can form the target value and pass the starting point and the target value to the next level via recursion.

Additionally, efficient pruning can prevent duplicate answers and save time: if any of the k current values is greater than the target value, since the current value is the smallest, it indicates that no solution exists in subsequent combinations, so we can terminate the search immediately.


## Time Complexity
$O(n^3)$
## Space Complexity
$O(n)$

