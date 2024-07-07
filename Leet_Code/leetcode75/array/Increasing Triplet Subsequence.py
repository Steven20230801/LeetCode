from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 先找後綴有沒有大於i的
        x = [False] * len(nums)
        max_n = 0
        for i in range(len(nums) - 2, -1, -1):
            max_n = max(max_n, nums[i + 1])
            if max_n > nums[i]:
                x[i] = True

        # 在找前綴
        min_n = nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i] > min_n and x[i]:
                return True
            else:
                min_n = min(min_n, nums[i])
        return False

    def increasingTriplet(self, nums):
        first = second = float("inf")
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


Solution().increasingTriplet([20, 100, 10, 12, 5, 13])

Solution().increasingTriplet([1, 5, 0, 4, 1, 3])
