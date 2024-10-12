from math import inf
from typing import Optional

from Leet_Code.Tree import TreeNode, list_to_tree_node, print_tree


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = inf

        def dfs(root):
            nonlocal res

            if not root:
                return
            if root.left:
                diff = root.val - root.left.val
                res = min(res, abs(diff))
                dfs(root.left)
            if root.right:
                diff = root.val - root.right.val
                res = min(res, abs(diff))
                dfs(root.right)

        dfs(root)

        return res


root = list_to_tree_node(List=[4, 2, 6, 1, 3])
print_tree(root=root)
Solution().getMinimumDifference(root=root)
