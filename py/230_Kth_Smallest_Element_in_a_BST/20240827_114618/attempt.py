# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        value = -1

        def visit(root: Optional[TreeNode]):
            nonlocal count, value
            if not root:
                return
            visit(root.left)
            if count == k:
                return
            count += 1
            value = root.val
            visit(root.right)

        visit(root)
        return value

