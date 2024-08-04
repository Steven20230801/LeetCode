from typing import Optional

from leetcode75.tree import TreeNode, root, root2, print_tree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # 若p跟q都是null的時候 -> 是相同的tree
        if not p and not q:
            return True
        # 若一個node非空則不相同
        if not p or not q:
            return False
        # 剩下狀況是都有node, 需比較node.val是否相同
        if p.val != q.val:
            return False

        is_left_same = self.isSameTree(p.left, q.left)
        is_right_same = self.isSameTree(p.right, q.right)

        return is_left_same and is_right_same

    def isSymmetric(sefl, root: Optional[TreeNode]) -> bool:
        # 判斷left right:
        def dfs(left, right):
            # 若左子 跟 右子都是NULL
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            # 判斷左的左 跟右的右
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)

        # check root.left = root.right


Solution().isSameTree(root, root)
Solution().isSameTree(root, root2)
Solution().isSymmetric(root)
