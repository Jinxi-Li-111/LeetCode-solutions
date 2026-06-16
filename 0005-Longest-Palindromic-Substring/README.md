# 0005. Longest Palindromic Substring

Given a string `s`, return the longest palindromic substring in `s`.

## 思路
代码核心思想与贪心类似，由最长substring的头指针`x`和最长的长度`max_length`来确定当前记录的最长palindrome切片。

算法循环只注重于寻找比当前最长更长的子字符串，因为palindrome可以形成奇数或偶数两种对称方式，因此`d_odd`和`d_even`分别负责寻找`max_length`上加一个长度和两个长度的起始索引，再利用遍历指针`i`计算并验证出当前围成的字符串是否是palindrome，同时更新数据。

## Method

The core idea of the code is similar to the greedy algorithm: it determines the longest palindrome slice for the current record using the pointer `x` to the start of the longest substring and the maximum length `max_length`.

The algorithm’s loop focuses solely on finding substrings longer than the current longest one. Since palindromes can form in either an odd or even symmetrical pattern, `d_odd` and `d_even` are responsible for finding the starting indices for lengths one and two units longer than `max_length`, respectively. Then, using the traversal pointer `i`, they calculate and verify whether the currently enclosed string is a palindrome, while simultaneously updating the data.

## Time Complexity
$O(n^2)$
## Space Complexity
$O(n)$
