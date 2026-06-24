# 0010. Regular Expression Matching

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

`'.'` Matches any single character.​​​​
`'*'` Matches zero or more of the preceding element.

Return a boolean indicating whether the matching covers the entire input string (not partial).

---

## 思路

对于这类匹配类型的题目，由于有不同的匹配规则，采用DP是最好的方法。

在初始化dp数组时，要注意长度预留出一行和一列，用于表示没有`s`的时候`s`和`p`的匹配结果，没有`p`的时候`s`和`p`的匹配结果

另外由于`*`的特性，`*`与其前一个字符在一起可以匹配空字符，所以要循环遍历更新**s = 0**时的dp初始化

将`p`中可能出现的字符分组，其对`s`的作用有以下几种：

1. 当前的字符`p[j]`是字母或'.'时，判断能否与`s[i]`匹配成功。若能，则则当前状态取决于上一个，即`p[j-1]`，`s[i-1]`；若不能，直接下定不可行的结论
2. 当前字符`p[j]`是'*'时，它与`p[j-1]`可以匹配零个`p[j-1]`或多个`p[j-1]`，核心的状态转移公式为
```python
dp[i][j] = (dp[i][j - 2]    #尝试匹配零个
            or (dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.')))    #尝试匹配多个，思路为当前s[i]让*吃掉，然后回看上一个字符s[i - 1]和p[j]的匹配情况
```

**最后，为了极致压缩代码的空间与时间复杂度，在具体实现上选择了一维数组进行滚动实时更新与两个高效剪枝**

1. 由于DP更新当前`s[i]`的所有可能被`p`匹配的可能只依赖于上一行`s[i - 1]`，我们建立一维数组，并采用先遍历`s`，在每一次循环中遍历`p`的结构，引入prev和temp变量，当循环遍历到`s[i]`，`p[j]`阶段时，`prev`表示在`s[i - 1]`，`p[j - 1]`的匹配情况，`temp`表示`s[i - 1]`，`p[j]`，用于在循环末尾传给`prev`，以用于下一次循环。

2. 因为`'*'`的出现必然前面有合法字符，又因为这样的组合最少匹配零个，我们在DP前计算`p`最少能匹配多少个字符，如果`s`小于最少的长度，则一定匹配失败。在面对长`p`短`s`的情况可以做到提前剪枝

3. 因为DP的当前行取决于当前行实际匹配情况和上一行的历史匹配情况，若在DP时某一行出现了全`False`的情况，那么对于下一行的状态转移一定不会匹配成功，这种情况也需要提前剪枝，直接返回结果，无需继续尝试后面的情况

---
## Method

For this type of matching problem, since there are different matching rules, using dynamic programming (DP) is the best approach.

When initializing the DP array, be sure to reserve one row and one column to represent the matching results for `s` and `p` when `s` is absent, and for `s` and `p` when `p` is absent.

Additionally, due to the nature of `*`—which can match an empty string when combined with the preceding character—you must iterate through the array to update the DP initialization when **s = 0**.

Grouping the possible characters in `p` has the following effects on `s`:

1. If the current character `p[j]` is a letter or ‘.’, determine whether it can successfully match `s[i]`. If so, the current state depends on the previous state, i.e., `p[j-1]` and `s[i-1]`; if not, immediately conclude that the match is impossible.
2. When the current character `p[j]` is ‘*’, it can match zero or multiple instances of `p[j-1]`. The core state transition formula is:
```python
dp[i][j] = (dp[i][j - 2]    # Attempt to match zero
            or (dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == ‘.’)))    # Attempt to match multiple; the idea is to have the current `s[i]` consumed by `*`, then examine the matching conditions between the previous character `s[i - 1]` and `p[j]`
```

**Finally, to minimize both the space and time complexity of the code, the implementation uses a one-dimensional array for rolling real-time updates and two efficient pruning techniques.**

1. Since updating the current `s[i]` in DP—which represents all possible matches with `p`—depends solely on the previous element `s[i - 1]`, we construct a one-dimensional array and adopt a structure where we first traverse `s`, then traverse `p` in each iteration. We introduce the variables `prev` and `temp`. When the loop reaches `s[i]`, at the `p[j]` stage, `prev` represents the match between `s[i - 1]` and `p[j - 1]`, while `temp` represents the match between `s[i - 1]` and `p[j]`. This value is passed to `prev` at the end of the loop for use in the next iteration.

2. Since the appearance of `‘*’` necessarily implies a valid character preceding it, and since such a combination matches at least zero characters, we calculate the minimum number of characters `p` can match before performing DP. If `s` is shorter than this minimum length, the match will definitely fail. This allows for early pruning when dealing with cases where `p` is long and `s` is short.

3. Since the current state in the DP depends on both the actual match of the current line and the historical match of the previous line, if a line in the DP yields all `False` values, the state transition for the next line will definitely fail to match. In this case, we also need to prune early, returning the result immediately without continuing to evaluate subsequent cases.

## Time Complexity
$O(len(s) * len(p))$

## Space Complexity
$O(len(p))$
