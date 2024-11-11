from cmath import inf
from typing import List, Optional

from Leet_Code.Tree import TreeNode, print_tree

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0

        def dfs(node, max_int):
            nonlocal res 
            if not node:
                return 

            if node.val >= max_int:
                res += 1
                max_int = max(max_int, node.val)
            
            dfs(node.left, max_int)
            dfs(node.right, max_int)

        dfs(root, -inf)
        return res