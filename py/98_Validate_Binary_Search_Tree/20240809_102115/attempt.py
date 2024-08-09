# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        in_order_traversal = []

        def in_order_traverse(node: Optional[TreeNode]):
            if not node:
                return
            if node.left:
                in_order_traverse(node.left)
            in_order_traversal.append(node.val)
            if node.right:
                in_order_traverse(node.right)

        in_order_traverse(root)

        for i in range(len(in_order_traversal) - 1):
            if in_order_traversal[i] >= in_order_traversal[i + 1]:
                return False
        return True

