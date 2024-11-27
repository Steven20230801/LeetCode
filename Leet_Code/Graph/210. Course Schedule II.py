from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 构建前置课程映射表
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # 用于记录访问状态：0=未访问, 1=访问中, 2=已访问
        visit_status = [0] * numCourses
        order = []
        possible = True  # 标记是否存在环

        def dfs(course):
            nonlocal possible
            if not possible:
                return
            if visit_status[course] == 1:
                # 检测到环
                possible = False
                return
            if visit_status[course] == 2:
                # 已经处理过，无需重复
                return

            # 标记为访问中
            visit_status[course] = 1
            for prereq in graph[course]:
                dfs(prereq)
            # 标记为已访问
            visit_status[course] = 2
            order.append(course)  # 添加到课程顺序中

        # 对每个课程进行 DFS
        for course in range(numCourses):
            if visit_status[course] == 0:
                dfs(course)
            if not possible:
                return []  # 如果检测到环，返回空列表

        # 由于是后序遍历，需要反转得到正确的课程顺序
        return order


Solution().findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]])
