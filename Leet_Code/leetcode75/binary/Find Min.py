from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        res = float("inf")
        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] <= nums[r]:
                r = m - 1
            else:
                l = m + 1

        return res
