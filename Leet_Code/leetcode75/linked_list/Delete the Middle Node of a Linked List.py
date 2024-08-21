from typing import Optional

from Leet_Code.leetcode75.linked_list import ListNode, print_head, linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        pre = ListNode(0, head)
        s, f = pre, head

        while f and f.next:
            f = f.next.next
            s = s.next
        print(s.val)
        s.next = s.next.next

        return head


root = linked_list([1])
print_head(root)
print_head(Solution().deleteMiddle(root))


root = linked_list([1, 3, 4, 7, 1, 2, 6])
print_head(root)
print_head(Solution().deleteMiddle(root))


root = linked_list([1, 2, 3, 4])
print_head(root)
print_head(Solution().deleteMiddle(root))
