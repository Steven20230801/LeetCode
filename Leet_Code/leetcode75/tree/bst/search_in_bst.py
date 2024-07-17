from typing import Optional
from Leet_Code.leetcode75.tree import TreeNode, root


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # 若到了沒有children的時候就反回
        if not root:
            return None

        if root.val < val:  # 若val 比較大 向右邊子樹找
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return root
