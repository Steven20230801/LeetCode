from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        curmin = prices[0]

        for p in range(1, len(prices)):
            curmin = min(curmin, p)
            maxprofit = max(maxprofit, p - curmin)

        return maxprofit


Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4])
