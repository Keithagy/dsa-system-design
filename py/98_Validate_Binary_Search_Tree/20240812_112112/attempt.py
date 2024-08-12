# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inner(
            root: Optional[TreeNode],
            low: Optional[int] = None,
            high: Optional[int] = None,
        ) -> bool:
            if not root:
                return True
            if (low is not None and root.val <= low) or (
                high is not None and root.val >= high
            ):
                return False
            return inner(root.left, low, root.val) and inner(root.right, root.val, high)

        return inner(root)

