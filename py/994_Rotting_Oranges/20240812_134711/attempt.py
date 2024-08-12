from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh_count = 0
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh_count += 1

        max_mins = 0
        while queue:
            next_rotten = deque()
            for _ in range(len(queue)):
                (row, col, time) = queue.popleft()
                max_mins = max(time, max_mins)

                for rd, cd in directions:
                    nr, nc = row + rd, col + cd
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh_count -= 1
                            next_rotten.append((nr, nc, time + 1))
            queue = next_rotten
        return max_mins if fresh_count == 0 else -1

