from typing import Optional

from leetcode75.linked_list import ListNode, print_head, linked_list


head = linked_list([1, 2, 2, 1])


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = []
        while head:
            st.append(head.val)
            head = head.next

        l, r = 0, len(st) - 1
        while l < r:
            if st[l] != st[r]:
                return False
            l += 1
            r -= 1
        return True


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 到達終點時表示slow 到達mid
        # print(slow.val, slow.next.val)
        # 將後半段反轉
        pre = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        # 測試反轉後的後半段跟前半段是否一樣
        r = pre
        l = head
        while r and l:
            if r.val != l.val:
                return False
            l = l.next
            r = r.next
        return True


Solution().isPalindrome(head)
