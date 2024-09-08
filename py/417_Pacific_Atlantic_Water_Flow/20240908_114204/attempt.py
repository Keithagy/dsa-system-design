from typing import List, Deque, Set, Tuple
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited_p, visited_a = set(), set()
        pacific = deque()
        atlantic = deque()
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or c == 0:
                    pacific.append((r, c))
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    atlantic.append((r, c))

        def bfs(q: Deque[Tuple[int, int]], v: Set[Tuple[int, int]]) -> None:
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            while q:
                (r, c) = q.popleft()
                v.add((r, c))
                for rd, rc in directions:
                    nr, nc = r + rd, c + rc
                    if (
                        0 <= nr < len(heights)
                        and 0 <= nc < len(heights[0])
                        and (nr, nc) not in v
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))

        bfs(pacific, visited_p)
        bfs(atlantic, visited_a)

        return [list(coords) for coords in visited_p & visited_a]

