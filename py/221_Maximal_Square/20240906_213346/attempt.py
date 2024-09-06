from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        max_size = 0

        memo = {}

        def dp(r: int, c: int) -> int:
            nonlocal max_size
            if r > rows - 1 or c > cols - 1:
                return 0
            if r == rows - 1 or c == cols - 1:
                memo[(r, c)] = int(matrix[r][c])
                dp(r, c + 1)
                dp(r + 1, c)
                dp(r + 1, c + 1)
                max_size = max(max_size, memo[(r, c)])
                return memo[(r, c)]
            if (r, c) in memo:
                return memo[(r, c)]
            max_square_here = int(matrix[r][c]) + min(
                dp(r, c + 1), dp(r + 1, c), dp(r + 1, c + 1)
            )
            if matrix[r][c] == "0":
                max_square_here = 0

            memo[(r, c)] = max_square_here
            max_size = max(max_size, memo[(r, c)])
            return memo[(r, c)]

        dp(0, 0)
        return max_size * max_size

