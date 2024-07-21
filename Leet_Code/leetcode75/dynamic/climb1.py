def dp(n):
    if n < 3:
        return n

    dp = [1, 2]
    i = 3
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]


class Solution:
    def climbStairs(self, n: int) -> int:
        return dp(n)


Solution().climbStairs(5)


def climbStairs(n):

    t1 = 1
    t2 = 2

    if n == 1:
        return t1

    if n == 2:
        return t2

    for i in range(n - 2):
        temp = t2
        res = t1 + t2
        t1 = temp
        t2 = res
    return res


climbStairs(3)
