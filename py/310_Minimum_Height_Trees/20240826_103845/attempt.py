from typing import Dict, List, Set
from collections import defaultdict


class Solution:
    # An obvious way to do this is to build the graph, tracking nodes via a hash map(key is int, val is list[int])
    # and then iterate through every node to test the height
    # step 1 is O(n)
    # step 2 is O(n^2) >> for all n nodes, traverse n nodes to identify height of tree with a given node as root
    # dominating is O(n^2)
    # space would be O(n) for the hash map
    #
    # input: n = 3, edges = [[1,0], [0,2]]
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {node: [] for node in range(n)}
        for [a, b] in edges:
            graph[a].append(b)
            graph[b].append(a)

        heights: Dict[int, List[int]] = defaultdict(list)
        min_height = n + 1  # impossibly large number

        # node: 0, visited: {}
        # result = 0
        # visited = {0}
        # graph[node] = [1,2]
        #   node: 1, visited: {0}
        #   result = 0
        #   visited = {0,1}
        #   graph[node] = [0]
        #       node: 0, visited: {0,1}
        #       return -1
        #   visited = {0}
        #   return 0
        #   node: 2, visited: {0}
        #   result = -1
        #   visited = {0,2}
        #   graph[node] = [0]
        #       node: 0, visited: {0,2}
        #       return -1
        #   visited = {0}
        #   return 0
        # return 1
        #
        # node: 1, visited: {}
        # result = 0
        # visited = {1}
        # graph[node] = [0]
        #
        #   node: 0, visited: {1}
        #   result = 0
        #   visited = {1,0}
        #   graph[node] = [1,2]
        #       node: 1, visited: {1,0}
        #       return -1
        #
        #       node: 2, visited: {1,0}
        #       result = 0
        #       visited = {1,0,2}
        #       graph[node] = [0]
        #
        #          node: 0, visited: {1,0,2}
        #          return -1
        #       return 0
        #   return 1
        # return 2
        #
        # depth = {
        # 1: 0
        # 2: 1
        # }
        # min_height = 1
        # return [0]
        def depth(node: int, visited: Set[int]) -> int:
            if node in visited:
                return -1
            result = 0
            visited.add(node)
            for child in graph[node]:
                result = max(result, 1 + depth(child, visited))
            visited.discard(node)
            return result

        for node in graph:
            h = depth(node, set())
            heights[h].append(node)
            min_height = min(min_height, h)

        return heights[min_height]

