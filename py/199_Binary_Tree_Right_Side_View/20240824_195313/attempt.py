# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # You can get the answer by traversing the tree level order and appending the final element of each level.
    # Level order can be attained using a queue (BFS)
    # We would be able to solve it in O(n) where n is number of nodes
    # Space: O(max( w, h )) where w is the max width of the tree and h is the depth
    # the dominating factor depends on whether the tree is wide, in which case the dominating allocation would be the queue,
    # or if it is deep, in which case the dominating allocation would be the result array.
    # input:
    #      [1]
    #   [2] [3]
    # [5]
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []

        queue = deque([root])

        while queue:  # [5]
            result.append(queue[-1].val)  # [1,3,5]
            nodes_in_level = len(queue)  # 2
            for _ in range(nodes_in_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

