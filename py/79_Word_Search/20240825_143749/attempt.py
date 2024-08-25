from typing import List, Set, Tuple


class Solution:
    # DFS backtracking
    # accumulate used letters in a set
    # in the worst case, dfs starting from every string, for l recursions
    # so O(mnl)
    # space would similarly be O(mnl)
    #
    # # board = [
    # ["X", "C","A"],
    # ["Z","X","A"]
    # ]
    # word = "ZXC"
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r: int, c: int, path: Set[Tuple[int, int]]) -> bool:
            if len(path) == len(word):
                return True
            if (r, c) in path:
                return False
            if board[r][c] != word[len(path)]:
                return False
            path.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for rd, cd in directions:
                nr, nc = r + rd, c + cd
                if 0 <= nr < rows and 0 <= nc < cols:
                    if dfs(nr, nc, path):
                        return True
            if len(path) == len(word):
                return True
            path.discard((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, set()):
                    return True
        return False

