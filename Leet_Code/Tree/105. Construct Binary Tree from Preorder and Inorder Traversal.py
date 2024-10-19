from collections import Counter
from typing import List, Optional

from Leet_Code.Tree import TreeNode, print_tree


# NEETCODE
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 如果前序遍歷為空，返回 None
        if not preorder:
            return None

        # 前序遍歷的第一個元素是根節點
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 找到根節點在中序遍歷中的索引
        mid = inorder.index(root_val)

        # 根節點左側的中序遍歷對應前序遍歷的 [1:mid+1]
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

        # 根節點右側的中序遍歷對應前序遍歷的 [mid+1:]
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root


# GPT
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 建立一個哈希表來存儲中序遍歷中每個值的索引
        inorder_index_map = {value: idx for idx, value in enumerate(inorder)}

        # 定義遞迴函數，使用指標來避免切片操作
        def array_to_tree(pre_left: int, pre_right: int, in_left: int, in_right: int) -> Optional[TreeNode]:
            if pre_left > pre_right:
                return None

            # 前序遍歷的第一個元素是根節點
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            # 根節點在中序遍歷中的索引
            in_root_idx = inorder_index_map[root_val]

            # 左子樹的大小
            left_size = in_root_idx - in_left

            # 構建左子樹
            root.left = array_to_tree(pre_left + 1, pre_left + left_size, in_left, in_root_idx - 1)

            # 构建右子樹
            root.right = array_to_tree(pre_left + left_size + 1, pre_right, in_root_idx + 1, in_right)

            return root

        n = len(preorder)
        return array_to_tree(0, n - 1, 0, n - 1)


print_tree(Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
