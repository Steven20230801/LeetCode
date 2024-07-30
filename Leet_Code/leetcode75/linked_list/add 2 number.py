from typing import Optional

from leetcode75.linked_list import ListNode, print_head, list_to_linked_list


head = list_to_linked_list([1, 2, 3, 4, 5])


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        next = 0
        x = dummy = ListNode()
        while l1 or l2 or next:

            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a + b + next
            next, now = divmod(total, 10)

            x.val = now

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 or l2 or next:
                x.next = ListNode()
                x = x.next

        print_head(dummy)
        return dummy


Solution().addTwoNumbers(list_to_linked_list([9, 9, 9]), list_to_linked_list([9, 9, 9, 9, 9]))

Solution().addTwoNumbers(list_to_linked_list([1, 2, 3]), list_to_linked_list([9, 9, 9]))
