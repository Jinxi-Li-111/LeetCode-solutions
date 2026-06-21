# 0008. String to Integer(atoi)

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm for `myAtoi(string s)` is as follows:

1. **Whitespace**: Ignore any leading whitespace (`" "`).
2. **Signedness**: Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity if neither present.
3. **Conversion**: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
4. **Rounding**: If the integer is out of the 32-bit signed integer range <code>[-2<sup>31</sup>, 2<sup>31</sup>-1]</code>
, then round the integer to remain in the range. Specifically, integers less than <code>-2<sup>31</sup></code> should be rounded to <code>-2<sup>31</sup></code>, and integers greater than <code>2<sup>31</sup>-1</code> should be rounded to <code>2<sup>31</sup>-1</code>.

Return the integer as the final result.

## 思路

使用状态机（DFA，确定性有限状态自动机）来实现，根据题意可以将状态总结为四个：
1. 起点

```text
识别当前字符 -> 空格   -> 起点（作为一串字符的开始，空格可以有很多个，并不影响它作为起点的状态）
            -> 正负号 -> 正负号（当前字符是正负号，证明起点状态结束，所以将状态转移为正负号）
            -> 数字   -> 数字（当前字符是数字，正式开始判断有效数字，将状态转移给数字。并且因为是由起点转移给的数字，正负号并没有出现，保存默认的正号）
            -> 其他   -> 结束（检测到其他无效字符，立即停止，准备输出合法部分）
```

2. 正负号

```text
识别当前字符 -> 空格   -> 结束（当前处于正负号状态，再检测到的空格是不合法的，因此转为结束状态）
            -> 正负号 -> 结束（因为一个有效数字不能有两个正负号，再检测到的正负号非法，结束）
            -> 数字   -> 数字（当前为数字，从正负号转到数字状态，表示为一个有正负号的数字）
            -> 其他   -> 结束（当前为其他的非法字符，结束）
```

3. 数字

```text
识别当前字符 -> 空格   -> 结束（当前处于数字状态，再检测到的空格是不合法的，因此转为结束状态）
            -> 正负号 -> 结束（因为一个有效数字的中间不能有正负号，检测到的正负号非法，结束）
            -> 数字   -> 数字（当前为数字，从数字转到数字状态，表示为一个多位数）
            -> 其他   -> 结束（当前为其他的非法字符，结束）
```

4. 结束

```text
识别当前字符 -> 空格   -> 结束（已经处于结束状态，检测到的任何字符都无效，依然处于结束状态）
            -> 正负号 -> 结束（已经处于结束状态，检测到的任何字符都无效，依然处于结束状态）
            -> 数字   -> 结束（已经处于结束状态，检测到的任何字符都无效，依然处于结束状态）
            -> 其他   -> 结束（已经处于结束状态，检测到的任何字符都无效，依然处于结束状态）
```

## Method


This is implemented using a state machine (DFA, deterministic finite-state automaton). Based on the problem statement, the states can be summarized as follows:
1. Start

```text
Identify the current character 
            -> Space   -> Start (As the beginning of a string, there can be multiple spaces, which does not affect its status as the start state)
            -> Plus/minus sign -> Plus/minus sign (If the current character is a plus or minus sign, this confirms that the start state has ended, so the state transitions to the plus/minus sign state)
            -> Digit   -> Digit (If the current character is a digit, the validation of valid digits officially begins, and the state transitions to the digit state. Since this transition originated from the start state and no plus or minus sign has appeared, the default positive sign is retained)
            -> Other   -> End (An invalid character is detected; processing stops immediately, and the valid portion is prepared for output)
```

2. Plus/Minus Sign

```text
Identify current character 
            -> Space   -> End (Currently in the plus/minus sign state; the next space detected is invalid, so the state transitions to End)
            -> Plus/Minus Sign -> End (Since a valid digit cannot have two plus/minus signs, the next detected plus/minus sign is invalid; the process ends)
            -> Digit   -> Digit (Currently in the digit state; transitioning from the plus/minus sign state to the digit state indicates a digit with a plus/minus sign)
            -> Other   -> End (Currently an invalid character; the process ends)
```

3. Digits

```text
Identify current character 
            -> Space   -> End (The current state is a digit; any subsequent space is invalid, so the state transitions to End)
            -> Plus/minus sign -> End (Since a valid digit cannot contain a plus or minus sign in the middle, the detected sign is invalid; the state transitions to End)
            -> Digit   -> Digit (Currently in digit mode; transitioning from one digit to another indicates a multi-digit number)
            -> Other   -> End (The current character is an invalid character; end)
```

4. End

```text
Identify current character
            -> Space   -> End (Already in end mode; any detected character is invalid; remains in end mode)
            -> Plus or minus sign -> End (Already in the end state; any detected character is invalid; remains in the end state)
            -> Digit   -> End (Already in the end state; any detected character is invalid; remains in the end state)
            -> Other   -> End (Already in the end state; any detected character is invalid; remains in the end state)
```

## Time Complexity
$O(N)$
## Space Complexity
$O(1)$
