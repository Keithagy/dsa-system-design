from typing import List


class Solution:
    # apply DP; two-pass, fill from top left, then fill from bottom right
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = [[float("inf") for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    result[r][c] = 0
                else:
                    directions = {
                        "left": (-1, 0),
                        "up": (0, -1),
                    }
                    for r_diff, c_diff in directions.values():
                        nr = r + r_diff
                        nc = c + c_diff
                        if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]):
                            result[r][c] = min(result[nr][nc] + 1, result[r][c])

        for r in range(len(mat))[::-1]:
            for c in range(len(mat[0]))[::-1]:
                if mat[r][c] == 0:
                    result[r][c] = 0
                else:
                    directions = {
                        "right": (1, 0),
                        "down": (0, 1),
                    }
                    for r_diff, c_diff in directions.values():
                        nr = r + r_diff
                        nc = c + c_diff
                        if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]):
                            result[r][c] = min(result[nr][nc] + 1, result[r][c])
        return result

