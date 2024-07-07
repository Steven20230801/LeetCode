from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = k
        l, remain = 0, k
        for r, x in enumerate(nums, 0):
            if x == 0:
                k -= 1
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
Solution().longestOnes(nums, k)


nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3
Solution().longestOnes(nums, k)


nums = [0, 0]
k = 2
Solution().longestOnes(nums, k)
