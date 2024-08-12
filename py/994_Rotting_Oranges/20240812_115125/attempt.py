from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # radiate out from rotten oranges until no fresh oranges left
        # "radiating out" lends well to breadth first traversal of a grid >> queue
        # with each passing minute, fresh orange count should decrease; if no decrease from one round to the next, return -1
        # edge cases:
        #   no rotten oranges to begin with, in which case it's zero minutes
        #   no fresh oranges to begin with, in which case it's zero minutes
        # early return opps:
        #   while indexing fresh oranges, any orange surrounded by empty space will never be reachable, so return early there

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        minutes_passed = 0
        fresh_orange_count = 0
        oranges_rotting_this_min = deque()
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh_orange_count += 1
                elif grid[row][col] == 2:
                    for row_offset, col_offset in directions:
                        new_row, new_col = row + row_offset, col + col_offset
                        if not (
                            0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])
                        ):
                            continue
                        if (
                            grid[new_row][new_col] != 1
                            and (new_row, new_col) in visited
                        ):
                            continue
                        visited.add((new_row, new_col))
                        oranges_rotting_this_min.append((new_row, new_col))

        # no fresh oranges to rot, or no rotten oranges to start
        if fresh_orange_count == 0:
            return 0
        if len(oranges_rotting_this_min) == 0:
            return -1
        while oranges_rotting_this_min:
            count = len(oranges_rotting_this_min)
            for _ in range(count):
                (row, col) = oranges_rotting_this_min.popleft()
                grid[row][col] = 2
                fresh_orange_count -= 1
                for row_offset, col_offset in directions:
                    new_row, new_col = row + row_offset, col + col_offset
                    if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
                        continue
                    if grid[new_row][new_col] != 1 or (new_row, new_col) in visited:
                        continue
                    visited.add((new_row, new_col))
                    oranges_rotting_this_min.append((new_row, new_col))
            minutes_passed += 1
        return minutes_passed if fresh_orange_count == 0 else -1

