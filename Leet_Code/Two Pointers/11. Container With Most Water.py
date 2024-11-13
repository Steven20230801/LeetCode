from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 初始化左指針和右指針
        l, r = 0, len(height) - 1
        # 初始化結果變量，用於存儲最大容積
        res = 0

        # 當左指針小於右指針時，繼續迭代
        while l < r:
            # 計算當前兩條線所能容納的容積
            ans = (r - l) * min(height[l], height[r])
            # 更新最大容積
            res = max(ans, res)

            # 根據較小的高度移動指針，以期找到更高的線
            if height[l] < height[r]:
                l += 1  # 移動左指針
            else:
                r -= 1  # 移動右指針

        # 返回最大容積
        return res
