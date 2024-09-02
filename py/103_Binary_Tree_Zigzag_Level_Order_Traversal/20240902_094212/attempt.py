# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time, O(w) space for the queue
    # bfs with a counter to track alternating levels
    # if alternating, reverse before appending
    # input: [3,9,20,8,45,15,7]
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])  # [9,20]
        rev = False  # False
        res = []  # [[3], [20,9]]
        while q:
            nq = deque()  # [8,45,15,7]
            output = []  # [20,9]
            n = len(q)  # 2
            for _ in range(n):  # [1]
                node = q.popleft()  # 20
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
                output.append(node.val)
            if rev:
                output.reverse()
            rev = not rev
            res.append(output)
            q = nq
        return res

