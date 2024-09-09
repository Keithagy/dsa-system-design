# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counts = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        def dfs(node: Optional[TreeNode], curSum: int) -> None:
            nonlocal counts
            if not node:
                return
            curSum += node.val
            excess = curSum - targetSum
            counts += prefix_sums[excess]
            prefix_sums[curSum] += 1
            dfs(node.left, curSum)
            dfs(node.right, curSum)
            prefix_sums[curSum] -= 1

        dfs(root, 0)
        return counts

