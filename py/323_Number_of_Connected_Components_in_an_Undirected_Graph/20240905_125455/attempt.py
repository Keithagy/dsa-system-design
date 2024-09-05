from collections import defaultdict
from typing_extensions import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {node: set() for node in range(n)}
        for [a, b] in edges:
            graph[a].add(b)
            graph[b].add(a)
        components = 0

        def dfs(node: int) -> None:
            neighbors = graph[node]
            del graph[node]
            for neighbor in neighbors:
                if neighbor in graph:
                    dfs(neighbor)

        for node in graph:
            dfs(node)
            components += 1
        return components
