# Definition for a binary tree node.
from typing_extensions import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        def subtreeAtNodeHas(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None

            if node is p or node is q:
                return node

            check_left, check_right = subtreeAtNodeHas(node.left), subtreeAtNodeHas(
                node.right
            )

            if check_left and check_right:
                return node

            return check_left if check_left else check_right

        return subtreeAtNodeHas(root) or root

