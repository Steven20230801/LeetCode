from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        l = 0
        cursum = 0

        for r in range(len(nums)):

            cursum += r

            if cursum == k:
                res += 1
