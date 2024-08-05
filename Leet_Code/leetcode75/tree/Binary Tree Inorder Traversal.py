from typing import List, Optional

from leetcode75.tree import TreeNode, print_tree, root


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

    def inorderTraversal_st(self, root):
        st = []
        cur = root
        while cur and cur.left:
            st.append(cur.val)
            cur = cur.left
        self.inorderTraversal_st(root.left)


print_tree(root)
Solution().inorderTraversal(root)
Solution().inorderTraversal_st(root)
