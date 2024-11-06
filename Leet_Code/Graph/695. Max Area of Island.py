from collections import deque
from typing import List
from Leet_Code.Graph import draw


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        nrow, ncol = len(grid), len(grid[0])

        def bfs(r, c):
            res = 0
            queue = deque()
            # 初始位子
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                # 檢查是否在迷宮範圍內
                if 0 <= r < nrow and 0 <= c < ncol and grid[r][c] == 1:
                    res += 1
                    grid[r][c] = 0
                    # 上下左右
                    queue.append((r + 1, c))
                    queue.append((r - 1, c))
                    queue.append((r, c + 1))
                    queue.append((r, c - 1))
            return res

        res = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    island_area = bfs(r, c)
                    res = max(res, island_area)

        return res


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        nrow, ncol = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= nrow or c >= ncol or grid[r][c] == 0:
                return 0
            grid[r][c] = 0  # 標記為已訪問
            # 遞歸訪問上下左右
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        res = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    island_area = dfs(r, c)
                    res = max(res, island_area)

        return res


Solution().maxAreaOfIsland(
    grid=[
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
)
