# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkRange(
            node: Optional[TreeNode], low: Optional[int], high: Optional[int]
        ) -> bool:
            if not node:
                return True
            if (low is not None and node.val <= low) or (
                high is not None and node.val >= high
            ):
                return False
            return checkRange(node.left, low, node.val) and checkRange(
                node.right, node.val, high
            )

        return checkRange(root, None, None)

