from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for _ in range(n + 1)]
        # dp[i] 代表站在i所需要的最少$$
        dp[0] = 0
        dp[1] = 0
        # dp[2] = min(dp[0])
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[n]


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)  # 階梯的總數
        dp = [0 for _ in range(n + 1)]  # 動態規劃陣列，dp[i] 表示到達第 i 階的最小花費

        # 初始化
        dp[0] = 0  # 從第 0 階開始，花費為 0
        dp[1] = 0  # 從第 1 階開始，花費為 0

        # 遍歷每一階，計算到達該階的最小花費
        for i in range(2, n + 1):
            # 要到達第 i 階，可以從第 i-1 階跨一步，或者從第 i-2 階跨兩步
            # 選擇其中花費較小的路徑
            cost_step_one = dp[i - 1] + cost[i - 1]  # 從第 i-1 階跨一步到第 i 階
            cost_step_two = dp[i - 2] + cost[i - 2]  # 從第 i-2 階跨兩步到第 i 階
            dp[i] = min(cost_step_one, cost_step_two)  # 選擇最小的花費

        # 返回到達頂部的最小花費
        return dp[n]
