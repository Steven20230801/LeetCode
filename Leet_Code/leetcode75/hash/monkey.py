from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        l = 1
        r = max(piles)

        if len(piles) == h:
            return r
        # 1, 2, 3, 4, 5
        while l <= r:
            mid = (l + r) // 2  # 一小時吃幾個香蕉
            total_hours = sum([math.ceil(x / mid) for x in piles])
            #  = mid * h  # 總共吃多少根
            # mid_h_add_1 = mid_h + mid

            if total_hours > h:
                l = mid + 1
            else:

                r = mid - 1
        return l


Solution().minEatingSpeed([30, 11, 23, 4, 20], 5)
