from collections import defaultdict
import enum
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        n = 6
        connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

        graph = defaultdict(list)
        edge_directions = {}

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            edge_directions[(u, v)] = 1  # 原始方向從 u 到 v

        count = 0

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
        # 把有帶0的作抓出來


Solution().minReorder(connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])
