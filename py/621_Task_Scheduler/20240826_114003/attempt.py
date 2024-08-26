from collections import defaultdict
from typing import List, Optional


class Solution:
    # scheduler does not care about order of task received, only about counts of tasks left
    # use a hashmap to track remaining counts of each task
    # need to track cooldowns on a task-by-task basis
    # a hashmap with one entry per task
    # maintain a loop that decrements all counts by 1 each round, pick something that has a remaining count and is off cooldown. else you need to idle
    # return number of cycles at the end
    # space: O(len(tasks)), for both the counter and the cooldown tracker
    # time: O(len(tasks) + len(tasks)*( m % n )), where n in the cooldown and m is the number of unique values
    #
    # tasks: ["A","B","B","C", "A","C"], n = 3
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldowns = defaultdict(int)
        # {
        # "A" : 3
        # "B" : 1
        # "C" : 2
        # }
        task_count = defaultdict(int)
        # {
        # "B" : 1
        # "C" : 1
        # }

        for task in tasks:
            task_count[task] += 1

        def decrement_all_cooldowns() -> None:
            for task in cooldowns:
                cooldowns[task] -= 1

        def pick_task_off_cooldown() -> Optional[str]:
            for task in task_count:
                if cooldowns[task] == 0 and task_count[task] != 0:
                    return task
            return None

        def execute(task: Optional[str]) -> None:
            if task is None:
                return  # idle this cycle
            task_count[task] -= 1
            if task_count[task] == 0:
                del task_count[task]
            cooldowns[task] = n + 1

        cycles = 0  # 3
        while task_count:
            decrement_all_cooldowns()
            execute(pick_task_off_cooldown())
            cycles += 1
        return cycles
