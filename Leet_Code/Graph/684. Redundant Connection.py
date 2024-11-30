from collections import defaultdict
from typing import List

from sklearn import neighbors


# 並查集
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edges = [[1, 2], [1, 3], [2, 3]]
        pa = [i for i in range(len(edges) + 1)]  # 目前都屬於自己的集合

        # 查找操作的目的是確定某個元素屬於哪個集合。通常，每個集合會有一個代表元素（通常稱為“根”），查找操作會返回這個根元素。
        def find(x):
            if x != pa[x]:
                pa[x] = find(pa[x])
            return pa[x]

        # 合併（Union）
        # 不同的集合合併為一個集合。這需要找到兩個集合的根元素，然後將其中一個根指向另一個根，從而將兩個集合連接起來。
        def union(x, y):
            pa[find(x)] = find(y)

        for f, t in edges:
            if find(f) != find(t):
                union(f, t)
            else:
                return [f, t]


Solution().findRedundantConnection(edges=[[1, 2], [1, 3], [2, 3]])


# dfs

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 建立鄰接表
        graph = {}

        # DFS 函數，檢查是否存在從 current 到 target 的路徑
        def dfs(current, target, visited):
            if current == target:
                return True
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            return False

        for u, v in edges:
            # 檢查是否已經存在從 u 到 v 的路徑
            if u in graph and v in graph:
                if dfs(u, v, set()):
                    return [u, v]
            # 添加邊到圖中
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)

        return []


Solution().findRedundantConnection(edges=[[1, 2], [1, 3], [2, 3]])
