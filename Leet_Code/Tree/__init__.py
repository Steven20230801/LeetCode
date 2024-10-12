class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


# 建立樹結構
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3))

# if root.left.left:
#     print("root.left.left")


def get_tree_depth(root):
    if not root:
        return 0
    return max(get_tree_depth(root.left), get_tree_depth(root.right)) + 1


def print_tree(root):
    if not root:
        return

    depth = get_tree_depth(root)
    width = 2**depth - 1
    rows = [[" " for _ in range(width)] for _ in range(depth)]

    def fill_rows(node, row, col, depth):
        if not node:
            return
        rows[row][col] = str(node.val)
        fill_rows(node.left, row + 1, col - 2 ** (depth - row - 2), depth)
        fill_rows(node.right, row + 1, col + 2 ** (depth - row - 2), depth)

    fill_rows(root, 0, width // 2, depth)
    rows = ["=========="] + rows + ["=========="]
    for row in rows:
        print("".join(row))


def preOrderTraversal(root):
    result = []

    def helper(node):
        if node:
            result.append(node.val)
            helper(node.left)
            helper(node.right)

    helper(root)
    return result


preOrderTraversal(root)


#     helper(root)
#     return result
# # 遞歸前序遍歷
# print(preOrderTraversal(root))  # 輸出: [1, 2, 4, 5, 3]

# # 迭代前序遍歷
# print(preOrderTraversal(root))  # 輸出: [1, 2, 4, 5, 3]


# def inOrderTraversal(root):
#     result = []

#     def helper(node):
#         if node:
#             helper(node.left)
#             result.append(node.val)
#             helper(node.right)

#     helper(root)
#     return result


# print(inOrderTraversal(root))  # 輸出: [4, 2, 5, 1, 3]


def list_to_tree_node(List):
    if not List:
        return None

    # 创建根节点
    root = TreeNode(List[0])
    queue = [root]
    i = 1

    # 使用队列构建二叉树
    while queue and i < len(List):
        node = queue.pop(0)

        # 构建左子节点
        if i < len(List) and List[i] is not None:
            node.left = TreeNode(List[i])
            queue.append(node.left)
        i += 1

        # 构建右子节点
        if i < len(List) and List[i] is not None:
            node.right = TreeNode(List[i])
            queue.append(node.right)
        i += 1

    return root


# 示例列表
