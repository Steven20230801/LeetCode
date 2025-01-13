from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 設定二分查找的範圍，最低速度為1，最高速度為最大香蕉堆數量
        l, r = 1, max(piles)

        # 進行二分查找
        while l <= r:
            m = (l + r) // 2  # 計算中間速度

            # 計算以速度m吃完所有香蕉所需的總小時數
            hours = sum(ceil(x / m) for x in piles)

            if hours <= h:
                # 如果總小時數小於等於h，嘗試更小的速度
                r = m - 1
            else:
                # 否則，增大速度
                l = m + 1

        # 返回最小的可行速度
        return l


Solution().minEatingSpeed([30, 11, 23, 4, 20], h=6)
