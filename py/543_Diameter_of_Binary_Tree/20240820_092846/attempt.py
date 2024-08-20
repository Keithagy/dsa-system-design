# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Key insight is that any node can choose to route the longest path through its children through it, or to consider its children path a closed circuit
    # The actions at each node are to `connect`(path through left and right) or `propagate` (bubble up path through left or right)
    # connecting yields path of length `left_path + right_path + 2` (because 2 additional edges are considered, node->left and node -> right)
    # propagate yields path of length `max(left_path, max(right_path))`
    # we need the longest path through any 2 nodes in a tree, so a given node might need to be aware of longest paths a few layers down
    # recursive function should thus return 2 paths, signalling payoff of each respective action
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        # path through left, path through right
        def inner(root: Optional[TreeNode]) -> Tuple[int, int]:
            nonlocal diameter
            if not root:
                return (-1, -1)
            path_left_left, path_left_right = inner(root.left)
            path_right_left, path_right_right = inner(root.right)
            left_longest = max(path_left_left, path_left_right)
            right_longest = max(path_right_left, path_right_right)
            path_through_me = left_longest + right_longest + 2
            diameter = max(diameter, path_through_me)
            return (
                left_longest + 1,
                right_longest + 1,
            )

        inner(root)
        return diameter

