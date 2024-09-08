from collections import defaultdict, deque
from typing import List


class Solution:
    # You are looking to traverse the graph of unlocks in topological order, returning early with an empty array if you find a cycle else returning with a valid topological traversal.
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        unlocks = defaultdict(set)
        prereq_count = [0 for _ in range(numCourses)]
        for [course, prereq] in prerequisites:
            unlocks[prereq].add(course)
            prereq_count[course] += 1
        q = deque(
            [course for course in range(len(prereq_count)) if prereq_count[course] == 0]
        )
        seq = []
        while q:
            take_this_next = q.popleft()
            seq.append(take_this_next)
            for subsequent in unlocks[take_this_next]:
                prereq_count[subsequent] -= 1
                if prereq_count[subsequent] == 0:
                    q.append(subsequent)
        return seq if len(seq) == numCourses else []

