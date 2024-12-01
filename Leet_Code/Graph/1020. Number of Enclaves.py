from collections import deque
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        nr, nc = len(grid), len(grid[0])
        queue = deque()

        # 初始化邊界, 若是1: 島嶼加進來, 將1 先換成 2
        for r in range(nr):
            if grid[r][0] == 1:
                queue.append((r, 0))
                grid[r][0] = 2
            if grid[r][nc - 1] == 1:
                queue.append((r, nc - 1))
                grid[r][nc - 1] = 2
        for c in range(nc):
            if grid[0][c] == 1:
                queue.append((0, c))
                grid[0][c] = 2
            if grid[nr - 1][c] == 1:
                queue.append((nr - 1, c))
                grid[nr - 1][c] = 2

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc))

        res = 0
        # 沒被換成2的代表是孤立島嶼

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res += 1

        return res


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):

            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1):
                return

            grid[r][c] = 2

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        # 初始化邊界, 若是1: 島嶼加進來, 將1 先換成 2
        # 遍歷邊界
        for r in range(nr):
            for c in range(nc):
                if r in [0, nr - 1] or c in [0, nc - 1]:
                    dfs(r, c)

        res = 0
        # 沒被換成2的代表是孤立島嶼

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res += 1

        return res


from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # 獲取網格的行數和列數
        num_rows, num_cols = len(grid), len(grid[0])

        # 定義四個可能的移動方向：上下左右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r: int, c: int):
            """
            深度優先搜索，將所有與邊界相連的陸地（1）標記為2
            """
            # 檢查當前格子是否在邊界內且為陸地
            if r < 0 or r >= num_rows or c < 0 or c >= num_cols or grid[r][c] != 1:
                return

            # 標記為2，表示已訪問且與邊界相連
            grid[r][c] = 2

            # 遍歷所有四個方向
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                dfs(new_r, new_c)

        # 遍歷所有邊界上的格子，並對其中的陸地進行DFS
        for r in range(num_rows):
            for c in range(num_cols):
                # 如果當前格子位於邊界且為陸地，則進行DFS
                if r == 0 or r == num_rows - 1 or c == 0 or c == num_cols - 1:
                    if grid[r][c] == 1:
                        dfs(r, c)

        # 計數飛地的數量
        enclave_count = 0
        for r in range(num_rows):
            for c in range(num_cols):
                # 如果格子為1，則表示該格子是飛地
                if grid[r][c] == 1:
                    enclave_count += 1

        return enclave_count


Solution().numEnclaves(grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
Solution().numEnclaves(grid=[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
