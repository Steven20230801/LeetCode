from collections import deque
from typing import List
from Leet_Code.Graph import draw


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        queue = deque()
        # 初始腐朽的位置
        fresh_count = 0
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 1:
                    fresh_count += 1
                elif item == 2:
                    queue.append([i, j])

        if not fresh_count:
            return 0
        if not queue:
            return -1

        rows, cols = len(grid), len(grid[0])  # 外牆
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 走的方向
        minutes = 0
        while queue and fresh_count != 0:
            minutes += 1
            # draw(grid)
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # 檢查是否在迷宮範圍內
                    if 0 <= nr < rows and 0 <= nc < cols:
                        # 檢查是否新鮮橘子
                        if grid[nr][nc] == 1:
                            fresh_count -= 1
                            # 標記為已訪問並加入隊列
                            grid[nr][nc] = 2
                            queue.append((nr, nc))

        # print(minutes)

        return minutes if fresh_count == 0 else -1


# GPT優化


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 检查网格是否为空
        if not grid or not grid[0]:
            return -1  # 根据题意，可以返回其他值

        rows, cols = len(grid), len(grid[0])
        queue = deque()  # 用于存储腐烂橘子的坐标
        fresh_count = 0  # 统计新鲜橘子的数量

        # 初始化队列和新鲜橘子计数
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))  # 将腐烂橘子的位置加入队列
                elif grid[r][c] == 1:
                    fresh_count += 1  # 统计新鲜橘子数量

        # 如果没有新鲜橘子，返回 0
        if fresh_count == 0:
            return 0

        # 定义四个方向的移动：上、下、左、右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0  # 记录经过的分钟数

        # BFS 遍历
        while queue and fresh_count > 0:
            minutes += 1  # 每层 BFS 表示一分钟
            for _ in range(len(queue)):
                r, c = queue.popleft()  # 取出当前腐烂橘子的位置
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc  # 计算相邻位置
                    # 检查新位置是否在网格内且为新鲜橘子
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # 将新鲜橘子腐烂
                        fresh_count -= 1  # 新鲜橘子数量减少
                        queue.append((nr, nc))  # 将新腐烂橘子的位置加入队列

        # 检查是否所有新鲜橘子都已腐烂
        return minutes if fresh_count == 0 else -1


# 示例调用
if __name__ == "__main__":
    solution = Solution()
    result = solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
    print(result)  # 输出应为 -1，因为有些橘子无法腐烂
    result = solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    print(result)  # 4
