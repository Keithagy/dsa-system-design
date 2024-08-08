from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.unlock_graph = defaultdict(list)
        self.in_degrees = {course: 0 for course in range(numCourses)}

        for [course, prereq] in prerequisites:
            self.unlock_graph[prereq].append(course)
            self.in_degrees[course] += 1

        # start_processesing from most basic courses (no prereqs)
        result = []
        queue = deque(
            [course for course in self.in_degrees if self.in_degrees[course] == 0]
        )

        while queue:
            course = queue.popleft()
            result.append(course)
            unlocks = self.unlock_graph[course]
            for unlock in unlocks:
                self.in_degrees[unlock] -= 1
                if self.in_degrees[unlock] == 0:
                    queue.append(unlock)
        return len(result) == len(self.in_degrees)

