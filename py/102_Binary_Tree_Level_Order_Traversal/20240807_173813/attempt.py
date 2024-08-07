from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([deque([root])])
        while queue:
            this_level = queue.popleft()
            values_this_level = [node.val for node in this_level]
            result.append(values_this_level)
            next_level = deque()
            while this_level:
                node = this_level.popleft()
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                queue.append(next_level)
        return result

