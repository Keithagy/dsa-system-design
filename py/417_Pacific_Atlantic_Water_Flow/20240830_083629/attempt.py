from typing import List
from collections import deque

class Solution:
    # Use a queue to multi-source BFS for each ocean, climbing up toward maximas
    # accumulate cells visited in a hash set
    # return the intersection of those sets
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      rows = len(heights)
      cols = len(heights[0])

      pacific_cells, atlantic_cells = set(), set()
      pacific_flows, atlantic_flows = deque(), deque()
      for c in range(cols):
        pacific_flows.append((0,c))
        pacific_cells.add((0,c))
        atlantic_flows.append((rows-1,c))
        atlantic_cells.add((rows-1,c))
      for r in range(rows):
        pacific_flows.append((r,0))
        pacific_cells.add((r,0))
        atlantic_flows.append((r,cols-1))
        atlantic_cells.add((r,cols-1))

      directions = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0),
      ]
      def canFlowToFrom(r1:int,c1:int, r2:int, c2:int)->bool:
        return heights[r1][c1] <= heights[r2][c2]

      while pacific_flows:
        (r,c) = pacific_flows.popleft()
        for (rd,cd) in directions:
          nr,nc = r+rd, c+cd
          if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in pacific_cells and canFlowToFrom(r,c,nr,nc):
            pacific_cells.add((nr,nc))
            pacific_flows.append((nr,nc))

      while atlantic_flows:
        (r,c) = atlantic_flows.popleft()
        for (rd,cd) in directions:
          nr,nc = r+rd, c+cd
          if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in atlantic_cells and canFlowToFrom(r,c,nr,nc):
            atlantic_cells.add((nr,nc))
            atlantic_flows.append((nr,nc))

      return [list(coords) for coords in pacific_cells if coords in atlantic_cells]
