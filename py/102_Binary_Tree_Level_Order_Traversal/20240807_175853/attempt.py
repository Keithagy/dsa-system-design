# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.height = 0
        self.nodes = {}

        def dfs(root: Optional[TreeNode], height: int) -> None:
            if not root:
                return
            self.height = max(self.height, height)
            dfs(root.left, height + 1)
            self.nodes.setdefault(height, []).append(root)
            dfs(root.right, height + 1)

        dfs(root, 1)

        result = []
        for i in range(1, self.height + 1):
            result.append([node.val for node in self.nodes[i]])
        return result

