from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        check = 0
        l, r = 0, 0
        while r < len(nums):
            while check > 1:
                if nums[l] == 0:
                    check -= 1
                l += 1

            if nums[r] == 0:
                check += 1

            ans = max(ans, r - l + 1 - check)
            r += 1
        if check == 0:  # 代表都沒0
            ans -= 1
        return ans


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        check = 0
        l, r = 0, 0
        while r < len(nums):

            if nums[r] == 0:
                check += 1

            while check > 1:
                if nums[l] == 0:
                    check -= 1
                l += 1

            if nums[r] == 0:
                check += 1

            ans = max(ans, r - l + 1 - check)
            r += 1
        if check == 0:  # 代表都沒0
            ans -= 1
        return ans


Solution().longestSubarray([1, 1, 0, 1])

Solution().longestSubarray([1, 1, 1])
