from collections import deque
from typing import List, Optional
from Leet_Code.Tree import TreeNode, list_to_tree_node, print_tree


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        res = []
        queue = deque()
        queue.append(root)

        while queue:

            n = len(queue)
            total = 0
            for i in range(n):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            avg = total / n
            res.append(avg)

        return res


# gpt

from collections import deque
from typing import Optional, List


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        res = []
        queue = deque([root])  # 直接在初始化時加入根節點

        while queue:
            level_size = len(queue)  # 當前層的節點數量
            total = 0

            for _ in range(level_size):
                node = queue.popleft()
                total += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(total / level_size)  # 直接計算並加入結果列表

        return res


root = list_to_tree_node([3, 9, 20, None, None, 15, 7])
Solution().averageOfLevels(root)
