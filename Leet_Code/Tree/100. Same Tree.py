from typing import Optional

from Leet_Code.Tree import TreeNode, root, print_tree, list_to_tree_node


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        value = p.val == q.val
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return value and left and right


# GPT
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 如果兩個節點都是空的，則相同
        if not p and not q:
            return True
        # 如果其中一個節點是空的，另一個不是，則不同
        if not p or not q:
            return False
        # 如果當前節點的值不同，則不同
        if p.val != q.val:
            return False
        # 遞迴比較左子樹和右子樹
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


print(Solution().isSameTree(root, root))

root1 = list_to_tree_node([1, 2, 1])
root2 = list_to_tree_node([1, 1, 2])
print(Solution().isSameTree(root1, root2))
