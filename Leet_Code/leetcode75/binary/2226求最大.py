from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        total = sum(candies)
        l, r = 1, total

        if total < k:
            return 0

        def check_packs(candies, mid):
            packs = 0
            for candy in candies:
                packs += candy // mid  # 這個大堆可以分成幾個小堆
            return packs

        while l <= r:

            mid = (l + r) // 2  # 分配糖果

            if check_packs(candies, mid) >= k:  # 若可以成功分得 試著再增加數量
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        # 結束後l = r+1, l-1表示最大可分發數量
        return ans


Solution().maximumCandies(candies=[5, 8, 6], k=3)

Solution().maximumCandies(candies=[2, 5], k=11)


Solution().maximumCandies(candies=[1], k=1)
