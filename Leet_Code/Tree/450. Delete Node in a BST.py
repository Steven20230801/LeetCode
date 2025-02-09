from typing import Optional

from Leet_Code.Tree import TreeNode, root, print_tree, list_to_tree_node


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                root = root.right  # 1. 不確定要return 還是 root =
            elif not root.right:
                root = root.left
            else:
                # 找root.right最小的節點
                cur = root.right
                while cur and cur.left:
                    cur = cur.left

                root.val = cur.val
                root.right = self.deleteNode(root.right, key=cur.val)
        return root
