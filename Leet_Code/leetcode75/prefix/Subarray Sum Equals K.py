from collections import Counter
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        res = 0
        prefixsum = [0] * n
        cursum = 0
        counter = {}
        for i in range(n):
            cursum += nums[i]

            if cursum == k:
                res += 1

            if cursum - k in counter:
                res += counter[cursum - k]

            counter[cursum] = counter.get(cursum, 0) + 1  # n 以前的couter

        return res


Solution().subarraySum(nums=[1, 2, 3], k=3)
Solution().subarraySum(nums=[-1, 2, -1, 2, -1], k=0)


# [-1, 2, -1, 2, -1]
