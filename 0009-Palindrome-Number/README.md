# 0009. Palindrome Number

Given an integer `x`, return `true` *if* `x` *is a palindrome, and* `false` *otherwise.*

## 思路

对于整数`x`，使用变量`reverted_number`从`x`的个位开始反向记录`x`的每一位数字，并且`x`时刻更新为自己的十分之一，当更新到`x`位数的一半，两变量比较并给出答案

## Method

For an integer `x`, use the variable `reverted_number` to record each digit of `x` in reverse order, starting from the ones place, and continuously update `x` to one-tenth of itself. When the count reaches half the number of digits in `x`, compare the two variables and return the answer.

## Time Complexity

$O(\log_{10}n)$
## Space Complexity

$O(1)$