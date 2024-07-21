from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, R = 0, 0
        res = float("inf")
        cursum = 0
        for R in range(len(nums)):

            cursum += nums[R]

            while cursum >= target:
                res = min(res, R - L + 1)  # 更新答案
                cursum -= nums[L]  # 刪除左邊界值
                L += 1  # 縮小左邊界

        if res == float("inf"):
            return 0
        else:
            return res


Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
Solution().minSubArrayLen(3, [1, 1, 1])
Solution().minSubArrayLen(111111, [2, 3, 1, 2, 4, 3])
