from typing import Optional

from leetcode75.tree import TreeNode, print_tree

root = TreeNode(4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7)))
print_tree(root)


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)


inorder(root)
