from collections import defaultdict, deque
import enum
import queue
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        n = 6
        connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
        graph = defaultdict(list)  #  建立每個節點連接的其他節點 ex 0: [1, 4]
        edge_directions = {}  # 建立方向

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            edge_directions[(u, v)] = 1  # 原始方向從 u 到 v

        def dfs(node, parent):
            nonlocal count
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                # 檢查邊的方向是否需要反轉
                if (node, neighbor) in edge_directions:
                    count += 1
                dfs(neighbor, node)

        count = 0
        dfs(0, -1)
        return count


class Solution2:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        n = 6
        connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
        graph = defaultdict(list)  #  建立每個節點連接的其他節點 ex 0: [1, 4]
        edge_directions = {}  # 建立方向

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            edge_directions[(u, v)] = 1  # 原始方向從 u 到 v

        count = 0
        q = deque()
        q.append(0)
        visited = [False] * n
        visited[0] = True
        while q:
            node = q.popleft()
            # node 連接的鄰居
            neighbors = graph[node]

            for neighbor in neighbors:
                if not visited[neighbor]:
                    visited[neighbor] = True

                    if (node, neighbor) in edge_directions:
                        count += 1

                    q.append(neighbor)

        return count


# GPT
from collections import defaultdict, deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        計算最少需要重排的道路數量，使得所有城市都可以通過某些道路到達城市 0。

        :param n: 城市的數量，標號為 0 到 n-1
        :param connections: 道路的列表，每條道路由 [u, v] 表示原始方向是從 u 到 v
        :return: 需要重排的道路數量
        """

        # 建立無向圖和記錄原始方向的集合
        graph = defaultdict(list)  # 無向圖：每個節點連接的鄰居節點列表
        edge_directions = set()  # 記錄原始方向的邊 (u, v) 表示從 u 到 v

        # 構建圖和記錄邊的方向
        for u, v in connections:
            graph[u].append(v)  # 從 u 指向 v
            graph[v].append(u)  # 從 v 指向 u，因為圖是無向的
            edge_directions.add((u, v))  # 記錄原始方向

        count = 0  # 計數需要重排的道路數量
        queue = deque([0])  # 初始化 BFS 隊列，從城市 0 開始
        visited = [False] * n  # 記錄每個城市是否已訪問
        visited[0] = True  # 標記城市 0 為已訪問

        # 開始 BFS 遍歷
        while queue:
            current = queue.popleft()  # 取出當前處理的城市

            # 遍歷當前城市的所有鄰居
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True  # 標記為已訪問

                    # 檢查邊的方向是否需要反轉
                    if (current, neighbor) in edge_directions:
                        count += 1  # 需要重排的道路數量增加

                    queue.append(neighbor)  # 將鄰居加入 BFS 隊列

        return count  # 返回需要重排的道路總數


# 2024.11.09
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        edges = {}

        for s, d in connections:
            graph[s].append(d)
            graph[d].append(s)
            edges[(s, d)] = 1

        print(graph)
        print(edges)

        res = 0
        visited = [False] * n
        q = deque()
        # init
        q.append(0)
        visited[0] = True

        while q:

            node = q.popleft()

            for neighbor in graph[node]:
                # 1, 4
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True

                    if (node, neighbor) in edges:
                        res += 1
        return res


Solution().minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])
