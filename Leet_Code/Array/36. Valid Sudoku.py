from collections import defaultdict
from typing import List

from traitlets import default


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        h_r = defaultdict(set)
        h_c = defaultdict(set)
        h_box = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                node = board[r][c]
                if node != ".":
                    box = (r // 3, c // 3)
                    if node in h_r[r] or node in h_c[c] or node in h_box[box]:
                        return False
                    h_r[r].add(node)
                    h_c[c].add(node)
                    h_box[box].add(node)
        return True


Solution().isValidSudoku(
    board=[
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)

Solution().isValidSudoku(
    board=[
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)
