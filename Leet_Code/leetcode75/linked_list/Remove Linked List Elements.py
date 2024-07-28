from typing import Optional

from Leet_Code.leetcode75.linked_list import ListNode, print_head, linked_list


head = linked_list([1, 2, 2, 1])


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        pre = cur = ListNode(0, next=head)

        while cur and cur.next:

            if cur.next.val == val:
                cur.next = cur.next.next
                continue
            cur = cur.next

        print_head(pre.next)
        return pre.next


Solution().removeElements(head, 1)


Solution().removeElements(linked_list([]), 1)
Solution().removeElements(linked_list([7, 7, 7, 7]), 7)
