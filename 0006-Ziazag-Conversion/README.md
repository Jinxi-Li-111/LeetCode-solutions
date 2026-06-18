# 0006. Ziazag Conversion


The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```text
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: `"PAHNAPLSIIGYIR"`

---

## 思路
模仿zigzag的书写过程，建立列表包括`numRows`个字符串，包括每一行的字符。遍历`s`，通过`curr_row`和`direction`来记录当前在哪一行，以及下一次循环去哪一行。

整个流程十分自然，没有过多的遍历或判断表达。

---
## Method

To mimic the process of writing a zigzag, create a list containing `numRows` strings, each representing the characters in a row. Iterate through `s`, using `curr_row` and `direction` to track the current row and determine which row to move to in the next iteration.

The entire process flows very naturally, without excessive looping or conditional statements.

## Time Complexity

$O(n)$
## Space Complexity

$O(n)$