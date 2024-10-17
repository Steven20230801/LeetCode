from typing import List, Optional

from Leet_Code.Tree import TreeNode, print_tree


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = dfs(l=l, r=m - 1)
            root.right = dfs(l=m + 1, r=r)
            return root

        root = dfs(0, len(nums) - 1)
        return root


# GPT
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l, r):
            # 如果左指針超過右指針，表示當前子陣列沒有元素，返回 None
            if l > r:
                return None
            # 找到當前子陣列的中間索引
            m = (l + r) // 2
            # 創建根節點，值為中間元素
            root = TreeNode(nums[m])
            # 遞迴構建左子樹，使用左半部分的子陣列
            root.left = dfs(l=l, r=m - 1)
            # 遞迴構建右子樹，使用右半部分的子陣列
            root.right = dfs(l=m + 1, r=r)
            return root

        # 初始調用，傳入整個陣列的起始和結束索引
        root = dfs(0, len(nums) - 1)
        return root


root = Solution().sortedArrayToBST(nums=[-10, -3, 0, 5, 9])
print_tree(root)
