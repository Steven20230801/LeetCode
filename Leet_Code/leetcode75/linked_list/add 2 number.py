from typing import Optional

from leetcode75.linked_list import ListNode, print_head, list_to_linked_list


head = list_to_linked_list([1, 2, 3, 4, 5])


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        next = 0
        cur = l1
        cur2 = l2
        x = dummy = ListNode()
        while cur and cur2:

            total = cur.val + cur2.val + next
            next, now = divmod(total, 10)

            x.val = now
            x.next = ListNode()

            cur = cur.next
            cur2 = cur2.next

        while cur:
            total = cur.val + next
            next, now = divmod(total, 10)
            cur.val = now
            cur = cur.next

        if cur2:
            cur = cur2
            while cur:
                total = cur.val + next
                next, now = divmod(total, 10)
                cur.val = now
                cur = cur.next
        print_head(dummy.next)
        return dummy.next


Solution().addTwoNumbers(list_to_linked_list([9, 9, 9]), list_to_linked_list([9, 9, 9, 9, 9]))

Solution().addTwoNumbers(list_to_linked_list([9, 9, 9]), list_to_linked_list([9, 9, 9]))
