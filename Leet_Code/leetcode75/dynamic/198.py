from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i): # 搶到了第i個房間
            if i < 0: 
                return 0
            # 搶到目前為止 最大的利潤是
            res = max(dfs(i-1), dfs(i-2) + nums[i]) # 

            return res 
        
        return dfs(n-1)
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        cache = [-1] * n

        def dfs(i): # 搶到了第i個房間
            if i < 0: 
                return 0
            if cache[i] != -1:
                return cache[i]
            # 搶到目前為止 最大的利潤是
            res = max(dfs(i-1), dfs(i-2) + nums[i]) # 
            cache[i] = res

            return res 
        
        return dfs(n-1)
    


# 遞推

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 处理特殊情况
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1]
        


# # 遞推, 空間優化
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [0,0]
#         dp[0] = nums[0]
#         dp[1] = nums[1]

#         for i in range(2,n):
#             temp = dp[i]
#             dp[i] = max(dp[i])
#             dp[i-1] = temp

Solution().rob([1,2,3,1])
Solution().rob([2,7,9,3,1])
