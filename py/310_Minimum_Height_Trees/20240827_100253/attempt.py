from collections import deque
from typing import List


class Solution:
    # We want to find the centres of the graph, of which there are a max of 2
    # remove leaves until no more than 2 remain
    # input: n=3, edges [[0,1], [0,2]]
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
      if n <= 1:
        return list(range(n))

      # {
      #   0: {},
      #   1: {},
      #   2: {},
      # }
      graph = [set() for _ in range(n)]
      for [a,b] in edges:
        graph[a].add(b)
        graph[b].add(a)

      def isLeaf(node:int)->bool:
        return len(graph[node])==1

      # [0]
      leaves = deque([node for node in range(n) if isLeaf(node)])

      node_count = n # 1
      while node_count > 2:
        leaf_count = len(leaves) # 2
        node_count -= leaf_count
        for _ in range(leaf_count): # x,1
          leaf = leaves.popleft() # 2
          for neighbor in graph[leaf]: # {0}
            graph[neighbor].discard(leaf) # graph[0]
            if isLeaf(neighbor):
              leaves.append(neighbor)
          graph[leaf].clear()
      return list(leaves) #[0]
