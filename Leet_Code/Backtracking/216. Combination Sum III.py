from functools import cache, lru_cache
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        path = []

        def dfs(i, remain):
            if len(path) == k and remain == 0:
                res.append(path[:])
                return

            if remain < 0 or i > 9:
                return

            path.append(i)
            dfs(i + 1, remain - i)
            path.pop()

            dfs(i + 1, remain)

        dfs(1, n)
        return res


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i, target):
            if len(path) == k and target == 0:
                ans.append(path.copy())
                return

            if target < 0 or i > 9:
                return

            path.append(i)
            dfs(i + 1, target - i)
            path.pop()

            dfs(i + 1, target)

        dfs(1, n)

        return ans


Solution().combinationSum3(k=3, n=7)
Solution().combinationSum3(k=3, n=9)
