from typing import List


class Solution:
    # You could probably do some math to figure out how many squares to traverse in each turn for constant memory...
    # But I will use the (m*n) memory approach to track visited squares first.
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        cur_row = cur_col = 0
        result = [matrix[cur_row][cur_col]]
        visited = set([(cur_row, cur_col)])

        def canGoRight():
            return (
                0 <= cur_row < len(matrix)
                and 0 <= cur_col < len(matrix[0]) - 1
                and (cur_row, cur_col + 1) not in visited
            )

        def canGoLeft():
            return (
                0 <= cur_row < len(matrix)
                and 1 <= cur_col < len(matrix[0])
                and (cur_row, cur_col - 1) not in visited
            )

        def canGoUp():
            return (
                1 <= cur_row < len(matrix)
                and 0 <= cur_col < len(matrix[0])
                and (cur_row - 1, cur_col) not in visited
            )

        def canGoDown():
            return (
                0 <= cur_row < len(matrix) - 1
                and 0 <= cur_col < len(matrix[0])
                and (cur_row + 1, cur_col) not in visited
            )

        def canGoAny() -> bool:
            return canGoRight() or canGoLeft() or canGoDown() or canGoUp()

        def go(direction: str):
            nonlocal cur_row, cur_col
            directions = {
                "left": (0, -1),
                "right": (0, 1),
                "up": (-1, 0),
                "down": (1, 0),
            }
            (row_diff, col_diff) = directions[direction]
            cur_row += row_diff
            cur_col += col_diff
            result.append(matrix[cur_row][cur_col])
            visited.add((cur_row, cur_col))

        while canGoAny():
            while canGoRight():
                go("right")
            while canGoDown():
                go("down")
            while canGoLeft():
                go("left")
            while canGoUp():
                go("up")
        return result

