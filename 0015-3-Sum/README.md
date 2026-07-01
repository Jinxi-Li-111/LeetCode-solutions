# 0015. 3 Sum


Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

---
## 思路

不同于两数和，这道题采用双指针思路，先对数组进行排序，保证数组从小到大排列，并且用i遍历每个数。

为了模拟找三个数的过程，对于当前i的位置，我们在范围`(i, len(nums))`内寻找另外两个数字，因为事先进行了排序，当前范围的最大值是`len(nums)-1`处的数字，最小值是`i+1`的数字。计算该组合的和，若等于零，记录答案；若大于零，说明组合需要小一点的数字，`k`向左移；若小于零，则`j`向右移。

另外，为了避免重复答案，需要在每一次判断`i`是否和上一个相同。并且每一次找到答案时要对`j`，`k`分别判断是否与上一次的相同。

最后，代码采用了一个高效剪枝，若当前位置的`i`已经大于零，那么它前面的`j`，`k`一定也大于零，三个正数不可能产生零，break终止。

## Method

Unlike the “Sum of Two Numbers” problem, this problem uses a two-pointer approach. First, sort the array to ensure the numbers are arranged in ascending order, and then iterate through each number using `i`.

To simulate the process of finding three numbers, for the current position of `i`, we search for the other two numbers within the range `(i, len(nums))`. Since the array has been sorted beforehand, the maximum value in this range is the number at position `len(nums)-1`, and the minimum value is the number at position `i+1`. Compute the sum of this combination. If it equals zero, record the answer; if it is greater than zero, the combination requires a smaller number, so shift `k` to the left; if it is less than zero, shift `j` to the right.

Additionally, to avoid duplicate answers, we must check whether `i` is the same as the previous value at each step. Furthermore, whenever a solution is found, we must check whether `j` and `k` are the same as their previous values.

Finally, the code employs an efficient pruning strategy: if the current `i` is greater than zero, then the preceding `j` and `k` must also be greater than zero. Since three positive numbers cannot sum to zero, the loop terminates with a `break`.

## Time Complexity
$O(n^2)$
## Space Complexity
$O(n)$

