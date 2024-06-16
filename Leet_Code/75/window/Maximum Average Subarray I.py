from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k
        now = max_sum = sum(nums[l:r])

        for s in range(k, len(nums)):
            now = now + nums[s] - nums[l]
            max_sum = max(max_sum, now)
            l += 1
            r += 1
        return max_sum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
Solution().findMaxAverage(nums, k)

nums = [0, 4, 1]
k = 1
Solution().findMaxAverage(nums, k)

nums = [0, 4, 0, 3, 2]
k = 1
Solution().findMaxAverage(nums, k)

nums = [4, 2, 1, 3, 3]
k = 2
Solution().findMaxAverage(nums, k)
