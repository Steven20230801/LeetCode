from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 找出 >= target的最左邊數
        l, r = 0, len(nums)
        while l <= r:
            mid = (l + r) // 2
            res = nums[mid]

            if res >= target:
                r = mid - 1
            else:
                l = mid + 1
