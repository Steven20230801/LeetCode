from typing import Optional

from Leet_Code.leetcode75.linked_list import ListNode, print_head, linked_list


head = linked_list([1, 2, 2, 5])


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur:

            if cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        # print_head(head)
        return head


Solution().deleteDuplicates(linked_list([1, 1, 1]))
