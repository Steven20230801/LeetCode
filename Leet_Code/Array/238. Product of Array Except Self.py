from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums = [1, 2, 3, 4]
        n = len(nums)
        # 前綴乘積：對於每個位置 i，計算 nums[0] * nums[1] * ... * nums[i-1]。

        # 後綴乘積：對於每個位置 i，計算 nums[i+1] * nums[i+2] * ... * nums[n-1]。
        prefix = [1] * (n + 1)
        postfix = [1] * (n + 1)
        cur = 1
        for i in range(1, n):
            cur = cur * nums[i]
            prefix[i] = cur
        print(prefix)

        prefix = [1] + [1, 2, 6, 24]
        postfix = [24, 24, 12, 4] + [1]
        for i, v in enumerate(nums):
            cur = cur * v
            print(cur)
        cur = 1
        for i in range(n - 1, -1, -1):
            cur = cur * nums[i]
            print(cur)
