# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def compare(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return self.compare(a.right, b.left) and self.compare(a.left, b.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.right and not root.left):
            return True
        if not root.right or not root.left:
            # one of the branches is empty whilst the other isn't
            return False
        return (
            root.left.val == root.right.val
            and self.compare(root.left.right, root.right.left)
            and self.compare(root.right.right, root.left.left)
        )

