from collections import deque
from typing import Optional

from Leet_Code.leetcode75.tree import TreeNode, root, print_tree

print_tree(root=root)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = deque()
        if not root:
            return
        d.append(root)

        while d:

            for i in range(len(d)):
                cur = d.popleft()

                if cur.left:
                    d.append(cur.left)
                if cur.right:
                    d.append(cur.right)

                cur.left, cur.right = cur.right, cur.left

        return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)

            root.left, root.right = root.right, root.left

        if not root:
            return None

        dfs(root)

        return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):
            if not root:
                return

            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)

        if not root:
            return None

        dfs(root)

        return root


print_tree(Solution().invertTree(root))
