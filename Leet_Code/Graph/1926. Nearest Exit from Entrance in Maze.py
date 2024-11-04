from collections import deque
from typing import List

from sympy import N


def draw(maze: List[List[str]]):
    for row in maze:
        print(" ".join(row))


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # draw(maze)
        rows, cols = len(maze), len(maze[0])
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))  # 將迷宮入口的位置以及初始步數加入到廣度優先搜索（BFS）的隊列中
        maze[entrance[0]][entrance[1]] = "+"  # 標記為已訪問
        # draw(maze)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 走的方向
        while queue:
            draw(maze)
            r, c, steps = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # 檢查是否在迷宮範圍內
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == ".":
                    # 檢查是否為出口（邊界且不是入口）
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return steps + 1
                    # 標記為已訪問並加入隊列
                    maze[nr][nc] = "+"
                    queue.append((nr, nc, steps + 1))

        return -1


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        nrow, ncol = len(maze), len(maze[0])
        res = 0
        queue = deque([entrance])
        maze[entrance[0]][entrance[1]] = "+"
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:

            for _ in range(len(queue)):
                r, c = queue.popleft()

                if (r == 0 or r == nrow - 1 or c == 0 or c == ncol - 1) and [r, c] != entrance:
                    return res

                for dr, dc in direction:

                    nr, nc = r + dr, c + dc
                    if 0 <= nr < nrow and 0 <= nc < ncol and maze[nr][nc] == ".":
                        maze[nr][nc] = "+"
                        queue.append((nr, nc))

            res += 1

        return -1


Solution().nearestExit(maze=[["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], entrance=[1, 2])
Solution().nearestExit(maze=[["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], entrance=[1, 0])
Solution().nearestExit(
    maze=[["+", ".", "+", "+", "+", "+", "+"], ["+", ".", "+", ".", ".", ".", "+"], ["+", ".", "+", ".", "+", ".", "+"], ["+", ".", ".", ".", "+", ".", "+"], ["+", "+", "+", "+", "+", ".", "+"]],
    entrance=[1, 0],
)
