from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # key is (row, col), val is distance to zero
        distances = {}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(row_no: int, col_no: int) -> None:
            queue = deque([(row_no, col_no, 0)])
            while queue:
                (row, col, distance_travelled) = queue.popleft()
                if mat[row][col] == 0:
                    distances[(row, col)] = distance_travelled
                    return
                for row_offset, col_offset in directions:
                    new_row = row_offset + row
                    new_col = col_offset + col
                    if not (
                        new_row >= 0
                        and new_row < len(mat)
                        and new_col >= col
                        and new_col < len(mat[0])
                    ):
                        continue
                    if (new_row, new_col) in distances:
                        distances[(row, col)] = distances[(new_row, new_col)] + 1
                        return
                    queue.append((new_row, new_col, distance_travelled + 1))

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    distances[(row, col)] = 0
                    continue
                bfs(row, col)
        result = []
        for row in range(len(mat)):
            row_zero = []
            for col in range(len(mat[0])):
                row_zero.append(0)
            result.append(row_zero)

        print(distances)
        for row_result in range(len(result)):
            for col_result in range(len(result[0])):
                print(row_result, col_result)
                print(distances[(row_result, col_result)])
                result[row_result][col_result] = distances[(row_result, col_result)]
                print(result)
        return result

