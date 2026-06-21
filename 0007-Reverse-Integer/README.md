# 0007. Reverse Integer

Given a signed 32-bit integer `x`, return `x` *with its digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**


## 思路

实现思路为利用python的强转类型，将`int`类型的`x`转化为`str`，在进行字符串反转操作。

**特别注意要处理x小于零时的负号和超32bit表示的上下限。**

## Method

The approach involves using Python's type casting to convert `x`, which is of type `int`, to `str`, and then reversing the string.

**Be sure to handle the negative sign when `x` is less than zero, as well as the upper and lower bounds of the 32-bit representation.**

## Time Complexity
$O(n)$
## Space Complexity
$O(1)$
