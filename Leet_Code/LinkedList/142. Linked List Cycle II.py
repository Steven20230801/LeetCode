from tkinter import NO
from typing import Optional

from Leet_Code.LinkedList import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        # 偵測是否存在環, 利用快慢指標進行循環偵測
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                break

        # 確認是否有環
        if not f or not f.next:
            return None

        # 找出循環的起始節點
        s = head
        while s != f:
            s = s.next
            f = f.next

        return s


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        # 偵測是否存在環, 利用快慢指標進行循環偵測
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:

                while s != head:
                    s = s.next
                    head = head.next
                return s
        return None
