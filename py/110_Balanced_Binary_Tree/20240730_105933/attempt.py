# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        # Initialize height_memo as an instance variable
        self.height_memo = {}

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Memoizing is potentially useful here becaue `isBalanced` calculates height of left/right subtrees twice each
        # memoizing saves (lh + rh) recursions, taking runtime complexity down from O(h^2) to O(h)
        # But of course, memory usage increases by a factor of `n`, since you memoize almost all nodes, wherehas previously memory would have
        # scaled only as a factor of h, which in a balaanced tree would be log n and in an unbalanced one would be n
        # so memory usage goes from log n - n, to n log n - n^2
        if root in self.height_memo:
            return self.height_memo[root]

        if not root.left and not root.right:
            height = 1
            self.height_memo[root] = height
            return height

        height = 1 + max(self.height(root.left), self.height(root.right))
        self.height_memo[root] = height
        return height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return (
            self.isBalanced(root.left)
            and self.isBalanced(root.right)
            and abs(self.height(root.left) - self.height(root.right)) <= 1
        )
