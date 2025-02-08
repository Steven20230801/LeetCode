from typing import Optional

from Leet_Code.Tree import TreeNode, root, print_tree, list_to_tree_node


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


# root = [4,2,7,1,3], val = 5

root = list_to_tree_node([4, 2, 7, 1, 3])
val = 5
print_tree(Solution().insertIntoBST(root, val))
