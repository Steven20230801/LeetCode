from collections import defaultdict
from functools import cache
from typing import List

# Cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # p
        # n = s-p
        # target = p-n
        # target = p-(s-p) = 2p-s
        # p = (target + s) / 2 -> 背包有(target + s) / 2容量, 選擇方案數
        target += sum(nums)

        if target < 0 or target % 2 == 1:
            return 0

        target = target / 2
        n = len(nums)

        @cache
        def dfs(i, t):

            if i < 0:
                return 1 if t == 0 else 0
            # 超出容量
            if nums[i] > t:
                return dfs(i - 1, t)

            res = dfs(i - 1, t) + dfs(i - 1, t - nums[i])  # 不選 + 選
            return res

        return dfs(n - 1, target)


# 記憶化
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # p
        # n = s-p
        # target = p-n
        # target = p-(s-p) = 2p-s
        # p = (target + s) / 2 -> 背包有(target + s) / 2容量, 選擇方案數
        target += sum(nums)

        if target < 0 or target % 2 == 1:
            return 0

        target = target / 2
        n = len(nums)

        memo = {}

        def dfs(i, t):

            if (i, t) in memo:
                return memo[(i, t)]

            if i < 0:
                return 1 if t == 0 else 0
            # 超出容量
            if nums[i] > t:
                memo[(i, t)] = dfs(i - 1, t)
            else:
                memo[(i, t)] = dfs(i - 1, t) + dfs(i - 1, t - nums[i])  # 不選 + 選

            return memo[(i, t)]

        return dfs(n - 1, target)



# 遞推
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # p
        # n = s-p
        # target = p-n
        # target = p-(s-p) = 2p-s
        # p = (target + s) / 2 -> 背包有(target + s) / 2容量, 選擇方案數
        
        nums=[1, 1, 1, 1, 1]
        target=3
        target += sum(nums)

        if target < 0 or target % 2 == 1:
            return 0

        target = target // 2
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i, x in enumerate(nums)

        def dfs(i, t):

            if (i, t) in memo:
                return memo[(i, t)]

            if i < 0:
                return 1 if t == 0 else 0
            # 超出容量
            if nums[i] > t:
                memo[(i, t)] = dfs(i - 1, t)
            else:
                memo[(i, t)] = dfs(i - 1, t) + dfs(i - 1, t - nums[i])  # 不選 + 選

            return memo[(i, t)]

        return dfs(n - 1, target)



class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo = {}
        
        def dfs(i, total): # total 選到nums[i]時, 前面的加總
            
            # base case 
            if i >= n: # 超出nums範圍
                return 1 if total == target else 0
            
            if (i, total) in memo:
                return memo[(i, total)]
            
            res = dfs(i+1, total=total+nums[i]) + dfs(i+1, total=total-nums[i])
            
            memo[(i, total)] = res
            return res
        
        return dfs(0, 0)
            


from functools import lru_cache
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)  # 獲取數組的長度

        # 使用 lru_cache 進行記憶化，以提高遞迴效率
        @lru_cache(maxsize=None)
        def dfs(i: int, total: int) -> int:
            # 基礎案例：如果已經處理完所有數字，檢查當前總和是否等於目標值
            if i == n:
                return 1 if total == target else 0

            # 選擇加上當前數字，並遞迴處理下一個數字
            add = dfs(i + 1, total + nums[i])
            # 選擇減去當前數字，並遞迴處理下一個數字
            subtract = dfs(i + 1, total - nums[i])

            # 返回加法和減法的結果之和，即所有可能的組合數
            return add + subtract

        # 從第一個數字開始，初始總和為 0
        return dfs(0, 0)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)  # 獲取數組的長度

        # 使用 lru_cache 進行記憶化，以提高遞迴效率
        @lru_cache(maxsize=None)
        def dfs(i: int, total: int) -> int:
            # 基礎案例：如果已經處理完所有數字，檢查當前總和是否等於目標值
            if i == n:
                return 1 if total == target else 0

            # 選擇加上當前數字，並遞迴處理下一個數字
            add = dfs(i + 1, total + nums[i])
            # 選擇減去當前數字，並遞迴處理下一個數字
            subtract = dfs(i + 1, total - nums[i])

            # 返回加法和減法的結果之和，即所有可能的組合數
            return add + subtract

        # 從第一個數字開始，初始總和為 0
        return dfs(0, 0)



Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3)
Solution().findTargetSumWays(nums=[1], target=1)
