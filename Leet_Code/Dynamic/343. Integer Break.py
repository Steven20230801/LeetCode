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
                res = max(res, max(j, dfs(j)) * max(i - j, dfs(i - j)))

            return res

        return dfs(n)


class Solution:
    def integerBreak(self, n: int) -> int:

        if n == 2:
            return 1

        dp = [0 for _ in range(n + 1)]
        dp[1], dp[2], dp[3] = 1, 2, 2
        for i in range(3, n + 1):

            res = 0
            for j in range(1, i + 1):
                res = max(res, j * dp[i - j])
            dp[i] = res

        return dp[n]


print(Solution().integerBreak(2))
print(Solution().integerBreak(3))
print(Solution().integerBreak(4))
print(Solution().integerBreak(5))
print(Solution().integerBreak(6))
print(Solution().integerBreak(7))
print(Solution().integerBreak(8))
print(Solution().integerBreak(9))
print(Solution().integerBreak(10))
print(Solution().integerBreak(11))
