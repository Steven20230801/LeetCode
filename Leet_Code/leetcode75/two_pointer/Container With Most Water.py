from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            volume = (r - l) * min(height[l], height[r])
            res = max(res, volume)
            # 先走牆壁比較低的

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
Solution().maxArea([1, 3])
Solution().maxArea([1, 3, 2, 5, 25, 24, 5])
