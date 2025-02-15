from math import inf
from typing import Optional

from Leet_Code.Tree import TreeNode, root, print_tree, list_to_tree_node


class Solution:
    def __init__(self) -> None:
        self.prev = -inf

    # def validate(self, val, right, left):
    #     if left < val < right:
    #         return True
    #     else:
    #         return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        # 檢驗左邊是否是有序的
        check_left = self.isValidBST(root.left)

        if not check_left:
            return False

        # 檢驗中間值與先前值
        if self.prev >= root.val:
            return False

        self.prev = root.val
        check_right = self.isValidBST(root.right)

        if not check_right:
            return False

        return True


root = list_to_tree_node([2, 1, 3])
print_tree(root)
Solution().isValidBST(root)


class Solution:

    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:

        if not root:
            return True

        # 要驗證左邊 & 右邊都是valid & val 介於left & right
        # left 最大值要小於root.val
        val = root.val
        return self.isValidBST(root.left, left, val) and self.isValidBST(root.right, val, right) and (left < val < right)


root = list_to_tree_node([2, 1, 3])
print_tree(root)
Solution().isValidBST(root)
