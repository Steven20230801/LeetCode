from typing import List


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        res = 0
        visit = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(r, c, res) -> int:

            # 若已經訪問過或是超出邊界則返回
            if r < 0 or c < 0 or r >= nrow or c >= ncol or visit[r][c] == True:
                return 0
            # 若是水或邊界則+1後返回
            if r in [0, nrow - 1] or c in [0, ncol - 1] or grid[r][c] == 0:
                return 1

            visit[r][c] = True
            # 檢查四個方向 若是邊界/ 水則+1
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for nr, nc in dirs:
                res += dfs(r + nr, c + nc, res)
            return res

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res += dfs(r, c, 0)

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
