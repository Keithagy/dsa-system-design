# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return -1
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            longest_path_thru_root = left_height + right_height + 2
            self.diameter = max(self.diameter, longest_path_thru_root)
            return max(left_height, right_height) + 1

        dfs(root)
        return self.diameter

