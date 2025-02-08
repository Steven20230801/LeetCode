# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

from Leet_Code.Tree import TreeNode, root, print_tree, list_to_tree_node


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return None

        if root.val == val:
            return root

        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)


# root = [4,2,7,1,3], val = 2
root = list_to_tree_node([4, 2, 7, 1, 3])
val = 2
print_tree(Solution().searchBST(root, val))  # [2,1,3]
