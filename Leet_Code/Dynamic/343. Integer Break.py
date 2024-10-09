from functools import cache


class Solution:
    def integerBreak(self, n: int) -> int:

        if n == 2:
            return 1

        @cache
        def dfs(i):

            if i == 1:
                return 1
            res = 0
            for j in range(1, i):
                val = dfs(j) * dfs(i - j)
                res = max(res, val)
            return res

        return dfs(n)


Solution().integerBreak(3)
