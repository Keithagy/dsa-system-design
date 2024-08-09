from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def checkIsland(row: int, col: int) -> bool:
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            is_land = grid[row][col] == "1"
            grid[row][col] = "0"
            if not is_land:
                return False
            for row_offset, col_offset in directions:
                new_row = row + row_offset
                new_col = col + col_offset
                if not (
                    new_row >= 0
                    and new_row < len(grid)
                    and new_col >= 0
                    and new_col < len(grid[0])
                ):
                    continue
                checkIsland(new_row, new_col)
            return True

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "0":
                    continue
                islands += 1 if checkIsland(row, col) else 0
        return islands

