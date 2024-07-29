from typing import Optional

from leetcode75.linked_list import ListNode, print_head, list_to_linked_list

head = list_to_linked_list([1, 2, 1])


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)
        cur_2 = dummy_prev = ListNode(next=dummy)

        for _ in range(k - 1):  # 走k-1
            cur = cur.next

        # print(cur.val)

        # 走完k-1, cur.next =  the values of the kth node from the beginning
        b_prev = cur
        b = cur.next
        b_after = cur.next.next

        while cur.next:
            cur = cur.next
            cur_2 = cur_2.next

        # print(cur.val)
        # print(cur_2.val)

        e_prev = cur_2
        e = cur_2.next
        e_after = cur_2.next.next

        temp = b.val
        b.val = e.val
        e.val = temp

        print_head(head)
        return head


head = list_to_linked_list([1, 2, 3, 6, 5])
print_head(head)
Solution().swapNodes(head, k=2)
