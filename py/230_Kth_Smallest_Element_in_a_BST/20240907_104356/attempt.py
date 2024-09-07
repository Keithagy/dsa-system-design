# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # key insight: in-order traversal of a bst gives a sorted list.
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        idx = -1
        result = 0

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal idx, result
            if not node:
                return
            inorder(node.left)
            if idx == k - 1:
                return
            idx += 1
            result = node.val
            if idx == k - 1:
                return
            inorder(node.right)

        inorder(root)
        return result

