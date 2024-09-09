"""

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

"""

from functools import cache
from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()  # 将硬币按面值升序排列，方便后续的剪枝操作

        @cache  # 使用缓存来存储中间结果，避免重复计算
        def dp(i, c):
            # 边界条件
            if i < 0:
                return 0 if c == 0 else float('inf')  # 如果没有硬币了，只有金额为0时是合法状态，其他情况返回无穷大
            
            if coins[i] > c:
                return dp(i-1, c)  # 当前硬币面值超过当前金额时，不用这个硬币，尝试下一个
            else:
                return min(dp(i-1, c), 1+dp(i, c-coins[i]))

        ans = dp(len(coins)-1, amount)  # 从最后一个硬币开始递归
        return ans if ans != float('inf') else -1 


Solution().coinChange(coins = [1,2,5], amount = 11)
Solution().coinChange(coins = [2], amount = 3)
Solution().coinChange(coins = [1], amount = 0)
Solution().coinChange(coins = [411,412,413,414,415,416,417,418,419,420,421,422], amount = 9864)