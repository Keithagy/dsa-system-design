from typing import List


class Solution:
    # O(mnk) solution, for board of m rows, n cols, k filled
    # if filled, check rows, cols and board
    # need to figure out how to resolve a cell to a subgrid
    # helper functions:
    # checkseq(seq, target) -> bool
    # checksubgrid(grid, target) -> bool
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        def ensureUnique(seq: List[str], val: str) -> bool:
            count = 0
            for c in seq:
                if c == val:
                    count += 1
                if count > 1:
                    return False
            return True

        def validRow(r: int, c: int) -> bool:
            val = board[r][c]
            seq = board[r]
            return ensureUnique(seq, val)

        def validCol(r: int, c: int) -> bool:
            val = board[r][c]
            seq = []
            for row in range(len(board)):
                seq.append(board[row][c])
            return ensureUnique(seq, val)

        def validGrid(r: int, c: int) -> bool:
            val = board[r][c]
            subGrid_row, subGrid_col = r // 3, c // 3
            seq = []
            rows, cols = range(subGrid_row * 3, ((subGrid_row + 1) * 3), 1), range(
                subGrid_col * 3, ((subGrid_col + 1) * 3), 1
            )
            for row in rows:
                for col in cols:
                    seq.append(board[row][col])
            return ensureUnique(seq, val)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] != ".":
                    if not validRow(r, c) or not validCol(r, c) or not validGrid(r, c):
                        return False
        return True

