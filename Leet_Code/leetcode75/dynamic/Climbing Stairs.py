class Solution:
    def climbStairs(self, n: int) -> int:

        cache = [0] * (n + 2)
        cache[1], cache[2] = 1, 2

        def dfs(i):
            if i <= 0:
                return 0

            if cache[i]:
                return cache[i]

            cache[i] = dfs(i - 1) + dfs(i - 2)

            return cache[i]

        return dfs(n)


Solution().climbStairs(1)
Solution().climbStairs(2)
Solution().climbStairs(3)
Solution().climbStairs(4)
