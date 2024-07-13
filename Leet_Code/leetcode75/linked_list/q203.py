from typing import Optional
from Leet_Code.leetcode75.linked_list import (
    ListNode,
    print_list,
    list_to_linked_list,
    print_head,
)


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(next=head)
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


head = list_to_linked_list([7, 7, 7, 7])

print_head(Solution().removeElements(head, 7))


head = list_to_linked_list([1, 2, 6, 3, 4, 5, 6])

print_head(Solution().removeElements(head, 6))
