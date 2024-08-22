from collections import deque
from typing import List


class Solution:
    # best modelled as BFS with queue
    # track edge cases:
    # isolated oranges >> if queue is empty but fresh count is non-zero >> return -1
    # no rotten oranges >> initial queue population finds nothing >> return -1
    #   (this is just mins; in while loop, you should only increment mins if there is a next round to simulate, i.e if after processing a round, len(queue)!=0)
    # no fresh oranges >> return 0
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        rot_q = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                match grid[r][c]:
                    case 1:
                        fresh_count += 1
                    case 2:
                        for rd, cd in directions:
                            nr, nc = r + rd, c + cd
                            if (
                                0 <= nr < len(grid)
                                and 0 <= nc < len(grid[0])
                                and grid[nr][nc] == 1
                            ):
                                rot_q.append((nr, nc))
        mins = 0
        while rot_q:
            # mins value marks the endpoint. so, if min == 0 then rotting_this_min denotes count rotting over the FIRST, not ZEROTH, minute, since 0th has already passed (which is why we have the initial rotten)
            rotting_this_min = len(rot_q)
            for _ in range(rotting_this_min):
                (r, c) = rot_q.popleft()
                if (
                    grid[r][c] == 2
                ):  # because queue might contain double entry >> accessing a square from mult diff sides
                    continue
                grid[r][c] = 2
                fresh_count -= 1
                for rd, cd in directions:
                    nr, nc = r + rd, c + cd
                    if (
                        0 <= nr < len(grid)
                        and 0 <= nc < len(grid[0])
                        and grid[nr][nc] == 1
                    ):
                        rot_q.append((nr, nc))
            mins += 1
        return mins if fresh_count == 0 else -1

