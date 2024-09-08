from typing import Optional

from Leet_Code.leetcode75.tree import TreeNode, root, root2, print_tree


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        l, r = [], []

        def dfs(root, leaf):
            if not root.left and not root.right:
                leaf.append(root.val)
                return

            if root.left:
                dfs(root.left, leaf)

            if root.right:
                dfs(root.right, leaf)

        dfs(root1, l)
        dfs(root2, r)

        return l == r


print_tree(root)
print_tree(root2)


Solution().leafSimilar(root, root)
