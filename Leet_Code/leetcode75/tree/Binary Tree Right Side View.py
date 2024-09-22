from collections import deque
from typing import List, Optional
from Leet_Code.leetcode75.tree import TreeNode, list_to_tree_node, print_tree


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


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        q = deque()
        q.append(root)
        ans = []
        while q:
            n = len(q) - 1
            for i in range(len(q)):

                node = q.popleft()

                if i == n:
                    ans.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
        return ans


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        def dfs(root, depth):
            if not root:
                return
            if len(ans) == depth:
                ans.append(root.val)

            # 先從右邊開始看
            dfs(root.right, 1 + depth)
            dfs(root.left, 1 + depth)

        dfs(root, 0)
        return ans


root = [1, 2, 3, None, 5, None, 4]
root = list_to_tree_node(root)
print_tree(root)
Solution().rightSideView(root)
