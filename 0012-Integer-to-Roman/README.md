# 0012. Integer to Roman

Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
| --- | --- |
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

1. If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.

2. If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (`I`) less than 5 (`V`): `IV` and 9 is 1 (`I`) less than 10 (`X`): `IX`. Only the following subtractive forms are used: 4 (`IV`), 9 (`IX`), 40 (`XL`), 90 (`XC`), 400 (`CD`) and 900 (`CM`).

3. Only powers of 10 (`I`, `X`, `C`, `M`) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (`V`), 50 (`L`), or 500 (`D`) multiple times. If you need to append a symbol 4 times use the **subtractive form**.


Given an integer, convert it to a Roman numeral.

---
## 思路

采用空间换时间思路，建立哈希表，将每一位可能的数字与对应的罗马数字相结合。因为本题的数字限制在[1,3999]，使用该方法稳定遍历四次，及数字的位数。

缺点：这种哈希表因为考虑所有情况，在位数增大时会难写。所以当位数增大时考虑只写基础骨架，用字符串乘法实习重复拼接。

## Method

Using the “space for time” approach, we construct a hash table that maps each possible digit to its corresponding Roman numeral. Since the numbers in this problem are restricted to the range [1, 3999], this method requires a constant four passes—equal to the number of digits in the number.

Drawback: Since this hash table must account for all possible cases, it becomes difficult to implement as the number of digits increases. Therefore, when the number of digits increases, consider implementing only the basic framework and use string multiplication to perform the repeated concatenation.

## Time Complexity
$O(n)$

## Space Complexity
$O(n)$

