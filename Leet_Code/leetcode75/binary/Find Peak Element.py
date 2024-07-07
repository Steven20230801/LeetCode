from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float("-inf"))
        nums.insert(0, float("-inf"))

        l, r = 0, len(nums) - 1

        # 若mid左邊比較大, 左邊是封頂, 右邊比較大, 右邊是封頂

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid - 1

            elif nums[mid] > nums[mid - 1]:
                l = mid + 1
            else:
                r = mid - 1

        return l


Solution().findPeakElement([1, 2, 3, 1])
Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4])
