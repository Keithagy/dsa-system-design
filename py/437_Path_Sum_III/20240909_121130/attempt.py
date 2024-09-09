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
        prefixSums = defaultdict(int)
        prefixSums[0] = 1  # There is always one way to drop a prefix of 0
        count = 0

        def dfs(node: Optional[TreeNode], curSum: int) -> None:
            nonlocal count
            if not node:
                return
            curSum += node.val
            need_drop = curSum - targetSum
            count += prefixSums[need_drop]

            prefixSums[curSum] += 1
            dfs(node.left, curSum)
            dfs(node.right, curSum)
            prefixSums[curSum] -= 1

        dfs(root, 0)
        return count

