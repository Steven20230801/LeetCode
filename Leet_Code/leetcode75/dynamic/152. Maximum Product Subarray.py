from typing import List




class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)

        def dp(i, mx, mn):

            if i >= n:
                return max(mx, mn)

            if nums[i] == 0:
                ans = max(0, dp(i + 1, 1, 1))
            elif nums[i] > 0:
                ans = dp(i + 1, mx * nums[i], mn * nums[i])
            else:
                ans = dp(i+1, mn * nums[i], mx * nums[i])
        
            return ans 
            
        return dp(0, 1, 1)

Solution().maxProduct(nums = [2, 3, -2, 4])