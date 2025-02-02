from typing import List


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        res = 0
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]

        def dfs(r, c):
            nonlocal res
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if r < 0 or c < 0 or r >= nrow or c >= ncol or grid[r][c] == 0:
                res += 1
                return
            if visited[r][c]:
                return
            visited[r][c] = True
            for nr, nc in dirs:
                dfs(r + nr, c + nc)

        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    dfs(r, c)

        return res


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        res = 0
        for r in range(nrow):
            for c in range(ncol):
                # 若是陸地 則先加4
                if grid[r][c] == 1:
                    res += 4
                    # 判斷右邊/ 下方是否是陸地, 若是的話 -2
                    if r < nrow - 1 and grid[r + 1][c] == 1:
                        res -= 2
                    if c < ncol - 1 and grid[r][c + 1] == 1:
                        res -= 2

        return res


Solution().islandPerimeter(grid=grid)
