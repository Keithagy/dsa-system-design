from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0

        return (
            self.maxHeightOfSubTrees(root.left)
            + self.maxHeightOfSubTrees(root.right)
            + 2
        )

    def maxHeightOfSubTrees(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if not root:
            return (-1, -1)

        left_subtree_heights = self.maxHeightOfSubTrees(root.left)
        right_subtree_heights = self.maxHeightOfSubTrees(root.right)
        return (
            max(left_subtree_heights[0], left_subtree_heights[1]) + 1,
            max(right_subtree_heights[0], right_subtree_heights[1]) + 1,
        )

