from typing import Optional
from Leet_Code.leetcode75.linked_list import (
    ListNode,
    print_list,
    list_to_linked_list,
    print_head,
)


lst = [1, 2, 3, 3, 4, 4, 5]
print_list(lst)
head = list_to_linked_list(lst)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 由於head也可能被刪除, 需要偽節點
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:  # 檢查下個值跟下下個值
            check_value = cur.next.val  # 目前檢查得值
            if cur.next.next.val == check_value:  # 當檢查的一樣的時候繼續檢查
                while (
                    cur.next and cur.next.val == check_value
                ):  # 繼續檢查下個有沒有一樣
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(next=head)
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if pre.next == cur:
                pre = cur
            else:
                pre.next = cur.next
            cur = cur.next
        return dummy.next


print_head(Solution().deleteDuplicates(head))
