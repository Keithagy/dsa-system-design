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
        rotten = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                match grid[r][c]:
                    case 1:
                        fresh_count += 1
                    case 2:
                        rotten.add((r, c))
        mins = 0
        while rotten:
            # mins value marks the endpoint. so, if min == 0 then rotting_this_min denotes count rotting over the FIRST, not ZEROTH, minute, since 0th has already passed (which is why we have the initial rotten)
            new_rot = set()
            for r, c in rotten:
                for rd, cd in directions:
                    nr, nc = r + rd, c + cd
                    if (
                        0 <= nr < len(grid)
                        and 0 <= nc < len(grid[0])
                        and grid[nr][nc] == 1
                    ):
                        grid[r][c] = 2
                        fresh_count -= 1
                        new_rot.add((nr, nc))
            rotten = new_rot
            mins += 1 if rotten else 0
        return mins if fresh_count == 0 else -1

