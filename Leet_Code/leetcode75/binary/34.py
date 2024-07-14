from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        # 找 >= target的第一個樹
        # 找 > target的遞一個樹
        def lower_bound(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def lower_bound2(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        x = lower_bound(nums, target)
        y = lower_bound2(nums, target)

        if x == y:
            return [-1, -1]
        else:
            return [x, y]


Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6)
