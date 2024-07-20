from typing import List

prices = [7, 1, 5, 3, 6, 4]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        min_so_far = prices[0]

        for i in range(1, len(prices)):

            price = prices[i]

            profit = price - min_so_far

            res = max(res, profit)

            min_so_far = min(min_so_far, price)

        return res


Solution().maxProfit([1])
