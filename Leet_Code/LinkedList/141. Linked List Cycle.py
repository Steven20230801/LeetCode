from typing import Optional

from Leet_Code.LinkedList import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指針
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
