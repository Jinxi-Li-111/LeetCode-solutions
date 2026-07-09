# 0019. Remove Nth Node From End of List

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

---
## 思路

第一遍循环`cur`遍历链表，记录长度；然后接入`dummy`节点，自然处理移除头节点的情况；第二遍循环`cur`遍历到移除节点前一个，并将移除节点后面部分接到`cur`后面。

## Method

In the first pass, iterate through the linked list using `cur` and record its length; then insert a `dummy` node, which naturally handles the removal of the head node. In the second pass, iterate through the list using `cur` until reaching the node immediately before the one to be removed, and append the portion of the list following the node to be removed to the end of `cur`.

## Time Complexity
$O(n)$
## Space Complexity
$O(1)$

