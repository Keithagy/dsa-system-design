# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        left_inv = self.invertTree(root.right)
        right_inv = self.invertTree(root.left)
        root.left = left_inv
        root.right = right_inv
        return root

