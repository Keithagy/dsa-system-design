from collections import deque
from typing import List


class Solution:
    # DFS with backtracking >> O(n+e) to build graph, O(n^2) to backtrack in the worst case
    # You also use topological sort via kahn's algo... but then you will need to track multiple possible paths
    # failure cases:
    # cycle
    # note: can have disconnected graph, you just need to take that course without it unlocking anything
    # input: numCourses = 5, [[1,0],[2,0],[3,0],[4,1],[4,2]]
    #   -> 1 ->
    # 0 -> 2 <=> 4
    #   -> 3*
    #
    # O(n+e) time and space
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # {
        #   0: {1,2,3},
        #   1: {4},
        #   2: {4},
        #   3: {},
        #   4: {},
        # }
        unlock_graph = {course: set() for course in range(numCourses)}
        # [0,0,1,0,0]
        prereq_count = [0 for _ in range(numCourses)]
        for [course, prereq] in prerequisites:  # course = 4; prereq = 2
            unlock_graph[prereq].add(course)
            prereq_count[course] += 1

        queue = deque(
            [course for course in unlock_graph if prereq_count[course] == 0]
        )  # []
        visited = set()  # {0,1,2,3,4}
        result = []  # [0,1,2,3,4]
        while queue:
            course = queue.popleft()  # 4
            if course in visited:
                return []
            visited.add(course)
            result.append(course)
            for next_course in unlock_graph[course]:  # 0<<[0]
                prereq_count[next_course] -= 1
                if prereq_count[next_course] == 0:
                    queue.append(next_course)
        return result if len(result) == numCourses else []  # [0,1,2,3,4]

