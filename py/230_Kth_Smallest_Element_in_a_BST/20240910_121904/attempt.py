# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = -1
        e = 0

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal i, e
            if not node or i == k - 1:
                return
            inorder(node.left)
            if i == k - 1:
                return
            i += 1
            e = node.val
            inorder(node.right)

        inorder(root)
        return e

