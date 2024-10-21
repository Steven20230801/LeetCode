from typing import Optional
from Leet_Code.LinkedList import ListNode, linked_list, print_list


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = current = ListNode()
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, value = divmod(carry, 10)
            current.next = ListNode(value)
            current = current.next
        return dummy.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = current = ListNode()
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # 獲取l1當前節點的值，若為None則為0
            val2 = l2.val if l2 else 0  # 獲取l2當前節點的值，若為None則為0
            total = val1 + val2 + carry  # 計算總和
            carry, value = divmod(total, 10)  # 計算本位的值和新的進位
            current.next = ListNode(value)  # 創建新的節點
            current = current.next  # 移'動到新的節點
            if l1:
                l1 = l1.next  # 移動到l1的下一個節點
            if l2:
                l2 = l2.next  # 移動到l2的下一個節點
        return dummy.next
