# 0013. Roman to Integer

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

|Symbol|Value|
|---|---|
|I|1|
|V|5|
|X|10|
|L|50|
|C|100|
|D|500|
|M|1000|

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II.`

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

1. `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.

2. `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 

3. `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.


Given a roman numeral, convert it to an integer.

---
## 思路
因为罗马数字对于4和9的倒序性，我们在对每个字符匹配对应数字时，应采用贪心算法——先尝试匹配当前字符和下一个字符，查看是否是4或9的罗马表达形式，若不符合，在单独匹配当前字符。

## Method
Because Roman numerals for 4 and 9 are reversible, we should use a greedy algorithm when matching each character to its corresponding number—first attempt to match the current character with the next one to see if it forms a Roman numeral for 4 or 9; if not, match the current character on its own.

## Time Complexity
$O(n)$
## Space Complexity
$O(n)$

