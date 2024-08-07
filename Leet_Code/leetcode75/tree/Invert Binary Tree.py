from collections import deque
from typing import Optional

from leetcode75.tree import TreeNode, root, print_tree

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
