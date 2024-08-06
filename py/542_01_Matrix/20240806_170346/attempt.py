class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        result = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
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
                        and new_col >= 0
                        and new_row < rows
                        and new_col < cols
                    ):
                        result[row][col] = min(
                            result[row][col], result[new_row][new_col] + 1
                        )

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
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
                        and new_col >= 0
                        and new_row < rows
                        and new_col < cols
                    ):
                        result[row][col] = min(
                            result[row][col], result[new_row][new_col] + 1
                        )
        return result

