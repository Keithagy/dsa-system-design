from collections import deque
from typing import List, Tuple


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = deque([(0, 0, 0)])  # row, col, time
        v = set()
        result = -1

        def nextMoves(r: int, c: int) -> List[Tuple[int, int]]:
            h = [(0, -1), (0, 1)]  # left, right
            v = [(-1, 0), (1, 0)]  # up,down
            result = []
            for rd, cd in h:
                for rrd, ccd in v:
                    next = (r + rrd, c + (2 * cd))
                    if next not in v:
                        result.append(next)

            for rd, cd in v:
                for rrd, ccd in h:
                    next = (r + (2 * rd), c + ccd)
                    if next not in v:
                        result.append(next)

            return result

        while q:
            r, c, t = q.popleft()
            if r == x and c == y:
                return result
            v.add((r, c))
            result = max(t, result)
            q.extend([(nr, nc, t + 1) for (nr, nc) in nextMoves(r, c)])
        raise ValueError("")
