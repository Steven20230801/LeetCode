from typing import List
import math


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        # 定義檢驗方式
        def check(ranks, mid):

            x = 0
            for rank in ranks:
                x += math.floor(math.sqrt(mid / rank))

            return x  # 共修了幾台車

        l, r = 1, 100 * cars**2  # 1 <= ranks[i] <= 100

        while l <= r:

            mid = (l + r) // 2

            if check(ranks, mid) < cars:  # 修太少, 需要增加
                l = mid + 1
            else:
                r = mid - 1

        return l


Solution().repairCars(ranks=[4, 2, 3, 1], cars=10)
Solution().repairCars(ranks=[5, 1, 8], cars=6)

Solution().repairCars(ranks=[100], cars=100)
