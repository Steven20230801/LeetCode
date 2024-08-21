from collections import deque
from typing import List, Optional
from Leet_Code.leetcode75.tree import TreeNode, list_to_tree_node


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        ans = []
        q = deque([root])
        while q:
            n = len(q) - 1
            for i in range(len(q)):
                node = q.popleft()
                if i == n:
                    ans.append(node.val)
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None

        return ans


root = [1, 2, 3, None, 5, None, 4]
root = list_to_tree_node(root)
Solution().rightSideView(root)
