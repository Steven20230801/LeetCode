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

# 顏色標記法
# 白色（0）：未訪問
# 灰色（1）：正在訪問
# 黑色（2）：已訪問且處理完成
