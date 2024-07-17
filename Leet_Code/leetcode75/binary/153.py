from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] < nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1
        res = 5001
        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return res


Solution().findMin(nums=[3, 1, 2])

Solution().findMin(nums=[4, 5, 6, 7, 0, 1, 2])

Solution().findMin(nums=[3, 4, 5, 1, 2])


Solution().findMin(nums=[11, 13, 15, 17])
