from collections import deque
import queue
from typing import List
from Leet_Code.Graph import draw


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
        # draw(grid)

        count = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"  # 標記為已訪問
            # 遞歸訪問上下左右
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque()
            # 初始位子
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                # 檢查是否在迷宮範圍內
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                    grid[r][c] = "0"
                    # 上下左右
                    queue.append((r + 1, c))
                    queue.append((r - 1, c))
                    queue.append((r, c + 1))
                    queue.append((r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)

        return count


# 2024.10.29
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        # 牆壁
        row, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r <= row and 0 <= c <= cols) or grid[r][c] == "0":  # fix -> (0 <= r < row and 0 <= c < cols)
                return

            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):

                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count


# 2024.11.2


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        draw(grid)
        nr, nc = len(grid), len(grid[0])

        res = 0

        def bfs(r, c):

            queue = deque()
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                if 0 <= r < nr and 0 <= c < nc and grid[r][c] == "1":
                    grid[r][c] = "0"
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        queue.append((r + dr, c + dc))

        for r in range(len(grid)):
            for c in range(len(grid[r])):

                if grid[r][c] == "1":
                    res += 1
                    bfs(r, c)

        return res


Solution().numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
Solution().numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
