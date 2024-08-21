from typing import List
from collections import Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        h = {}
        ans = 0
        for n in nums:
            if k - n in h and h[k - n] > 0:
                h[k - n] -= 1
                ans += 1
            else:
                h[n] = h.get(n, 0) + 1
        return ans


Solution().maxOperations(nums=[1, 2, 4, 3], k=6)


Solution().maxOperations(nums=[3, 3, 3, 3], k=6)


Solution().maxOperations(nums=[2, 1, 1, 1, 2, 2, 2], k=3)
