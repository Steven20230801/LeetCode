from functools import cache
from typing import List


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        def dp(nums):
            n = len(nums)  # 獲取房屋的數量
            # 如果房屋數量少於或等於2，直接返回其中的最大值
            if n <= 2:
                return max(nums)

            # 定義dp陣列，其中dp[i]表示搶到第i間房子時可以拿到的最大金額
            dp = [0 for _ in range(n)]
            dp[0] = nums[0]  # 初始化第一間房子的最大金額為其自身的金額
            dp[1] = max(nums[0], nums[1])  # 第二間房子的最大金額為前兩間中較大的金額

            # 從第三間房子開始，依次計算每間房子的最大金額
            for i in range(2, n):
                # 對於第i間房子，有兩種選擇：
                # 1. 搶第i間房子，則不能搶第i-1間房子，最大金額為dp[i-2] + nums[i]
                # 2. 不搶第i間房子，則最大金額為dp[i-1]
                # 取兩者中的較大值作為dp[i]
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp[n - 1]

        if len(nums) <= 2:
            return max(nums)

        dp1 = dp(nums=nums[1:])
        dp2 = dp(nums=nums[:-1])
        return max(dp1, dp2)


Solution().rob(nums=[2, 3, 2])
Solution().rob(nums=[1, 2, 3, 1])
Solution().rob(nums=[1, 2, 3])
