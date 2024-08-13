# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        lowest_common_ancestor: Optional[TreeNode] = None

        def find(
            node: Optional[TreeNode], p: TreeNode, q: TreeNode
        ) -> Tuple[bool, bool, bool]:
            nonlocal lowest_common_ancestor
            if (
                not node or lowest_common_ancestor
            ):  # second clause because you want recusion stack to collapse to nothing as soon as the LOWEST common ancestor is found
                return (False, False, False)
            is_me = in_my_left = in_my_right = False
            if p.val == node.val or q.val == node.val:
                is_me = True
            in_left_left, is_my_left, in_left_right = find(node.left, p, q)
            if in_left_left or is_my_left or in_left_right:
                in_my_left = True
            in_right_left, is_my_right, in_right_right = find(node.right, p, q)
            if in_right_left or is_my_right or in_right_right:
                in_my_right = True
            if (is_me and (in_my_left or in_my_right)) or (
                in_my_left and in_my_right and not lowest_common_ancestor
            ):
                lowest_common_ancestor = node
            return (in_my_left, is_me, in_my_right)

        find(root, p, q)
        return lowest_common_ancestor

