from typing import Optional
from Leet_Code.LinkedList import ListNode, linked_list, print_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 先用快慢指針找到終點
        l, r = head, head

        while r and r.next:
            l = l.next
            r = r.next.next

        return l
