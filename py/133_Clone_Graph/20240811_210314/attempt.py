"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        cloned = {}
        visited = set()
        queue = deque([node])
        while queue:
            base = queue.popleft()
            if base in visited:
                continue
            if base not in cloned:
                cloned[base] = Node(val=base.val)
            for neighbor in base.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(val=neighbor.val)
                cloned[base].neighbors.append(cloned[neighbor])
                queue.append(neighbor)
            visited.add(base)
        return cloned[node]

