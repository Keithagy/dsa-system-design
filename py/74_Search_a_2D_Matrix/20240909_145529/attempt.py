from typing import List, Tuple


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols) - 1

        def coords(idx: int) -> Tuple[int, int]:
            rowNo = idx // cols
            colNo = idx - (rowNo * cols)
            return (rowNo, colNo)

        def predicate(idx: int) -> bool:
            (r, c) = coords(idx)
            return matrix[r][c] >= target

        while left < right:
            mid = left + ((right - left) // 2)
            if predicate(mid):
                right = mid
            else:
                left = mid + 1
        (r, c) = coords(left)
        return matrix[r][c] == target

