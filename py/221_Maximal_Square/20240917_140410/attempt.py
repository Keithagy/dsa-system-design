from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        def valid(idx: int, max_val: int) -> bool:
            return 0 <= idx < max_val

        memo = {}
        longest_side = 0

        def largest_square_at(r: int, c: int) -> int:
            nonlocal longest_side
            if not (valid(r, rows) and valid(c, cols)):
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            me = int(matrix[r][c])
            largest_my_right = largest_square_at(r, c + 1)
            largest_my_down = largest_square_at(r + 1, c)
            largest_my_diag = largest_square_at(r + 1, c + 1)
            if (
                me != 0
                and largest_my_right != 0
                and largest_my_down != 0
                and largest_my_diag != 0
            ):
                memo[(r, c)] = 1 + min(
                    largest_my_right, largest_my_down, largest_my_diag
                )
            else:
                memo[(r, c)] = me
            longest_side = max(longest_side, memo[(r, c)])
            return memo[(r, c)]

        largest_square_at(0, 0)
        return longest_side**2

