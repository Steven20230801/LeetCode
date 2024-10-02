from typing import Optional
from Leet_Code.leetcode75.tree import TreeNode, print_tree, list_to_tree_node

root = list_to_tree_node([5,3,6,2,4,None,7])
print_tree(root)

class Solution:
    def find_min(self, root):
        """
        找到以 root 為根的子樹中的最小節點（即最左下的節點）
        """
        if not root:
            return None  # 如果樹為空，返回 None
        cur = root
        while cur and cur.left:
            cur = cur.left  # 一直往左走，直到沒有左子節點
        return cur  # 返回最小節點

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        刪除 BST 中值為 key 的節點，並返回刪除後的樹的根節點
        """
        if not root:
            return None  # 如果樹為空，直接返回 None

        val = root.val  # 當前節點的值

        if key > val:
            # 如果 key 大於當前節點的值，則在右子樹中刪除
            root.right = self.deleteNode(root.right, key)
        elif key < val:
            # 如果 key 小於當前節點的值，則在左子樹中刪除
            root.left = self.deleteNode(root.left, key)
        else:
            # 找到了要刪除的節點
            if not root.left:
                # 如果沒有左子節點，返回右子節點（可能為 None）
                return root.right
            elif not root.right:
                # 如果沒有右子節點，返回左子節點
                return root.left
            else:
                # 如果有兩個子節點，找到右子樹中的最小節點
                min_node = self.find_min(root.right)
                # 用最小節點的值替換當前節點的值
                root.val = min_node.val
                # 刪除右子樹中的最小節點
                root.right = self.deleteNode(root.right, min_node.val)
        return root  # 返回（可能已更新的）根節點
        
Solution().find_min(root)

root = Solution().deleteNode(root, key=3)
print_tree(root)

root = Solution().deleteNode(root, key=30)
print_tree(root)