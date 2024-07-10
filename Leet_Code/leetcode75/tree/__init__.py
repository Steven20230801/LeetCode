class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 建立樹結構
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

if root.left.left:
    print("root.left.left")


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
