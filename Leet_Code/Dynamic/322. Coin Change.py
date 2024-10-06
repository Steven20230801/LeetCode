from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        memo = {}

        def dfs(i, remains):
            if i == n:  # 基礎情況：已經考慮完所有硬幣
                return 0 if remains == 0 else inf

            if (i, remains) in memo:  # 如果當前狀態已經計算過，直接返回結果
                return memo[(i, remains)]

            if coins[i] <= remains:  # 嘗試使用當前硬幣
                memo[(i, remains)] = min(dfs(i + 1, remains), 1 + dfs(i, remains - coins[i]))
            else:  # 嘗試不使用當前硬幣
                memo[(i, remains)] = dfs(i + 1, remains)

            return memo[(i, remains)]

        res = dfs(0, amount)
        if res != inf:
            return res
        else:
            return -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        # coins.sort(reverse=True)
        memo = {}

        def dfs(i, remains):

            if remains == 0:
                return 0
            if remains < 0 or i >= n:
                return inf

            if (i, remains) in memo:
                return memo[(i, remains)]

            if coins[i] <= remains:
                memo[(i, remains)] = min(dfs(i + 1, remains), 1 + dfs(i, remains - coins[i]))
            else:
                memo[(i, remains)] = dfs(i + 1, remains)

            return memo[(i, remains)]

        res = dfs(0, amount)
        return res if res != inf else -1


# 2D DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)  # 硬幣種類數量

        # 初始化 2D DP 表格
        # dp[i][j] 表示使用前 i 種硬幣來組成金額 j 所需的最少硬幣數
        dp = [[inf for _ in range(amount + 1)] for _ in range(n + 1)]

        # 初始化第一欄：組成金額 0 所需的硬幣數為 0
        for i in range(n + 1):
            dp[i][0] = 0
        # 填充 DP 表格
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                # 不使用第 i 種硬幣
                dp[i][j] = dp[i - 1][j]

                # 使用第 i 種硬幣（前提是硬幣面額不超過當前金額 j）
                if j >= coins[i - 1]:  # 修正條件：包含 j 等於硬幣面額
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]] + 1)
        # 返回最終結果
        return dp[n][amount] if dp[n][amount] != inf else -1


# 靈茶山
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)  # 硬幣種類數量

        # 初始化 2D DP 表格
        # dp[i][j] 表示使用前 i 種硬幣來組成金額 j 所需的最少硬幣數
        dp = [[inf for _ in range(amount + 1)] for _ in range(n + 1)]
        dp[0][0] = 0
        for i, v in enumerate(coins):
            for c in range(amount + 1):
                if c < v:
                    dp[i + 1][c] = dp[i][c]
                else:
                    dp[i + 1][c] = min(dp[i][c], dp[i + 1][c - v] + 1)

        res = dp[n][amount]
        return res if res != inf else -1


# 1D DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        dp = [inf] * (amount + 1)
        dp[0] = 0  # 0不用任何硬幣組成

        for coin in coins:  # 遍歷每一種硬幣
            # 對於每一種硬幣，遍歷所有可能的金額從 coin 到 amount
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
                # 註解：
                # dp[x - coin] 表示組成金額 (x - coin) 所需的最少硬幣數
                # 加上 1 表示再加上一枚當前的硬幣
                # min(dp[x], dp[x - coin] + 1) 表示選擇不使用當前硬幣或使用當前硬幣的最小值

        return dp[amount] if dp[amount] != inf else -1


Solution().coinChange(coins=[1, 2, 5], amount=11)
Solution().coinChange(coins=[2], amount=3)
Solution().coinChange(coins=[1], amount=0)
