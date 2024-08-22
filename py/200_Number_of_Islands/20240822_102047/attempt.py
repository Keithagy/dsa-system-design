from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def sinkLandAndSearch(row: int, col: int) -> None:
            if grid[row][col] != "1":
                return  # incorporates backtracking
            grid[row][col] = "0"
            for rd, cd in directions:
                nr, nc = row + rd, col + cd
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    sinkLandAndSearch(nr, nc)

        def sinkIsland(row: int, col: int) -> int:
            sinkLandAndSearch(row, col)
            return 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += sinkIsland(r, c)
        return count

