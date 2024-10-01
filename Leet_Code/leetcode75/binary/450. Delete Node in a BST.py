from typing import Optional
from Leet_Code.leetcode75.tree import TreeNode, print_tree, list_to_tree_node

root = list_to_tree_node([5,3,6,2,4,None,7])
print_tree(root)

class Solution:

    def find_min(self, root):

        if not root:
            return 
        
        res = root.val

        while root.left:
            res = root.left.val
            root = root.left
            
        return res
            

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        if key > root.val:# 往右邊找
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key) # 往左邊找
        else:
            # 找到了 開始刪除
            if not root.left: # 若left是None, 把root換成右邊節點
                return root.right
            if not root.right:
                return root.left
            else:
                min_node_val = self.find_min(root.right)
                root.val = min_node_val
                root.right = self.deleteNode(root.right, min_node_val)

        return root         
        
        
Solution().find_min(root)

root = Solution().deleteNode(root, key=3)
print_tree(root)

root = Solution().deleteNode(root, key=30)
print_tree(root)