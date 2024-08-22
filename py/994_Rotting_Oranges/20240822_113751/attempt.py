from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh_oranges = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c, 0))
        max_mins = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while rotten:
            (r, c, time) = rotten.popleft()
            max_mins = max(max_mins, time)
            for rd, cd in directions:
                nr, nc = r + rd, c + cd
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    rotten.append((nr, nc, time + 1))
        return max_mins if fresh_oranges == 0 else -1

