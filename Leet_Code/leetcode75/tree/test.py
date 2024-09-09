from typing import List, Optional

from Leet_Code.leetcode75.tree import TreeNode, print_tree, root


class Solution:

    def __init__(self):
        self.ans = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        self.inorderTraversal(root.left)
        self.ans.append(root.val)
        self.inorderTraversal(root.right)

        return self.ans
