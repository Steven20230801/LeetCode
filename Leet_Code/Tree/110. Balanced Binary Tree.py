from typing import Optional

from Leet_Code.Tree import TreeNode, root, print_tree, list_to_tree_node


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def dfs(root) -> list:

            if not root:
                return [True, 0]

            l_balance, l_height = dfs(root.left)
            r_balance, r_height = dfs(root.right)

            # 判斷是否平衡
            if not l_balance or not r_balance or abs(l_height - r_height) > 1:
                balance = False
            else:
                balance = True
            # 判斷高度
            height = max(l_height, r_height) + 1

            return [balance, height]

        balance, height = dfs(root)

        return balance


root = list_to_tree_node([1, 2, 2, 3, 3, None, None, 4, 4])

Solution().isBalanced(root)
