from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        prefix = 0

        for i in range(0, len(nums)):
            if prefix == nums_sum - prefix - nums[i]:
                return i
            prefix += nums[i]

        return -1


Solution().pivotIndex([1, 7, 3, 6, 5, 6])


Solution().pivotIndex([-1, -1, -1, 1, 1, 1])
