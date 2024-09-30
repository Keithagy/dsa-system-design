from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)

        for [a, b] in edges:
            graph[a].add(b)
            graph[b].add(a)

        q = deque([node for node in range(n) if len(graph[node]) == 1])

        while len(graph) > 2:
            nodes_at_height = len(q)
            for _ in range(nodes_at_height):
                leaf = q.popleft()
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) == 1:
                        q.append(neighbor)
                del graph[leaf]
        return [node for node in graph]

