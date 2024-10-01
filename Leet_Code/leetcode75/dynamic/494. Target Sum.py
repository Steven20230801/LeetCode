from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        memo = {}
        def dfs(i, total):

            if i == len(nums):
                # 如果Total = target 才是合法答案
                return 1 if total == target else 0 
            
            if (i, total) in memo:
                return memo[(i, total)]
            
            # (i, total) 子樹有 可+ nums[i] 或是可- nums[i]的兩個子樹, 兩個子樹的答案等於母樹
            ans = (dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])) 
            memo[(i, total)] = ans
            return ans 
        return dfs(0, 0)
    
sorted()



    