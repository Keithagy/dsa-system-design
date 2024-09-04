# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # subtree needs to provide info
    # if p is my right child, then i am the successor
    # if p is my right child, then my (grand)parent might be the successor
    # in which case, my recursive search function should tell left bound, right bound indices
    # then, i can know my index ( left-right + 1 ), and i can know my right bound (right-right + idx)
    # recursive search should also say Optional[p-index]
    # then, when i figure out my index, i update global state with myself if i come immediately after
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        result: Optional[TreeNode] = None

        def visit(
            node: Optional[TreeNode],
        ) -> Tuple[int, Optional[int], int]:
            nonlocal result
            if not node:
                return (-1, None, -1)
            if not node.left and not node.right:
                return (0, 0 if node.val == p.val else None, 0)
            left_low, left_p_idx, left_high = visit(node.left)
            my_idx = left_high + 1
            if left_p_idx and my_idx == left_p_idx + 1:
                result = node
                return (-1, None, -1)
            _, right_p_idx, right_high = visit(node.right)
            return (
                left_low,
                (
                    left_p_idx
                    if left_p_idx is not None
                    else right_p_idx + my_idx + 1 if right_p_idx else None
                ),
                right_high + my_idx + 1,
            )

        visit(root)
        return result
