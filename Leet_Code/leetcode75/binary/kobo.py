from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:

            m = (l + r) // 2

            total_spend = sum([math.ceil(pile / m) for pile in piles])

            if total_spend > h:
                l = m + 1
            else:
                r = m - 1
        return r + 1


6
Solution().minEatingSpeed([30, 11, 23, 4, 20], h=6)
