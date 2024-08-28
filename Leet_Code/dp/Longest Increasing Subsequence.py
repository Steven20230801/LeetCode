from functools import cache
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i):
            res = 0
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    res = max(res, dfs(j))
            return res + 1

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans


Solution().lengthOfLIS(nums=[0, 1, 0, 3, 2, 3])
Solution().lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18])
