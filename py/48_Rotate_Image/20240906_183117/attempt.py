from typing import List


class Solution:
    # you can think of the rotations in a ring, that you walk and then do
    # how many rotations in a ring? always 4, because a square has 4 sides
    # how many walks? (side - 1), because that's how many squares you have before you hit the next corner
    # after that, you move into the next bottom right corner, until the side length is <= 1. (because then there's nothing else to rotate.)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        cur = ((n - 1), (n - 1))  # bottom-left start

        while n > 1:
            for _ in range(n - 1):
                tmp = matrix[cur[0]][cur[1]]
                for _ in range(4):
                    (rr, rc) = rotatedCoords(cur)
                    tmp, matrix[rr][rc] = matrix[rr][rc], tmp
                    cur = (rr, rc)
                cur = nextStartPoint(cur)
            n -= 1

