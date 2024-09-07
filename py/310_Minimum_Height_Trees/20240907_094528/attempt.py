from collections import deque
from typing import List


class Solution:
    # Topological-sort-like approach where you keep removing from the edges until at most 2 nodes remain
    # core idea: the height is minimized at the nodes that centre the longest path through the tree
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {node: set() for node in range(n)}
        for [a, b] in edges:
            graph[a].add(b)
            graph[b].add(a)
        q = deque(
            [node for node in graph if len(graph[node]) <= 1]
        )  # start from the leaves; assuming that the graph is guaranteed to be a tree there should not be disconnected components
        while len(graph) > 2:
            nodes_at_height = len(q)
            for _ in range(nodes_at_height):
                leaf = q.popleft()
                if leaf not in graph:
                    continue  # already visited from some other previous leaf
                for neighbor in graph[leaf]:
                    graph[neighbor].discard(leaf)
                    if len(graph[neighbor]) <= 1:
                        q.append(neighbor)
                del graph[leaf]
        return [node for node in graph]

