from typing import List


# ans 照順序搬完
# ans = 15
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check_days(weights, speed):
            days = 1
            init = 0
            for weight in weights:
                if init + weight > speed:
                    days += 1
                    init = 0
                init += weight
            return days

        l, r = 1, sum(weights)

        while l <= r:

            speed = (l + r) // 2
            spend = check_days(weights, speed)
            if spend <= days:  # 可以放慢速度
                r = speed - 1
            else:
                l = speed + 1

        return l


# Solution().shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5)

Solution().shipWithinDays(weights=[1, 2, 3, 1, 1], days=4)
