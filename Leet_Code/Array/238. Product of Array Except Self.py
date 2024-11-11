from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        # 前綴乘積：對於每個位置 i，計算 nums[0] * nums[1] * ... * nums[i-1]。
        cur = 1
        prefix = [1] * (n)
        for i in range(1, n):
            prefix[i] = cur
            cur = cur * nums[i]
            
        # 後綴乘積：對於每個位置 i，計算 nums[i+1] * nums[i+2] * ... * nums[n-1]。
        postfix = [1] * (n)
        cur = 1
        for i in range(n - 1, -1, -1):
            postfix[i] = cur
            cur = cur * nums[i]
            
        res = []
        for i in range(n):
            res.append(prefix[i] * postfix[i])

        return res
    
# GPT
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        # 前綴乘積：對於每個位置 i，計算 nums[0] * nums[1] * ... * nums[i-1]。
        cur = 1
        prefix = [1] * (n)
        for i in range(n):
            prefix[i] = cur
            cur = cur * nums[i]
            
        # 後綴乘積：對於每個位置 i，計算 nums[i+1] * nums[i+2] * ... * nums[n-1]。
        postfix = [1] * (n)
        cur = 1
        for i in range(n - 1, -1, -1):
            postfix[i] = cur
            cur = cur * nums[i]
            
        res = []
        for i in range(n):
            res.append(prefix[i] * postfix[i])

        return res
    
Solution().productExceptSelf(nums = [-1,1,0,-3,3])
Solution().productExceptSelf(nums = [1,2,3,4])
Solution().productExceptSelf(nums = [3,2,3,4])