# 0003. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

## 思路
## Method

采用双指针思路，通过快指针`right`顺序遍历，判断新字符是否之前出现过，与慢指针`left`记录当前子字符串的开始，不断更新最长子字符串。

具体实现：初始建立`char_set`集合，记录所有`right`走过的字符。`right`从字符串开始循环遍历，若当前字符之前出现过，则不断向前移动慢指针`left`，并从`char_set`里移除该字符，循环遍历直到`right`所指的字符被移除。然后将`right`字符加入集合，并更新`max_length`，直至`s`被完整遍历。

Using a two-pointer approach, we traverse the sequence using the fast pointer `right` to determine whether a new character has appeared before, while the slow pointer `left` records the start of the current substring, continuously updating the longest substring.

Implementation: First, create a `char_set` to track all characters that the `right` pointer has traversed. `right` iterates through the string. If the current character has appeared previously, the left pointer `left` is incremented, and the character is removed from `char_set`. The iteration continues until the character pointed to by `right` is removed. Then, the character at `right` is added to the set, and `max_length` is updated, until `s` has been fully traversed.

## Time Complexity

$O(n^2)$

## Space Complexity

$O(n)$