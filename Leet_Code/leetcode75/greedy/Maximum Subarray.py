from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cursum = 0
        max_sum = 0

        for x in nums:

            cursum = max(x, cursum + x)
            max_sum = max(max_sum, cursum)

        return max_sum


Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
