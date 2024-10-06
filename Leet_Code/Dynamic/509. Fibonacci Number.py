class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        # 建立DP
        dp = [0 for _ in range(n + 1)]
        # init
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]


class Solution:
    def fib(self, n: int) -> int:
        """
        计算第 n 个斐波那契数。

        参数:
        n (int): 要计算的斐波那契数的索引。

        返回:
        int: 第 n 个斐波那契数。
        """
        # 处理特殊情况
        if n == 0:
            return 0
        if n == 1:
            return 1

        # 初始化前两个斐波那契数
        prev, curr = 0, 1

        # 从第2个斐波那契数开始迭代计算
        for i in range(2, n + 1):
            # 计算当前斐波那契数
            next_fib = prev + curr
            # 更新前两个数以便下一次迭代
            prev, curr = curr, next_fib

        # 返回第 n 个斐波那契数
        return curr


solution = Solution()
print(solution.fib(2))
print(solution.fib(3))
print(solution.fib(4))
print(solution.fib(0))
print(solution.fib(1))
