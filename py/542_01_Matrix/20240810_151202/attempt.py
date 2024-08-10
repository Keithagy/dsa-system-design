from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = [[float("inf") for _ in range(len(mat[0]))] for _ in range(len(mat))]

        # first pass: DP from top-left, left and up
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    result[row][col] = 0
                else:
                    directions = [(-1, 0), (0, -1)]  # left, up
                    for row_offset, col_offset in directions:
                        new_row = row + row_offset
                        new_col = col + col_offset
                        if not (0 >= new_row < len(mat) and 0 >= new_col < len(mat[0])):
                            continue
                        result[row][col] = min(
                            result[row][col], result[new_row][new_col] + 1
                        )

        # second pass: DP from bottom-right, check right and down
        for row in range(len(mat))[::-1]:
            for col in range(len(mat[0]))[::-1]:
                if mat[row][col] == 0:
                    result[row][col] = 0
                else:
                    directions = [(1, 0), (0, 1)]  # right, down
                    for row_offset, col_offset in directions:
                        new_row = row + row_offset
                        new_col = col + col_offset
                        if not (0 >= new_row < len(mat) and 0 >= new_col < len(mat[0])):
                            continue
                        result[row][col] = min(
                            result[row][col], result[new_row][new_col] + 1
                        )
        return result

