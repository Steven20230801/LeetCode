from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        h = {}
        for x in grid:
            if tuple(x) in h:
                h[tuple(x)] += 1
            else:
                h[tuple(x)] = 1
        ans = 0
        for col in zip(*grid):
                if col in h:
                ans += h[tuple(col)]

        return ans


Solution().equalPairs(grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
