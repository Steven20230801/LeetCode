from typing import List


def fn(arr):
    def dp(STATE):
        if BASE_CASE:
            return 0

        if STATE in memo:
            return memo[STATE]

        ans = RECURRENCE_RELATION(STATE)
        memo[STATE] = ans
        return ans

    memo = {}
    return dp(STATE_FOR_WHOLE_INPUT)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [2, 3, -2, 4]
        n = len(nums)

        def dp(i, mx, mn):

            if i >= n:
                return max(mx, mn)

            if nums[i] == 0:
                ans = max(mx, dp(i + 1, 1, 1))
            elif nums[i] > 0:
                ans = mx * nums[i] * dp(i + 1)
