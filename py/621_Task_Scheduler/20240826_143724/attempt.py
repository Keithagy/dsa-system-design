from collections import Counter, deque
from typing import List
import heapq


class Solution:
    # input: "AAABBCC" n = 3
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # {
        #   "A":3
        #   "B":2
        #   "C":2
        # }
        counts = Counter(tasks)
        # [
        # ]
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        # [
        # (-2,4)
        # (-1,5)
        # (-1,6)
        # ]
        cooldown_tracker = deque()
        time = 0  # 3
        while max_heap or cooldown_tracker:
            if cooldown_tracker and cooldown_tracker[0][1] == time:
                heapq.heappush(max_heap, cooldown_tracker.popleft()[0])
            most_freq = heapq.heappop(max_heap) if max_heap else None  # -2
            if most_freq is not None:
                most_freq += 1  # -1
                do_again = time + n + 1  # 5
                if most_freq != 0:
                    cooldown_tracker.append((most_freq, do_again))
            time += 1
        return time

