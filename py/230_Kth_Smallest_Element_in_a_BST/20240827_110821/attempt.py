# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # in order traversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        result = -1

        def visitKthSmallest(root: Optional[TreeNode]) -> Tuple[int, int]:
            nonlocal result
            if not root:
                return (0, 0)
            (left_low, left_high) = visitKthSmallest(root.left)
            root_order = left_high + 1
            if root_order == k:
                result = root.val
            (_, right_high) = visitKthSmallest(root.right)
            return (left_low, right_high + root_order)

        visitKthSmallest(root)
        return result

