from typing import Optional

from Leet_Code.LinkedList import ListNode, linked_list, print_head, print_list

head = linked_list([1, 2, 3, 4, 5])
print_head(head)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 後半反轉
        s, f = head, head
        while f and f.next:
            f = f.next.next
            s = s.next

        pre = None
        cur = s
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        # 1 -> 2 -> 3 -> None
        # 5 -> 4 -> 3 -> None
        cur = head
        while pre.next:
            head_temp, tail_temp = cur.next, pre.next  # 儲存頭尾的next
            cur.next = pre  # 將cur.next 換成尾巴
            pre.next = head_temp
            cur = head_temp
            pre = tail_temp
        print_head(head)
        return head
