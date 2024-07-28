from typing import Optional

from leetcode75.linked_list import ListNode, print_head, list_to_linked_list

head = list_to_linked_list([1, 2, 3, 4, 5])


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> bool:

        # 先切半
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 後半段反轉

        pre = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        print_head(pre)
        print_head(head)

        tail = pre
        cur = head
        while cur and tail and cur.next and tail.next:
            temp_head = cur.next
            temp_tail = tail.next

            cur.next = tail
            tail.next = temp_head
            tail = temp_tail
            cur = temp_head

        # print_head(head)

        return head


Solution().reorderList(head)
