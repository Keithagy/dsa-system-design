from collections import deque
from typing import List


class Solution:
    # Iterative leaf removal approach
    # core intuition: a graph can only have 2 centers at maximum
    # these centers have to be the roots of the minimum height tree,
    # since they sit in the middle of the longest path through the graph.
    # build the graph, then use a queue to remove leaves layer by layer until no more than 2 nodes remain.
    # time: O(n), since you visit n nodes to build the graph, then pop up to (n-1) nodes
    # space: O(n) for the graph.
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        graph = [set() for _ in range(n)]
        for [a, b] in edges:
            graph[a].add(b)
            graph[b].add(a)

        def isLeaf(node: int):
            return len(graph[node]) == 1

        queue = deque([node for node in range(len(graph)) if isLeaf(node)])
        nodes_remaining = n
        while nodes_remaining > 2:
            leaf_count = len(queue)
            nodes_remaining -= leaf_count
            for _ in range(leaf_count):
                leaf = queue.popleft()
                for neighbor in graph[leaf]:
                    graph[neighbor].discard(leaf)
                    if isLeaf(neighbor):
                        queue.append(neighbor)
        return list(queue)

