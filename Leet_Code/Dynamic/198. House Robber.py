from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n <= 2:
            return max(nums)
        # 定義dp[i] = 搶到dp[i]的房子時可以拿到的最大價值
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        @cache
        def dfs(i):
            if i < 0:
                return 0
            return max(dfs(i - 2) + nums[i], dfs(i - 1))

        return dfs(n - 1)


Solution().rob(nums=[1, 2, 3, 1])
Solution().rob(nums=[2, 7, 9, 3, 1])
Solution().rob(nums=[2])
