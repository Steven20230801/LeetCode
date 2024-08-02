from typing import Optional
from leetcode75.tree import TreeNode, root


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        is_left_same = self.isSameTree(p.left, q.left)
        is_right_same = self.isSameTree(p.right, q.right)

        return is_left_same and is_right_same


def preOrderTraversal(root):
    result = []

    def helper(node):
        if node:
            result.append(node.val)
            helper(node.left)
            helper(node.right)

    helper(root)
    return result
