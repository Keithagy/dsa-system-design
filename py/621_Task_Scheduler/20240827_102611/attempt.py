from collections import deque
from typing import Counter, List
import heapq


class Solution:
    # input: ["A","A","A","B","B","B","C","C"], n = 3
    # output: ABC_ABC_AB >> 10
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        # {
        #   "A" : 3,
        #   "B" : 3,
        #   "C" : 2,
        # }
        task_counts = Counter(tasks)

        # []
        maxHeap = [-task_counts[task] for task in task_counts]
        heapq.heapify(maxHeap)

        # [(-1, 8), (-1,9)]
        cooldowns = deque()
        while maxHeap or cooldowns:
            if cooldowns and cooldowns[0][1] == time:
                heapq.heappush(maxHeap, cooldowns.popleft()[0])
            if maxHeap:
                next_task = heapq.heappop(maxHeap)  # -1
                if next_task < -1:
                    cooldowns.append((next_task + 1, time + n + 1))
            time += 1
        return time  # 8

