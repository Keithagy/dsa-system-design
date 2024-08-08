from typing import Dict, List, Set


class Course:
    def __init__(self, name: int) -> None:
        self.name: int = name
        self.prereqs: List[Course] = []


class Solution:
    # You can visualize the courses as a set of nodes in a graph, each with their own unlocks (other nodes).
    # `prerequisites` essentially traces through a number of paths on the dependency graph.
    # `numCourses` indicates the maximum number a nodes a path can traverse.
    # use prereqs to build the links, then iterate through node as an entry point to check for cycles
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.courses: Dict[int, Course] = {}
        for [course, prereq] in prerequisites:
            print(course, prereq)
            course_node = self.courses.setdefault(course, Course(name=course))
            course_node.prereqs.append(
                self.courses.setdefault(prereq, Course(name=prereq))
            )

        print(
            [
                (course.name, [prereq.name for prereq in course.prereqs])
                for course in self.courses.values()
            ]
        )
        self.ok_courses: Set[int] = (
            set()
        )  # contains courses confirmed not to have a cycle starting at them
        for i in range(numCourses):
            if self.hasCycle(i, set()):
                return False
        return True

    def hasCycle(self, course_name: int, traversed: Set[int]) -> bool:
        if course_name not in self.courses or course_name in self.ok_courses:
            return False  # course not mentioned at all in prereqs list
        if course_name in traversed:
            return True
        traversed.add(course_name)
        course = self.courses[course_name]
        for prereq in course.prereqs:
            if self.hasCycle(prereq.name, traversed):
                return True
        traversed.remove(course_name)
        self.ok_courses.add(course_name)
        return False

