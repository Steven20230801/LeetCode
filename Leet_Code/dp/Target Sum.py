from collections import defaultdict
from functools import cache
from typing import List

#


# Cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # p
        # n = s-p
        # target = p-n
        # target = p-(s-p) = 2p-s
        # p = (target + s) / 2 -> 背包有(target + s) / 2容量, 選擇方案數
        target += sum(nums)

        if target < 0 or target % 2 == 1:
            return 0

        target = target / 2
        n = len(nums)

        @cache
        def dfs(i, t):

            if i < 0:
                return 1 if t == 0 else 0
            # 超出容量
            if nums[i] > t:
                return dfs(i - 1, t)

            res = dfs(i - 1, t) + dfs(i - 1, t - nums[i])  # 不選 + 選
            return res

        return dfs(n - 1, target)


# 記憶化
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # p
        # n = s-p
        # target = p-n
        # target = p-(s-p) = 2p-s
        # p = (target + s) / 2 -> 背包有(target + s) / 2容量, 選擇方案數
        target += sum(nums)

        if target < 0 or target % 2 == 1:
            return 0

        target = target / 2
        n = len(nums)

        memo = {}

        def dfs(i, t):

            if (i, t) in memo:
                return memo[(i, t)]

            if i < 0:
                return 1 if t == 0 else 0
            # 超出容量
            if nums[i] > t:
                memo[(i, t)] = dfs(i - 1, t)
            else:
                memo[(i, t)] = dfs(i - 1, t) + dfs(i - 1, t - nums[i])  # 不選 + 選

            return memo[(i, t)]

        return dfs(n - 1, target)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        

# 遞推
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # p
        # n = s-p
        # target = p-n
        # target = p-(s-p) = 2p-s
        # p = (target + s) / 2 -> 背包有(target + s) / 2容量, 選擇方案數
        
        nums=[1, 1, 1, 1, 1]
        target=3
        target += sum(nums)

        if target < 0 or target % 2 == 1:
            return 0

        target = target // 2
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i, x in enumerate(nums)

        def dfs(i, t):

            if (i, t) in memo:
                return memo[(i, t)]

            if i < 0:
                return 1 if t == 0 else 0
            # 超出容量
            if nums[i] > t:
                memo[(i, t)] = dfs(i - 1, t)
            else:
                memo[(i, t)] = dfs(i - 1, t) + dfs(i - 1, t - nums[i])  # 不選 + 選

            return memo[(i, t)]

        return dfs(n - 1, target)


Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3)
Solution().findTargetSumWays(nums=[1], target=1)
