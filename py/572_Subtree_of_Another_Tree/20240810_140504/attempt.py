# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        assert subRoot
        if not root:
            return False

        def isSameTree(
            candidate: Optional[TreeNode], target: Optional[TreeNode]
        ) -> bool:
            if not candidate and not target:
                return True
            if not candidate or not target:
                return False
            if candidate.val != target.val:
                return False
            return isSameTree(candidate.left, target.left) and isSameTree(
                candidate.right, target.right
            )

        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

