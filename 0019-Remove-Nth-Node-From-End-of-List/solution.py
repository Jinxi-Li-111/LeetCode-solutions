# LeetCode Solution
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head

        while cur:
            length += 1
            cur = cur.next

        dummy = ListNode(0, head)

        cur = dummy
        times = length - n

        for i in range(times):
            cur = cur.next
        cur.next = cur.next.next

        return dummy.next
