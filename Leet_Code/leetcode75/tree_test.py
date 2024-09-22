from collections import deque
from typing import Optional

from Leet_Code.leetcode75.tree import TreeNode, root, print_tree

print_tree(root=root)


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":

        if not root:
            return

        if root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left:
            return left

        if right:
            return right


print_tree(Solution().lowestCommonAncestor(root, TreeNode(4), TreeNode(5)))
