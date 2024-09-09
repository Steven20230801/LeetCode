from typing import Optional

from Leet_Code.leetcode75.linked_list import ListNode, print_head, list_to_linked_list


head = list_to_linked_list([1, 2, 3, 4])


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> bool:
        
        s, f = head, head

        while f and f.next:
            f = f.next.next
            s = s.next
        
        # print_head(s)

        pre = None
        cur = s 
        while cur:
            temp = cur.next 
            cur.next = pre 
            pre = cur 
            cur = temp 

        h = head 
        t = pre 
        while t and t.next:
            t_next = t.next 
            h_next = h.next
            # t = 5 t_next = 4 h = 1, h_next = 2
            h.next = t 
            t.next = h_next 
            t = t_next
            h = h_next
        # print_head(head)

        return head
Solution().reorderList(head)

        