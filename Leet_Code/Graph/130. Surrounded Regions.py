from collections import deque
from typing import List
from Leet_Code.Graph import draw


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
        draw(board)

        nr, nc = len(board), len(board[0])

        queue = deque()

        # 初始化邊界, 若是O加進來
        for r in range(nr):
            if board[r][0] == "O":
                queue.append((r, 0))
                board[r][0] = "."
            if board[r][nc - 1] == "O":
                queue.append((r, nc - 1))
                board[r][nc - 1] = "."
        for c in range(nc):
            if board[0][c] == "O":
                queue.append((0, c))
                board[0][c] = "."
            if board[nr - 1][c] == "O":
                queue.append((nr - 1, c))
                board[nr - 1][c] = "."
        draw(board)

        directions = [(0, 1), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= r < nr and 0 <= c < nc and board[nr][nc] == "O":
                    board[nr][nc] = "."
                    queue.append((nr, nc))

        for r in range(nr):
            for c in range(nc):
                if board[r][c] == ".":
                    board[r][c] = "X"


draw(Solution().solve(board=[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
