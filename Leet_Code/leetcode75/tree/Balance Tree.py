from typing import Optional
from Leet_Code.leetcode75.tree import TreeNode, print_tree, list_to_tree_node


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        path = []

        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            path.append(abs(left - right) <= 1)
            return max(left, right) + 1

        check(root)

        return sum(path) == len(path)
    


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        path = []

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1:
                return -1
            if abs(left - right) > 1:
                return -1  # 当前节点不平衡
            return max(left, right) + 1

        return dfs(root) != -1



root = list_to_tree_node([1, 2, 3, None, None, 4, 5, 4])
print_tree(root)

Solution().isBalanced(root)
