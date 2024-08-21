from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = {course: 0 for course in range(numCourses)}
        unlocked_by = defaultdict(list)
        for [course, prereq] in prerequisites:
            unlocked_by[prereq].append(course)
            in_degrees[course] += 1

        queue = deque([course for course in in_degrees if in_degrees[course] == 0])
        taken = 0
        while queue:
            no_dept_course = queue.popleft()
            taken += 1
            next = unlocked_by[no_dept_course]
            for course in next:
                in_degrees[course] -= 1
                if in_degrees[course] == 0:
                    queue.append(course)
        return taken == numCourses

