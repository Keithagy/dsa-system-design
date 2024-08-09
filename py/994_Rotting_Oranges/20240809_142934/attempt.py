from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        fresh_oranges = 0
        rotten_oranges_minute_end = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rotten_oranges_minute_end.append((row, col))
                    continue
                if grid[row][col] == 1:
                    fresh_oranges += 1
                    continue

        minutes = -1
        while rotten_oranges_minute_end:
            oranges_rotting_this_minute = len(rotten_oranges_minute_end)
            for _ in range(oranges_rotting_this_minute):
                (row, col) = rotten_oranges_minute_end.popleft()
                for row_offset, col_offset in directions:
                    new_row = row + row_offset
                    new_col = col + col_offset
                    if not (
                        new_row >= 0
                        and new_row < len(grid)
                        and new_col >= 0
                        and new_col < len(grid[0])
                        and grid[new_row][new_col] == 1
                    ):
                        continue
                    fresh_oranges -= 1
                    grid[new_row][new_col] = 2
                    rotten_oranges_minute_end.append((new_row, new_col))
            minutes += 1

        return max(0, minutes) if fresh_oranges == 0 else -1

