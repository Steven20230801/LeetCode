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

        
        for r in range(len(board)):
            if board[r][nc] == 'O'
        
        ans = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
        draw(ans)
        
        

        return ans 
draw(Solution().solve(board=[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
