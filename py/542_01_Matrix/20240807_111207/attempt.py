from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = [[float("inf") for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    result[row][col] = 0
                    continue

                directions = {
                    "left": (-1, 0),
                    "up": (0, -1),
                }
                for row_offset, col_offset in directions.values():
                    new_row = row_offset + row
                    new_col = col_offset + col
                    if (
                        new_row >= 0
                        and new_row < len(mat)
                        and new_col >= 0
                        and new_col < len(mat[0])
                    ):
                        result[row][col] = min(
                            result[new_row][new_col] + 1, result[row][col]
                        )

        for row in range(len(mat))[::-1]:
            for col in range(len(mat[0]))[::-1]:
                if mat[row][col] == 0:
                    result[row][col] = 0
                    continue
                directions = {
                    "right": (1, 0),
                    "down": (0, 1),
                }
                for row_offset, col_offset in directions.values():
                    new_row = row_offset + row
                    new_col = col_offset + col
                    if (
                        new_row >= 0
                        and new_row < len(mat)
                        and new_col >= 0
                        and new_col < len(mat[0])
                    ):
                        result[row][col] = min(
                            result[new_row][new_col] + 1, result[row][col]
                        )
        return result

