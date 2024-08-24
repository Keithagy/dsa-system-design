from typing import List


class Solution:
    # use a visited set to track already visited
    # traverse in right-down-left-up order
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        def dfs(r: int, c: int, pos_idx: int) -> None:
            if (r, c) in visited:
                return
            original = pos_idx
            visited.add((r, c))
            result.append(matrix[r][c])
            rd, cd = directions[pos_idx]
            nr, nc = r + rd, c + cd
            while not (
                0 <= nr < len(matrix)
                and 0 <= nc < len(matrix[0])
                and (nr, nc) not in visited
            ):
                pos_idx = (pos_idx + 1) % 4
                rd, cd = directions[pos_idx]
                nr, nc = r + rd, c + cd
                if pos_idx == original:
                    return
            dfs(nr, nc, pos_idx)

        dfs(0, 0, 0)
        return result

