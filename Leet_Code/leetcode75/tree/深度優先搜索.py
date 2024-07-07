from Leet_Code.leetcode75.tree import TreeNode, root


# 前中後續遍歷遞歸
def preOrderTraversal(root: TreeNode):
    s = []
    # 前序遍历: 根左右
    if not root:
        return

    print(root.val)
    # s.append(root.val)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


def inOrderTraversal(root: TreeNode):
    # 中序遍历: 左根右
    if not root:
        return

    inOrderTraversal(root.left)
    print(root.val)
    # s.append(root.val)
    inOrderTraversal(root.right)


def postOrderTraversal(root: TreeNode):
    # 後序遍历: 左右根
    if not root:
        return

    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.val)
    # s.append(root.val)


preOrderTraversal(root)
inOrderTraversal(root)
postOrderTraversal(root)


# 深度優先搜索
def dfs(root: TreeNode, target: int) -> TreeNode:
    if not root:
        return None

    if root.val == target:
        return root

    left = dfs(root.left, target)
    if left:
        return left

    right = dfs(root.right, target)
    if right:
        return right

    return None
