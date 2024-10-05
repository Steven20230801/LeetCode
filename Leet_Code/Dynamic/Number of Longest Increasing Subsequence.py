from functools import cache
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        nums = [1, 3, 5, 4, 7]
        n = len(nums)

        @cache
        def dfs(i):
            res = 0
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    res = max(res, dfs(j))
            return res + 1

        dfs(0)


Solution().findNumberOfLIS([1, 3, 5, 4, 7])
