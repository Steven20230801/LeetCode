from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float("-inf"))
        nums.insert(0, float("-inf"))
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            res = nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]

            if res:
                return mid - 1
            elif nums[mid] > nums[mid - 1]:
                l = mid + 1
            else:
                r = mid - 1

        return 0 if r == -1 else len(nums) - 1


Solution().findPeakElement([1])
Solution().findPeakElement([1, 3, 2, 1, 1, 1])
Solution().findPeakElement([3, 2, 1])
Solution().findPeakElement([1, 2, 3])
