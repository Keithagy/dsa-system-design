from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_count_of = {}
        unlocks = {}

        for [course, prereq] in prerequisites:
            unlocks.setdefault(prereq, []).append(course)
            prereq_count_of[course] = prereq_count_of.setdefault(course, 0) + 1

        queue = deque(
            [
                course_name
                for course_name in range(numCourses)
                if course_name not in prereq_count_of
            ]
        )
        seen = set()
        while queue:
            no_prereqs = queue.popleft()
            seen.add(no_prereqs)
            if no_prereqs not in unlocks:
                continue
            for one_less_prereq in unlocks[no_prereqs]:
                if one_less_prereq in seen:
                    return False
                prereq_count_of[one_less_prereq] -= 1
                if prereq_count_of[one_less_prereq] == 0:
                    queue.append(one_less_prereq)

        return len(seen) == numCourses

