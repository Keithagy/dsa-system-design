from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs_of = {course: [] for course in range(numCourses)}
        for [course, prereq] in prerequisites:
            prereqs_of[course].append(prereq)
        path = set()
        seen = set()

        def dfs(course: int) -> bool:
            if course in path:
                return False
            if course in seen:
                return True
            path.add(course)
            next = prereqs_of[course]
            for now_unlocked in next:
                if not dfs(now_unlocked):
                    return False
            path.remove(course)
            seen.add(course)
            return True

        for course in [
            course for course in prereqs_of.keys() if len(prereqs_of[course]) != 0
        ]:
            if not dfs(course):
                return False
        return True

