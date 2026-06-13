# 0002. Add Two Numbers

给定两个单向链表，输出一个链表，每个节点保存它们在每个节点的值之和

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

## 思路
## Method

使用头节点dummy进行答案的存储，循环遍历两链表的节点，每次将该节点的值求和，并将进位的放入变量carry中带到下一次循环，停止条件为两链表遍历到结尾且无carry

Use the head node `dummy` to store the answer. Iterate through the nodes of both linked lists, summing the values of each node, and storing the carry in the variable `carry` to carry over to the next iteration. The termination condition is when both linked lists have been traversed to the end and there is no carry.

## Time Complexity

O(max(l1,l2))

## Space Complexity

O(max(l1,l2))