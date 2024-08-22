# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(
            node: Optional[TreeNode], low: Optional[int], high: Optional[int]
        ) -> bool:
            if not node:
                return True
            if (
                not (low if low is not None else -float("inf"))
                < node.val
                < (high if high is not None else float("inf"))
            ):
                return False
            return validate(node.left, low, node.val) and validate(
                node.right, node.val, high
            )

        return validate(root, None, None)

