from typing import Optional

from sklearn import dummy
from Leet_Code.LinkedList import ListNode, linked_list, print_list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = current = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return dummy.next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 創建一個虛擬節點作為新鏈表的起點
        dummy = current = ListNode()

        # 遍歷兩個鏈表，直到其中一個遍歷完
        while list1 and list2:
            if list1.val < list2.val:
                # 將 list1 的當前節點連接到新鏈表
                current.next = list1
                # 移動 list1 的指針
                list1 = list1.next
            else:
                # 將 list2 的當前節點連接到新鏈表
                current.next = list2
                # 移動 list2 的指針
                list2 = list2.next
            # 移動新鏈表的當前指針
            current = current.next

        # 將剩餘的節點連接到新鏈表
        current.next = list1 if list1 else list2

        # 返回合併後的鏈表（跳過虛擬節點）
        return dummy.next
