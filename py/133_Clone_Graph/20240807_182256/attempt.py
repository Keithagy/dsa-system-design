"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def __init__(self):
        self.node_pool = {}

    def set_links(self, for_ref: int, to_ref: int) -> None:
        self.node_pool[for_ref].neighbors.append(self.node_pool[to_ref])

    def create_if_not_exists(self, node_val: int) -> bool:
        if node_val in self.node_pool:
            return False
        self.node_pool[node_val] = Node(node_val, None)
        return True

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        self.create_if_not_exists(node.val)
        for neighbor in node.neighbors:
            new_neighbor = self.create_if_not_exists(neighbor.val)
            self.set_links(node.val, neighbor.val)
            if new_neighbor:
                self.cloneGraph(neighbor)
        return self.node_pool[node.val]

