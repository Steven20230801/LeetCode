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


prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
numCourses = 5

prerequisites = [[0, 1], [1, 0]]
numCourses = 2

premap = defaultdict(list)
visited = set()
for c, p in prerequisites:
    premap[c].append(p)

print(premap)


def dfs(course):
    # base case 1: 當前課程已在 visited 集合中，表示遇到了循環，返回 False。
    if course in visited:
        return False
    # base case 2:
    prerequisites = premap[course]
    if prerequisites == []:
        return True
    # 將當前課程添加到 visited 集合中。
    visited.add(course)

    for p in prerequisites:
        if not dfs(p):  # 如果任何一個先修課程的 DFS 返回 False，則表示存在循環，返回 False。
            return False

    # 移除當前課程從 visited 集合，表示該課程已完成檢查。
    visited.remove(course)
    # 將 premap[course] 設為空列表，表示該課程已被處理過且無循環，可以加速後續的檢查。
    premap[course] = []
    return True


for course in range(numCourses):
    if not dfs(course):
        print(False)
        break
print(True)


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
from collections import defaultdict
from typing import List

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
