from math import inf
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


# 2024-09-29
class Solution:
    def findMin(self, nums: List[int]) -> int:

        # if sorted
        if nums[0] < nums[-1]:
            return nums[0]

        # if not sorted
        l, r = 0, len(nums) - 1
        res = inf
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[r]:  # 最小在m+1右邊
                l = m + 1
            else:
                r = m - 1
                res = min(res, nums[m])

        return res


Solution().findMin([3, 4, 5, 1, 2])
Solution().findMin([4, 5, 6, 7, 0, 1, 2])
Solution().findMin([3, 1, 2])
