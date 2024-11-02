from collections import deque
import queue
from typing import List, Optional

from regex import R

from Leet_Code.Tree import TreeNode, list_to_tree_node, print_tree


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)
        while queue:

            length = len(queue)

            for i in range(length):

                node = queue.popleft()

                if i == length - 1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return res


# GPT註解
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 如果根節點為空，返回空列表
        if not root:
            return []

        res = []  # 用於存儲每一層最右邊的節點值
        queue = deque()  # 初始化隊列，用於 BFS
        queue.append(root)  # 將根節點加入隊列

        while queue:
            length = len(queue)  # 當前層的節點數量

            for i in range(length):
                node = queue.popleft()  # 取出當前層的節點

                # 如果是當前層的最後一個節點，將其值加入結果
                if i == length - 1:
                    res.append(node.val)

                # 將左子節點加入隊列（若存在）
                if node.left:
                    queue.append(node.left)

                # 將右子節點加入隊列（若存在）
                if node.right:
                    queue.append(node.right)

        return res  # 返回結果列表


root = [1, 2, 3, None, 5, None, 4]

print_tree(list_to_tree_node(root))
