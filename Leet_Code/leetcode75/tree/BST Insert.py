from typing import Optional

from leetcode75.tree import TreeNode, print_tree

root = TreeNode(3, TreeNode(2), TreeNode(5))
print_tree(root)


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            # return root
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root


test = Solution().insertIntoBST(root, val=4)
print_tree(test)
