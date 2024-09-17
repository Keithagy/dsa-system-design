from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        side = len(matrix)
        left, right = 0, side - 1
        top, bottom = 0, side - 1
        while left < right and top < bottom:
            for i in range((right - left)):
                topLeftTemp = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = topLeftTemp
            left += 1
            right -= 1
            top += 1
            bottom -= 1

