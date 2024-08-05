# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root, subRoot, seeking_exact):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if seeking_exact and root.val != subRoot.val:
                return False
            if (
                root.val == subRoot.val
                and helper(root.left, subRoot.left, True)
                and helper(root.right, subRoot.right, True)
            ):
                return True
            return helper(root.left, subRoot, False) or helper(
                root.right, subRoot, False
            )

        return helper(root, subRoot, False)

