from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if m > 0 and nums[m - 1] > nums[m]:
                r = m - 1
            elif m < len(nums) - 1 and nums[m + 1] > nums[m]:
                l = m + 1
            else:
                return m


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 2  # nums[-1]一定是峰頂
        while l <= r:
            m = (l + r) // 2

            if nums[m + 1] > nums[m]:  # 0 ~ m 是峰頂左側
                l = m + 1
            else:
                r = m - 1

        return l  # = r+1 = nums[m] > nums[m+1]
    

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) # 左閉右開
        while l < r:
            m = (l + r) // 2

            if nums[m + 1] > nums[m]:  # 0 ~ m 是峰頂左側
                l = m + 1
            else:
                r = m

        return l 

Solution().findPeakElement([1, 2, 3, 1])
Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4])
