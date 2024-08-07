# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mirrors(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return self.mirrors(a.right, b.left) and self.mirrors(a.left, b.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        if root.left.val != root.right.val:
            return False
        return self.mirrors(root.left.right, root.right.left) and self.mirrors(
            root.right.right, root.left.left
        )

