from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        maxSum = nums[0]
        curSum = 0

        minSum = nums[0]
        curMin = 0

        for n in nums:

            # 紀錄最大
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)

            # 紀錄最小
            curMin = min(curMin, 0)
            curMin += n
            minSum = min(minSum, curMin)

        if sum(nums) == minSum:
            return maxSum
        else:

            return max(maxSum, sum(nums) - minSum)


Solution().maxSubarraySumCircular([5, -3, 5])

Solution().maxSubarraySumCircular([-3, -2, -3])


Solution().maxSubarraySumCircular([1, -2, 3, -2])
