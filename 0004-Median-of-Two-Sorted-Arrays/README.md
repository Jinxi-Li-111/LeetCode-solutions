# 0004. Median of Two Sorted Arrays

Given two sorted arrays `nums1` and `nums2` of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`


## 思路

这道题的重点围绕`get`函数展开，其接收列表`nums1`和当前位置`n1`；`nums2`和当前位置`n2`,还有要找的第`k`个数字。

其中，`k`会平均到两个列表之中，并比较指向的两个值,因为两数组内部有序，所以值小的那边及其与其当前位置围成的范围一定不会是目标数字，即舍弃。重复此动作，直到`k`被缩减成1，即两数组当前位置的较小值，返回，查找完毕

## Method

The key to this problem lies in the `get` function, which takes the list `nums1` and the current position `n1`; the list `nums2` and the current position `n2`; and the `k`th number to be found.

In this process, `k` is distributed evenly between the two lists, and the two corresponding values are compared. Since both arrays are internally sorted, the range formed by the smaller value and its current position will never contain the target number, so it is discarded. This process is repeated until `k` is reduced to 1—that is, the smaller of the two current positions—at which point the search is complete and the result is returned.

## Time Complexity

$O(log(min(m,n)))$

## Space Complexity

$O(log(min(m,n)))$
