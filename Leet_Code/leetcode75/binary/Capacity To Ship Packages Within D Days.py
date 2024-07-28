from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def consume_days(w: list, s: int):
            res = 1
            temp = s
            for x in w:

                if temp >= x:
                    temp -= x
                else:
                    temp = s
                    res += 1
                    temp -= x
            return res

        l, r = max(weights), 500 * len(weights)

        while l <= r:
            m = (l + r) // 2
            d = consume_days(weights, m)

            if d <= days:
                r = m - 1
            else:
                l = m + 1

        # print(r + 1)

        return r + 1

        # weights = [3, 2, 2, 4, 1, 4]
        # days = 3
        # weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # days = 5
        # weights = [1, 2, 3, 1, 1]
        # days = 4


Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3)
Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
Solution().shipWithinDays([1, 2, 3, 1, 1], 4)
