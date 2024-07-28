from typing import Optional

from leetcode75.linked_list import ListNode, print_head, linked_list


head = linked_list([1, 2, 3, 4, 5])
print_head(head)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            temp = cur.next  # 記錄資訊
            cur.next = pre  # 更新資訊
            pre = cur  # 跳
            cur = temp  # 跳

        print_head(pre)


Solution().reverseList(head)
