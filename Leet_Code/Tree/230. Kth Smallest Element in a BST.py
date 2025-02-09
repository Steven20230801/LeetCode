from typing import Optional

from Leet_Code.Tree import TreeNode, root, print_tree, list_to_tree_node


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res[k - 1]
    
    def kthSmallest_stack(self, root: Optional[TreeNode], k: int) -> int:
        
        



root = list_to_tree_node([5, 3, 6, 2, 4, None, None, 1])
k = 3
print_tree(root)
Solution().kthSmallest(root, k)