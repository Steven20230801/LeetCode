from typing import Optional

from leetcode75.tree import TreeNode, root, print_tree

print_tree(root=root)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1


Solution().maxDepth(root)
