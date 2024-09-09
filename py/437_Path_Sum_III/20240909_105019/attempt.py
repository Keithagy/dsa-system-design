# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # You want the number of paths
    # Path does not have to start at root or leaf >> you might need to 'backtrack' the front of the path. use deque for path?
    # again node values can be negative, so you cannot prune branches based on seeing the target sum. E.g you can have targetsum as a single-node path, and you can then have targetSum +1 -1 as another path.
    """
    consider cases:
    single node: 1 path only
    one parent one child: 3 paths
        parent only
        child only
        parent + child
    one parent 2 children: 5 paths
        parent only
        left only
        right only
        parent + left
        parent + right

    """

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path_count = 0

        def checkPaths(node: Optional[TreeNode], sum: int) -> None:
            nonlocal path_count
            if not node:
                return
            sum += node.val
            if sum == targetSum:
                path_count += 1

            checkPaths(node, 0)

            checkPaths(node.left, sum)
            checkPaths(node.right, sum)

        checkPaths(root, 0)
        return path_count

