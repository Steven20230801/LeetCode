from typing import List, Optional

from Leet_Code.leetcode75.tree import TreeNode, print_tree, root, list_to_tree_node


lst = [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2]
root = list_to_tree_node(lst)
print_tree(root)


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def max_depth(root):
            if not root:
                return 0
            left = max_depth(root.left)
            right = max_depth(root.right)

            return max(left, right) + 1

        max_sum = 0
        if not root:

            return

            max_depth(root.left)
            max_depth(root.right)
        left = max_depth(root.left)
        right = max_depth(root.right)
        return left + right


print_tree(root)
Solution().diameterOfBinaryTree(root)
