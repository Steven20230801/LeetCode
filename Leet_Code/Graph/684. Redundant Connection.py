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


from typing import List  # 從 typing 模塊導入 List 類型，用於類型提示


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 建立一個空的鄰接表，用於表示圖的結構
        graph = {}

        # 定義一個內部的 DFS 函數，用於檢查從 current 節點是否能到達 target 節點
        def dfs(current, target, visited):
            if current == target:
                # 如果當前節點就是目標節點，表示存在路徑，返回 True
                return True
            # 將當前節點標記為已訪問
            visited.add(current)
            # 遍歷當前節點的所有鄰居
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    # 如果鄰居節點未被訪問，遞迴調用 DFS 函數檢查
                    if dfs(neighbor, target, visited):
                        # 如果在鄰居節點中找到到達目標的路徑，返回 True
                        return True
            # 如果所有鄰居都無法到達目標，返回 False
            return False

        # 遍歷所有的邊，逐一檢查是否形成循環
        for u, v in edges:
            # 檢查當前邊的兩個節點是否已經在圖中存在
            if u in graph and v in graph:
                # 使用 DFS 檢查是否已經存在從 u 到 v 的路徑
                if dfs(u, v, set()):
                    # 如果存在路徑，說明添加這條邊會形成循環，返回這條冗餘邊
                    return [u, v]
            # 如果節點 u 還不在圖中，初始化其鄰居列表
            if u not in graph:
                graph[u] = []
            # 如果節點 v 還不在圖中，初始化其鄰居列表
            if v not in graph:
                graph[v] = []
            # 將節點 v 加入節點 u 的鄰居列表
            graph[u].append(v)
            # 將節點 u 加入節點 v 的鄰居列表，因為圖是無向圖
            graph[v].append(u)

        # 如果沒有找到冗餘的邊，返回空列表（根據題意，這種情況不會發生）
        return []


Solution().findRedundantConnection(edges=[[1, 2], [1, 3], [2, 3]])
