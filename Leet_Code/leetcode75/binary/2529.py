from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # 找比0大的第一個i
        # 找比0小的第一個i

        def lower_bound(nums, target):
            # 找比0大的第一個i
            l, r = 0, len(nums) - 1
            while l <= r:

                mid = (l + r) // 2
                if nums[mid] <= target:  # 跟目標符號相反
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def lower_bound_2(nums, target):
            # 找比0小的第一個i -> 找大於等於0的第一個i - 1
            l, r = 0, len(nums) - 1
            while l <= r:

                mid = (l + r) // 2
                if nums[mid] < target:  # 跟目標符號相反
                    l = mid + 1
                else:
                    r = mid - 1
            return l - 1

        x = lower_bound(nums, 0)
        y = lower_bound_2(nums, 0)
        return max(len(nums) - x + 1, y + 1)


Solution().maximumCount([-3, -2, -1, 0, 0, 1, 2])
