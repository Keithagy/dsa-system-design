from collections import defaultdict
from typing import Dict, List, Optional, Set


class Solution:
    # What dictates a valid tree?
    # no cycles
    # each node has 1 parent
    # fully connected
    # You can construct the graph based on the adjacency list (O(n))
    # This gives you a hashmap repr Dict[Node,Set[Node]]
    # Pick one entry point and traverse dfs. You should not loop back into visited set
    # At the end of the traversal, len(visited) == len(graph)
    # O(n) time, O(n) extra memory
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n <= 1
        graph: Dict[int, Set[int]] = defaultdict(set)
        for [a, b] in edges:
            graph[a].add(b)
            graph[b].add(a)
        visited = set()

        def dfs(node: int) -> bool:
            if node in visited:
                return False
            visited.add(node)
            next = graph[node]
            for next_node in next:
                graph[next_node].discard(node)
                if not dfs(next_node):
                    return False
            return True

        return len(graph) == len(visited) == n and dfs(edges[0][0])
