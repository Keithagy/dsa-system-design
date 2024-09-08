from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # node values can be negative, so there goes an opening for terminating early
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []

        def dfs(node: Optional[TreeNode], path: List[int], sum: int) -> None:
            if not node:
                return
            if sum == targetSum and not node.left and not node.right:
                result.append(path[:])
                return
            if node.left:
                path.append(node.left.val)
                dfs(node.left, path, sum + node.left.val)
                path.pop()
            if node.right:
                path.append(node.right.val)
                dfs(node.right, path, sum + node.right.val)
                path.pop()

        dfs(root, [root.val], root.val)
        return result

