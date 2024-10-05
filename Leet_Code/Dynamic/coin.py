from typing import List
from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化 dp 陣列，dp[i] 表示組成金額 i 所需的最少硬幣數
        # 設定為無限大表示初始狀態下無法組成該金額
        dp = [inf] * (amount + 1)
        dp[0] = 0  # 組成金額 0 需要 0 枚硬幣

        # 遍歷每一種硬幣
        for coin in coins:
            # 對於每一種硬幣，遍歷所有可能的金額從 coin 到 amount
            for x in range(coin, amount + 1):
                # 如果使用當前硬幣後，可以組成金額 x
                # 則更新 dp[x] 為 dp[x - coin] + 1 和當前 dp[x] 的最小值
                dp[x] = min(dp[x], dp[x - coin] + 1)
                # 註解：
                # dp[x - coin] 表示組成金額 (x - coin) 所需的最少硬幣數
                # 加上 1 表示再加上一枚當前的硬幣
                # min(dp[x], dp[x - coin] + 1) 表示選擇不使用當前硬幣或使用當前硬幣的最小值

        # 最後檢查 dp[amount] 是否被更新過
        # 如果 dp[amount] 仍為無限大，表示無法組成該金額，返回 -1
        # 否則返回 dp[amount]，即最少需要的硬幣數
        return dp[amount] if dp[amount] != inf else -1


Solution().coinChange(coins = [1,2,5], amount = 11)
Solution().coinChange(coins = [2], amount = 3)
Solution().coinChange(coins = [1], amount = 0)