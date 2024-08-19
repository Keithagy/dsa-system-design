# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Dict, Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        memo: Dict[TreeNode, int] = {}

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            if node in memo:
                return memo[node]
            result = 1 + max(depth(node.left), depth(node.right))
            memo[node] = result
            return result

        def isHeightBalanced(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            return abs(depth(node.left) - depth(node.right)) <= 1

        def inner(root: Optional[TreeNode]) -> bool:
            if not root:
                return True
            return isHeightBalanced(root) and inner(root.left) and inner(root.right)

        return inner(root)

