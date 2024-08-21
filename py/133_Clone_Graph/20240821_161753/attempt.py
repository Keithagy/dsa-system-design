"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Dict, Optional


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        cloned: Dict[Node, Node] = {}
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur not in cloned:
                cloned[cur] = Node(val=cur.val)
            for neighbor in cur.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(val=neighbor.val)
                    stack.append(neighbor)
                cloned[cur].neighbors.append(cloned[neighbor])
        return cloned[node]

