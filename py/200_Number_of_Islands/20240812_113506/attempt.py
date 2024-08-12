from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0

        def sink_island(row: int, col: int) -> None:
            grid[row][col] = "0"

            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for row_offset, col_offset in directions:
                new_row, new_col = row + row_offset, col + col_offset
                if not (
                    0 <= new_row < len(grid)
                    and 0 <= new_col < len(grid[0])
                    and grid[new_row][new_col] != "1"
                ):
                    continue
                sink_island(new_row, new_col)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    sink_island(row, col)
                    island_count += 1
        return island_count

