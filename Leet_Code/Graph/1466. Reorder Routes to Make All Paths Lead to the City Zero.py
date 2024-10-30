from collections import defaultdict
import enum
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


Solution().minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])
