from math import inf
from typing import Optional

from Leet_Code.Tree import TreeNode, list_to_tree_node, print_tree


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float('inf')  # 初始化最小差值為正無窮大
        prev = None  # 初始化前一個節點為 None

        def dfs(node):
            nonlocal res, prev  # 使用非局部變數 res 和 prev

            if not node:
                return  # 如果當前節點為空，則返回

            # 遍歷左子樹
            dfs(node.left)

            if prev is not None:
                # 計算當前節點值與前一個節點值的差，更新最小差值
                res = min(res, node.val - prev)
            
            # 更新前一個節點的值為當前節點的值
            prev = node.val

            # 遍歷右子樹
            dfs(node.right)

        # 開始深度優先搜尋
        dfs(root)

        # 返回最小差值
        return res


root = list_to_tree_node(List=[4, 2, 6, 1, 3])
print_tree(root=root)
Solution().getMinimumDifference(root=root)


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []          # 用於模擬調用棧的棧
        current = root      # 當前節點指針
        prev = None         # 初始化前一個節點為 None
        res = float('inf')  # 初始化最小差值為正無窮大

        # 中序遍歷迭代實現
        while stack or current:
            # 遍歷左子樹，將節點壓入棧中
            while current:
                stack.append(current)
                current = current.left
            
            # 訪問當前節點
            current = stack.pop()
            if prev is not None:
                # 計算當前節點值與前一個節點值的差，更新最小差值
                res = min(res, current.val - prev)
            prev = current.val  # 更新前一個節點的值為當前節點的值

            # 遍歷右子樹
            current = current.right

        return res  # 返回最小差值



root = list_to_tree_node(List=[4, 2, 6, 1, 3])
print_tree(root=root)
Solution().getMinimumDifference(root=root)