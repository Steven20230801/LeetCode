from typing import Optional

from Leet_Code.leetcode75.tree import TreeNode, print_tree, list_to_tree_node, root


class Solution:
    def __init__(self) -> None:

        self.prev = float("-inf")

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
        left = self.isValidBST(root.left)
        # 检查当前节点的值是否大于前一个节点的值
        if root.val > self.prev:
            self.prev = root.val
        else:
            return False

        right = self.isValidBST(root.right)

        return left and right


root = list_to_tree_node([2, 1, 3])
print_tree(root)
Solution().isValidBST(root)


root = list_to_tree_node([5, 1, 4, None, None, 3, 6])
print_tree(root)
Solution().isValidBST(root)
