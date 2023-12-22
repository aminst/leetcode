from collections import defaultdict
from enum import Enum

class VisitStatus(Enum):
    NOT_VISITED = 1
    VISITED = 2
    VISITING = 3

class Solution:
    def create_graph(self, prereqs):
        graph = defaultdict(set)
        for prereq in prereqs:
            x = prereq[0]
            y = prereq[1]
            graph[y].add(x)
        return graph

    def has_cycle(self, course, graph, visit_status):
        if visit_status[course] == VisitStatus.VISITING: return True
        if visit_status[course] == VisitStatus.VISITED: return 
        visit_status[course] = VisitStatus.VISITING
        for connected_course in graph[course]:
            if self.has_cycle(connected_course, graph, visit_status) == True: return True
        visit_status[course] = VisitStatus.VISITED
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.create_graph(prerequisites)
        visit_status = [VisitStatus.NOT_VISITED] * numCourses
        for course in range(numCourses):
            if self.has_cycle(course, graph, visit_status):
                return False
        return True

"""
[ai, bi]: should take bi -> ai
1 <= numCourses <= 2000
0 <= prereq <= 5000
prereq can be empty

Examples:
Example 1:
0 -> 1, courses: 0, 1 true

0 -> 1, 1 -> 0, courses: 0, 1 false

0 -> 1, 1 -> 2, 2 -> 0, courses: 0, 1, 2

Solution:
    * make the graph of prereqs
    * find if a cycle exists
    * if cycle exists: false, else true

finding a cycle:
    * dfs
"""


