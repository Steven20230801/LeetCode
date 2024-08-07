from typing import Optional
from leetcode75.linked_list import ListNode, linked_list, print_head


list1 = linked_list([])
list2 = linked_list([1, 3, 4])


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        pre = cur = ListNode(0)

        while list1 and list2:

            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if not list1:
            cur.next = list2
        else:
            cur.next = list1

        print_head(pre.next)
        return pre.next


Solution().mergeTwoLists(list1, list2)
