from typing import Optional

from Leet_Code.LinkedList import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next

            if s == f:
                break

        if not f:
            return None

        s = head
        while s != f:
            s = s.next
            f = f.next

        return s
