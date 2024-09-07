from collections import deque
from typing import Counter, List, Optional
import heapq


class Solution:
    # the key idea is that you always need to prioritize doing the highest-count task, and then slot lesser-count tasks around their cooldowns.
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        heap = [-count for count in (Counter(tasks).values())]
        heapq.heapify(heap)
        cooldown_tasks = deque()

        def getNextCooledDownTaskIfAny() -> Optional[int]:
            if not cooldown_tasks or cooldown_tasks[0][1] != time:
                return None
            return cooldown_tasks.popleft()[0]

        while heap or cooldown_tasks:
            if cooldown_tasks:
                cooled_down_task = getNextCooledDownTaskIfAny()
                if cooled_down_task is not None:
                    heapq.heappush(heap, cooled_down_task)
            if heap:
                next_task_done = heapq.heappop(heap)
                if next_task_done + 1 != 0:
                    cooldown_tasks.append(
                        (next_task_done + 1, time + n + 1)
                    )  # if done in time 2 and n is 3, take 3 timeframes of break, so next you can do is 6 (3+1==4)
            time += 1
        return time

