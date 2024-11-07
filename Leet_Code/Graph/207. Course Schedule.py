from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
        # numCourses = 5
        premap = defaultdict(list)
        visited = set()
        for c, p in prerequisites:
            premap[c].append(p)

        print(premap)

        def dfs(course):
            if course in visited:
                return False

            pres = premap[course]
            if pres == []:
                return True

            visited.add(course)
            for c in pres:
                if not dfs(c):
                    return False
            visited.remove(course)
            premap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
