from collections import deque
from typing import List

class Solution:
    # BFS >> m*n time, m*n space
    # input
    # [
    #   [],
    #   [],
    # ]
    def getFood(self, grid: List[List[str]]) -> int:
      queue = deque()
      rows = len(grid)
      cols = len(grid[0])
      for r in range(rows):
        for c in range(cols):
          if grid[r][c]=="*":
            queue.append((r,c, 0))

      directions = [
        (0,1), # down
        (0,-1), # up
        (1,0), # right
        (-1,0), # left
      ]
      invalid = set(["X", "*", "-"])
      while queue:
        (r,c,time) = queue.popleft()
        if grid[r][c] == "#":
          return time
        for (rd,cd) in directions:
          nr,nc = r+rd, c+cd
          if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] not in invalid:
            grid[nr][nc] = "-"
            queue.append((nr,nc,time+1))
      return -1
