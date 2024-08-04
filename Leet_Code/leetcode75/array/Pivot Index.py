from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # [1, 7, 3, 6, 5, 6]
        # [0, 1, 8, 11, 17, 22]
        # [         11,  6, 0]
        presum = [0] * len(nums)
        postsum = [0] * len(nums)

        temp = 0
        for i in range(len(nums)):
            presum[i] = temp
            temp += nums[i]

        temp = 0
        for i in range(len(nums) - 1, -1, -1):
            postsum[i] = temp
            temp += nums[i]

        for i in range(len(nums)):
            if presum[i] == postsum[i]:
                return i
        return -1


Solution().pivotIndex(nums=[1, 7, 3, 6, 5, 6])
Solution().pivotIndex(nums=[2, 1, -1])
