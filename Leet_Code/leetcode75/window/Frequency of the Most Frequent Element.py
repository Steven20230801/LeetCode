from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        res = 0
        total = 0
        l, r = 0, 0

        for r in range(len(nums)):

            total += nums[r]
            while (r - l + 1) * nums[r] > total + k:
                total -= nums[l]
                l += 1
            window_size = r - l + 1
            res = max(res, window_size)

        return res


Solution().maxFrequency(nums=[1, 2, 4], k=5)
Solution().maxFrequency(nums=[1, 4, 8, 13], k=5)
