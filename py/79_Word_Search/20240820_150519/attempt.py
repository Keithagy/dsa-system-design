from typing import List, Set, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        directions = {
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        }
        if len(word) > len(board) * len(board[0]):
            return False

        def explore(row: int, col: int, word_idx: int) -> bool:
            if word_idx == len(word) - 1:
                return board[row][col] == word[word_idx]
            if board[row][col] != word[word_idx]:
                return False
            for row_diff, col_diff in directions:
                nr = row + row_diff
                nc = col + col_diff
                if (
                    0 <= nr < len(board)
                    and 0 <= nc < len(board[0])
                    and (nr, nc) not in path
                ):
                    path.add((nr, nc))
                    has_word = explore(nr, nc, word_idx + 1)
                    path.remove((nr, nc))
                    if has_word:
                        return True
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                path.add((row, col))
                has_word = explore(row, col, 0)
                path.remove((row, col))
                if has_word:
                    return True
        return False

