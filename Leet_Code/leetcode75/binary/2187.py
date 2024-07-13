# time = [1,2,3], totalTrips = 5

# t = 1  [1, 0, 0]
# t = 2  [2, 1, 0]
# t = 3  [3, 1, 1] == 5 - > t = 3


from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # 假設ans = x
        # [ans / time[i]] 加總 = totalTrips]
        # 最短時間為1
        # 最大時間為totalTrips
        l, r = 0, max(sum(time), totalTrips)
        # 目標找>=
        while l <= r:
            # 目前時間
            mid = (l + r) // 2
            # 判斷目前能不能完成
            x = sum([mid // x for x in time])
            if x < totalTrips:  # 若目前不能完成, 調整時間
                l = mid + 1
            else:
                r = mid - 1

        return l


Solution().minimumTime([1, 2, 3], 5)
Solution().minimumTime([5, 10, 10], 9)
Solution().minimumTime([1], 4)
