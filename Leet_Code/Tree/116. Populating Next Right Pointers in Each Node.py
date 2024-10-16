from collections import deque
from pickle import NONE
from typing import Optional

from Leet_Code.Tree import TreeNode as p


class TreeNode(p):
    def __init__(self, x, left=None, right=None, next=None):
        super().__init__(x, left, right)
        self.next = next


class Solution:
    def connect(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 使用雙端隊列來進行廣度優先搜索（BFS）
        q = deque()

        # 如果根節點為空，返回 None
        if not root:
            return None

        # 將根節點加入隊列
        q.append(root)

        # 持續遍歷隊列直到為空
        while q:
            level_length = len(q) - 1  # 當前層的最後一個節點的索引
            current_level_size = len(q)  # 當前層的節點數量

            for i in range(current_level_size):
                current = q.popleft()  # 取出當前節點

                # 如果不是當前層的最後一個節點，將 next 指向隊列中的下一個節點
                if i != level_length:
                    current.next = q[0]
                else:
                    current.next = None  # 如果是最後一個節點，next 指向 None

                # 將左子節點加入隊列（如果存在）
                if current.left:
                    q.append(current.left)
                # 將右子節點加入隊列（如果存在）
                if current.right:
                    q.append(current.right)

        return root  # 返回已連接 next 指針的樹
