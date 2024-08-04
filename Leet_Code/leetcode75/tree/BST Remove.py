from typing import Optional

from leetcode75.tree import TreeNode, print_tree

root = TreeNode(4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7)))
print_tree(root)


# Find Min


class Solution:

    def find_min(self, root: TreeNode):
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur

    def remove(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if val > root.val:
            root.right = self.remove(root.right, val)
        elif val < root.val:
            root.left = self.remove(root.left, val)
            # return root
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.find_min(root.right)
                root.val = minNode.val
                root.right = self.remove(root.right, minNode.val)
        return root


root = Solution().remove(root, val=2)
print_tree(root)
