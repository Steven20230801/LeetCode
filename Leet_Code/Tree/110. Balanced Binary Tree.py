from typing import Optional

from Leet_Code.Tree import TreeNode, root, print_tree, list_to_tree_node


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 左右高度差 <= 1
        def maxDepth(root: Optional[TreeNode]) -> int:
            # 如果當前節點為空，深度為0
            if not root:
                return 0
            # 遞迴計算左子樹的最大深度
            left = self.maxDepth(root.left)
            # 遞迴計算右子樹的最大深度
            right = self.maxDepth(root.right)
            # 返回左右子樹中較大深度加1（當前節點）
            return max(left, right) + 1
