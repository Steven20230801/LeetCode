# 示例 2：

# 输入：dist = [1,3,2], hour = 2.7
# 输出：3
# 解释：速度为 3 时：
# - 第 1 趟列车运行需要 1/3 = 0.33333 小时。
# - 由于不是在整数时间到达，故需要等待至第 1 小时才能搭乘列车。第 2 趟列车运行需要 3/3 = 1 小时。
# - 由于是在整数时间到达，可以立即换乘在第 2 小时发车的列车。第 3 趟列车运行需要 2/3 = 0.66667 小时。
# - 你将会在第 2.66667 小时到达。
# 示例 3：

# 输入：dist = [1,3,2], hour = 1.9
# 输出：-1
# 解释：不可能准时到达，因为第 3 趟列车最早是在第 2 小时发车。


# 最大時速 = [sum(dist) / hour] = 4
# [1/4] = 1
# [1/3] = 1

import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        # 時間一定要大於len(dist)-1(每個站至少一小時)
        if hour <= len(dist) - 1:
            return -1

        def calculate_hours(dist, speed):
            n = len(dist)
            # n-1需要無條件進入
            x = sum([math.ceil(dist[i] / speed) for i in range(n - 1)])
            x += dist[-1] / speed
            return x

        l, r = 1, 10**7  # // hour + 1  # 最大時速
        # 求最小時速 = 大於的第一個下標
        while l <= r:
            mid = (l + r) // 2  # mid時速
            now_hours = calculate_hours(dist, mid)
            if now_hours <= hour:  # 若目前花費時間比較少, 降低時速
                r = mid - 1
            else:
                l = mid + 1

        return l


Solution().minSpeedOnTime([1, 3, 2], 2.7)
Solution().minSpeedOnTime([1, 3, 2], 6)
Solution().minSpeedOnTime([1, 3, 2], 1.9)
Solution().minSpeedOnTime([1, 1, 1], 2)
