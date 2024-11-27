from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 建立課程圖，key 為課程，value 為其先修課程列表
        graph = defaultdict(list)
        # 記錄當前路徑中已訪問的課程，用於檢測循環
        visited = set()

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # 定義 DFS 函數，用於檢測是否存在循環
        def dfs(course):
            # 如果當前課程已在訪問路徑中，則存在循環
            if course in visited:
                return False

            # 如果課程沒有先修課程，則可以直接完成
            if not graph[course]:
                return True

            # 將當前課程標記為已訪問
            visited.add(course)

            # 遍歷所有先修課程
            for prereq in graph[course]:
                # 如果先修課程無法完成，則當前課程也無法完成
                if not dfs(prereq):
                    return False

            # 移除當前課程的訪問標記，回溯
            visited.remove(course)
            # 優化：將當前課程的先修課程清空，避免重複計算
            graph[course] = []
            return True

        # 遍歷所有課程，檢查是否可以完成
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


# 顏色標記法
# 白色（0）：未訪問
# 灰色（1）：正在訪問
# 黑色（2）：已訪問且處理完成
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 建立課程圖，key 為課程，value 為其先修課程列表
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # 使用列表來標記每門課程的狀態
        # 0 = 未訪問, 1 = 正在訪問, 2 = 已訪問
        state = [0] * numCourses

        # 定義 DFS 函數
        def dfs(course):
            if state[course] == 1:
                # 當前課程正在訪問中，存在循環
                return False
            if state[course] == 2:
                # 當前課程已經訪問過，無需重複
                return True

            # 標記為正在訪問
            state[course] = 1
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            # 標記為已訪問
            state[course] = 2
            return True

        # 遍歷所有課程
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


Solution().canFinish(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]])
Solution().canFinish(prerequisites=[[0, 1], [1, 0]], numCourses=2)
