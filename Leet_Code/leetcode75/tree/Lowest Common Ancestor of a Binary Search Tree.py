from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):

            if i > 0:
                left_sum += nums[i - 1]
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i

        return -1


Solution().pivotIndex(nums=[1, 7, 3, 6, 5, 6])
