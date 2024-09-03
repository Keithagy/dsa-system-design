# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # You can use a level-scoped coordinate system to determine the end nodes
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        mw = 0
        q = deque([(root, 1)])
        level = 0
        while q:
            nodes_this_level = len(q)
            min_coord, max_coord = (2**level) + 1, 0
            for _ in range(nodes_this_level):
                (node, coord) = q.popleft()
                min_coord = min(min_coord, coord)
                max_coord = max(max_coord, coord)
                if node.left:
                    q.append((node.left, (coord * 2) - 1))
                if node.right:
                    q.append((node.right, coord * 2))
            w = max_coord - min_coord + 1
            mw = max(mw, w)
            level += 1
        return mw

