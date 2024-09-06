from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_area = 0
        rows, cols = range(len(matrix)), range(len(matrix[0]))

        def dfs(r: int, c: int, side: int) -> None:
            nonlocal rows, cols, max_area
            if not (
                0 <= (r + side - 1) < len(rows) and 0 <= (c + side - 1) < len(cols)
            ):
                return
            sRows = [row for row in range(r, r + side, 1)]
            sCols = [col for col in range(c, c + side, 1)]

            for sr in sRows:
                for sc in sCols:
                    if matrix[sr][sc] == "0":
                        return
            max_area = max(max_area, side * side)
            dfs(r, c, side + 1)

        for r in rows:
            for c in cols:
                dfs(r, c, 1)
        return max_area

