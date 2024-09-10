from typing import List, Optional


class Solution:
    def setZeroes(self, matrix: List[List[Optional[int]]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[r][c] = None  # sentinel value

        def modify(r: int, c: int) -> None:
            for col in range(cols):
                if matrix[r][col] is not None:
                    matrix[r][col] = 0
            for row in range(rows):
                if matrix[row][c] is not None:
                    matrix[row][c] = 0
            matrix[r][c] = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] is None:
                    modify(r, c)

